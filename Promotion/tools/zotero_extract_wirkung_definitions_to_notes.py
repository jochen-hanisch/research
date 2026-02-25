#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import os
import random
import re
import shutil
import sqlite3
import string
import subprocess
from dataclasses import dataclass
from typing import Iterable


DEFAULT_TAG = "Promotion:Literaturverzeichnis"
NOTE_TITLE = "Extrakte: Wirkung/Definition (auto)"

PLACEHOLDER_REASONS_SQL = r"""
WITH candidates AS (
  SELECT DISTINCT parentItemID AS itemID
  FROM itemNotes
  WHERE parentItemID IS NOT NULL
    AND (
      note LIKE '%Definition Wirkung%'
      OR note LIKE '%Definition wirken%'
      OR note LIKE '%Definition Wirkungs%'
      OR note LIKE '%Begriff Wirkungsforschung%'
      OR note LIKE '%Wirkungsforschung%Definition%'
    )
  UNION
  SELECT DISTINCT d.itemID
  FROM itemData d
  JOIN itemDataValues v ON v.valueID=d.valueID
  JOIN fields f ON f.fieldID=d.fieldID
  WHERE (v.value LIKE '%Definition%' AND (v.value LIKE '%Wirkung%' OR v.value LIKE '%wirken%'))
    AND f.fieldName IN ('title','abstractNote','extra','shortTitle','url')
)
SELECT itemID FROM candidates;
"""

WIDE_CANDIDATES_SQL = r"""
WITH pdf_parents AS (
  SELECT DISTINCT parentItemID AS itemID
  FROM itemAttachments
  WHERE parentItemID IS NOT NULL
    AND contentType IS NOT NULL
    AND (contentType = 'application/pdf' OR contentType LIKE '%pdf%')
),
note_hits AS (
  SELECT DISTINCT parentItemID AS itemID
  FROM itemNotes
  WHERE parentItemID IS NOT NULL
    AND (
      note LIKE '%Wirkung%'
      OR note LIKE '%Wirksamkeit%'
      OR note LIKE '%Wirkungsforschung%'
      OR note LIKE '%Wirkungsorient%'
      OR note LIKE '%effect%'
      OR note LIKE '%impact%'
      OR note LIKE '%outcome%'
    )
    AND (
      note LIKE '%Definition%'
      OR note LIKE '%definier%'
      OR note LIKE '%bezeichnet%'
      OR note LIKE '%verstanden%'
      OR note LIKE '%versteht man%'
      OR note LIKE '%meint%'
      OR note LIKE '%Wirkung ist%'
      OR note LIKE '%Unter Wirkung%'
      OR note LIKE '%understand%'
      OR note LIKE '%is defined%'
      OR note LIKE '%refers to%'
      OR note LIKE '%means%'
    )
),
field_hits AS (
  SELECT DISTINCT d.itemID
  FROM itemData d
  JOIN itemDataValues v ON v.valueID=d.valueID
  JOIN fields f ON f.fieldID=d.fieldID
  WHERE f.fieldName IN ('title','abstractNote','extra','shortTitle','url')
    AND (
      v.value LIKE '%Wirkung%'
      OR v.value LIKE '%Wirksamkeit%'
      OR v.value LIKE '%Wirkungsforschung%'
      OR v.value LIKE '%Wirkungsorient%'
      OR v.value LIKE '%effect%'
      OR v.value LIKE '%impact%'
      OR v.value LIKE '%outcome%'
    )
    AND (
      v.value LIKE '%Definition%'
      OR v.value LIKE '%definier%'
      OR v.value LIKE '%bezeichnet%'
      OR v.value LIKE '%verstanden%'
      OR v.value LIKE '%versteht man%'
      OR v.value LIKE '%meint%'
      OR v.value LIKE '%Wirkung ist%'
      OR v.value LIKE '%Unter Wirkung%'
      OR v.value LIKE '%is defined%'
      OR v.value LIKE '%refers to%'
      OR v.value LIKE '%means%'
    )
),
candidates AS (
  SELECT itemID FROM note_hits
  UNION
  SELECT itemID FROM field_hits
)
SELECT c.itemID
FROM candidates c
JOIN pdf_parents p ON p.itemID = c.itemID;
"""


@dataclass(frozen=True)
class Attachment:
    attachment_item_id: int
    file_path: str


