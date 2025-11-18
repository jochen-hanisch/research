#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"  # geht in das Verzeichnis des Skripts

pandoc \
  dissertation.md \
  "04 Kapitelstruktur/04-01 Einleitung/04-01 Einleitung.md" \
  "04 Kapitelstruktur/04-02 Theorieteil/04-02 Theorieteil.md" \
  "04 Kapitelstruktur/04-03 Forschungsgegenstand/04-03 Forschungsgegenstand.md" \
  "04 Kapitelstruktur/04-04 Methodologie/04-04 Methodologie.md" \
  "04 Kapitelstruktur/04-05 Ergebnisse/04-05 Ergebnisse.md" \
  "04 Kapitelstruktur/04-06 Diskussion/04-06 Diskussion.md" \
  "04 Kapitelstruktur/04-07 Conclusio/04-07 Conclusio.md" \
  literaturverzeichnis.md \
  "04 Kapitelstruktur/04-A Anhang/04-A Anhang.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A-1 Begriffe.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A-2 Analyseprompt.md" \
  --filter pandoc-crossref \
  -o dissertation.pdf \
  --pdf-engine=xelatex \
  --citeproc

echo "Fertig: $(pwd)/dissertation.pdf"
