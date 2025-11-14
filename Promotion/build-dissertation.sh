#!/usr/bin/env bash
set -euo pipefail

# Immer relativ zum Projektordner arbeiten (dort, wo dieses Skript liegt)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

pandoc \
  dissertation.md \
  chapters/01_einleitung_und_theoretischer_rahmen.md \
  chapters/02_theorieteil.md \
  chapters/03_forschungsgegenstand.md \
  chapters/04_methodologie.md \
  chapters/05_ergebnisse.md \
  chapters/06_diskussion.md \
  chapters/07_conclusio.md \
  -o dissertation.pdf \
  --pdf-engine=xelatex \
  --citeproc

echo "Fertig: $SCRIPT_DIR/dissertation.pdf"

