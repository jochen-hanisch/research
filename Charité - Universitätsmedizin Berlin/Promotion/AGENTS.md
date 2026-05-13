---
author: Jochen Hanisch-Johannsen
title: AGENTS Promotion
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
# AGENTS Promotion

## Vaultweite Startreferenz

Vor jeder Arbeit zuerst lesen:

- `/Users/jochenhanisch-johannsen/Library/Mobile Documents/com~apple~CloudDocs/webapps/Projektmanagement/Betrieb/Agenten-Startreferenz.md`

Diese Datei ist der aktuelle CloudDocs-Pflichtanker. Der frühere Obsidian-Container `iCloud~md~obsidian` ist nicht mehr maßgeblich. Die lokalen Regeln dieser `AGENTS.md` bleiben zusätzlich verbindlich.

Die Parent-AGENTS.md im Research-Verzeichnis ([../../AGENTS.md](../../AGENTS.md)) gilt auch für die Promotion. Durch den iCloud-/CloudDocs-Umzug liegt die Promotion nicht mehr direkt unter `Research/Promotion`, sondern unter `Research/Charité - Universitätsmedizin Berlin/Promotion`. Diese Datei ergänzt nur die spezifischen Arbeitsregeln für die Dissertation.

## Aktuelle Ordnerlogik nach dem Umzug

Der iCloud-/CloudDocs-Bestand ist der maßgebliche Arbeitsstand. Der Git-Stand dient der nachvollziehbaren Versionierung ausgewählter Dateien, ersetzt aber nicht den lokalen iCloud-Bestand als Arbeitswahrheit.

Die aktuelle Promotionsstruktur ist:

- `00 Projektstruktur/`: Exposé, Fragenstruktur, Theorieansatz, Glossar und interne Dokumentation.
- `01 Methodologie/`, `02 Suchstrategie/`, `03 Quellenanalyse/`: methodische Arbeitsstände, Suchlogik, Analysevorbereitung und Materialerschließung.
- `04 Kapitelstruktur/`: Hauptkapitel, Anhänge und kapitelspezifische Arbeitsnotizen.
- `05 Textarbeit/`: Entwürfe, Überarbeitungen, Lesepfade und Feedback.
- `06 Transfer/`: Artikel, Präsentationen und Lehreinsatz.
- `07 Archiv/`: Altstruktur, verworfene und übertragene Arbeitsstände.
- `08 Metaquellen/`: Abbildungen, Forschungsdesign, Digitalmethodik, Daten, Quellcodes und Metadaten.
- `09 Backup/`: JSON-/Bib-Exporte und Abgleichstände.
- `tools/`: Pandoc-, Zotero- und Hilfswerkzeuge für Build, Literaturpflege und Arbeitskontrolle.

Versioniert werden nur bewusst ausgewählte Dateien. In Markdown-Dateien kennzeichnet `versioned: true` den aktuellen versionierten Kern. Große, sensible, temporäre oder rein lokale Arbeitsbestände bleiben außerhalb des Git-Kerns, sofern nicht ausdrücklich anders beauftragt.

## Build- und Dokumentationsanker

Vor inhaltlichen oder technischen Änderungen sind mindestens zu prüfen:

- `README.md`
- `08 Metaquellen/Matadaten/README.md`
- `08 Metaquellen/Matadaten/CONTRIBUTING.md`
- `08 Metaquellen/08-05 Quellcodes/README.md`
- `00 Projektstruktur/00-05 Dokumentation/Bestandsaufnahme Promotion.md`, sofern vorhanden

Builds werden aus dem Promotionsordner gestartet:

```bash
./build-dissertation.sh fast
./build-dissertation-docx.sh fast
```

Der Fast-PDF-Build ist die Standardprüfung nach Änderungen an Kapiteltexten, Frontmatter, Abbildungen, Literaturpfaden oder Pandoc-/LaTeX-nahen Dateien. Bei reinen Dokumentationsänderungen reicht eine gezielte Plausibilitätsprüfung, sofern keine Build-relevanten Pfade geändert wurden.

