#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import secrets
import shutil
import sqlite3
import sys


KEY_ALPHABET = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
NOTE_MARKER = "<!-- codex:methodenkritik:04-04 -->"


def utc_timestamp() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat(sep=" ")


def generate_item_key(cur: sqlite3.Cursor) -> str:
    while True:
        key = "".join(secrets.choice(KEY_ALPHABET) for _ in range(8))
        cur.execute("SELECT 1 FROM items WHERE key=? LIMIT 1", (key,))
        if cur.fetchone() is None:
            return key


def ensure_backup(db_path: str, backup_dir: str) -> str:
    os.makedirs(backup_dir, exist_ok=True)
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    base = os.path.basename(db_path)
    dst = os.path.join(backup_dir, f"{base}.{ts}.bak")
    shutil.copy2(db_path, dst)
    return dst


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create Zotero child notes locally by writing to zotero.sqlite (safe backup + dedupe marker)."
    )
    parser.add_argument(
        "--db",
        default=os.path.expanduser("~/Zotero/zotero.sqlite"),
        help="Path to zotero.sqlite (default: ~/Zotero/zotero.sqlite)",
    )
    parser.add_argument("--notes-file", required=True, help="JSON file with attachmentKey + noteHtml + tags")
    parser.add_argument(
        "--backup-dir",
        default=os.path.join(os.path.dirname(__file__), "zotero_db_backups"),
        help="Directory to write sqlite backups into (default: tools/zotero_db_backups)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write anything, just print actions")
    args = parser.parse_args()

    if not os.path.exists(args.db):
        print(f"DB not found: {args.db}", file=sys.stderr)
        return 2

    try:
        with open(args.notes_file, "r", encoding="utf-8") as f:
            notes = json.load(f)
    except Exception as e:
        print(f"Failed to read notes file: {e}", file=sys.stderr)
        return 2

    con = sqlite3.connect(args.db, timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("PRAGMA busy_timeout=10000")
    cur = con.cursor()

    cur.execute("SELECT itemTypeID FROM itemTypes WHERE typeName='note'")
    row = cur.fetchone()
    if row is None:
        print("Could not resolve itemTypeID for note", file=sys.stderr)
        return 2
    note_type_id = int(row[0])

    to_create = []
    for entry in notes:
        attachment_key = entry.get("attachmentKey")
        short_title = entry.get("shortTitle") or attachment_key
        tags = entry.get("tags") or []
        note_html = (entry.get("noteHtml") or "").strip()
        if not attachment_key or len(attachment_key) != 8:
            print(f"Skip invalid attachmentKey: {attachment_key!r}", file=sys.stderr)
            continue
        if not note_html:
            print(f"Skip empty noteHtml for {attachment_key}", file=sys.stderr)
            continue
        if NOTE_MARKER not in note_html:
            note_html = NOTE_MARKER + note_html

        cur.execute("SELECT itemID, libraryID FROM items WHERE key=? LIMIT 1", (attachment_key,))
        att = cur.fetchone()
        if att is None:
            print(f"[{attachment_key}] {short_title}: attachment not found in items", file=sys.stderr)
            continue

        cur.execute("SELECT parentItemID FROM itemAttachments WHERE itemID=? LIMIT 1", (att["itemID"],))
        att_row = cur.fetchone()
        parent_item_id = att_row["parentItemID"] if att_row else None
        if not parent_item_id:
            print(f"[{attachment_key}] {short_title}: parentItemID not found (is it a top-level item?)", file=sys.stderr)
            continue

        cur.execute(
            "SELECT itemID FROM itemNotes WHERE parentItemID=? AND note LIKE ? LIMIT 1",
            (parent_item_id, f"%{NOTE_MARKER}%"),
        )
        if cur.fetchone() is not None:
            print(f"[{attachment_key}] {short_title}: skip (marker note already exists) parentItemID={parent_item_id}")
            continue

        to_create.append(
            {
                "attachmentKey": attachment_key,
                "shortTitle": short_title,
                "tags": tags,
                "noteHtml": note_html,
                "parentItemID": int(parent_item_id),
            }
        )

    if args.dry_run:
        for it in to_create:
            print(
                f"[{it['attachmentKey']}] {it['shortTitle']}: would create note under parentItemID={it['parentItemID']}"
            )
        return 0

    backup_path = ensure_backup(args.db, args.backup_dir)
    print(f"Backup written: {backup_path}")

    now = utc_timestamp()
    try:
        con.execute("BEGIN IMMEDIATE")
        for it in to_create:
            parent_item_id = it["parentItemID"]
            cur.execute("SELECT libraryID FROM items WHERE itemID=? LIMIT 1", (parent_item_id,))
            parent = cur.fetchone()
            if parent is None:
                print(
                    f"[{it['attachmentKey']}] {it['shortTitle']}: parent item missing, skip",
                    file=sys.stderr,
                )
                continue
            library_id = int(parent["libraryID"])

            item_key = generate_item_key(cur)
            cur.execute(
                "INSERT INTO items (itemTypeID, dateAdded, dateModified, clientDateModified, libraryID, key, version, synced) "
                "VALUES (?, ?, ?, ?, ?, ?, 0, 0)",
                (note_type_id, now, now, now, library_id, item_key),
            )
            note_item_id = cur.lastrowid
            cur.execute(
                "INSERT INTO itemNotes (itemID, parentItemID, note, title) VALUES (?, ?, ?, ?)",
                (note_item_id, parent_item_id, it["noteHtml"], it["shortTitle"]),
            )

            for tag in it["tags"]:
                cur.execute("SELECT tagID FROM tags WHERE name=? LIMIT 1", (tag,))
                tag_row = cur.fetchone()
                if tag_row is None:
                    cur.execute("INSERT INTO tags (name) VALUES (?)", (tag,))
                    tag_id = cur.lastrowid
                else:
                    tag_id = int(tag_row["tagID"])
                cur.execute(
                    "INSERT OR IGNORE INTO itemTags (itemID, tagID, type) VALUES (?, ?, 0)",
                    (note_item_id, tag_id),
                )

            print(
                f"[{it['attachmentKey']}] {it['shortTitle']}: created note itemID={note_item_id} key={item_key} parentItemID={parent_item_id}"
            )

        con.commit()
    except sqlite3.OperationalError as e:
        con.rollback()
        print(
            f"SQLite error: {e}\nIf Zotero is running, please close it and rerun the script.",
            file=sys.stderr,
        )
        return 1
    finally:
        con.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

