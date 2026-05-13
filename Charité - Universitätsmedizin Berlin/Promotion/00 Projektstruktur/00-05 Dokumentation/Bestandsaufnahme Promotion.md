---
author: Jochen Hanisch-Johannsen
title: Bestandsaufnahme Promotion
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2026-05-13
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
# Bestandsaufnahme Promotion

Diese Bestandsaufnahme dokumentiert den Promotionsordner nach dem Umzug in die iCloud-/CloudDocs-Struktur. Maßgeblich ist der lokale Ordner:

`/Users/jochenhanisch-johannsen/Documents/Allgemein beruflich/Research/Charité - Universitätsmedizin Berlin/Promotion`

Der Umzug ist abgeschlossen. Git versioniert den kuratierten Kernbestand; der lokale iCloud-Dateibaum bleibt die Arbeitswahrheit.

## 1 Zentrale Arbeitslogik

Die Dissertation wird als Markdown-/Pandoc-Projekt geführt. `dissertation.md` klammert die Kapitel, Metadaten, Verzeichnisse, Build-Optionen und Literatursteuerung. Die Kapiteltexte liegen in `04 Kapitelstruktur/`, die Daten-, Abbildungs- und Softwarebasis in `08 Metaquellen/`.

Der Bestand verbindet vier Ebenen:

- Schreibebene: Hauptkapitel, Anhänge, Arbeitsnotizen und Entwürfe.
- Datenebene: Umfrage, Eye-Tracking, Korrelationsmatrizen, TEI und zugehörige Exporte.
- Analyseebene: Python-Skripte zur Literatur-, Netzwerk-, Korrelations-, LMS-, Eye-Tracking- und TEI-Auswertung.
- Simulations- und Modellierungsebene: Simulation des digitalen Bildungswirkgefüges und TEI-gestützte Kopplung von Urteilsspur und Strukturspur.

## 2 Ordnerstruktur

| Ordner | Funktion |
|---|---|
| `00 Projektstruktur/` | Exposé, Fragenstruktur, Theorieansatz, Glossar und Dokumentation des Arbeitsbestands. |
| `01 Methodologie/` | methodologische Vorarbeiten, Designarten, Methodenquellen, Samplinglogik und Analysemodell. |
| `02 Suchstrategie/` | Suchergebnisse, Begriffslogik, Filterkriterien, Tagstruktur und Fundübersichten. |
| `03 Quellenanalyse/` | Kategorien, Typenstruktur, Clustermodelle, Bewertungskriterien, Eye-Tracking, Umfrage und Paradigmenanalyse. |
| `04 Kapitelstruktur/` | Hauptkapitel, Prolog/Epilog, Anhänge und kapitelspezifische Arbeitsnotizen. |
| `05 Textarbeit/` | Entwürfe, Überarbeitungen, Lesepfade, Feedback und Verteidigungsvorbereitung. |
| `06 Transfer/` | Artikel, Präsentationen und Lehreinsatz. |
| `07 Archiv/` | Altstruktur, verworfene Arbeitsstände und Übertragungen. |
| `08 Metaquellen/` | Abbildungen, Forschungsdesign, Digitalmethodik, Daten, Quellcodes und Metadaten. |
| `09 Backup/` | JSON-Exporte, Bib-Exporte und Abgleichstände. |
| `tools/` | Pandoc-, Zotero- und Kontrollwerkzeuge. |

## 3 Kapitel- und Schreibbestand

Der versionierte Schreibkern liegt in:

- `04 Kapitelstruktur/04-01 Einleitung/04-01 Einleitung.md`
- `04 Kapitelstruktur/04-02 Theorieteil/04-02 Theorieteil.md`
- `04 Kapitelstruktur/04-03 Forschungsgegenstand/04-03 Forschungsgegenstand.md`
- `04 Kapitelstruktur/04-04 Methodologie/04-04 Methodologie.md`
- `04 Kapitelstruktur/04-05 Ergebnisse/04-05 Ergebnisse.md`
- `04 Kapitelstruktur/04-06 Diskussion/04-06 Diskussion.md`
- `04 Kapitelstruktur/04-07 Conclusio/04-07 Conclusio.md`
- `04 Kapitelstruktur/04-A Anhang/04-A Anhang.md`

