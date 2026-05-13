---
author: Jochen Hanisch-Johannsen
title: README
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2026-05-11
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
# Quellcodes

Dieser Ordner enthält die Python-Skripte und paketierten Quellcode-Stände zur Dissertationsarbeit. Die Skripte bilden mehrere Analyse- und Simulationslinien ab und greifen auf Daten, Abbildungen und Metadaten im Promotionsordner zurück.

## Grundprinzip

Die Skripte sind Arbeits- und Reproduktionswerkzeuge, keine automatisch auszuführenden Build-Schritte. Vor jedem Lauf sind die jeweilige Konfigurationsdatei, Eingabedaten, Exportpfade und mögliche externe Abhängigkeiten zu prüfen.

Besonders zu beachten:

- Einzelne Skripte erwarten `ci_template` für Plotly-/CI-Themes.
- Die Simulationen erwarten zusätzlich ein Modul `archetypen`.
- Exportpfade können absolute lokale Ordner, Remote-SCP-Ziele oder Umgebungsvariablen nutzen.
- Zotero-nahe Skripte liegen im Ordner `tools/`, nicht hier, und dürfen mit Schreibzugriff nur nach ausdrücklicher Freigabe laufen.
- Python-Dateien erhalten kein rohes YAML-Frontmatter mit `---`, weil dies Python-Syntaxfehler erzeugt. Metadaten werden für Skripte über README, CITATION-Dateien, `zenodo.json`, kommentierte Metadaten oder Modul-Docstrings geführt.

## Herkunft aus `charite-promotion`

Die Literaturanalyseskripte wurden gegen das frühere GitHub-Repository `https://github.com/jochen-hanisch/charite-promotion` geprüft. Die Historie dieses früheren Repositories ist im Research-Repo verbunden und auf die heutigen Pfade unter `08 Metaquellen/08-05 Quellcodes/` abgebildet. Der aktuelle iCloud-Stand bleibt dabei inhaltlich maßgeblich. Das alte Repository enthielt insbesondere:

- `Systematische Literaturrecherche/analyse_korrelation.py`
- `Systematische Literaturrecherche/analyse_netzwerk.py`
- `Systematische Literaturrecherche/deskriptive-literaturauswahl.py`
- `Systematische Literaturrecherche/requirements.txt`
- BibTeX-Zwischenstände unter `Systematische Literaturrecherche/Bibliothek/`

Der aktuelle Promotionsordner führt die Skripte nun im Research-Repo unter `08 Metaquellen/08-05 Quellcodes/`. Die Anforderungen der alten Literaturanalyselinie sind in `requirements-literaturanalyse.txt` gesichert; der importierte historische Setup-Hinweis liegt ergänzend in `README.charite-promotion.md`. BibTeX-Zwischenstände aus dem alten Repo werden nicht pauschal importiert; maßgeblich für den Pandoc-/Zotero-Workflow bleibt `08 Metaquellen/Matadaten/Literaturverzeichnis.bib`, sofern nicht ausdrücklich eine historische Vergleichsbibliothek benötigt wird.

## Skriptmatrix

| Skript | Funktion | Konfiguration | Eingaben | Typische Ausgaben / Bezug |
|---|---|---|---|---|
| `deskriptive-literaturauswahl.py` | Jahresdiagnostik, Fallzahlen, Silhouette-Scores, volumengewichtete Abweichungen der Literaturauswahl | `config_deskriptive_literaturauswahl.py` | BibTeX-Korpus `02-01 Suchergebnisse.bib` | Methodik-Abbildungen wie `silhouette-scores-und-fallzahlen.png`, `delta-sc-n-pro-jahr.png`; Kapitel 4 |
| `analyse_netzwerk.py` | semantische Netzwerk-, Tag-, Quellen-, Zeitreihen- und Relevanzvisualisierungen | `config_netzwerk.py` | BibTeX-Korpus und deduktive Analysefelder | Abbildungen unter `08 Metaquellen/08-01 Abbildungen/methodik/`; Anhang Korpusvisualisierungen |
| `analyse_korrelation.py` | deduktiv-statistische Clusteranalyse und bivariate Korrelationsmatrizen | `config_korrelation.py` | BibTeX-Korpus, Kategorien, Suchbegriffe, Forschungsunterfragen, Indizes | Korrelationsgrafiken und CSV-Matrizen; Anhang Korrelationsatlas |
| `Auswertung-LMS.py` | Auswertung der LMS-Umfrage mit Likert-, Freitext-, Cluster- und Korrelationsanteilen | `config-auswertung-lms.py` | `UmfrageOnline-Beantwortungen.csv` bzw. bereinigte Exporte | `items_summary.*`, `cluster_data.csv`, HTML-/PNG-Auswertungen; Kapitel 3 bis 5 |
| `verteilung-konfidenz.py` | Visualisierung der Eye-Tracking-Bildanzahl und Verteilung/Konfidenz | `config_eye_tracking.py` | aggregierte Eye-Tracking-Bildbasis | `eye_tracking_bildanzahl.png`, `eye_tracking_verteilung_konfidenz.png`; Anhang Bilder-Eye-Tracking |
| `simulation-bildungswirkgefuege.py` | Monte-Carlo-Simulation von Neugier, Motivation, Kompetenzentwicklung und Wirkgefüge-Dynamiken | `config_bildungswirkgefuege.py` | Modellparameter, didaktischer Ansatz, Archetyp | Abbildungen unter `08 Metaquellen/08-01 Abbildungen/didaktik/`; Zenodo-Paket Simulation |
| `tei-bildungswirkgefuege.py` | TEI-gestützte Kopplung von Urteilsspur und simulationsgestützter Strukturspur | `config_bildungswirkgefuege.py`, TEI-Umgebungsvariablen | TEI-CSV/Excel-Exporte | TEI-Berichte, CSVs, Plotly-Dashboards; Datenset 04 |
| `modellpruefung.py` | Wrapper für die optionale Modellprüfung der Simulation | `config_bildungswirkgefuege.py` | Simulationsergebnisse | Modellprüfungsberichte und Anschluss an die Simulationsauswertung |
| `Kontrollliste.py` | Hilfswerkzeug für Excel-/Kontrolllisten | im Skript | Excel-Dateien | lokale Kontroll- und Arbeitslisten |