def ensure_zotero_not_running(db_path: str) -> None:
    wal = db_path + "-wal"
    shm = db_path + "-shm"
    if os.path.exists(wal) or os.path.exists(shm):
        raise SystemExit(
            "Zotero DB appears in WAL mode (likely Zotero still open). "
            "Please close Zotero before running this script."
        )


def backup_db(db_path: str) -> str:
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = f"{db_path}.codex-extract-wirkung.{ts}.bak"
    shutil.copy2(db_path, backup_path)
    return backup_path


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_tag_id(conn: sqlite3.Connection, tag_name: str) -> int:
    row = conn.execute("SELECT tagID FROM tags WHERE name = ?", (tag_name,)).fetchone()
    if row:
        return int(row["tagID"])
    cur = conn.execute("INSERT INTO tags (name) VALUES (?)", (tag_name,))
    return int(cur.lastrowid)


def ensure_item_tag(conn: sqlite3.Connection, item_id: int, tag_id: int) -> None:
    row = conn.execute(
        "SELECT 1 FROM itemTags WHERE itemID = ? AND tagID = ?",
        (item_id, tag_id),
    ).fetchone()
    if row:
        return
    # type = 0 (manual)
    conn.execute("INSERT INTO itemTags (itemID, tagID, type) VALUES (?, ?, 0)", (item_id, tag_id))


def resolve_storage_path(zotero_root: str, attachment_key: str, rel_path: str) -> str:
    # rel_path like "storage:filename.pdf"
    if not rel_path.startswith("storage:"):
        raise ValueError(f"Unsupported attachment path: {rel_path}")
    filename = rel_path.split("storage:", 1)[1]
    return os.path.join(zotero_root, "storage", attachment_key, filename)


def list_pdf_attachments(conn: sqlite3.Connection, zotero_root: str, parent_item_id: int) -> list[Attachment]:
    rows = conn.execute(
        """
        SELECT a.itemID AS attachmentItemID, a.path AS relPath, a.contentType AS contentType, i.key AS itemKey
        FROM itemAttachments a
        JOIN items i ON i.itemID = a.itemID
        WHERE a.parentItemID = ?
          AND a.path LIKE 'storage:%'
          AND a.contentType IS NOT NULL
          AND (a.contentType = 'application/pdf' OR a.contentType LIKE '%pdf%')
        """,
        (parent_item_id,),
    ).fetchall()

    out: list[Attachment] = []
    for r in rows:
        out.append(
            Attachment(
                attachment_item_id=int(r["attachmentItemID"]),
                file_path=resolve_storage_path(zotero_root, str(r["itemKey"]), str(r["relPath"])),
            )
        )
    return out


