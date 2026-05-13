---
author: Jochen Hanisch-Johannsen
title: README
versioned: false
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2026-05-11
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
# TEI-Bildungswirkgefüge: TEI-gestützte Simulation von Neugier, Motivation und Kompetenzentwicklung (Gesundheitsberufe) [Python]

Dieses Zenodo-Paket enthält die TEI-gestützte Anwendung `tei-bildungswirkgefuege.py`. Sie verbindet TEI-Daten (Training Evaluation Inventory) über mehrere Handlungssituationen mit der Simulation des digitalen Bildungswirkgefüges (Neugier, Motivation, Kompetenzentwicklung) und erzeugt Kennwerte, CSV-Exports und Plotly-Dashboards.

## Veröffentlichung

Zenodo: https://zenodo.org/records/18051116
DOI: `10.5281/zenodo.18051116`

## Inhalt

- `tei-bildungswirkgefuege.py` – Hauptskript (TEI-Import + Simulation + Visualisierung)
- `config_bildungswirkgefuege.py` – Basis-Konfiguration (z. B. `initial_neugier`, `start_kompetenz`, `selected_archetyp`)
- `modellpruefung.py` – optionale Modellprüfung (über `config_bildungswirkgefuege.py`)
- `TEI/Daten/` – Platzhalterordner für TEI-Dateien (Excel/CSV)

## Voraussetzungen

- Python `>= 3.10`
- Pakete: siehe `requirements.txt`

Hinweis: Das Skript nutzt projektspezifische Module, die in diesem Paket **nicht** enthalten sind:

- `ci_template` (Plotly-Theme/CI) – wird über `CI_TEMPLATE_PATH` gesucht
- `archetypen` (Archetypen/Parameter) – muss im `PYTHONPATH` liegen

## TEI-Daten (Input)

Das Skript lädt TEI-Dateien aus einem Verzeichnis (Default: `TEI/Daten/`) oder via Umgebungsvariablen:

- `BILDWIRK_TEI_DIR` (Verzeichnis mit TEI-Dateien)
- `BILDWIRK_TEI_FILE_GLOB` (Default: `*.xlsx`)
- `BILDWIRK_TEI_EXCEL_SHEET` (Default: `TEI`)
- optional: `BILDWIRK_TEI_EXCEL_PATH` (einzelne Datei statt Ordner)

## Ausführung

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 tei-bildungswirkgefuege.py
```

## Exporte/Outputs

- `BILDWIRK_EXPORT_ROOT` (CSV/Logs; Default: `~/Documents/scripte/.../Modellpruefung`)
- `BILDWIRK_TEI_EXPORT_ROOT` (TEI-spezifische Logs/Reports; Default: `<BILDWIRK_EXPORT_ROOT>/tei-modellpruefung`)
- `BILDWIRK_PNG_DIR` (PNGs)

## Lizenz / Nutzung

Dieses Paket ist **proprietär** (alle Rechte vorbehalten). Eine Nutzung/Weitergabe ist nur mit expliziter schriftlicher Genehmigung des Rechteinhabers erlaubt.
