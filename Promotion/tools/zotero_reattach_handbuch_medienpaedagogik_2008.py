#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import sqlite3
from dataclasses import dataclass


PLACEHOLDER_RE = re.compile(r"978-3-531-91158-8_(\d+)")
TARGET_DOI_RE = re.compile(r"10\.1007/978-3-531-91158-8_(\d+)$")


@dataclass(frozen=True)
class ItemRef:
    item_id: int
    chapter: str
    value: str


def ensure_zotero_not_running(db_path: str) -> None:
    # Heuristic: Zotero usually creates WAL/SHM when open.
    wal = db_path + "-wal"
    shm = db_path + "-shm"
    if os.path.exists(wal) or os.path.exists(shm):
        raise SystemExit(
            f"Refusing to modify while WAL/SHM exist. Please close Zotero first.\n"
            f"Found: {wal if os.path.exists(wal) else ''} {shm if os.path.exists(shm) else ''}".strip()
        )


def backup_db(db_path: str) -> str:
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = f"{db_path}.codex-reattach-handbuch-2008.{ts}.bak"
    shutil.copy2(db_path, backup_path)
    return backup_path


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def load_placeholders(conn: sqlite3.Connection) -> dict[str, list[ItemRef]]:
    # title fieldID = 1
    rows = conn.execute(
        """
        SELECT i.itemID AS itemID, v.value AS title
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID AND d.fieldID = 1
        JOIN itemDataValues v ON v.valueID = d.valueID
        WHERE v.value LIKE '978-3-531-91158-8_%'
        """
    ).fetchall()

    out: dict[str, list[ItemRef]] = {}
    for r in rows:
        title = (r["title"] or "").strip()
        m = PLACEHOLDER_RE.search(title)
        if not m:
            continue
        chap = m.group(1)
        out.setdefault(chap, []).append(ItemRef(int(r["itemID"]), chap, title))
    return out


def load_targets(conn: sqlite3.Connection) -> dict[str, ItemRef]:
    # DOI fieldID = 59
    rows = conn.execute(
        """
        SELECT i.itemID AS itemID, v.value AS doi
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID AND d.fieldID = 59
        JOIN itemDataValues v ON v.valueID = d.valueID
        WHERE v.value LIKE '10.1007/978-3-531-91158-8_%'
        """
    ).fetchall()

    out: dict[str, ItemRef] = {}
    for r in rows:
        doi = (r["doi"] or "").strip()
        m = TARGET_DOI_RE.search(doi)
        if not m:
            continue
        chap = m.group(1)
        out[chap] = ItemRef(int(r["itemID"]), chap, doi)
    return out


def get_pdf_attachments(conn: sqlite3.Connection, parent_item_id: int) -> list[int]:
    rows = conn.execute(
        """
        SELECT itemID, contentType
        FROM itemAttachments
        WHERE parentItemID = ?
          AND contentType IS NOT NULL
          AND (contentType = 'application/pdf' OR contentType LIKE '%pdf%')
        """,
        (parent_item_id,),
    ).fetchall()
    return [int(r["itemID"]) for r in rows]


def move_item_tags(conn: sqlite3.Connection, src_item_id: int, dst_item_id: int) -> int:
    # Copy itemTags rows, ignore duplicates
    rows = conn.execute("SELECT tagID FROM itemTags WHERE itemID = ?", (src_item_id,)).fetchall()
    if not rows:
        return 0
    tag_ids = {int(r["tagID"]) for r in rows}
    if not tag_ids:
        return 0
    existing = conn.execute("SELECT tagID FROM itemTags WHERE itemID = ?", (dst_item_id,)).fetchall()
    existing_ids = {int(r["tagID"]) for r in existing}
    to_add = sorted(tag_ids - existing_ids)
    for tag_id in to_add:
        conn.execute("INSERT INTO itemTags (itemID, tagID) VALUES (?, ?)", (dst_item_id, tag_id))
    return len(to_add)