def pdf_pages(pdf_path: str) -> int:
    try:
        proc = subprocess.run(
            ["pdfinfo", pdf_path],
            text=True,
            errors="ignore",
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        info = proc.stdout or ""
    except FileNotFoundError as e:
        raise SystemExit("Missing `pdfinfo` (poppler). Install poppler to continue.") from e
    m = re.search(r"^Pages:\s+(\d+)\s*$", info, flags=re.M)
    return int(m.group(1)) if m else 1


def pdftotext_page(pdf_path: str, page: int) -> str:
    try:
        proc = subprocess.run(
            ["pdftotext", "-layout", "-f", str(page), "-l", str(page), pdf_path, "-"],
            text=True,
            errors="ignore",
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return proc.stdout or ""
    except FileNotFoundError as e:
        raise SystemExit("Missing `pdftotext` (poppler). Install poppler to continue.") from e


def find_definitional_excerpts(pdf_path: str, patterns: list[re.Pattern], max_pages: int | None = None) -> list[tuple[int, str]]:
    pages = pdf_pages(pdf_path)
    if max_pages:
        pages = min(pages, max_pages)
    hits: list[tuple[int, str]] = []
    for p in range(1, pages + 1):
        text = pdftotext_page(pdf_path, p)
        if not any(pat.search(text) for pat in patterns):
            continue
        lines = text.splitlines()
        for idx, line in enumerate(lines):
            if not any(pat.search(line) for pat in patterns):
                continue
            ctx_lines = lines[max(0, idx - 2) : min(len(lines), idx + 3)]
            ctx = "\n".join(l.rstrip() for l in ctx_lines).strip()
            if ctx:
                hits.append((p, ctx))
    # Deduplicate (page+ctx)
    seen: set[tuple[int, str]] = set()
    out: list[tuple[int, str]] = []
    for p, ctx in hits:
        key = (p, ctx)
        if key in seen:
            continue
        seen.add(key)
        out.append((p, ctx))
    return out


def random_key(conn: sqlite3.Connection, library_id: int) -> str:
    # Zotero item keys avoid 0, 1, and O (observed in existing DB).
    alphabet = "23456789" + "ABCDEFGHIJKLMNPQRSTUVWXYZ"
    while True:
        k = "".join(random.choice(alphabet) for _ in range(8))
        exists = conn.execute("SELECT 1 FROM items WHERE libraryID = ? AND key = ?", (library_id, k)).fetchone()
        if not exists:
            return k


def note_item_type_id(conn: sqlite3.Connection) -> int:
    row = conn.execute("SELECT itemTypeID FROM itemTypes WHERE typeName = 'note'").fetchone()
    if not row:
        raise RuntimeError("Could not find itemTypeID for note")
    return int(row["itemTypeID"])


def upsert_note(
    conn: sqlite3.Connection,
    parent_item_id: int,
    title: str,
    html_note: str,
) -> tuple[int, bool]:
    existing = conn.execute(
        "SELECT itemID FROM itemNotes WHERE parentItemID = ? AND title = ?",
        (parent_item_id, title),
    ).fetchone()
    if existing:
        note_item_id = int(existing["itemID"])
        conn.execute("UPDATE itemNotes SET note = ? WHERE itemID = ?", (html_note, note_item_id))
        conn.execute("UPDATE items SET dateModified = CURRENT_TIMESTAMP, clientDateModified = CURRENT_TIMESTAMP WHERE itemID = ?", (note_item_id,))
        return note_item_id, False

    lib_row = conn.execute("SELECT libraryID FROM items WHERE itemID = ?", (parent_item_id,)).fetchone()
    if not lib_row:
        raise RuntimeError(f"Missing parent item: {parent_item_id}")
    library_id = int(lib_row["libraryID"])

    key = random_key(conn, library_id)
    item_type_id = note_item_type_id(conn)
    cur = conn.execute(
        "INSERT INTO items (itemTypeID, libraryID, key) VALUES (?, ?, ?)",
        (item_type_id, library_id, key),
    )
    note_item_id = int(cur.lastrowid)
    conn.execute(
        "INSERT INTO itemNotes (itemID, parentItemID, note, title) VALUES (?, ?, ?, ?)",
        (note_item_id, parent_item_id, html_note, title),
    )
    return note_item_id, True


def html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def build_note_html(source_path: str, excerpts: Iterable[tuple[int, str]]) -> str:
    parts: list[str] = []
    parts.append("<div class=\"codex-extract\">")
    parts.append(f"<p><strong>Quelle (PDF):</strong> {html_escape(source_path)}</p>")
    parts.append("<p><strong>Extrakte (Treffer auf Muster):</strong></p>")
    parts.append("<ol>")
    for page, ctx in excerpts:
        ctx_norm = re.sub(r"[ \t]+", " ", ctx).strip()
        parts.append("<li>")
        parts.append(f"<p><strong>Seite {page}</strong></p>")
        parts.append(f"<blockquote><pre>{html_escape(ctx_norm)}</pre></blockquote>")
        parts.append("</li>")
    parts.append("</ol>")
    parts.append("</div>")
    return "\n".join(parts)


def default_candidate_item_ids(conn: sqlite3.Connection) -> list[int]:
    rows = conn.execute(PLACEHOLDER_REASONS_SQL).fetchall()
    return sorted({int(r["itemID"]) for r in rows})


def wide_candidate_item_ids(conn: sqlite3.Connection) -> list[int]:
    rows = conn.execute(WIDE_CANDIDATES_SQL).fetchall()
    return sorted({int(r["itemID"]) for r in rows})


def already_noted_parent_ids(conn: sqlite3.Connection, note_title: str) -> set[int]:
    rows = conn.execute(
        "SELECT DISTINCT parentItemID AS itemID FROM itemNotes WHERE parentItemID IS NOT NULL AND title = ?",
        (note_title,),
    ).fetchall()
    return {int(r["itemID"]) for r in rows if r["itemID"] is not None}


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract definitional 'Wirkung' excerpts from PDFs and write as Zotero item notes.")
    ap.add_argument("--db", default=os.path.expanduser("~/Zotero/zotero.sqlite"))
    ap.add_argument("--zotero-root", default=os.path.expanduser("~/Zotero"))
    ap.add_argument("--tag", default=DEFAULT_TAG)
    ap.add_argument("--note-title", default=NOTE_TITLE)
    ap.add_argument(
        "--mode",
        choices=["strict", "wide"],
        default="strict",
        help="Candidate selection + regex strictness (default: strict).",
    )
    ap.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Max pages per PDF to scan (default: strict=250, wide=80).",
    )
    ap.add_argument(
        "--max-excerpts",
        type=int,
        default=20,
        help="Max excerpts per PDF (default: 20).",
    )
    ap.add_argument(
        "--limit-items",
        type=int,
        default=None,
        help="Limit number of parent items processed (default: no limit).",
    )
    ap.add_argument(
        "--skip-already-noted",
        action="store_true",
        help="Skip parent items that already have a note with --note-title.",
    )
    ap.add_argument(
        "--item-id",
        action="append",
        type=int,
        help="Parent Zotero itemID to process (repeatable). If omitted, auto-detect candidates.",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    db_path = os.path.abspath(args.db)
    zotero_root = os.path.abspath(args.zotero_root)
    if not os.path.exists(db_path):
        raise SystemExit(f"DB not found: {db_path}")
    if not os.path.isdir(zotero_root):
        raise SystemExit(f"Zotero root not found: {zotero_root}")

    ensure_zotero_not_running(db_path)

    backup_path = backup_db(db_path) if not args.dry_run else None

    conn = connect(db_path)
    try:
        if args.item_id:
            item_ids = args.item_id
        else:
            item_ids = wide_candidate_item_ids(conn) if args.mode == "wide" else default_candidate_item_ids(conn)
        if args.limit_items is not None:
            item_ids = item_ids[: args.limit_items]
        if args.skip_already_noted:
            done = already_noted_parent_ids(conn, args.note_title)
            item_ids = [i for i in item_ids if i not in done]
            if args.limit_items is not None:
                item_ids = item_ids[: args.limit_items]
        tag_id = get_tag_id(conn, args.tag)

        if args.mode == "wide":
            patterns = [
                re.compile(r"\bWirkungsforschung\b", re.I),
                re.compile(r"\bWirksamkeit\b", re.I),
                re.compile(r"\bWirkungsorient\w*\b", re.I),
                re.compile(r"\bWirkung(en)?\b", re.I),
                re.compile(r"\b(effect|impact|outcome)\b", re.I),
                re.compile(
                    r"\b(Definition|definier\w*|bezeichnet|verstanden|versteht man|meint|Wirkung ist|Unter Wirkung|is defined|refers to|means)\b",
                    re.I,
                ),
            ]
        else:
            patterns = [
                re.compile(r"\bWirkungsforschung\b", re.I),
                re.compile(r"\bWirkung(en)?\b", re.I),
                re.compile(r"\bBegriff\b", re.I),
                re.compile(r"\bDefinition\b", re.I),
            ]

        written = 0
        updated = 0
        processed_pdfs = 0
        empty_pdfs = 0

        if not args.dry_run:
            conn.execute("BEGIN IMMEDIATE")

        for parent_item_id in item_ids:
            pdfs = list_pdf_attachments(conn, zotero_root, parent_item_id)
            if not pdfs:
                continue

            if not args.dry_run:
                ensure_item_tag(conn, parent_item_id, tag_id)

            for att in pdfs:
                if not os.path.exists(att.file_path):
                    continue
                processed_pdfs += 1
                max_pages = args.max_pages
                if max_pages is None:
                    max_pages = 80 if args.mode == "wide" else 250
                excerpts = find_definitional_excerpts(att.file_path, patterns, max_pages=max_pages)
                if args.max_excerpts is not None:
                    excerpts = excerpts[: args.max_excerpts]
                if not excerpts:
                    empty_pdfs += 1
                    continue
                if not args.dry_run:
                    html = build_note_html(att.file_path, excerpts)
                    _note_id, created = upsert_note(conn, parent_item_id, args.note_title, html)
                    if created:
                        written += 1
                    else:
                        updated += 1

        if not args.dry_run:
            conn.commit()

        print("Zotero extract report")
        print(f"DB: {db_path}")
        if backup_path:
            print(f"Backup: {backup_path}")
        print(f"Candidate parent items scanned: {len(item_ids)}")
        print(f"PDFs processed: {processed_pdfs}")
        print(f"PDFs with no excerpts: {empty_pdfs}")
        if args.dry_run:
            print("Dry-run: no notes written, no tags applied.")
        else:
            print(f"Notes created: {written}")
            print(f"Notes updated: {updated}")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
