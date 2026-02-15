#!/usr/bin/env python3
import argparse
import csv
import datetime as dt
import os
import re
import shutil
import sqlite3
import sys


SEC_ID_RE = re.compile(r"\{#(sec:[^}]+)\}")
ZOTERO_STORAGE_KEY_RE = re.compile(r"/Zotero/storage/([A-Z0-9]{8})/")
CITEKEY_RE = re.compile(r"(?<![\\w-])@([A-Za-z0-9][A-Za-z0-9_:\\-]*)(?![\\w-])")
CHAPTER_ID_RE = re.compile(r"^(\d{2}-\d{2})\b")


def eprint(msg: str) -> None:
    print(msg, file=sys.stderr)


def utc_timestamp() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat(sep=" ")


def ensure_backup(db_path: str, backup_dir: str) -> str:
    os.makedirs(backup_dir, exist_ok=True)
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    base = os.path.basename(db_path)
    dst = os.path.join(backup_dir, f"{base}.{ts}.bak")
    shutil.copy2(db_path, dst)
    return dst


def iter_markdown_files(md_root: str) -> list[str]:
    paths: list[str] = []
    for root, _dirs, files in os.walk(md_root):
        for name in files:
            if name.lower().endswith(".md"):
                paths.append(os.path.join(root, name))
    return sorted(paths)


def parse_markdown_citations(md_paths: list[str]) -> dict[str, set[str]]:
    citekey_to_sections: dict[str, set[str]] = {}
    for md_path in md_paths:
        current_section = None
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    sec_match = SEC_ID_RE.search(line)
                    if sec_match:
                        current_section = sec_match.group(1)
                    for m in CITEKEY_RE.finditer(line):
                        citekey = m.group(1)
                        if current_section is None:
                            continue
                        citekey_to_sections.setdefault(citekey, set()).add(current_section)
        except UnicodeDecodeError:
            eprint(f"Skip non-utf8 Markdown: {md_path}")
        except FileNotFoundError:
            eprint(f"Missing Markdown file: {md_path} (line {line_no})")
    return citekey_to_sections


