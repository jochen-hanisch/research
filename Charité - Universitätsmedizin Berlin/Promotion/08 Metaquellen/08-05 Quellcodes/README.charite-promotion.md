# Setup

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
