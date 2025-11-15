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

- Pandoc 3.8.x erzeugt eine LaTeX-Ausgabe und nutzt:
  - `--pdf-engine=xelatex`
  - `--citeproc` (APA-Style, Quellen aus `08 Metaquellen/Matadaten/Literaturverzeichnis.bib`)
  - `--filter pandoc-crossref` (optional, aktuell aktiv)
- Die Abschnittsnummerierung ist mauell gepflegt, um volle Kontrolle zu gewährleisten.

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

- Die sichtbaren Kapitelnummern werden weiterhin im Text manuell geführt, um maximale Kontrolle über Syntax (z.B. „1.1“, „1.2.3“) zu behalten.
- Labels (`{#sec:1-2-3}`) bleiben unabhängig von Änderungen an der Gliederung.
- Verweise folgen dem vereinbarten Format `(s. Kapitel 1.2.3 / #{1-2-3})`; optional können `[ @sec:1-2-3 ]` eingesetzt werden.

## 8. Resultat

- Jede Ausführung des Build-Skripts erzeugt `dissertation.pdf` im Projektordner.
- Der Workflow ist vollständig reproduzierbar und geeignet für versionierte wissenschaftliche Arbeiten.
