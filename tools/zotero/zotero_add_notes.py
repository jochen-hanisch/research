#!/usr/bin/env python3
import argparse
import getpass
import json
import sys
import urllib.error
import urllib.request


ZOTERO_API_BASE = "https://api.zotero.org"
API_VERSION = "3"


def http_json(method: str, url: str, api_key: str, body_obj=None):
    data = None
    headers = {
        "Zotero-API-Version": API_VERSION,
        "Zotero-API-Key": api_key,
        "Accept": "application/json",
    }
    if body_obj is not None:
        encoded = json.dumps(body_obj).encode("utf-8")
        data = encoded
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            if not raw:
                return resp.status, None
            return resp.status, json.loads(raw)
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        return e.code, raw


def get_attachment_item(user_id: str, attachment_key: str, api_key: str):
    url = f"{ZOTERO_API_BASE}/users/{user_id}/items/{attachment_key}?format=json"
    status, payload = http_json("GET", url, api_key)
    if status != 200:
        raise RuntimeError(f"GET attachment {attachment_key} failed ({status}): {payload}")
    return payload


def list_child_notes(user_id: str, parent_key: str, api_key: str):
    url = f"{ZOTERO_API_BASE}/users/{user_id}/items/{parent_key}/children?itemType=note&format=json&limit=100"
    status, payload = http_json("GET", url, api_key)
    if status != 200:
        raise RuntimeError(f"GET children notes for {parent_key} failed ({status}): {payload}")
    return payload or []


def create_note(user_id: str, parent_key: str, note_html: str, tags: list[str], api_key: str):
    url = f"{ZOTERO_API_BASE}/users/{user_id}/items"
    item = {
        "itemType": "note",
        "parentItem": parent_key,
        "note": note_html,
        "tags": [{"tag": t} for t in (tags or [])],
    }
    status, payload = http_json("POST", url, api_key, body_obj=[item])
    if status not in (200, 201):
        raise RuntimeError(f"POST note failed ({status}): {payload}")
    return payload


def main():
    parser = argparse.ArgumentParser(
        description="Create Zotero child notes for items referenced by attachment keys (e.g. Zotero/storage/XXXXXXXX)."
    )
    parser.add_argument("--user-id", required=True, help="Zotero user ID, e.g. 6542084")
    parser.add_argument("--notes-file", required=True, help="JSON file with attachmentKey + noteHtml")
    parser.add_argument("--dry-run", action="store_true", help="Resolve parent items and print actions, do not write")
    args = parser.parse_args()

    try:
        with open(args.notes_file, "r", encoding="utf-8") as f:
            notes = json.load(f)
    except Exception as e:
        print(f"Failed to read notes file: {e}", file=sys.stderr)
        return 2

    api_key = getpass.getpass("Zotero API key (will not echo): ").strip()
    if not api_key:
        print("No API key provided.", file=sys.stderr)
        return 2

    marker = "<!-- codex:methodenkritik:04-04 -->"

    for entry in notes:
        attachment_key = entry.get("attachmentKey")
        if not attachment_key or len(attachment_key) != 8:
            print(f"Skip invalid attachmentKey: {attachment_key!r}", file=sys.stderr)
            continue

        short_title = entry.get("shortTitle", attachment_key)
        tags = entry.get("tags") or []
        note_html = entry.get("noteHtml") or ""
        if marker not in note_html:
            note_html = marker + note_html

        try:
            attachment = get_attachment_item(args.user_id, attachment_key, api_key)
        except Exception as e:
            print(f"[{attachment_key}] {short_title}: failed to resolve attachment: {e}", file=sys.stderr)
            continue

        parent_key = (attachment.get("data") or {}).get("parentItem") or attachment_key

        try:
            existing = list_child_notes(args.user_id, parent_key, api_key)
            already = any(marker in ((it.get("data") or {}).get("note") or "") for it in existing)
        except Exception as e:
            print(f"[{attachment_key}] {short_title}: failed to list existing notes: {e}", file=sys.stderr)
            continue

        if already:
            print(f"[{attachment_key}] {short_title}: skip (note marker already present) parent={parent_key}")
            continue

        if args.dry_run:
            print(f"[{attachment_key}] {short_title}: would create note parent={parent_key}")
            continue

        try:
            create_note(args.user_id, parent_key, note_html, tags, api_key)
            print(f"[{attachment_key}] {short_title}: created note parent={parent_key}")
        except Exception as e:
            print(f"[{attachment_key}] {short_title}: failed to create note: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