def move_collection_membership(conn: sqlite3.Connection, src_item_id: int, dst_item_id: int) -> int:
    rows = conn.execute(
        "SELECT collectionID FROM collectionItems WHERE itemID = ?", (src_item_id,)
    ).fetchall()
    if not rows:
        return 0
    col_ids = {int(r["collectionID"]) for r in rows}
    existing = conn.execute(
        "SELECT collectionID FROM collectionItems WHERE itemID = ?", (dst_item_id,)
    ).fetchall()
    existing_ids = {int(r["collectionID"]) for r in existing}
    to_add = sorted(col_ids - existing_ids)
    for col_id in to_add:
        conn.execute(
            "INSERT INTO collectionItems (collectionID, itemID) VALUES (?, ?)", (col_id, dst_item_id)
        )
    return len(to_add)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Reattach PDF child attachments from placeholder Handbuch Medienpädagogik chapter items "
            "(title like 978-3-531-91158-8_XX) to DOI-created chapter items "
            "(DOI 10.1007/978-3-531-91158-8_XX)."
        )
    )
    ap.add_argument(
        "--db",
        default=os.path.expanduser("~/Zotero/zotero.sqlite"),
        help="Path to zotero.sqlite (default: ~/Zotero/zotero.sqlite)",
    )
    ap.add_argument("--dry-run", action="store_true", help="Only report, don't modify DB.")
    ap.add_argument(
        "--move-tags",
        action="store_true",
        help="Also copy tags from placeholder items to target items.",
    )
    ap.add_argument(
        "--move-collections",
        action="store_true",
        help="Also copy collection membership from placeholder items to target items.",
    )
    args = ap.parse_args()

    db_path = os.path.abspath(args.db)
    if not os.path.exists(db_path):
        raise SystemExit(f"DB not found: {db_path}")

    ensure_zotero_not_running(db_path)

    backup_path = None
    if not args.dry_run:
        backup_path = backup_db(db_path)

    conn = connect(db_path)
    try:
        placeholders = load_placeholders(conn)
        targets = load_targets(conn)

        missing_targets = sorted([c for c in placeholders.keys() if c not in targets], key=lambda x: int(x))
        missing_placeholders = sorted([c for c in targets.keys() if c not in placeholders], key=lambda x: int(x))

        moved_attachments = 0
        moved_tags = 0
        moved_collections = 0

        # Transaction for modifications
        if not args.dry_run:
            conn.execute("BEGIN IMMEDIATE")

        for chap, ph_items in placeholders.items():
            target = targets.get(chap)
            if not target:
                continue

            for ph in ph_items:
                att_ids = get_pdf_attachments(conn, ph.item_id)
                for att_id in att_ids:
                    if not args.dry_run:
                        conn.execute(
                            "UPDATE itemAttachments SET parentItemID = ? WHERE itemID = ?",
                            (target.item_id, att_id),
                        )
                    moved_attachments += 1

                if args.move_tags:
                    if not args.dry_run:
                        moved_tags += move_item_tags(conn, ph.item_id, target.item_id)
                    else:
                        moved_tags += 0
                if args.move_collections:
                    if not args.dry_run:
                        moved_collections += move_collection_membership(conn, ph.item_id, target.item_id)
                    else:
                        moved_collections += 0

        if not args.dry_run:
            conn.commit()

        print("Handbuch Medienpädagogik – Reattach report")
        print(f"DB: {db_path}")
        if backup_path:
            print(f"Backup: {backup_path}")
        print(f"Placeholders (chapters): {len(placeholders)}")
        print(f"Targets (chapters): {len(targets)}")
        print(f"Moved PDF attachments: {moved_attachments}")
        if args.move_tags:
            print(f"Copied tags: {moved_tags}")
        if args.move_collections:
            print(f"Copied collections: {moved_collections}")
        print(f"Missing DOI targets: {', '.join(missing_targets) if missing_targets else '-'}")
        print(f"Missing placeholders: {', '.join(missing_placeholders) if missing_placeholders else '-'}")

        if args.dry_run:
            print("Dry-run: no changes written.")

        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())