## Daten- und Abbildungsbezüge

- Literatur- und Korrelationsanalysen beziehen sich auf Such- und Korpusmaterial aus `02 Suchstrategie/`, `03 Quellenanalyse/` und `08 Metaquellen/Matadaten/Literaturverzeichnis.bib`.
- Kuratierte Korrelationsmatrizen liegen in `08 Metaquellen/08-04 Daten/Datenset/korrelationsmatrizen/`.
- Umfragedaten und Analyse-Tabellen liegen in `08 Metaquellen/08-04 Daten/Datenset/umfrage-analysen/`.
- Eye-Tracking-Bilder liegen als aggregierte Exporte in `08 Metaquellen/08-04 Daten/Datenset/eye-tracking-bilder/`; die für die Dissertation eingebundenen Abbildungen liegen unter `08 Metaquellen/08-01 Abbildungen/eye-traking/`.
- Simulationsabbildungen des Bildungswirkgefüges liegen unter `08 Metaquellen/08-01 Abbildungen/didaktik/`.
- Prozessgrafiken und TikZ-/LaTeX-Abbildungen liegen unter `08 Metaquellen/08-01 Abbildungen/prozesse/`.

## Umgebungsvariablen und lokale Pfade

Die Simulationsskripte unterstützen Umgebungsvariablen, um Exporte aus dem lokalen Altpfad herauszulösen:

- `BILDWIRK_EXPORT_ROOT`
- `BILDWIRK_PNG_DIR`
- `BILDWIRK_HTML_DIR`
- `BILDWIRK_REMOTE_SCP_DEST`
- `BILDWIRK_TEI_DIR`
- `BILDWIRK_TEI_FILE_GLOB`
- `BILDWIRK_TEI_EXCEL_SHEET`
- `BILDWIRK_TEI_EXCEL_PATH`
- `BILDWIRK_TEI_EXPORT_ROOT`

Wenn diese Variablen nicht gesetzt sind, können Skripte auf ältere lokale Defaultpfade zurückfallen. Vor produktiven Läufen deshalb prüfen, ob der Zielpfad in den aktuellen Promotionsordner oder in einen bewusst gewählten Exportordner zeigt.

## Installation der Literaturanalyse-Abhängigkeiten

Die aus `charite-promotion` übernommene Anforderungsliste liegt in:

```bash
python3.12 -m pip install --user -r "08 Metaquellen/08-05 Quellcodes/requirements-literaturanalyse.txt"
```

Falls `ci_template` nicht über den normalen `PYTHONPATH` gefunden wird, kann der lokale CI-Pfad gesetzt werden:

```bash
export CI_TEMPLATE_PATH="/Users/jochenhanisch-johannsen/Documents/scripte/Jochen-Hanisch/CI"
```

## Veröffentlichte Software auf Zenodo

- `analyse_netzwerk.py`
  Zenodo: https://zenodo.org/records/15387108
  DOI: `10.5281/zenodo.15387108`

- `analyse_korrelation.py`
  Zenodo: https://zenodo.org/records/15386334
  DOI: `10.5281/zenodo.15386334`

- `zenodo-simulation-bildungswirkgefuege/`
  Zenodo: https://zenodo.org/records/18050984
  DOI: `10.5281/zenodo.18050984`

- `zenodo-tei-bildungswirkgefuege/`
  Zenodo: https://zenodo.org/records/18051116
  DOI: `10.5281/zenodo.18051116`

## Offene technische Pflegepunkte

- Einige Konfigurationen enthalten noch ältere absolute Exportpfade außerhalb des Promotionsordners.
- `eye-traking` ist als Ordnername im Bestand vorhanden und deshalb vorerst nicht still umzubenennen.
- Für produktive Reproduktionsläufe sollte ein gemeinsames lokales Export-Root über Umgebungsvariablen gesetzt werden.
- Die beiden Zenodo-Paketordner dokumentieren veröffentlichte Softwarestände und sollten nur mit Blick auf die jeweilige Veröffentlichung verändert werden.
