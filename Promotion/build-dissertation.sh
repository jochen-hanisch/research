#!/usr/bin/env bash

# Bash-Skript zum Erstellen der Dissertation als PDF mit Pandoc
# Pfad: cd '/Users/jochenhanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein beruflich/Research/Promotion'
# ./build-dissertation.sh

set -euo pipefail

cd "$(dirname "$0")"  # geht in das Verzeichnis des Skripts

# einfacher Spinner während Pandoc läuft, damit Fortschritt sichtbar ist
spinner() {
  local pid=$1
  local frames='|/-\'
  local i=0
  while kill -0 "$pid" 2>/dev/null; do
    printf "\rBaue PDF … %s" "${frames:i++%${#frames}:1}"
    sleep 0.2
  done
  printf "\rBaue PDF … erledigt\n"
}

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
  "04 Kapitelstruktur/04-A Anhang/04-A Begriffe.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A Analyseprompt.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A P-QIA-Prompt.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A EyeTracking-Prompt.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A Handlungssituationen.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A Fortschrittsübersichten.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A Suchordner.md" \
  "04 Kapitelstruktur/04-A Anhang/04-A Bilder-Eye-Tracking.md" \
  --filter pandoc-crossref \
  -o dissertation.pdf \
  --pdf-engine=xelatex \
  --citeproc &

pandoc_pid=$!
spinner "$pandoc_pid"
wait "$pandoc_pid"

echo "Fertig: $(pwd)/dissertation.pdf"