## Analyse-, Daten- und Simulationslinien

Die technischen Analysepfade liegen gebündelt unter `08 Metaquellen/08-05 Quellcodes/` und beziehen sich auf Daten und Abbildungen in `08 Metaquellen/08-04 Daten/` und `08 Metaquellen/08-01 Abbildungen/`.

- Literatur- und Korpusanalyse: `analyse_netzwerk.py`, `analyse_korrelation.py`, `deskriptive-literaturauswahl.py` mit den jeweiligen `config_*`-Dateien.
- LMS-/Umfrageauswertung: `Auswertung-LMS.py` und `config-auswertung-lms.py`; offene Datensätze liegen in `08 Metaquellen/08-04 Daten/Datenset/umfrage-analysen/`.
- Eye-Tracking: `verteilung-konfidenz.py`, `config_eye_tracking.py` und die aggregierten Bildexports in `08 Metaquellen/08-04 Daten/Datenset/eye-tracking-bilder/` sowie Abbildungen unter `08 Metaquellen/08-01 Abbildungen/eye-traking/`.
- Simulation digitales Bildungswirkgefüge: `simulation-bildungswirkgefuege.py`, `config_bildungswirkgefuege.py`, `modellpruefung.py` und Abbildungen unter `08 Metaquellen/08-01 Abbildungen/didaktik/`.
- TEI-gestützte Simulation: `tei-bildungswirkgefuege.py`, TEI-Daten unter `08 Metaquellen/08-04 Daten/Datenset/TEI/` und das Zenodo-Paket `zenodo-tei-bildungswirkgefuege/`.

Skripte können lokale absolute Pfade, externe Module (`ci_template`, `archetypen`) oder Umgebungsvariablen erwarten. Vor Ausführung sind README, Konfiguration und Ausgabeziel zu prüfen. Keine Skripte mit Schreibzugriff auf Zotero, Remote-Server, Exportordner oder veröffentlichte Datensätze ohne ausdrückliche Freigabe ausführen.

## Git und Veröffentlichungen

Gitea bleibt nicht implizit zu nutzen. Für `tea` gilt auf diesem Gerät weiterhin `--login uss-research-gitea`. Git-Remotes, Branches und Account-Konfigurationen werden nicht ohne ausdrücklichen Auftrag geändert.

Bei Abweichungen zwischen iCloud-Dateibaum und Remote gilt für diesen Promotionsordner zuerst der iCloud-Dateibaum. Remote-Stände dürfen nicht per Pull/Rebase/Merge über den iCloud-Stand gelegt werden, ohne vorher eine reine Vergleichsansicht zu erstellen und die Entscheidung offenzulegen.

## Arbeitsprinzipien für die Dissertation

Diese Datei enthält verbindliche Schreib- und Bearbeitungsregeln für die Dissertation. Die Regeln dienen wissenschaftlicher Nachvollziehbarkeit, methodischer Stringenz, begrifflicher Kohärenz und sprachlicher Einheitlichkeit.

## Zitation und Herkunft

- Der Zitationsstil folgt dem aktuellen APA-Stil.
- Quellen werden über Zotero verwaltet. Referenzen liegen als BibLaTeX-Zitierschlüssel vor.
- Jede tragende Aussage braucht einen Herkunftsstatus nach der Tabelle in der Parent-AGENTS.md des Research-Verzeichnisses ([../AGENTS.md](../AGENTS.md)).
- Die allgemeinen Zitierregeln aus der Parent-AGENTS.md gelten auch für die Dissertation.

## Sprachstil

