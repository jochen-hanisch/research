---
author: Jochen Hanisch-Johannsen
title: README charite-promotion
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2025-11-26
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
# Setup

Diese Datei dokumentiert den importierten Setup-Stand aus dem früheren Repository `https://github.com/jochen-hanisch/charite-promotion`. Die Historie dieses früheren Repositories ist im Research-Repo als Merge-Historie verbunden; der aktuelle Arbeitsstand bleibt unter `08 Metaquellen/08-05 Quellcodes/` maßgeblich.

1. Abhängigkeiten einmalig mit Python 3.12 (User-Scope reicht) installieren:
   ```bash
   python3.12 -m pip install --user -r requirements.txt
   ```
2. Stelle sicher, dass VS Code den Interpreter `python3.12` nutzt (siehe `.vscode/settings.json`).
3. Sorge dafür, dass das CI-Paket auf dem `PYTHONPATH` liegt (oder setze die Env-Variable), damit `ci_template` gefunden wird:
   ```bash
   export CI_TEMPLATE_PATH="/Users/jochenhanisch-johannsen/Documents/scripte/Jochen-Hanisch/CI"
   ```

Hinweis: `.vscode/settings.json` enthält bereits einen `extraPaths`-Eintrag für den CI-Pfad, damit Pylance den Import findet.