Daneben liegen zahlreiche Arbeitsnotizen, Mappings, Gliederungen und Kapitelentwürfe. Diese Dateien bilden Denk- und Arbeitsstände ab und dürfen nicht pauschal gelöscht oder zusammengeführt werden. Für Schreibarbeit gilt: Hauptkapitel zuerst prüfen, Arbeitsnotizen als Herleitungs- und Klärungsspur nutzen.

## 4 Datenbestand

Die kuratierten Datensets liegen unter `08 Metaquellen/08-04 Daten/Datenset/`.

| Datenset | Ordner | Inhalt | Bezug |
|---|---|---|---|
| Datenset 01 | `umfrage-analysen/` | bereinigter Umfragedatensatz, Item-Zusammenfassungen, Cluster- und Kontextgrafiken | LMS-Auswertung, Ergebnisse, Anhang Umfrage |
| Datenset 02 | `eye-tracking-bilder/` | aggregierte Heatmaps, View-Maps und Fog-Views | Eye-Tracking-Methodik und Anhang Bilder-Eye-Tracking |
| Datenset 03 | `korrelationsmatrizen/` | CSV-Matrizen zwischen Forschungsunterfragen, Indizes, Kategorien und Suchbegriffen | Korrelationsatlas und Methodologie |
| Datenset 04 | `TEI/` | aggregierte TEI-Feedback-Exporte und konsolidierte Tabellen | TEI-/P-QIA-Auswertung und simulationsgestützte Urteilsspur |

Zusätzlich liegen im übergeordneten Datenordner Arbeits- und HTML-Exporte, die teilweise Vorstufen oder lokale Ausgabestände darstellen. Vor Veröffentlichung ist zwischen kuratiertem Datenset, Arbeitsoutput und sensiblem Roh-/Zwischenstand zu unterscheiden.

## 5 Quellcodes und Analysepfade

Die Quellcodes liegen unter `08 Metaquellen/08-05 Quellcodes/`.

| Analysepfad | Skripte | Trägt zu |
|---|---|---|
| Literaturauswahl und Jahresdiagnostik | `deskriptive-literaturauswahl.py`, `config_deskriptive_literaturauswahl.py` | Korpusaufbau, Jahresverteilung, Silhouette-Scores, Drift-/Verdichtungsinterpretation |
| Netzwerk- und Strukturvisualisierung | `analyse_netzwerk.py`, `config_netzwerk.py` | semantische Netzwerke, Tag-/Quellen-/Zeitreihenvisualisierungen, Relevanzdarstellungen |
| Korrelationsanalyse | `analyse_korrelation.py`, `config_korrelation.py` | Korrelationsmatrizen und Korrelationen zwischen Forschungsunterfragen, Indizes, Kategorien und Suchbegriffen |
| LMS-Umfrage | `Auswertung-LMS.py`, `config-auswertung-lms.py` | Likert-, Freitext-, Cluster- und Skalenanalysen des LMS-Feedbacks |
| Eye-Tracking-Kontext | `verteilung-konfidenz.py`, `config_eye_tracking.py` | aggregierte Bildanzahl und Verteilung/Konfidenz der Eye-Tracking-Bildbasis |
| Simulation Bildungswirkgefüge | `simulation-bildungswirkgefuege.py`, `config_bildungswirkgefuege.py`, `modellpruefung.py` | simulationsgestützte Modellierung von Neugier, Motivation, Kompetenzentwicklung und Wirkgefügedynamik |
| TEI-gestützte Simulation | `tei-bildungswirkgefuege.py`, `config_bildungswirkgefuege.py` | Kopplung von TEI-Urteilsspur und simulationsgestützter Strukturspur |

Die Skripte sind nicht alle unmittelbar lauffähige Ein-Klick-Werkzeuge. Mehrere erwarten externe Module (`ci_template`, `archetypen`), lokale Datenpfade oder bewusst gesetzte Umgebungsvariablen. Produktive Läufe müssen daher vorbereitet und dokumentiert werden.

## 6 Simulationen

Die zentrale Simulation des digitalen Bildungswirkgefüges modelliert Neugier, Motivation und Kompetenzentwicklung über Zeit. Sie arbeitet mit didaktischen Ansätzen, Lernenden-Archetypen, Monte-Carlo-Durchläufen und Visualisierungen. Ihre wichtigsten Outputs liegen unter `08 Metaquellen/08-01 Abbildungen/didaktik/` und werden als Modellierungs- und Reflexionsspur der Dissertation genutzt.

