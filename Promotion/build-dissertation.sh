#!/usr/bin/env bash

# Bash-Skript zum Erstellen der Dissertation als PDF mit Pandoc
# Pfad: cd '/Users/jochenhanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein beruflich/Research/Promotion'
# ./build-dissertation.sh

set -euo pipefail

cd "$(dirname "$0")"  # geht in das Verzeichnis des Skripts

# Build-Modus bestimmen (full | fast)
MODE="fast"
DEFAULT_MODE="$MODE"
case "${1:-$DEFAULT_MODE}" in
  fast)
    MODE="fast"
    ;;
  full)
    MODE="full"
    ;;
  *)
    echo "Usage: $(basename "$0") [fast|full]  (default: $DEFAULT_MODE)" >&2
    exit 2
    ;;
esac

echo "Build-Modus: $MODE"

# Dateiliste definieren
FILES=(
  dissertation.md
  "04 Kapitelstruktur/04-01 Einleitung/04-01 Einleitung.md"
  "04 Kapitelstruktur/04-02 Theorieteil/04-02 Theorieteil.md"
  "04 Kapitelstruktur/04-03 Forschungsgegenstand/04-03 Forschungsgegenstand.md"
  "04 Kapitelstruktur/04-04 Methodologie/04-04 Methodologie.md"
  "04 Kapitelstruktur/04-05 Ergebnisse/04-05 Ergebnisse.md"
  "04 Kapitelstruktur/04-06 Diskussion/04-06 Diskussion.md"
  "04 Kapitelstruktur/04-07 Conclusio/04-07 Conclusio.md"
  literaturverzeichnis.md
  "04 Kapitelstruktur/04-A Anhang/04-A Anhang.md"
  # Reihenfolge der Anhänge: Nach Erstnennung innerhalb der Dissertation (links: Anhang-Nummer)
  "04 Kapitelstruktur/04-A Anhang/04-A Begriffe.md" # A-1
  "04 Kapitelstruktur/04-A Anhang/04-A Analyseprompt.md" # A-2
  "04 Kapitelstruktur/04-A Anhang/04-A P-QIA-Prompt.md" # A-3
  "04 Kapitelstruktur/04-A Anhang/04-A P-QIA-Ergebnisse.md" # A-9
  "04 Kapitelstruktur/04-A Anhang/04-A Handlungssituationen.md" # A-5
  "04 Kapitelstruktur/04-A Anhang/04-A Suchordner.md" # A-6
  "04 Kapitelstruktur/04-A Anhang/04-A Fortschrittsübersichten.md" # A-11
  "04 Kapitelstruktur/04-A Anhang/04-A Korpusvisualisierungen.md" # A-13
  "04 Kapitelstruktur/04-A Anhang/04-A Technologieintegration.md" # A-14
  "04 Kapitelstruktur/04-A Anhang/04-A Software und Quellcode.md" # A-15
  "04 Kapitelstruktur/04-A Anhang/04-A EyeTracking-Prompt.md" # A-8
)

# Eye-Tracking-Datei abhängig vom Modus einbinden (Anhang A-7)
if [[ "$MODE" == "full" ]]; then
  FILES+=("04 Kapitelstruktur/04-A Anhang/04-A Bilder-Eye-Tracking.md")
else
  FILES+=("04 Kapitelstruktur/04-A Anhang/04-A Bilder-Eye-Tracking_stub.md")
fi

# Korrelationsatlas abhängig vom Modus einbinden (Anhang A-4)
if [[ "$MODE" == "full" ]]; then
  FILES+=("04 Kapitelstruktur/04-A Anhang/04-A Korrelationsatlas.md")
else
  FILES+=("04 Kapitelstruktur/04-A Anhang/04-A Korrelationsatlas_stub.md")
fi

# Umfrage-Prompt/Vorlage und Ergebnisse (Anhänge A-10 / A-12)
FILES+=(
  "04 Kapitelstruktur/04-A Anhang/04-A Umfrage-Prompt.md" # A-10
  "04 Kapitelstruktur/04-A Anhang/04-A Umfrage-Ergebnisse.md" # A-12
)

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

pandoc "${FILES[@]}" \
  --filter pandoc-crossref \
  --lua-filter tools/pandoc/ensure-figsubcaption.lua \
  -o "dissertation-${MODE}.pdf" \
  --pdf-engine=latexmk \
  --pdf-engine-opt=-pdf \
  --pdf-engine-opt=-xelatex \
  --citeproc &

pandoc_pid=$!
spinner "$pandoc_pid"
wait "$pandoc_pid"

echo "Fertig: $(pwd)/dissertation-${MODE}.pdf"