- Die Arbeit folgt gendergerechter Sprache.
- Gendergerechte Sprache soll Inklusion, Diversität, Gleichstellung, wissenschaftliche Präzision und Verständlichkeit fördern.
- Der Gender-Asterisk wird verwendet, wenn Personenbezeichnungen nicht geschlechtsneutral formuliert werden können oder sollen.
- Geschlechtsneutrale Formulierungen sind zu bevorzugen, wenn sie präzise und gut lesbar bleiben.
- Diktate, Hinweise und mündliche Formulierungen des Autors sind als Stilquelle zu nutzen. Aus ihnen wird die persönliche Denk- und Sprechbewegung erschlossen und in eine wissenschaftlich tragfähige Sprache übertragen.
- Der Text soll die persönliche Arbeitsweise des Autors erkennen lassen. Er soll argumentativ geführt, mündlich nachvollziehbar, fachlich präzise und ohne unnötig verdichtete Wissenschaftssprache sein.
- Formulierungen dürfen die Denkbewegung sichtbar machen, also erst klären, warum etwas an einer Stelle steht, und dann zur nächsten argumentativen Station überleiten.
- Wortwiederholungen in unmittelbarer Nähe vermeiden, insbesondere bei abstrakten Verben wie „entfalten“, „bestimmen“, „zeigen“ oder „verdeutlichen“.
- Kontrastierungen sparsam einsetzen. Formulierungen mit „nicht ..., sondern ...“, scharfe Gegenüberstellungen und ausschließende Abgrenzungen nur verwenden, wenn sie argumentativ notwendig sind.
- Bevorzugt wird eine verbindende Sprache, die Unterschiede kenntlich macht, ohne Lesende in gedankliche Sackgassen zu führen.
- Das Stilwort „aber“ vermeiden. Wenn damit Gleichzeitigkeit oder Ambivalenz gemeint ist, stattdessen „zugleich“, „gleichzeitig“, „während“, „dabei“, „unter diesen Bedingungen“ oder eine eigenständige Anschlussformulierung verwenden.
- Das Stilwort „klar“ vermeiden. Präzisere Alternativen sind je nach Kontext „tragfähig“, „sichtbar“, „nachvollziehbar“, „präzise“, „bestimmt“, „konturiert“ oder „ausgewiesen“.
- Keine satzinternen Doppelpunkte als argumentative Verdichtungsform verwenden.
- Komplexe Begründungen werden in eigenständige Sätze aufgelöst.
- Die Abkürzung „z. B.“ wird nur in Klammern und Fußnoten genutzt.
- Im Fließtext wird „beispielsweise“ verwendet.
- Die Formen „zum Beispiel“, „z. B.“ im Fließtext und „bspw.“ werden nicht verwendet.

## Verweise

- Im Fließtext werden „Kapitel“, „Abschnitt“, „Tabelle“, „Abbildung“ und „Seite“ in der Regel ausgeschrieben.
- Interne Verweise werden als klickbare Querverweise mit `\hyperref` gesetzt.
- Auf Kapitel und Unterkapitel wird über die jeweilige Nummer verwiesen, etwa `\hyperref[sec:Theorieteil]{Kapitel 2}`.
- Auf Anhänge wird über „Anhang“ und den jeweiligen Titel verwiesen, etwa `\hyperref[sec:A-1]{Anhang „Verzeichnis zentraler Begriffe“}`.
- Anhänge werden nicht über eine fortlaufende Kapitelnummer behandelt, sondern über ihre eigene Anhangsbezeichnung.
- Technische und klammergebundene Verweise nutzen standardisierte Abkürzungen.
- `S.` steht für Seite, etwa `[@doring_forschungsmethoden_2023, Seite 4-5]`.
- `Kap.` steht für Kapitel, etwa `[@doring_forschungsmethoden_2023, Kapitel 2.2]`.
- `Abb.` steht für Abbildung, etwa `\hyperref[fig:eyetracking-verteilung]{Abb.~\ref{fig:eyetracking-verteilung}}`.
- `Tab.` steht für Tabelle, etwa `\hyperref[tab:methoden_FU]{Tab.~\ref{tab:methoden_FU}}`.
- Ausgeschriebene Formen bleiben ebenfalls klickbar, etwa `\hyperref[fig:eyetracking-verteilung]{Abbildung~\ref{fig:eyetracking-verteilung}}`.
- Gleichungen werden mit `Gl.` referenziert, etwa `\hyperref[eq:verlust]{Gl.~\eqref{eq:verlust}}`.

