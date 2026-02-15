#!/usr/bin/env python3
import argparse
import csv
import getpass
import json
import os
import re
from typing import Optional, Dict, Any, Tuple
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


ZOTERO_API_BASE = "https://api.zotero.org"
API_VERSION = "3"


SEC_ID_RE = re.compile(r"\{#(sec:[^}]+)\}")
ZOTERO_STORAGE_KEY_RE = re.compile(r"/Zotero/storage/([A-Z0-9]{8})/")
CITEKEY_RE = re.compile(r"(?<![\\w-])@([A-Za-z0-9][A-Za-z0-9_:\\-]*)(?![\\w-])")
CHAPTER_ID_RE = re.compile(r"^(\d{2}-\d{2})\b")


def eprint(msg: str) -> None:
    print(msg, file=sys.stderr)


def iter_markdown_files(md_root: str) -> list[str]:
    paths: list[str] = []
    for root, _dirs, files in os.walk(md_root):
        for name in files:
            if name.lower().endswith(".md"):
                paths.append(os.path.join(root, name))
    return sorted(paths)


def parse_markdown_citations(md_paths: list[str]) -> tuple[dict[str, set[str]], dict[str, dict]]:
    citekey_to_sections: dict[str, set[str]] = {}
    sections_meta: dict[str, dict] = {}

    for md_path in md_paths:
        current_section = None
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    sec_match = SEC_ID_RE.search(line)
                    if sec_match:
                        current_section = sec_match.group(1)
                        sections_meta.setdefault(
                            current_section,
                            {"firstSeenFile": md_path, "firstSeenLine": line_no},
                        )

                    for m in CITEKEY_RE.finditer(line):
                        citekey = m.group(1)
                        if current_section is None:
                            continue
                        citekey_to_sections.setdefault(citekey, set()).add(current_section)
        except UnicodeDecodeError:
            eprint(f"Skip non-utf8 Markdown: {md_path}")
        except FileNotFoundError:
            eprint(f"Missing Markdown file: {md_path}")

    return citekey_to_sections, sections_meta


def chapter_id_from_path(md_path: str) -> Optional[str]:
    base = os.path.basename(md_path)
    m = CHAPTER_ID_RE.match(base)
    if m:
        return m.group(1)
    parent = os.path.basename(os.path.dirname(md_path))
    m = CHAPTER_ID_RE.match(parent)
    if m:
        return m.group(1)
    return None


def parse_markdown_chapter_citations(md_paths: list[str]) -> dict[str, set[str]]:
    citekey_to_chapters: dict[str, set[str]] = {}
    for md_path in md_paths:
        chapter_id = chapter_id_from_path(md_path)
        if not chapter_id:
            continue
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                for line in f:
                    for m in CITEKEY_RE.finditer(line):
                        citekey = m.group(1)
                        citekey_to_chapters.setdefault(citekey, set()).add(chapter_id)
        except UnicodeDecodeError:
            eprint(f"Skip non-utf8 Markdown: {md_path}")
        except FileNotFoundError:
            eprint(f"Missing Markdown file: {md_path}")
    return citekey_to_chapters


def parse_bib_storage_keys(bib_path: str) -> dict[str, set[str]]:
    with open(bib_path, "r", encoding="utf-8") as f:
        content = f.read()

    starts = [(m.start(), m.group(1)) for m in re.finditer(r"^@\w+\{([^,]+),", content, flags=re.M)]
    storage_by_citekey: dict[str, set[str]] = {}

    for idx, (start, citekey) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(content)
        entry = content[start:end]
        keys = set(ZOTERO_STORAGE_KEY_RE.findall(entry))
        if keys:
            storage_by_citekey[citekey] = keys

    return storage_by_citekey


