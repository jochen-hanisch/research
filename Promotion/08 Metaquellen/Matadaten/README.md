# README – Workflow Markdown → Pandoc → XeLaTeX

Dieses Projekt entsteht vollständig in Markdown und wird über Pandoc + XeLaTeX zu einer druckfertigen PDF verarbeitet. Der folgende Überblick dokumentiert den aktuellen Stand.

## 1. Arbeitsoberfläche

- Markdown-Dateien liegen kapitelweise in `04 Kapitelstruktur/`.
- Obsidian dient als Editor (Tags, Backlinks, Live Preview).
- Überschriften tragen Labels `{#sec:x-y-z}` für interne Verweise.
- Verweise im Text werden kombiniert mit manueller Nummerierung:  
  `(s. Kapitel 1.2.3 / #{1-2-3})`.

## 2. Referenzen und Labels

- Labels folgen dem Schema `sec:1-2-3`, `sec:4-1-2` usw.
- Crossrefs können mit `[@sec:1-2-3]` verwendet werden, wenn `pandoc-crossref` aktiv ist.
- Für Gleichungen, Tabellen und Abbildungen bleibt die klassische LaTeX-Notation (`\label{eq:…}`) verfügbar.

## 3. Pandoc-Konvertierung

- Pandoc 3.8.x erzeugt die LaTeX-Ausgabe.
- YAML-Metadaten in `dissertation.md` steuern globale Optionen:
  ```yaml
  numberSections: true
  sectionsDepth: 2
  ```
- Der Build nutzt:
  - `--pdf-engine=xelatex`
  - `--citeproc`
  - `--filter pandoc-crossref`

## 4. Schrift- und LaTeX-Konfiguration

```latex
\usepackage{fontspec}
\usepackage{unicode-math}
\setmainfont{STIX Two Text}
\setsansfont{STIX Two Text}
\setmathfont{STIX Two Math}
```

- XeLaTeX setzt Unicode-konform und harmonisiert Text- und Mathefont.
- `mathastext` steht als Fallback bereit, falls kein dediziertes Math-Font genutzt werden soll.

## 5. Build-Skript

Das Skript liegt im Repo `https://github.com/jochen-hanisch/charite-promotion` und wird direkt aus dem Skripte-Ordner ausgeführt:
```bash
cd "/Users/jochenhanisch-johannsen/Documents/scripte/Research/Charité - Universitätsmedizin Berlin"
./build-dissertation.sh
```

## 6. Struktur des Gesamtdokuments

- `dissertation.md` enthält Titelseite, Verzeichnisse, globale Einstellungen, Hinweise.
- `04-01` … `04-07` liefern Einleitung, Theorie, Forschungsgegenstand, Methodologie, Ergebnisse, Diskussion, Conclusio.
- `04-A` enthält den Anhang.
- `literaturverzeichnis.md` definiert das Literaturkapitel mit `# Literatur` + `::: {#refs}`.

## 7. Nummerierung & Kapitelverweise

- Die sichtbaren Ziffern können zusätzlich im Text geführt werden.
- Verweise folgen dem Format `(s. Kapitel 1.2.3 / #{1-2-3})`; optional `[ @sec:1-2-3 ]`.

## 8. Abbildungen & Medienstruktur
- Zentraler Ordner `08 Metaquellen/` mit thematischen Unterordnern. Beispiel:

  ```
  08-01 Abbildungen/
  ├── lms/
  │    └── lms-architektur.png
  ├── didaktik/
  │    └── kompetenzstruktur.png
  ├── prozesse/
  │    └── entwicklungsprozess.png
  ├── methodik/
  │    └── clusteranalyse.png
  ├── statistik/
  │    └── silhouette-scores.png
  └── allgemein/
       └── schema-allgemein.png
  ```
- Vorteile: klare Themenzuordnung, Wiederverwendbarkeit über Kapitel hinweg, stabile Pfade beim Umstrukturieren.
- Einbindung in Markdown:
  ```markdown
  ![Abb. 4.4-01: Heatmap der Blickpfade](Abbildungen/methodik/heatmap.png){#fig:4-4-01}
  ```
- Rohdaten, Skripte und zusätzliche Materialien bleiben in `05 Textarbeit`, `06 Transfer` bzw. `07 Archiv`.

## 9. Resultat

- Jede Ausführung des Build-Skripts erzeugt `dissertation.pdf` im Projektordner.
- Der Workflow ist vollständig reproduzierbar und geeignet für versionierte wissenschaftliche Arbeiten.
