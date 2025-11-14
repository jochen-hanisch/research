#!/usr/bin/env bash
set -euo pipefail

# Immer relativ zum Projektordner arbeiten (dort, wo dieses Skript liegt)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

pandoc \
  dissertation.md \
  "04 Kapitelstruktur/04-01 Einleitung/04-01 Einleitung.md" \
  "04 Kapitelstruktur/04-02 Theorieteil/04-02 Theorieteil.md" \
  "04 Kapitelstruktur/04-03 Forschungsgegenstand/04-03 Forschungsgegenstand.md" \
  "04 Kapitelstruktur/04-04 Methodologie/04-04 Methodologie.md" \
  "04 Kapitelstruktur/04-05 Ergebnisse/04-05 Ergebnisse.md" \
  "04 Kapitelstruktur/04-06 Diskussion/04-06 Diskussion.md" \
  "04 Kapitelstruktur/04-07 Conclusio/04-07 Conclusio.md" \
  -o dissertation.pdf \
  --pdf-engine=xelatex \
  --citeproc

echo "Fertig: $SCRIPT_DIR/dissertation.pdf"

