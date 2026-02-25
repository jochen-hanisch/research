#!/usr/bin/env python3
"""
Audit Zotero attachments for missing local files and non-synced link modes.

Typical use:
  python3 tools/zotero_audit_missing_attachments.py --db ~/Zotero/zotero.sqlite --pdf-only

This is read-only and safe to run while Zotero is open (uses SQLite immutable mode).
"""

from __future__ import annotations

import argparse
import csv
import os
import sqlite3
import sys
from dataclasses import dataclass
from typing import Iterable, Optional


LINK_MODE_LABELS = {
    0: "imported_file (synced)",
    1: "imported_url (synced)",
    2: "linked_file (NOT synced)",
    3: "linked_url (NOT synced)",
    4: "embedded_image (synced?)",
}


@dataclass(frozen=True)
class AttachmentRow:
    attachment_item_id: int
    attachment_key: str
    parent_item_id: Optional[int]
    title: str
    parent_title: str
    link_mode: int
    content_type: str
    path: Optional[str]

    def link_mode_label(self) -> str:
        return LINK_MODE_LABELS.get(self.link_mode, f"unknown({self.link_mode})")


def zotero_storage_dir(db_path: str) -> str:
    # Default Zotero data dir is the folder containing zotero.sqlite
    return os.path.join(os.path.dirname(os.path.abspath(db_path)), "storage")


def resolve_attachment_file_path(db_path: str, row: AttachmentRow) -> Optional[str]:
    if not row.path:
        return None

    if row.link_mode == 0 and row.path.startswith("storage:"):
        filename = row.path.split("storage:", 1)[1]
        return os.path.join(zotero_storage_dir(db_path), row.attachment_key, filename)

    if row.link_mode == 2:
        return row.path

    return None


def connect_immutable(db_path: str) -> sqlite3.Connection:
    # Immutable mode bypasses locks; good for auditing while Zotero is open.
    uri = f"file:{os.path.abspath(db_path)}?immutable=1"
    return sqlite3.connect(uri, uri=True)


def fetch_attachments(conn: sqlite3.Connection, pdf_only: bool) -> Iterable[AttachmentRow]:
    where = ""
    params: list[object] = []
    if pdf_only:
        where = "WHERE ia.contentType = ?"
        params.append("application/pdf")

    # Titles:
    # - attachment title stored in itemData (fieldID=1) OR filename; we keep itemData title if present.
    # - parent title similarly.
    sql = f"""
        WITH titles AS (
          SELECT id.itemID,
                 MAX(CASE WHEN f.fieldName = 'title' THEN v.value END) AS title
          FROM itemData id
          JOIN fields f ON f.fieldID = id.fieldID
          JOIN itemDataValues v ON v.valueID = id.valueID
          GROUP BY id.itemID
        )
        SELECT
          i.itemID AS attachmentItemID,
          i.key AS attachmentKey,
          ia.parentItemID,
          COALESCE(t.title, '') AS attachmentTitle,
          COALESCE(pt.title, '') AS parentTitle,
          ia.linkMode,
          COALESCE(ia.contentType, '') AS contentType,
          ia.path
        FROM items i
        JOIN itemAttachments ia ON ia.itemID = i.itemID
        LEFT JOIN titles t ON t.itemID = i.itemID
        LEFT JOIN titles pt ON pt.itemID = ia.parentItemID
        {where}
        ORDER BY ia.parentItemID, i.itemID;
    """

    cur = conn.execute(sql, params)
    for (
        attachment_item_id,
        attachment_key,
        parent_item_id,
        attachment_title,
        parent_title,
        link_mode,
        content_type,
        path,
    ) in cur.fetchall():
        yield AttachmentRow(
            attachment_item_id=int(attachment_item_id),
            attachment_key=str(attachment_key),
            parent_item_id=int(parent_item_id) if parent_item_id is not None else None,
            title=str(attachment_title or ""),
            parent_title=str(parent_title or ""),
            link_mode=int(link_mode),
            content_type=str(content_type or ""),
            path=str(path) if path is not None else None,
        )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=os.path.expanduser("~/Zotero/zotero.sqlite"))
    ap.add_argument("--pdf-only", action="store_true", help="Only check PDF attachments")
    ap.add_argument(
        "--out",
        default="",
        help="Write CSV report to this path (optional). If omitted, prints a short summary.",
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of reported rows (0 = no limit)",
    )
    args = ap.parse_args()

    if not os.path.exists(args.db):
        print(f"DB not found: {args.db}", file=sys.stderr)
        return 2

    conn = connect_immutable(args.db)
    rows = list(fetch_attachments(conn, pdf_only=bool(args.pdf_only)))

    missing_local: list[tuple[AttachmentRow, str]] = []
    not_synced: list[AttachmentRow] = []
    has_no_resolvable_path: list[AttachmentRow] = []

    for row in rows:
        resolved = resolve_attachment_file_path(args.db, row)
        if row.link_mode in (2, 3):
            not_synced.append(row)
        if resolved is None:
            has_no_resolvable_path.append(row)
            continue
        if row.link_mode == 0 and row.path and row.path.startswith("storage:"):
            if not os.path.exists(resolved):
                missing_local.append((row, resolved))

    if args.out:
        out_path = os.path.abspath(os.path.expanduser(args.out))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "parentItemID",
                    "attachmentItemID",
                    "attachmentKey",
                    "parentTitle",
                    "attachmentTitle",
                    "linkMode",
                    "linkModeLabel",
                    "contentType",
                    "path",
                    "resolvedLocalPath",
                    "localFileExists",
                ]
            )
            count = 0
            for row in rows:
                resolved = resolve_attachment_file_path(args.db, row) or ""
                exists = "1" if (resolved and os.path.exists(resolved)) else "0"
                w.writerow(
                    [
                        row.parent_item_id or "",
                        row.attachment_item_id,
                        row.attachment_key,
                        row.parent_title,
                        row.title,
                        row.link_mode,
                        row.link_mode_label(),
                        row.content_type,
                        row.path or "",
                        resolved,
                        exists,
                    ]
                )
                count += 1
                if args.limit and count >= args.limit:
                    break
        print(out_path)
        return 0

    def fmt_row(r: AttachmentRow) -> str:
        parent = f"{r.parent_item_id}" if r.parent_item_id is not None else "—"
        parent_title = (r.parent_title or "").strip()
        parent_title = parent_title if len(parent_title) <= 60 else parent_title[:57] + "..."
        return f"parent {parent} | {r.link_mode_label():>22} | {parent_title}"

    print(f"Attachments checked: {len(rows)} (pdf_only={bool(args.pdf_only)})")
    print(f"Missing local files (imported_file): {len(missing_local)}")
    print(f"Not synced link modes (linked_*): {len(not_synced)}")

    show = missing_local[: min(len(missing_local), 15 if not args.limit else args.limit)]
    if show:
        print("\nExamples missing local file:")
        for row, resolved in show:
            print(f"- {fmt_row(row)} -> {resolved}")

    show2 = not_synced[: min(len(not_synced), 15)]
    if show2:
        print("\nExamples NOT synced (linked_*):")
        for row in show2:
            print(f"- {fmt_row(row)} | path={row.path or ''}")

    if missing_local:
        print(
            "\nInterpretation: These are 'imported_file' attachments whose expected file is missing in Zotero/storage.\n"
            "If file syncing (WebDAV) works, Zotero should download them on demand. If it doesn't, check Sync errors/Verify Server."
        )
    if not_synced:
        print(
            "\nInterpretation: These are linked attachments; they never sync via WebDAV/Zotero.\n"
            "Fix by re-attaching as 'stored copy' (import) instead of linking."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

