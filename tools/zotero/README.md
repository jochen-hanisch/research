---
author: Jochen Hanisch-Johannsen
title: Zotero Tools
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication:
created: 2026-05-14
updated: 2026-05-14
publish: false
published:
status:
priority:
project: Research
due:
tags: []
---
# Zotero Tools

Dieser Ordner enthält Research-weite Zotero-Werkzeuge. Einige Skripte lesen nur aus Zotero oder lokalen Exporten, andere schreiben Tags, Notizen oder lokale SQLite-Daten. Schreibende Skripte nur nach ausdrücklicher Freigabe ausführen.

## Sicherheitslogik

- `API` bedeutet Zugriff über die Zotero-Web-API. Schreibzugriffe benötigen einen Zotero-API-Key.
- `lokale SQLite` bedeutet direkter Zugriff auf `~/Zotero/zotero.sqlite`. Schreibende lokale Werkzeuge legen Backups an und sollen nur bei geschlossenem Zotero laufen.
- `lesend` darf zur Bestandsaufnahme genutzt werden.
- `schreibend` verändert Zotero, lokale Zotero-Daten oder Metadaten und braucht vorher eine ausdrückliche Freigabe.

## Skriptmatrix

| Skript | Zugriff | Wirkung | Typischer Einsatz |
|---|---|---|---|
| `zotero_generate_bibkeys.js` | lokale JSON-Datei, lesend | erzeugt deterministische BibTeX-/Pandoc-Keys aus Zotero-JSON | schnelle Key-Vorschläge ohne Zotero-Schreibzugriff |
| `zotero_audit_missing_attachments.py` | lokale SQLite, lesend | prüft Anhänge, Link-Modi und fehlende lokale Dateien | Audit vor Aufräumarbeiten oder Sync-Kontrollen |
| `zotero_tag_sections.py` | Zotero-API, optional schreibend | ordnet Pandoc-Citekeys aus Markdown-Dateien Abschnitten zu und setzt Zotero-Tags | Kapitel-/Abschnittsnachweis in Zotero über API |
| `zotero_sync_section_tags.py` | Zotero-API, schreibend | synchronisiert Abschnitts- und Kapitel-Tags, entfernt veraltete Tags aus berührten Parent-Items | aktuelle Markdown-Zitationen als Quelle der Zotero-Tags |
| `zotero_tag_sections_local.py` | lokale SQLite, schreibend | setzt Abschnitts-/Kapitel-Tags direkt in der lokalen Zotero-Datenbank | lokale Alternative zur API, nur mit Backup und geschlossenem Zotero |
| `zotero_add_notes.py` | Zotero-API, schreibend | legt Child-Notes an Zotero-Items oder Attachments an | methodische Notizen aus vorbereiteten JSON-Dateien einspielen |
| `zotero_add_notes_local.py` | lokale SQLite, schreibend | legt Child-Notes direkt lokal an und nutzt Dedupe-Marker | lokale Notizergänzung mit Backup und geschlossenem Zotero |
| `zotero_extract_wirkung_definitions_to_notes.py` | lokale SQLite und PDF-Text, schreibend | sucht Wirkungs-/Definitionsspuren und erzeugt daraus Zotero-Notizen | gezielte Begriffs- und Wirkungsdefinitionen für die Dissertation sichern |
| `zotero_fix_invalid_note_item_keys.py` | lokale SQLite, schreibend | repariert ungültige Zotero-Item-Keys bei Notizen | technische Reparatur nach fehlerhaften lokalen Note-Keys |
| `zotero_reattach_handbuch_medienpaedagogik_2008.py` | lokale SQLite, schreibend | verknüpft Handbuch-Medienpädagogik-Kapitel/Anhänge neu | einmalige Reparatur-/Konsolidierungsaufgabe für diesen Quellenbestand |

## Begleitdateien

| Datei | Funktion |
|---|---|
| `zotero_notes_04-04_methodik_kritik.json` | vorbereitete Notizdaten für Methodenkritik im Kapitel `04-04` |
| `zotero_notes_04-04_methodik_kritik_more.json` | ergänzende vorbereitete Notizdaten für Methodenkritik im Kapitel `04-04` |
| `zotero_promotion_section_*.csv` | lokale Reports aus Tagging-/Sync-Läufen; werden nicht versioniert |
| `zotero_db_backups/` | lokale SQLite-Backups; werden nicht versioniert |

## Bibkeys

`zotero_generate_bibkeys.js` erzeugt aus Zotero-JSON deterministische BibTeX-/Pandoc-Keys. Es schreibt nicht nach Zotero.

Beispiel:

```bash
node tools/zotero/zotero_generate_bibkeys.js zotero-items.json --format csv
```

Unterstützt werden JSON-Arrays aus der Zotero-API sowie Objekte mit einem Feld `items`.