def http_json(
    method: str,
    url: str,
    api_key: str,
    body_obj=None,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Tuple[int, Dict[str, str], Any]:
    data = None
    headers = {
        "Zotero-API-Version": API_VERSION,
        "Zotero-API-Key": api_key,
        "Accept": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)
    if body_obj is not None:
        encoded = json.dumps(body_obj).encode("utf-8")
        data = encoded
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            payload = json.loads(raw) if raw else None
            return resp.status, dict(resp.headers), payload
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
    return e.code, dict(e.headers), raw


def zotero_item_url(library_type: str, library_id: str, item_key: str) -> str:
    safe_key = urllib.parse.quote(item_key)
    return f"{ZOTERO_API_BASE}/{library_type}s/{library_id}/items/{safe_key}?format=json"


def get_item(library_type: str, library_id: str, item_key: str, api_key: str):
    url = zotero_item_url(library_type, library_id, item_key)
    status, headers, payload = http_json("GET", url, api_key)
    if status != 200:
        raise RuntimeError(f"GET item {item_key} failed ({status}): {payload}")
    return headers, payload


def update_item(library_type: str, library_id: str, item_key: str, api_key: str, item_obj: dict, version: str):
    url = zotero_item_url(library_type, library_id, item_key)
    status, _headers, payload = http_json(
        "PUT",
        url,
        api_key,
        body_obj=(item_obj.get("data") or {}),
        extra_headers={"If-Unmodified-Since-Version": version},
    )
    if status != 204:
        raise RuntimeError(f"PUT item {item_key} failed ({status}): {payload}")


def ensure_tags(item_obj: dict, tags_to_add: set[str]) -> tuple[dict, set[str]]:
    data = item_obj.get("data") or {}
    existing_tags = data.get("tags") or []
    existing_set = {t.get("tag") for t in existing_tags if isinstance(t, dict) and t.get("tag")}

    to_add = {t for t in tags_to_add if t and t not in existing_set}
    if not to_add:
        return item_obj, set()

    new_tags = list(existing_tags)
    for tag in sorted(to_add):
        new_tags.append({"tag": tag})
    data["tags"] = new_tags
    item_obj["data"] = data
    return item_obj, to_add


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Tag Zotero items with Promotion section IDs based on Pandoc citekeys used in Markdown chapters. "
            "Default is dry-run + CSV report; use --apply to write tags via Zotero Web API."
        )
    )
    ap.add_argument(
        "--md-root",
        default=os.path.join("04 Kapitelstruktur"),
        help="Root folder to scan for Markdown (default: 04 Kapitelstruktur)",
    )
    ap.add_argument(
        "--bib",
        default=os.path.join("08 Metaquellen", "Matadaten", "Literaturverzeichnis.bib"),
        help="BibTeX file with citekeys and Zotero storage paths",
    )
    ap.add_argument(
        "--library-type",
        choices=["user", "group"],
        default="user",
        help="Zotero library type (default: user)",
    )
    ap.add_argument(
        "--library-id",
        required=True,
        help="Zotero user ID or group ID",
    )
    ap.add_argument(
        "--tag-prefix",
        default="Promotion:",
        help="Tag prefix (default: Promotion:)",
    )
    ap.add_argument(
        "--tag-chapters",
        action="store_true",
        help="Also tag cited items with chapter IDs inferred from Markdown filenames (e.g., Promotion:chap:04-02).",
    )
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Write tags to Zotero (otherwise dry-run only)",
    )
    ap.add_argument(
        "--citekeys-only",
        action="store_true",
        help="Only produce citekey->section->storageKey report CSV (no Zotero API calls)",
    )
    ap.add_argument(
        "--out",
        default=os.path.join("tools", "zotero_promotion_section_tags.csv"),
        help="CSV output path (default: tools/zotero_promotion_section_tags.csv)",
    )
    ap.add_argument(
        "--sleep",
        type=float,
        default=0.05,
        help="Sleep seconds between Zotero API calls (default: 0.05)",
    )
    args = ap.parse_args()
    chapter_prefix = f"{args.tag_prefix}chap:"

    md_paths = iter_markdown_files(args.md_root)
    if not md_paths:
        eprint(f"No Markdown files found under: {args.md_root}")
        return 2
    if not os.path.exists(args.bib):
        eprint(f"BibTeX not found: {args.bib}")
        return 2

    citekey_to_sections, _sections_meta = parse_markdown_citations(md_paths)
    citekey_to_chapters = parse_markdown_chapter_citations(md_paths) if args.tag_chapters else {}
    if not citekey_to_sections and not citekey_to_chapters:
        eprint("No citekeys found (neither inside labeled sections {#sec:...} nor for chapter tagging).")
        return 2

    storage_by_citekey = parse_bib_storage_keys(args.bib)

    citekey_rows: list[dict] = []
    attachment_to_tags: dict[str, set[str]] = {}
    missing_in_bib = 0
    missing_storage = 0

    citekeys_all = set(citekey_to_sections.keys()) | set(citekey_to_chapters.keys())
    for citekey in sorted(citekeys_all):
        sections = citekey_to_sections.get(citekey) or set()
        chapters = citekey_to_chapters.get(citekey) or set()
        section_tags = {f"{args.tag_prefix}{sec}" for sec in sections}
        chapter_tags = {f"{chapter_prefix}{c}" for c in chapters}
        all_tags = section_tags | chapter_tags
        storage_keys = storage_by_citekey.get(citekey) or set()
        if citekey not in storage_by_citekey:
            missing_in_bib += 1
        if not storage_keys:
            missing_storage += 1
        for sk in (storage_keys or {""}):
            citekey_rows.append(
                {
                    "citekey": citekey,
                    "sections": ";".join(sorted(sections)),
                    "chapters": ";".join(sorted(chapters)),
                    "tagCount": str(len(all_tags)),
                    "storageKey": sk,
                }
            )
        for storage_key in storage_keys:
            attachment_to_tags.setdefault(storage_key, set()).update(all_tags)

    # Always write citekey-level report (useful for auditing before touching Zotero).
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    citekey_out = os.path.splitext(args.out)[0] + ".citekeys.csv"
    with open(citekey_out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["citekey", "sections", "chapters", "tagCount", "storageKey"],
        )
        w.writeheader()
        w.writerows(citekey_rows)

    if args.citekeys_only:
        print(
            json.dumps(
                {
                    "markdownFiles": len(md_paths),
                    "citekeysInSections": len(citekey_to_sections),
                    "citekeysInChapters": len(citekey_to_chapters),
                    "itemsResolvedFromBib": len(attachment_to_tags),
                    "missingInBib": missing_in_bib,
                    "missingStorage": missing_storage,
                    "citekeyCsv": citekey_out,
                    "mode": "citekeys-only",
                },
                ensure_ascii=False,
            )
        )
        return 0

    api_key = (os.environ.get("ZOTERO_API_KEY") or "").strip()
    if not api_key:
        api_key = getpass.getpass("Zotero API key (will not echo): ").strip()
    if not api_key:
        eprint("No API key provided (set ZOTERO_API_KEY or enter it interactively).")
        return 2

    # Resolve attachments -> parent items, then aggregate tags on parent.
    attachment_parent_cache: dict[str, str] = {}
    parent_to_tags: dict[str, set[str]] = {}
    parent_sources: dict[str, set[str]] = {}

    for attachment_key, tags in sorted(attachment_to_tags.items()):
        try:
            _headers, attachment_item = get_item(args.library_type, args.library_id, attachment_key, api_key)
        except Exception as e:
            eprint(f"[{attachment_key}] resolve failed: {e}")
            continue
        time.sleep(max(0.0, args.sleep))

        parent_key = ((attachment_item.get("data") or {}).get("parentItem")) or attachment_key
        attachment_parent_cache[attachment_key] = parent_key
        parent_to_tags.setdefault(parent_key, set()).update(tags)
        parent_sources.setdefault(parent_key, set()).add(attachment_key)

    report_rows: list[dict] = []
    changed = 0
    unchanged = 0
    failed = 0

    for parent_key, tags in sorted(parent_to_tags.items()):
        try:
            headers, item = get_item(args.library_type, args.library_id, parent_key, api_key)
            time.sleep(max(0.0, args.sleep))
            version = headers.get("Last-Modified-Version") or str((item.get("version") or ""))
            if not version:
                raise RuntimeError("Could not determine item version for update")
            updated_item, added = ensure_tags(item, tags)
            if not added:
                unchanged += 1
                report_rows.append(
                    {
                        "parentKey": parent_key,
                        "sources": ";".join(sorted(parent_sources.get(parent_key) or [])),
                        "wouldAddTags": "",
                        "status": "unchanged",
                    }
                )
                continue

            if args.apply:
                update_item(args.library_type, args.library_id, parent_key, api_key, updated_item, version)
                time.sleep(max(0.0, args.sleep))
                status = "updated"
            else:
                status = "dry-run"
            changed += 1
            report_rows.append(
                {
                    "parentKey": parent_key,
                    "sources": ";".join(sorted(parent_sources.get(parent_key) or [])),
                    "wouldAddTags": ";".join(sorted(added)),
                    "status": status,
                }
            )
        except Exception as e:
            failed += 1
            report_rows.append(
                {
                    "parentKey": parent_key,
                    "sources": ";".join(sorted(parent_sources.get(parent_key) or [])),
                    "wouldAddTags": ";".join(sorted(tags)),
                    "status": f"failed: {e}",
                }
            )
            continue

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["parentKey", "sources", "wouldAddTags", "status"],
        )
        w.writeheader()
        w.writerows(report_rows)

    print(
        json.dumps(
            {
                "markdownFiles": len(md_paths),
                "citekeysInSections": len(citekey_to_sections),
                "citekeysInChapters": len(citekey_to_chapters),
                "itemsResolvedFromBib": len(attachment_to_tags),
                "parentItemsToTag": len(parent_to_tags),
                "changed": changed,
                "unchanged": unchanged,
                "failed": failed,
                "missingInBib": missing_in_bib,
                "missingStorage": missing_storage,
                "reportCsv": args.out,
                "citekeyCsv": citekey_out,
                "mode": "apply" if args.apply else "dry-run",
            },
            ensure_ascii=False,
        )
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
