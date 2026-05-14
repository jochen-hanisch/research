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

## Bibkeys

`zotero_generate_bibkeys.js` erzeugt aus Zotero-JSON deterministische BibTeX-/Pandoc-Keys. Es schreibt nicht nach Zotero.

Beispiel:

```bash
node tools/zotero/zotero_generate_bibkeys.js zotero-items.json --format csv
```

Unterstützt werden JSON-Arrays aus der Zotero-API sowie Objekte mit einem Feld `items`.
