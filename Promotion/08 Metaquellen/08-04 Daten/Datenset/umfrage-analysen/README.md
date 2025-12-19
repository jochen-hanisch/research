# Datenset 01: Umfrage (Open) & Analyse-Tabellen

Dieses Verzeichnis ist für einen separaten Zenodo-Upload vorgesehen (Dateilimit < 100).

## Inhalt

- `UmfrageOnline-Beantwortungen_bereinigt.csv`  
  Bereinigter, für Open Data vorgesehener Umfragedatensatz (keine IP-/Geräte-/Zeitstempel-Metadaten; keine Freitextantworten; keine Kurs-/Geschlechts-/Eye-Tracking-Linkage-Variablen).  
  Kodierung: überwiegend Likert-Antworten als Ziffern `1`–`5` (ordinal), außerdem eine Ja/Nein-Variable (`Ja`/`Nein`). Fehlende Werte sind als leere Felder kodiert.
- `items_summary.csv`, `items_summary.json`  
  Zusammenfassungen/Export der Item- und Auswertungsstruktur (maschinenlesbar).
- `cluster_data.csv`  
  Tabellarische Daten für die Cluster-/Strukturvisualisierungen.
- `eye_tracking_bildanzahl.png`, `eye_tracking_verteilung_konfidenz.png`  
  Aggregierte Übersichten zur Eye-Tracking-Bildbasis (für Kontext; die vollständigen Eye-Tracking-Exports sind in Datenset 02).

## Datenschutz

Die Datei `UmfrageOnline-Beantwortungen_bereinigt.csv` wurde so bereinigt, dass keine direkten Identifikatoren (z.B. IP-Adresse, Geräteangaben) und keine Freitextfelder enthalten sind. Zusätzlich wurden Linkage-/Quasi-Identifikatoren entfernt, um Re-Identifikationsrisiken im kleinen Stichprobenkontext zu reduzieren.

## Bezug zur Dissertation

Das Datenset ist Bestandteil der Dissertation im Repository „Promotion“ und steht in Beziehung zu:

- Datenset 02: Eye-Tracking-Bilder (aggregierte Exports)
- Datenset 03: Korrelationsmatrizen (zwischen FU/Indizes/Kategorien/Suchbegriffen)

## Lizenz

Empfehlung für Zenodo: `CC BY 4.0` (sofern institutionell/prüfungsrechtlich zulässig).

## Zitierempfehlung (Template)

Bitte nach dem Upload den DOI einsetzen:

Hanisch-Johannsen, Jochen. (Jahr). *Datenset 01: Umfrage (Open) & Analyse-Tabellen*. Zenodo. DOI: `10.5281/zenodo.XXXXXXX`