Die TEI-gestützte Simulation ergänzt diese Strukturspur durch eine Urteilsspur aus TEI-Feedbackdaten. Damit entsteht eine Schnittstelle zwischen empirischer Rückmeldung, didaktischer Modellannahme und simulativem Verlauf.

Die beiden Zenodo-Paketordner dokumentieren veröffentlichte Softwarestände:

- `zenodo-simulation-bildungswirkgefuege/`
- `zenodo-tei-bildungswirkgefuege/`

Diese Ordner sind Veröffentlichungsstände und sollten nur mit Bezug auf die jeweilige Publikation verändert werden.

## 7 Abbildungen und Anhänge

Abbildungen liegen thematisch unter `08 Metaquellen/08-01 Abbildungen/`:

- `methodik/`: Literatur-, Netzwerk-, Korrelations- und Korpusdiagnostik.
- `didaktik/`: Simulation und Bildungswirkgefüge.
- `eye-traking/`: Eye-Tracking-Grafiken und aggregierte Bildübersichten.
- `LMS-Abbildungen/`: LMS-Architektur, Kursansichten und curriculare Struktur.
- `prozesse/`: TikZ-/LaTeX-Prozessgrafiken.
- `statistik/`: externe/statistische Kontextabbildungen.

Die Anhangsdateien in `04 Kapitelstruktur/04-A Anhang/` stellen diese Spuren für die Dissertation bereit. Besonders relevant sind `04-A Korpusvisualisierungen.md`, `04-A Korrelationsatlas.md`, `04-A Bilder-Eye-Tracking.md`, `04-A Umfrage-Ergebnisse.md`, `04-A P-QIA-Ergebnisse.md` und `04-A Software und Quellcode.md`.

## 8 Literatur und Zotero

Die Literaturbasis liegt in `08 Metaquellen/Matadaten/Literaturverzeichnis.bib`. Der Pandoc-/CSL-Workflow wird in `08 Metaquellen/Matadaten/README.md` beschrieben.

Zotero-nahe Hilfsskripte liegen unter `tools/`. Dazu gehören Abschnitts-/Kapitel-Tagging, lokale Zotero-Varianten, Notiz-Erzeugung und Audits. Schreibzugriffe auf Zotero oder `zotero.sqlite` nur nach ausdrücklicher Freigabe ausführen.

## 9 Aktuelle offene Ordnungspunkte

- Die Research-Parent-`AGENTS.md` verweist noch auf den alten Obsidian-Pflichtanker; die lokale Promotions-`AGENTS.md` korrigiert dies für den Promotionsordner.
- Einige Konfigurationen enthalten noch ältere absolute Exportpfade außerhalb des Promotionsordners.
- Der Ordnername `eye-traking` ist im Bestand vorhanden. Nicht still umbenennen, weil Kapitel- und Bildpfade davon abhängen können.
- Zwei unversionierte Tool-Dateien liegen im aktuellen Arbeitsbaum: `tools/pandoc/docx-workversion.lua` und `tools/zotero_sync_section_tags.py`. Vor einer späteren Versionierung ist zu prüfen, ob sie in den kuratierten Git-Kern gehören.
- Der Bestand enthält viele nicht versionierte Markdown-Dateien. Das ist beabsichtigt, solange sie Arbeitsnotizen, Zwischenstände oder lokale Denkspuren sind.

## 10 Empfohlene nächste Prüfungen

1. Konfigurationen auf alte absolute Exportpfade prüfen und schrittweise auf Umgebungsvariablen oder relative Projektpfade umstellen.
2. Für jedes veröffentlichte Zenodo-Paket prüfen, ob README, DOI, Lizenz und enthaltene Dateien konsistent sind.
3. Für die Anhangsdateien prüfen, ob alle in der Dissertation referenzierten Abbildungen im aktuellen Pfad vorhanden sind.
4. Zotero-Tagging nur trocken prüfen, bevor Schreibzugriffe auf API oder lokale Datenbank erfolgen.
5. Nach Änderungen an Kapiteltexten, Abbildungen, Literatur oder YAML mindestens `./build-dissertation.sh fast` ausführen.
