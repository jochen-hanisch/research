---
author: Jochen Hanisch-Johannsen
title: README
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2025-11-15
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
# README – Workflow Markdown → Pandoc → XeLaTeX

Dieses Projekt entsteht vollständig in Markdown und wird über Pandoc + XeLaTeX zu einer druckfertigen PDF verarbeitet. Der folgende Überblick dokumentiert den aktuellen Stand.

## 1. Arbeitsoberfläche

- Markdown-Dateien liegen kapitelweise in `04 Kapitelstruktur/`.
- Die Arbeitsdateien liegen im iCloud-/CloudDocs-Projektordner. Obsidian ist nicht mehr Arbeitsoberfläche oder Pfadanker.
- Überschriften tragen semantische Labels `{#sec:…}` für interne Verweise.
- Verweise im Text können Nummern nennen, referenzieren aber per Label:  
  `(s. Kapitel 1.4 / \@ref(sec:FU-Herleitung))`.

## 2. Referenzen und Labels

- Labels folgen semantischen Bezeichnern (z.B. `sec:Erkenntnisinteresse`, `sec:FU-Herleitung`).
- Crossrefs können mit `[@sec:FU-Herleitung]` verwendet werden, wenn `pandoc-crossref` aktiv ist.
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

Das Skript liegt im Promotionsordner des Research-Bestands und wird direkt aus diesem Ordner ausgeführt:
```bash
cd "/Users/jochenhanisch-johannsen/Documents/Allgemein beruflich/Research/Charité - Universitätsmedizin Berlin/Promotion"
./build-dissertation.sh
```

## 6. Struktur des Gesamtdokuments

- `dissertation.md` enthält Titelseite, Verzeichnisse, globale Einstellungen, Hinweise.
- `04-01` … `04-07` liefern Einleitung, Theorie, Forschungsgegenstand, Methodologie, Ergebnisse, Diskussion, Conclusio.
- `04-A` enthält den Anhang.
- `literaturverzeichnis.md` definiert das Literaturkapitel mit `# Literatur` + `::: {#refs}`.

## 7. Nummerierung & Kapitelverweise

- Die sichtbaren Ziffern können zusätzlich im Text geführt werden.
- Verweise können Nummern nennen, referenzieren aber per Label (z.B. `@sec:FU-Herleitung`).

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

- `./build-dissertation.sh fast` erzeugt `dissertation-fast.pdf`; `./build-dissertation.sh full` erzeugt `dissertation-full.pdf`.
- `./build-dissertation-docx.sh fast` erzeugt `dissertation-fast.docx`; der Full-Modus erzeugt entsprechend `dissertation-full.docx`.
- Der Workflow ist vollständig reproduzierbar und geeignet für versionierte wissenschaftliche Arbeiten.

## 10. Markdown + Pandoc: bewährte Einstellungen

- Markdown bleibt die Quellform. Absätze werden durch Leerzeilen getrennt, damit Pandoc sie korrekt erkennt.
- Einige Raw-LaTeX-Elemente, etwa `\hyperref`, rendern erst im PDF vollständig.
- `dissertation.md` enthält das technische Pandoc-Frontmatter. Einzelne Markdown-Dateien tragen zusätzlich ein Verwaltungs-YAML mit Feldern wie `author`, `title`, `versioned`, `created`, `updated` und `publish`. Dieses Verwaltungs-YAML darf nicht mit der Pandoc-Steuerung verwechselt werden.
- UTF-8 nutzen; Pfade im Markdown immer relativ zum Projektroot halten.

## 11. Crossrefs und Hyperlinks

- Sections: `# 4.3 Datenanalyse {#sec:4-3}` und im Text `\@ref(sec:4-3)` oder als Raw-LaTeX `\hyperref[sec:4-3]{Abschnitt 4.3}`.
- Abbildungen/Tabellen: `![Titel](pfad.png){#fig:xyz width=80%}` und Referenz `Abb.~\@ref(fig:xyz)` bzw. `Tab.~\@ref(tab:xyz)`.
- Gleichungen: `$$ E = mc^2 \label{eq:mass} $$` und Verweis `\eqref{eq:mass}`.
- Literaturnachweise: `[@quelle_2024, Seite 4–5]`; `citeproc` rendert gemäß CSL.
- Döring-Verweise mit Kapitelangaben: `[@doring_forschungsmethoden_2023, Kapitel 10.6]`.

## 12. Typische Stolperfallen

- Fehlende Dateien brechen Pandoc ab (`withBinaryFile: does not exist`). Pfad prüfen oder Platzhalter (z.B. `literaturverzeichnis.md`) anlegen.
- Abbildungen mit Leerzeichen funktionieren, besser jedoch konsistente Ordner- und Dateinamen wie `08 Metaquellen/08-01 Abbildungen/...`.
- `\@hyperref(...)` ist kein Pandoc-Crossref. Entweder `\@ref(label)` (pandoc-crossref) oder klassisch `\hyperref[label]{Text}`.
- Bei Raw-LaTeX-Blöcken eigene Zeilen verwenden, um Parser-Konflikte zu vermeiden.
