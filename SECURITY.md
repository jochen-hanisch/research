# Sicherheitsrichtlinie für den Research-Workspace

Diese Richtlinie definiert Anforderungen an Informationssicherheit, Datenschutz und Forschungsethik für alle Projekte, Materialien und Daten im Verzeichnis „Research“. Sie gilt für interne Mitarbeitende, Kooperationspartner:innen sowie externe Beitragende.

## 1. Verantwortlichkeiten

- **Workspace-Maintainer:innen**: Koordination des Sicherheitsmanagements, Freigaben, Incident-Response.
- **Projektleitungen**: Umsetzung dieser Richtlinie in den jeweiligen Forschungsprojekten, Dokumentation von Maßnahmen.
- **Forschungsteams**: Sorgfältiger Umgang mit Daten, Tools und Zugängen; Meldung von Sicherheits- oder Datenschutzproblemen.
- **Kooperationspartner:innen**: Vertragliche Verpflichtung zur Einhaltung von Datenschutz- und Sicherheitsanforderungen.

## 2. Schutzumfang

- Forschungsdaten (qualitativ, quantitativ, Roh- und Auswertungsdaten)
- Projektunterlagen, Designs, Protokolle, Interviewscripts, Feldnotizen
- Software, Skripte, Analysepipelines, Konfigurationsdateien
- Personenbezogene Daten von Studienteilnehmenden, Expert:innen, Institutionen
- Vertrauliche Vereinbarungen, Ethikvoten, Förderinformationen

## 3. Datenklassifikation

1. **Öffentlich**: Veröffentlichte Artikel, Blogposts, Open-Data-Sets mit Freigabe.
2. **Intern**: Arbeitsstände ohne personenbeziehbare Informationen.
3. **Vertraulich**: Projektinterne Dokumente mit sensiblen Kontextinformationen.
4. **Besonders schützenswert**: Personenbezogene bzw. pseudonymisierte Daten, Gesundheitsinformationen, Evaluationsdaten.

Dokumentiere die Klassifikation in den jeweiligen Projektordnern und passe Schutzmaßnahmen entsprechend an.

## 4. Speicherung & Zugriff

- Bewahre Rohdaten in verschlüsselten Speichern oder datenschutzkonformen Cloud-Diensten auf.
- Nutze Versionskontrolle für Skripte und Dokumente; sensible Dateien nur mit Zugriffsbeschränkung committen.
- Verteile Zugriffsrechte nach dem Need-to-know-Prinzip; überprüfe Rechte regelmäßig.
- Halte Backups verschlüsselt bereit und teste Wiederherstellung in definierten Intervallen.

## 5. Verarbeitung & Analyse

- Separiere Identifikatoren von Inhaltsdaten (z. B. Key-Datei mit Pseudonymisierung).
- Dokumentiere Verarbeitungsschritte, eingesetzte Tools und Parameter für Nachvollziehbarkeit.
- Verwende aktuelle, sicher konfigurierte Analyseumgebungen; halte Bibliotheken und Abhängigkeiten aktuell.
- Prüfe Open-Source-Tools auf Sicherheitsrisiken; dokumentiere Lizenz- und Compliance-Aspekte.

## 6. Datenweitergabe & Publikation

- Übermittle Daten nur verschlüsselt und mit Freigabe der Projektleitung.
- Lege bei Datenteilung Verträge oder Data-Use-Agreements ab (insb. bei externen Partner:innen).
- Stelle anonymisierte/pseudonymisierte Varianten bereit, wenn Publikation oder Open Data geplant ist.
- Prüfe rechtliche Vorgaben (DSGVO, Ethik-Kommission, Förderer) vor Veröffentlichung.

## 7. Forschungsethik & Compliance

- Halte Genehmigungen (Ethikvoten, Einverständniserklärungen) bereit und dokumentiere sie im Projektordner.
- Informiere Teilnehmende transparent über Datennutzung, Speicherdauer und Rechte.
- Lösche oder archiviere Daten nach Ablauf gesetzlicher bzw. vertraglicher Fristen.

## 8. Meldewege für Sicherheits- oder Datenschutzvorfälle

Melde Vorfälle, Schwachstellen oder Verdachtsmomente unverzüglich an:

- `kontakt@jochen-hanisch.de`
- Alternativ: Direktnachricht an die verantwortliche Projektleitung über das vereinbarte Kollaborationstool

Gib betroffene Systeme/Dateien, Zeitpunkt, vermutete Auswirkungen und bereits gesetzte Maßnahmen an. Eine Rückmeldung erfolgt innerhalb von 48 Stunden.

## 9. Incident-Response-Prozess

1. **Identifikation & Priorisierung**: Ereignis bewerten, Schweregrad und betroffene Daten bestimmen.
2. **Eindämmung & Behebung**: Zugriff einschränken, Schwachstelle schließen, Daten sichern oder entfernen.
3. **Dokumentation**: Vorfallprotokoll erstellen, Lessons Learned festhalten.
4. **Kommunikation**: Betroffene Personen, Institutionen oder Fördermittelgeber informieren; rechtliche Pflichten prüfen.

## 10. Schulung & Sensibilisierung

- Führe regelmäßige Briefings zu Datenschutz, Informationssicherheit und Forschungsethik durch.
- Stelle Checklisten für Datenerhebung, -speicherung und -publikation bereit.
- Aktualisiere Best Practices bei neuen Tools, Plattformen oder gesetzlichen Änderungen.

## 11. Überprüfung & Aktualisierung

- Evaluieren diese Richtlinie mindestens jährlich oder bei relevanten Projekt- bzw. Technologieänderungen.
- Protokolliere Anpassungen in den Projekt- oder Metadateien und informiere alle Beteiligten.

Für Rückfragen oder Vorschläge wende dich an `kontakt@jochen-hanisch.de`.