def chapter_id_from_path(md_path: str):
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


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Tag Zotero items locally (zotero.sqlite) with Promotion section IDs based on citations in Markdown. "
            "This writes item tags (not notes) and creates a sqlite backup first."
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
        "--db",
        default=os.path.expanduser("~/Zotero/zotero.sqlite"),
        help="Path to zotero.sqlite (default: ~/Zotero/zotero.sqlite)",
    )
    ap.add_argument(
        "--backup-dir",
        default=os.path.join(os.path.dirname(__file__), "zotero_db_backups"),
        help="Directory to write sqlite backups into (default: tools/zotero_db_backups)",
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
    ap.add_argument("--apply", action="store_true", help="Write tags (otherwise dry-run)")
    ap.add_argument(
        "--out",
        default=os.path.join("tools", "zotero_promotion_section_tags.local.csv"),
        help="CSV output path (default: tools/zotero_promotion_section_tags.local.csv)",
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
    if not os.path.exists(args.db):
        eprint(f"Zotero DB not found: {args.db}")
        return 2

    citekey_to_sections = parse_markdown_citations(md_paths)
    citekey_to_chapters = parse_markdown_chapter_citations(md_paths) if args.tag_chapters else {}
    if not citekey_to_sections and not citekey_to_chapters:
        eprint("No citekeys found (neither inside labeled sections {#sec:...} nor for chapter tagging).")
        return 2

    storage_by_citekey = parse_bib_storage_keys(args.bib)

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
        for storage_key in storage_keys:
            attachment_to_tags.setdefault(storage_key, set()).update(all_tags)

    if args.apply:
        con = sqlite3.connect(args.db, timeout=10)
    else:
        con = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True, timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("PRAGMA busy_timeout=10000")
    cur = con.cursor()

    ops: list[dict] = []
    skipped_missing_attachment = 0
    skipped_missing_parent = 0

    for attachment_key, tags in sorted(attachment_to_tags.items()):
        cur.execute("SELECT itemID FROM items WHERE key=? LIMIT 1", (attachment_key,))
        att = cur.fetchone()
        if att is None:
            skipped_missing_attachment += 1
            continue

        cur.execute("SELECT parentItemID FROM itemAttachments WHERE itemID=? LIMIT 1", (att["itemID"],))
        att_row = cur.fetchone()
        parent_item_id = att_row["parentItemID"] if att_row else None
        if not parent_item_id:
            skipped_missing_parent += 1
            continue

        cur.execute("SELECT key FROM items WHERE itemID=? LIMIT 1", (parent_item_id,))
        parent_row = cur.fetchone()
        parent_key = parent_row["key"] if parent_row else ""

        cur.execute(
            "SELECT tags.name AS name "
            "FROM itemTags JOIN tags ON itemTags.tagID = tags.tagID "
            "WHERE itemTags.itemID=?",
            (parent_item_id,),
        )
        existing = {r["name"] for r in cur.fetchall()}
        to_add = sorted(t for t in tags if t not in existing)
        if not to_add:
            ops.append(
                {
                    "attachmentKey": attachment_key,
                    "parentItemID": str(parent_item_id),
                    "parentKey": parent_key,
                    "tagsToAdd": "",
                    "status": "unchanged",
                }
            )
            continue

        ops.append(
            {
                "attachmentKey": attachment_key,
                "parentItemID": str(parent_item_id),
                "parentKey": parent_key,
                "tagsToAdd": ";".join(to_add),
                "status": "dry-run" if not args.apply else "pending",
            }
        )

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["attachmentKey", "parentItemID", "parentKey", "tagsToAdd", "status"],
        )
        w.writeheader()
        w.writerows(ops)

    if not args.apply:
        changed = sum(1 for r in ops if r["status"] == "dry-run")
        unchanged = sum(1 for r in ops if r["status"] == "unchanged")
        print(
            f"DRY_RUN markdownFiles={len(md_paths)} citekeysInSections={len(citekey_to_sections)} "
            f"attachmentsFromBib={len(attachment_to_tags)} changed={changed} unchanged={unchanged} "
            f"missingInBib={missing_in_bib} missingStorage={missing_storage} "
            f"missingAttachment={skipped_missing_attachment} missingParent={skipped_missing_parent} "
            f"reportCsv={args.out}"
        )
        con.close()
        return 0

    backup_path = ensure_backup(args.db, args.backup_dir)
    now = utc_timestamp()

    try:
        con.execute("BEGIN IMMEDIATE")
        for row in ops:
            if row["status"] != "pending":
                continue
            parent_item_id = int(row["parentItemID"])
            tags_to_add = [t for t in (row["tagsToAdd"] or "").split(";") if t]
            for tag in tags_to_add:
                cur.execute("SELECT tagID FROM tags WHERE name=? LIMIT 1", (tag,))
                tag_row = cur.fetchone()
                if tag_row is None:
                    cur.execute("INSERT INTO tags (name) VALUES (?)", (tag,))
                    tag_id = cur.lastrowid
                else:
                    tag_id = int(tag_row["tagID"])
                cur.execute(
                    "INSERT OR IGNORE INTO itemTags (itemID, tagID, type) VALUES (?, ?, 0)",
                    (parent_item_id, tag_id),
                )

            cur.execute(
                "UPDATE items SET dateModified=?, clientDateModified=?, synced=0 WHERE itemID=?",
                (now, now, parent_item_id),
            )
            row["status"] = "updated"

        con.commit()
    except sqlite3.OperationalError as e:
        con.rollback()
        con.close()
        eprint(
            f"SQLite error: {e}\n"
            "If Zotero is running, please close Zotero completely and rerun.\n"
            f"Backup already written: {backup_path}"
        )
        return 1
    finally:
        con.close()

    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["attachmentKey", "parentItemID", "parentKey", "tagsToAdd", "status"],
        )
        w.writeheader()
        w.writerows(ops)

    changed = sum(1 for r in ops if r["status"] == "updated")
    unchanged = sum(1 for r in ops if r["status"] == "unchanged")
    print(
        f"APPLIED backup={backup_path} markdownFiles={len(md_paths)} citekeysInSections={len(citekey_to_sections)} "
        f"attachmentsFromBib={len(attachment_to_tags)} updated={changed} unchanged={unchanged} "
        f"missingInBib={missing_in_bib} missingStorage={missing_storage} "
        f"missingAttachment={skipped_missing_attachment} missingParent={skipped_missing_parent} "
        f"reportCsv={args.out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
