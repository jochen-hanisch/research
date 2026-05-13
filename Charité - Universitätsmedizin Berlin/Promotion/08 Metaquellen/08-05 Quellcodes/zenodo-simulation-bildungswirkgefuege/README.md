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
# Simulation des digitalen Bildungswirkgefüges: Neugier, Motivation und Kompetenzentwicklung (Gesundheitsberufe) [Python]

Dieses Zenodo-Paket enthält den Python-Quellcode zur Simulation eines digitalen Bildungswirkgefüges im Kontext von Lern‑Management‑Systemen (LMS): Kompetenzentwicklung über Zeit, Monte‑Carlo‑Durchläufe, Plotly‑Visualisierungen und CSV‑Exporte.

## Veröffentlichung

Zenodo: https://zenodo.org/records/18050984
DOI: `10.5281/zenodo.18050984`

## Inhalt

- `simulation-bildungswirkgefuege.py` – Hauptskript (führt die Simulation aus und erzeugt Ausgaben)
- `config_bildungswirkgefuege.py` – Parameter/Konfiguration
- `modellpruefung.py` – optionale Modellprüfung (steuerbar über `config_bildungswirkgefuege.py`)

## Voraussetzungen

- Python `>= 3.10`
- Pakete: siehe `requirements.txt`

Hinweis: Das Skript nutzt zusätzlich projektspezifische Module, die in diesem Paket **nicht** enthalten sind:

- `ci_template` (für Plotly-Theme/CI) – wird über `CI_TEMPLATE_PATH` gesucht
- `archetypen` (Lernenden‑Archetypen und Parameter) – muss im `PYTHONPATH` liegen (z. B. als `archetypen.py` im selben Ordner)

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ausführung

1) Parameter anpassen: `config_bildungswirkgefuege.py` (z. B. `quartale`, `simulations_durchlaeufe`, `ansatz_wahl`, `selected_archetyp`)

2) Falls nötig, externe Module verfügbar machen, z. B.:

```bash
export CI_TEMPLATE_PATH="/pfad/zu/ci_template"
export PYTHONPATH="$PYTHONPATH:/pfad/zu/archetypen-modul"
```

3) Simulation starten:

```bash
python3 simulation-bildungswirkgefuege.py
```

## Ausgaben/Exports

Standardmäßig schreibt das Skript Logs/CSVs/HTML/PNGs in vordefinierte Verzeichnisse. Diese können über Umgebungsvariablen umgebogen werden:

- `BILDWIRK_EXPORT_ROOT` (CSV/Logs)
- `BILDWIRK_PNG_DIR` (PNG)
- `BILDWIRK_HTML_DIR` (HTML)
- `BILDWIRK_REMOTE_SCP_DEST` (optional: `scp`-Ziel für HTML)

## Zitieren

Siehe `CITATION.cff` (Metadaten bitte vor Release auf Zenodo finalisieren, z. B. ORCID, Version, Lizenz).

## Lizenz / Nutzung

Dieses Paket ist **proprietär** (alle Rechte vorbehalten). Eine Nutzung/Weitergabe ist nur mit expliziter schriftlicher Genehmigung des Rechteinhabers erlaubt.