## Begriffsbestimmung

- Definition, Herleitung und Begründung zentraler Begriffe erfolgen dort, wo die Terminologie erstmalig für die Argumentation gebraucht wird.
- Begriffe werden kontextbezogen eingeführt und nicht isoliert in einem vorgelagerten Definitionsblock gesammelt.
- Die Begriffsverwendung muss im spezifischen Bezugsrahmen erklärt werden.
- Eine weitergehende formale Unterscheidung von Definitionstypen wird nur vorgenommen, wenn sie für die Argumentation notwendig ist.
- Zentrale Begriffe werden zusätzlich im Begriffsverzeichnis auffindbar gemacht.
- Bei neu zusammengesetzten Begriffen werden die Bestandteile einzeln hergeleitet und erst danach synthetisiert.
- Synthesebegriffe sind als „Schlussfolgerung“ oder neues Gerüst kenntlich zu machen, wenn sie nicht als etablierte Literaturbegriffe vorliegen.
- Wenn eine Begriffskombination in der Bildungswissenschaft kaum oder nicht etabliert bearbeitet ist, wird dies als Forschungslücke und Eigenleistung ausgewiesen, nicht als Schwäche der Argumentation.
- Zentrale Synthesebegriffe müssen aus den Denkspuren des Autors im Vault heraus rekonstruiert werden, wenn dort einschlägige Notizen, Vorarbeiten, Diktate oder frühere Textfassungen vorhanden sind.
- Eigene Denkspuren ersetzen keine Literaturbasis. Sie liefern die argumentative Eigenlogik, die anschließend mit externer Fachliteratur und vorhandenen Vorarbeiten abgesichert wird.
- Bei der Herleitung des digitalen Bildungswirkgefüges ist ausdrücklich zu prüfen, welche Bestandteile literaturbasiert gestützt sind und welche Zusammenführung als neues Gerüst beziehungsweise Schlussfolgerung des Autors geführt werden muss.
- Literaturbelege dürfen nicht überwiegend selbstreferenziell auf Hanisch-Johannsen/Hanisch gestützt werden. Eigene Vorarbeiten können die Linie tragen, benötigen aber externe Referenzen für zentrale fachliche Begriffe, Wirkannahmen und methodische Plausibilisierung.
- Wenn Zotero-PDFs lokal vorhanden sind, sind relevante Seitenzahlen in den PDFs zu prüfen und in der Argumentation möglichst seitenpräzise nach aktuellem APA-Stil anzugeben.

## Umgang mit Lehr-Lern-Paradigmen

- Lehr-Lern-Paradigmen werden nicht als historische Abfolge oder normative Rangordnung dargestellt.
- Sie werden als Bündel impliziter Wirkannahmen rekonstruiert.
- Für jedes Paradigma ist einzeln zu klären, welches Bildungsverständnis, Lernverständnis, Wissensverständnis und welche Steuerungslogik es nahelegt.
- Keine Aussage zu einem Paradigma ohne passenden Beleg.
- Bildung wird in dieser Arbeit nicht primär über einen Humboldt-Exkurs hergeleitet.
- Bildung wird gegenstandsbezogen aus den im LMS wirksamen Lehr-Lern-Paradigmen rekonstruiert und anschließend zu einem übergeordneten Arbeitsbegriff verdichtet.

## Kapitelaufbau und Tabellen

