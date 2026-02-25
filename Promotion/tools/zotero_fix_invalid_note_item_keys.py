#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import os
import random
import shutil
import sqlite3


VALID_KEY_ALPHABET = "23456789" + "ABCDEFGHIJKLMNPQRSTUVWXYZ"
INVALID_KEY_CHARS = set("01O")


def ensure_zotero_not_running(db_path: str) -> None:
    wal = db_path + "-wal"
    shm = db_path + "-shm"
    if os.path.exists(wal) or os.path.exists(shm):
        raise SystemExit("Zotero DB appears to be in use (WAL/SHM present). Close Zotero and retry.")


def backup_db(db_path: str) -> str:
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = f"{db_path}.codex-fix-keys.{ts}.bak"
    shutil.copy2(db_path, backup_path)
    return backup_path


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def is_valid_key(k: str) -> bool:
    if not k or len(k) != 8:
        return False
    if any(ch in INVALID_KEY_CHARS for ch in k):
        return False
    return all(ch in VALID_KEY_ALPHABET for ch in k)


def generate_key(conn: sqlite3.Connection, library_id: int) -> str:
    while True:
        k = "".join(random.choice(VALID_KEY_ALPHABET) for _ in range(8))
        exists = conn.execute(
            "SELECT 1 FROM items WHERE libraryID = ? AND key = ?",
            (library_id, k),
        ).fetchone()
        if not exists:
            return k


def main() -> int:
    ap = argparse.ArgumentParser(description="Fix invalid Zotero note item keys (avoid 0,1,O) in zotero.sqlite.")
    ap.add_argument("--db", default=os.path.expanduser("~/Zotero/zotero.sqlite"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--only-item-id",
        action="append",
        type=int,
        help="Only fix specific note itemID(s) (repeatable).",
    )
    args = ap.parse_args()

    db_path = os.path.abspath(args.db)
    if not os.path.exists(db_path):
        raise SystemExit(f"DB not found: {db_path}")

    ensure_zotero_not_running(db_path)
    backup = backup_db(db_path) if not args.dry_run else None

    conn = connect(db_path)
    try:
        if args.only_item_id:
            rows = conn.execute(
                "SELECT itemID, libraryID, key FROM items WHERE itemTypeID = 28 AND itemID IN (%s)"
                % ",".join("?" for _ in args.only_item_id),
                tuple(args.only_item_id),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT itemID, libraryID, key FROM items WHERE itemTypeID = 28 AND (key GLOB '*[01O]*' OR length(key) != 8)"
            ).fetchall()

        to_fix = []
        for r in rows:
            item_id = int(r["itemID"])
            lib_id = int(r["libraryID"])
            key = str(r["key"])
            if not is_valid_key(key):
                to_fix.append((item_id, lib_id, key))

        if not to_fix:
            print("No invalid note keys found.")
            return 0

        if not args.dry_run:
            conn.execute("BEGIN IMMEDIATE")

        fixed = 0
        for item_id, lib_id, old_key in to_fix:
            new_key = generate_key(conn, lib_id)
            if not args.dry_run:
                conn.execute("UPDATE items SET key = ? WHERE itemID = ?", (new_key, item_id))
            fixed += 1
            print(f"{item_id}\t{old_key}\t->\t{new_key}")

        if not args.dry_run:
            conn.commit()

        print(f"Fixed note keys: {fixed}")
        if backup:
            print(f"Backup: {backup}")
        if args.dry_run:
            print("Dry-run: no changes written.")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())

