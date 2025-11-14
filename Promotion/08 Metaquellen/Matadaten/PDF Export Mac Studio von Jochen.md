---
author: 
title: 
Repository: 
created: 
updated: 
publish: 
tags: []
published: 
project: Wirkgefüge im digitalen Bildungsraum
---

# Pfad

cd "/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein beruflich/Research/Charité - Universitätsmedizin Berlin/Dissertation"

# Pandoc direkt über das Terminal

## Ohne Mermaid Integration

pandoc "Wirkgefüge im digitalen Bildungsraum.md" \
  --citeproc \
  --bibliography="/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein beruflich/Research/Charité - Universitätsmedizin Berlin/Matadaten/Literaturverzeichnis.bib" \
  --csl="/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/pandoc-templates/bibliography/apa.csl" \
  --pdf-engine=xelatex \
  -o "Wirkgefüge im digitalen Bildungsraum.pdf"




## Mit Mermaid Integration

pandoc "Wirkgefüge im digitalen Bildungsraum.md" \
  --citeproc \
  --bibliography="/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein beruflich/Research/Charité - Universitätsmedizin Berlin/Matadaten/Literaturverzeichnis.bib" \
  --csl="/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/pandoc-templates/bibliography/apa.csl" \
  --pdf-engine=xelatex \
  --filter mermaid-filter \
  -o "Wirkgefüge im digitalen Bildungsraum.pdf"