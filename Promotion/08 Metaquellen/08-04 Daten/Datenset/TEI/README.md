# Datenset 04: TEI-Feedback (aggregierte Exports) & konsolidierte Tabellen

Dieses Verzeichnis ist für einen separaten Zenodo-Upload vorgesehen.

## Inhalt

### Roh-Exports (pro Handlungssituation)

Die Dateien `feedback_eigene Evaluation-01.csv` bis `feedback_eigene Evaluation-32.csv` sind aggregierte TEI-Exporte pro beruflicher Handlungssituation.

- **Eine Datei = eine Handlungssituation** (fortlaufend nummeriert).
- **Pro Datei**: `Fragen: 46` (Items). Davon sind 45 Items als 6-stufige Likert-Skala (`1` = Zustimmung hoch, `6` = Ablehnung hoch) plus `Mittelwert` exportiert. Ein Item ist als Freitextfrage exportiert.
- **Ausgefüllte Feedbacks** gibt die Anzahl der eingegangenen TEI-Feedbacks für die jeweilige Handlungssituation an (je Handlungssituation variierend).

### Konsolidierte/maschinenlesbare Tabellen (abgeleitet aus den Roh-Exports)

- `tei_export_meta.csv`  
  Metadaten pro Exportdatei (Handlungssituationsnummer, Zeitstempel im Export, Rücklaufzahl, Itemanzahl).
- `tei_items.csv`  
  Itemliste (Index `1..46` → Fragetext), aus dem ersten Export extrahiert.
- `tei_counts_long.csv`  
  Tidy-Format: Handlungssituation × Item × Antwortkategorie → Häufigkeit (Counts). Für das Freitext-Item wird die Kategorie `Freitext` verwendet; `count` entspricht der Anzahl nicht-leerer Texte im Export.
- `tei_item_means.csv`  
  Tidy-Format: Handlungssituation × Item → `n` und `mean_exported` (Mittelwert aus dem Export). Beim Freitext-Item ist `mean_exported` leer; `n` entspricht der Anzahl nicht-leerer Texte im Export.
- `tei_build_dataset.py`  
  Reproduzierbares Skript, das die konsolidierten Tabellen aus den Roh-Export-CSVs erzeugt.

## Datenschutz

Die TEI-Dateien sind überwiegend **aggregierte Exporte** (Antwortkategorien als Häufigkeiten, plus Mittelwerte). Zusätzlich enthalten die Roh-Exportdateien ein Freitext-Item. Die Exporte enthalten keine direkten Identifikatoren; Freitexte können dennoch kontextuell sensible Inhalte enthalten und sind entsprechend zu prüfen.

## Bezug zur Dissertation

Das Datenset ist Bestandteil der Dissertation im Repository „Promotion“ und steht in Beziehung zu:

- Datenset 01: Umfrage (Open) & Analyse-Tabellen
- Datenset 02: Eye-Tracking-Bilder (aggregierte Exports)
- Datenset 03: Korrelationsmatrizen

Inhaltlich wird TEI als **Urteilsspur** genutzt und im Abgleich mit der simulationsgestützten **Strukturspur** (Bildungswirkgefüge) geführt.

## Reproduzierbarkeit

Konsolidierte Tabellen können aus den Roh-Export-CSVs neu erzeugt werden mit:

`python3 tei_build_dataset.py`

## Lizenz

Empfehlung für Zenodo: `CC BY 4.0` (sofern institutionell/prüfungsrechtlich zulässig).

## Zitierempfehlung (Template)

Bitte nach dem Upload den DOI einsetzen:

Hanisch-Johannsen, Jochen. (Jahr). *Datenset 04: TEI-Feedback (aggregierte Exports) & konsolidierte Tabellen*. Zenodo. DOI: `10.5281/zenodo.XXXXXXX`
