---
author: Jochen Hanisch-Johannsen
title: README
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2025-12-19
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
# Datenset 02: Eye-Tracking-Bilder (aggregierte Exports)

Dieses Verzeichnis ist für einen separaten Zenodo-Upload vorgesehen (Dateilimit < 100).

## Veröffentlichung

Zenodo: https://zenodo.org/records/17989978  
DOI: `10.5281/zenodo.17989978`

## Inhalt

Aggregierte Bildexporte aus dem Eye-Tracking-Teil der Studie:

- Heatmaps (`*_Heatmap_*.png`)
- Viewmaps (`*_View-Map_*.png`)
- Fog-Views (`*_Fog-View_*.png`)

Die Dateien sind aggregierte Darstellungen (keine Video-/Webcam-Rohdaten, keine personenspezifischen Aufzeichnungen).

## Dateibenennung (Konvention)

Die Dateinamen folgen dem Schema:

`F<Stimulus>-S<Serie>_<Typ>_<Kohorte>-NFS-09_Gesamt.png`

Beispiel: `F10-S3_Heatmap_21-NFS-09_Gesamt.png`

- `F…-S…`: Stimulus-/Serienkennung
- `<Typ>`: `Heatmap`, `View-Map` oder `Fog-View`
- `<Kohorte>`: z.B. `21`, `22`, `23` (Stichproben-/Jahrgangscluster)
- `Gesamt`: aggregierte Darstellung innerhalb der jeweiligen Kohorte

## Bezug zur Dissertation

Die methodische Einordnung (Design, Durchführung, Auswertungslogik) ist in der Dissertation dokumentiert. Für die übrigen zugehörigen Datenartefakte siehe:

- Datenset 01: Umfrage (Open) & Analyse-Tabellen
- Datenset 03: Korrelationsmatrizen

## Lizenz

Empfehlung für Zenodo: `CC BY 4.0` (Stimuli gehören dem Autor; keine personenbezogenen Rohmedien enthalten).

## Zitierempfehlung (Template)

Bitte nach dem Upload den DOI einsetzen:

Hanisch-Johannsen, Jochen. (2025). *Wirkgefüge im digitalen Bildungsraum – Eye-Tracking (aggregierte Heatmaps, Viewmaps, Fog-Views)*. Zenodo. DOI: `10.5281/zenodo.17989978`
