#!/usr/bin/env python3
"""Synchronize dissertation section/chapter tags in Zotero.

The older tagging helper only adds tags. This tool treats the Markdown
citations as the source of truth, removes stale Promotion:sec:/Promotion:chap:
tags from touched Zotero parent items, and adds the currently derived tags.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any


API_BASE = "https://api.zotero.org"
API_VERSION = "3"
SCRIPT_DIR = Path(__file__).resolve().parent
SEC_ID_RE = re.compile(r"\{#(sec:[^}]+)\}")
CITEKEY_RE = re.compile(r"(?<![\w-])@([A-Za-z0-9][A-Za-z0-9_:\-]*)(?![\w-])")
ENTRY_RE = re.compile(r"^@\w+\{([^,]+),", re.M)
STORAGE_RE = re.compile(r"/Zotero/storage/([A-Z0-9]{8})/")
CHAPTER_RE = re.compile(r"^(\d{2}-\d{2})\b")


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def md_files(md_root: Path) -> list[Path]:
    return sorted(p for p in md_root.rglob("*.md") if p.is_file())


def chapter_from_path(path: Path) -> str | None:
    for candidate in (path.name, path.parent.name):
        match = CHAPTER_RE.match(candidate)
        if match:
            return match.group(1)
    return None


def parse_markdown(paths: list[Path], tag_chapters: bool) -> dict[str, set[str]]:
    tags_by_citekey: dict[str, set[str]] = defaultdict(set)
    for path in paths:
        current_section: str | None = None
        chapter = chapter_from_path(path)
        for line in path.read_text(encoding="utf-8").splitlines():
            sec_match = SEC_ID_RE.search(line)
            if sec_match:
                current_section = sec_match.group(1)
            for cite_match in CITEKEY_RE.finditer(line):
                citekey = cite_match.group(1)
                if current_section:
                    tags_by_citekey[citekey].add(f"Promotion:{current_section}")
                if tag_chapters and chapter:
                    tags_by_citekey[citekey].add(f"Promotion:chap:{chapter}")
    return tags_by_citekey


def parse_bib(bib_path: Path) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    content = bib_path.read_text(encoding="utf-8")
    starts = [(m.start(), m.group(1)) for m in ENTRY_RE.finditer(content)]
    storage_by_citekey: dict[str, set[str]] = defaultdict(set)
    old_tags_by_citekey: dict[str, set[str]] = defaultdict(set)

    for idx, (start, citekey) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(content)
        entry = content[start:end]
        storage_by_citekey[citekey].update(STORAGE_RE.findall(entry))
        for tag in re.findall(r"Promotion:(?:sec|chap):[^,}\n]+", entry):
            old_tags_by_citekey[citekey].add(tag.strip())
    return dict(storage_by_citekey), dict(old_tags_by_citekey)


def http_json(method: str, url: str, api_key: str, body: Any = None, headers: dict[str, str] | None = None):
    request_headers = {
        "Zotero-API-Version": API_VERSION,
        "Zotero-API-Key": api_key,
        "Accept": "application/json",
    }
    if headers:
        request_headers.update(headers)
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        request_headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=request_headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
            payload = json.loads(raw) if raw else None
            return response.status, dict(response.headers), payload
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        return exc.code, dict(exc.headers), raw


def item_url(library_type: str, library_id: str, item_key: str) -> str:
    safe = urllib.parse.quote(item_key)
    return f"{API_BASE}/{library_type}s/{library_id}/items/{safe}?format=json"


def get_item(library_type: str, library_id: str, item_key: str, api_key: str) -> tuple[dict[str, str], dict[str, Any]]:
    status, headers, payload = http_json("GET", item_url(library_type, library_id, item_key), api_key)
    if status != 200:
        raise RuntimeError(f"GET {item_key} failed ({status}): {payload}")
    return headers, payload


def put_item(library_type: str, library_id: str, item_key: str, api_key: str, data: dict[str, Any], version: str) -> None:
    status, _headers, payload = http_json(
        "PUT",
        item_url(library_type, library_id, item_key),
        api_key,
        body=data,
        headers={"If-Unmodified-Since-Version": version},
    )
    if status != 204:
        raise RuntimeError(f"PUT {item_key} failed ({status}): {payload}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Synchronize Promotion section/chapter tags via Zotero Web API.")
    parser.add_argument("--md-root", default="04 Kapitelstruktur")
    parser.add_argument("--bib", default="08 Metaquellen/08-06 Metadaten/Literaturverzeichnis.bib")
    parser.add_argument("--library-type", choices=["user", "group"], default="user")
    parser.add_argument("--library-id", required=True)
    parser.add_argument("--tag-chapters", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--out", default=str(SCRIPT_DIR / "zotero_promotion_section_tag_sync.csv"))
    parser.add_argument("--sleep", type=float, default=0.05)
    args = parser.parse_args()

    api_key = os.environ.get("ZOTERO_API_KEY", "").strip()
    if not api_key:
        eprint("ZOTERO_API_KEY is required.")
        return 2

    markdown_tags = parse_markdown(md_files(Path(args.md_root)), tag_chapters=args.tag_chapters)
    storage_by_citekey, old_tags_by_citekey = parse_bib(Path(args.bib))

    citekeys = set(markdown_tags) | set(old_tags_by_citekey)
    attachment_to_tags: dict[str, set[str]] = defaultdict(set)
    unresolved: list[dict[str, str]] = []
    for citekey in sorted(citekeys):
        storage_keys = storage_by_citekey.get(citekey) or set()
        if not storage_keys:
            if markdown_tags.get(citekey) or old_tags_by_citekey.get(citekey):
                unresolved.append({"citekey": citekey, "reason": "no Zotero storage key in BibTeX"})
            continue
        for storage_key in storage_keys:
            attachment_to_tags[storage_key].update(markdown_tags.get(citekey, set()))

    parent_to_tags: dict[str, set[str]] = defaultdict(set)
    parent_sources: dict[str, set[str]] = defaultdict(set)
    rows: list[dict[str, str]] = []
    failed = 0

    for attachment_key, tags in sorted(attachment_to_tags.items()):
        try:
            _headers, attachment = get_item(args.library_type, args.library_id, attachment_key, api_key)
            parent_key = (attachment.get("data") or {}).get("parentItem") or attachment_key
            parent_to_tags[parent_key].update(tags)
            parent_sources[parent_key].add(attachment_key)
        except Exception as exc:
            failed += 1
            rows.append(
                {
                    "parentKey": "",
                    "sources": attachment_key,
                    "removedTags": "",
                    "addedTags": ";".join(sorted(tags)),
                    "keptTags": "",
                    "status": f"resolve failed: {exc}",
                }
            )
        time.sleep(max(0.0, args.sleep))

    stale_prefixes = ("Promotion:sec:", "Promotion:chap:")
    changed = 0
    unchanged = 0
    for parent_key, desired_tags in sorted(parent_to_tags.items()):
        try:
            headers, item = get_item(args.library_type, args.library_id, parent_key, api_key)
            data = item.get("data") or {}
            version = headers.get("Last-Modified-Version") or str(item.get("version") or "")
            old_tag_items = data.get("tags") or []
            old_tags = [t.get("tag") for t in old_tag_items if isinstance(t, dict) and t.get("tag")]
            retained = [t for t in old_tags if not t.startswith(stale_prefixes)]
            new_tags = sorted(set(retained) | desired_tags)
            removed = sorted(set(old_tags) - set(retained))
            added = sorted(desired_tags - set(old_tags))
            kept = sorted(desired_tags & set(old_tags))
            status = "unchanged"
            if new_tags != old_tags:
                changed += 1
                status = "dry-run"
                if args.apply:
                    data["tags"] = [{"tag": tag} for tag in new_tags]
                    put_item(args.library_type, args.library_id, parent_key, api_key, data, version)
                    status = "updated"
            else:
                unchanged += 1
            rows.append(
                {
                    "parentKey": parent_key,
                    "sources": ";".join(sorted(parent_sources[parent_key])),
                    "removedTags": ";".join(removed),
                    "addedTags": ";".join(added),
                    "keptTags": ";".join(kept),
                    "status": status,
                }
            )
        except Exception as exc:
            failed += 1
            rows.append(
                {
                    "parentKey": parent_key,
                    "sources": ";".join(sorted(parent_sources[parent_key])),
                    "removedTags": "",
                    "addedTags": ";".join(sorted(desired_tags)),
                    "keptTags": "",
                    "status": f"update failed: {exc}",
                }
            )
        time.sleep(max(0.0, args.sleep))

    for item in unresolved:
        rows.append({"parentKey": "", "sources": item["citekey"], "removedTags": "", "addedTags": "", "keptTags": "", "status": item["reason"]})

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["parentKey", "sources", "removedTags", "addedTags", "keptTags", "status"])
        writer.writeheader()
        writer.writerows(rows)

    print(
        json.dumps(
            {
                "citekeysInMarkdown": len(markdown_tags),
                "citekeysWithExistingSectionTags": len(old_tags_by_citekey),
                "attachmentItems": len(attachment_to_tags),
                "parentItems": len(parent_to_tags),
                "changed": changed,
                "unchanged": unchanged,
                "failed": failed,
                "unresolved": len(unresolved),
                "mode": "apply" if args.apply else "dry-run",
                "reportCsv": str(out_path),
            },
            ensure_ascii=False,
        )
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
