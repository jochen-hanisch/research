# Pfad

cd "/Users/jochenhanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein_beruflich/Research/Charité - Universitätsmedizin Berlin/Dissertation"

# Pandoc direkt über das Terminal

pandoc "Wirkgefüge im digitalen Bildungsraum.md" \
  --citeproc \
  --bibliography="/Users/jochenhanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein_beruflich/Research/Charité - Universitätsmedizin Berlin/Matadaten/Literaturverzeichnis.bib" \
  --csl="/Users/jochenhanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/pandoc-templates/bibliography/apa.csl" \
  --pdf-engine=xelatex \
  -o "Wirkgefüge im digitalen Bildungsraum.pdf"