- Keine Zwischenfazits, Fazit-Unterkapitel oder Abschlusskapitel als Standardlösung verwenden.
- Kernaussagen, Vergleichsachsen und argumentative Funktion eines Kapitels gehören an den Anfang des jeweiligen Kapitels oder Abschnitts.
- Unterabschnitte entfalten die am Anfang gesetzte Leitlogik.
- Tabellen stehen möglichst dort, wo die Vergleichslogik eingeführt wird, nicht erst nachträglich am Ende einer Unterkapitelreihe.
- Tabellen werden als formal beschriftete Tabellen mit Caption und Label angelegt.
- Lose Markdown-Tabellen ohne `Table:`-Caption und Label vermeiden.
- Tabellen müssen im Fließtext eingeführt und nach ihrer Funktion für die Argumentation gerahmt werden.
- Auf eine Tabelle darf nicht unmittelbar eine neue Überschrift folgen.
- Nach Tabellen folgt ein kurzer Übergangstext, der die Funktion der Tabelle aufnimmt und in den nächsten Abschnitt überleitet.

## Begriffe Digitalität, Bildung, Gefüge

- Der Begriff „Bildung“ wird aus den Bildungsverständnissen der verwendeten Lehr-Lern-Paradigmen heraus gelesen.
- Der Begriff „digital“ beziehungsweise „Digitalität“ wird nicht auf Techniknutzung reduziert. Er bezeichnet kulturelle, mediale, infrastrukturelle und soziale Bedingungen digital vermittelter Bildungsräume.
- Der Begriff „Gefüge“ darf technisch-naturwissenschaftlich beginnen, insbesondere über Werkstoffkunde, Maschinenbau und technische Wirklogik.
- Der Transfer von „Gefüge“ in den Bildungsraum muss explizit begründet werden.
- Im Bildungsraum bezeichnet „Gefüge“ keine bloße Ansammlung von Elementen, sondern eine Kopplungsordnung aus Aufgaben, Rollen, Rückmeldungen, Sichtbarkeiten, Zeitlogiken, Beziehungen, technischen Funktionen und organisationalen Regeln.
- Der Begriff „digitales Bildungswirkgefüge“ ist als Synthesebegriff zu behandeln. Ziel ist seine Herleitung und Einführung als Wirkgefüge im digitalen Bildungsraum. Die Literatur stützt die Bestandteile, die Zusammenführung ist ein neues Gerüst.

## LLM-Einsatz

- Generative Sprachmodelle werden als kognitive Assistenz genutzt, nicht als Ersatz für menschliche Urteils- und Verantwortungsfunktionen.
- Wenn konkret generative Sprachmodelle gemeint sind, wird „LLM“ oder „generative Sprachmodelle“ verwendet.
- „KI“ bleibt der Oberbegriff für allgemeinere Zusammenhänge.
- Es ist jeweils die spezifischste zutreffende Bezeichnung zu verwenden.
- LLM können für strukturierte Zusammenfassungen, Extraktion von Kernaussagen, promptbasierte Vorstrukturierung, Konsistenzunterstützung bei qualitativen Codierungen und redaktionelle Unterstützung genutzt werden.
- LLM-Outputs gelten als analytische Verdichtungen.
- LLM-Outputs müssen kontrolliert, korrigiert und mit Primärquellen sowie eigener Einschätzung abgeglichen werden.
- Risiken wie Halluzinationen, Referenzfehler, Verzerrungen, Integritätsfragen, Zuschreibungsprobleme und epistemische Verflachung sind mitzudenken.
- Standardisierte Prompts, Protokollierung von Prompt-Ständen und menschliche Endredaktion sind verbindliche Absicherungsmaßnahmen.
- Detektionsverfahren für LLM-generierte Textanteile dürfen nur als ergänzende Kontrollspur verwendet werden.
- Detektionsverfahren sind keine alleinige Begründungsbasis.
- Die Textgenese soll nachvollziehbar bleiben. Entwicklungsstände, Revisionen und inhaltliche Entscheidungen sind so weit wie praktikabel rekonstruierbar zu halten.
