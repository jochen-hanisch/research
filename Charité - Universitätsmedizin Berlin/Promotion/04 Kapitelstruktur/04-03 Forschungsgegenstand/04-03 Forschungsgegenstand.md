---
author: Jochen Hanisch-Johannsen
title: 04-03 Forschungsgegenstand
versioned: true
Repository: https://git.jochen-hanisch.de/jochen-hanisch/research
Discussion:
Publication: https://zenodo.org/records/###
created: 2026-05-10
updated: 2026-05-13
publish: false
published:
status:
priority:
project:
due:
tags: []
---
\newpage

# 3 Forschungsgegenstand als LMS-Architektur {#sec:Forschungsgegenstand}

Dieses Kapitel beschreibt den Forschungsgegenstand in seiner rechtlich-funktionalen, didaktischen und technischen Architektur. Es konkretisiert damit die in \hyperref[sec:Theorieteil]{Kapitel 2} entwickelte Wirkgefügeperspektive am untersuchten Learning Management System und schafft die Grundlage für die spätere Ergebnisdarstellung in \hyperref[sec:Ergebnisse]{Kapitel 5}.

Der Forschungsgegenstand wird dabei als Kopplungsordnung beschrieben. Im Zentrum steht die Frage, wie Norm, Didaktik, technische Infrastruktur und operative Nutzung im untersuchten LMS so zusammenwirken, dass Lernhandlungen ermöglicht, strukturiert oder begrenzt werden.

Begriffe und Wirkannahmen aus Kapitel \hyperref[sec:Theorieteil]{2} bleiben abstrakt, solange sie nicht am konkreten Fall greifen müssen. Genau hier setzt das Kapitel an. Es beschreibt den Gegenstand so, dass anschließend methodisch nachvollziehbar untersucht werden kann, worin die tragenden Kopplungen des Systems bestehen und an welchen Stellen ihre Wirkung empirisch sichtbar wird.

Für das Verständnis des Kapitels steht daher die Funktion der Moodle-Bausteine im Ausbildungsalltag im Vordergrund. Aufgaben, Quellen, Foren, Feedback, Datenbanken, Kursorganisation und Portfolio-Anschlüsse werden als Orte beschrieben, an denen Lernen, Dokumentation, Rückmeldung und Verantwortung miteinander verbunden werden.

\phantomsection\label{sec:Gefuegeperspektive-FG}

**Begriffsrahmung: Gefügeperspektive auf die LMS-Architektur**

Die Darstellung des Forschungsgegenstandes erfolgt als Rekonstruktion einer Kopplungsordnung. Das LMS wird als *Gefüge* im Sinn der in \hyperref[sec:Theorieteil]{Kapitel 2} entwickelten Begriffsarbeit beschrieben. Die Begriffsdefinitionen (Wirkung, Gefüge, Wirkgefüge) werden dabei ausschließlich in \hyperref[sec:Begriffe-Wirkung-Gefuege]{Abschnitt~2.2.4} festgelegt; im vorliegenden Kapitel wird die Perspektive auf die Systemarchitektur angewendet. Im Fokus steht damit, wie strukturierte Elemente (z. B. Aufgaben, Foren, Feedback, Rollen‑ und Sichtbarkeitsregeln, Zeitlogiken) zueinander gekoppelt sind und welche Anschlussbedingungen diese Kopplungen für Lernhandlungen bereitstellen.

Anschaulich lässt sich der Gefügebegriff über eine werkstoffkundliche Analogie präzisieren. Die Anordnung der Körner (Korngrenzen, Verteilung, Orientierung) prägt die Eigenschaften eines Materials und wird erst über ein „Schliffbild“ sichtbar. Übertragen auf digitale Bildungsräume heißt das, dass Wirksamkeit aus der Kopplung mehrerer Elemente im Nutzungsverlauf entsteht, beispielsweise aus Aufgabenstellung, Rückmeldung, Sichtbarkeit und sozialen Bezugnahmen, die zusammen eine Anschlusskette ermöglichen oder blockieren.

Für die weiteren Abschnitte bedeutet das, dass \hyperref[sec:Kontext-FG]{Kontext (3.1)} und \hyperref[sec:Entwicklung-Einbettung]{Entwicklung/Einbettung (3.2)} so beschrieben werden, dass die jeweils relevanten Kopplungen zwischen Norm, Didaktik und technischer Architektur als Gefüge sichtbar werden und später als Wirkgefüge‑Analyse anschlussfähig bleiben.

## 3.1 Kontext des Forschungsgegenstands {#sec:Kontext-FG}

Der Kontext des Forschungsgegenstands wird über zwei Rahmungen bestimmt. Die rechtlich-funktionale Rahmung klärt, welche normativen Anforderungen den Ausbildungsgang strukturieren; die didaktisch-strukturelle Verortung zeigt, wie diese Anforderungen in eine lernorganisatorische Ordnung überführt werden.

### 3.1.1 Rechtlich-funktionale Rahmung {#sec:RechtlicheRahmung}

Das hier zu beschreibende LMS wird in einem Feld eingesetzt, das durch bundes- und landesrechtliche Vorgaben für Gesundheits- und Heilberufe geprägt ist. Für die hier interessierende Ausbildung von Notfallsanitäterinnen und Notfallsanitätern ist vor allem relevant, dass die Berufsbezeichnung rechtlich geschützt ist und an eine staatlich geregelte Ausbildung sowie Prüfung gebunden bleibt [@bundesgesundheitsministerium_gesundheitsberufe_2025].

Im Anwendungsfeld der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern unterliegen sowohl die Ausbildung selbst als auch die Erlaubnis zum Führen der Berufsbezeichnung staatlichen Regelungen. Maßgeblich verantwortlich für die gesetzeskonforme Umsetzung ist nach § 5 Abs. 3 Satz 4 NotSanG die Schule, in deren Gesamtverantwortung die „Organisation und Koordination des theoretischen und praktischen Unterrichts und der praktischen Ausbildung entsprechend dem Ausbildungsziel“ [@bundesrepublik_deutschland_gesetz_2023, § 5 (3) Satz 4] liegt. Die genaue Bedeutung dieses Auftrages verdeutlichen Dielmann & Malottke [@dielmann_notfallsanitatergesetz_2017, Seite 137-138] in ihrem Kommentar und bieten damit eine zentrale normierte Grundlage zur Herleitung der Rolle eines LMS innerhalb der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern.

Den Kommentatoren nach liegt die Gesamtverantwortung der Schule bei der Organisation und Koordination des Unterrichts und der praktischen Ausbildung; die Gesamtverantwortung für die Ausbildung bleibt weiterhin dem Träger zugeordnet [@dielmann_notfallsanitatergesetz_2017, Seite 137-138]. Für die Praxis bedeutet das eine abgestimmte Verzahnung der Lernorte Lehrrettungswache, Schule und Krankenhaus entlang des gesetzlich vorgegebenen Ausbildungsziels (§ 4 NotSanG) [@bundesrepublik_deutschland_gesetz_2023, § 4]. Die Schule kann diesen Rahmen gestalten und bleibt dabei an die rechtlichen und organisatorischen Vorgaben gebunden.

Aus der Koordinations- und Organisationsverantwortung der Schule lässt sich ableiten, dass ein LMS als geeignetes Instrument verstanden werden kann, um diese Aufgabe verlässlich wahrzunehmen. Die nachvollziehbare Zusammenführung von Kursen, Kalendern, Lernfortschritten, Aufgaben und Einsatzberichten in E-Portfolios\label{term:e-portfolio} bietet dafür eine tragfähige Struktur. Ergänzend entsteht durch Fallbearbeitungen, Praxisreflexionen und dokumentierte Rückmeldeschleifen ein didaktisches Gerüst, das die Abstimmung zwischen Lernorten sowie zwischen theoretischen und praktischen Ausbildungsanteilen stützt. Unter diesen Voraussetzungen wird das LMS zu einem konkreten Werkzeug schulischer Koordination und Organisation.

Die rechtlichen Ausbildungsbestimmungen verlangen, individuelle Ausbildungspläne so zu gestalten, dass Rahmenlehrplan, Stundenplan und Einsatzplan inhaltlich aufeinander bezogen bleiben. Das LMS muss folglich in der Lage sein, die einzelnen Elemente individuell und lernortspezifisch aufeinander abzustimmen. Damit fungiert es als strukturelles Bindeglied zwischen Theorie (Stundenplan), Praxis (Einsatzorte) und Individualisierung (Ausbildungspläne) und kann diese zunächst getrennten Elemente über Planungs- und Synchronisationsfunktionen miteinander verbinden.

Aus der geteilten Verantwortungsstruktur folgt ein sachlicher Bedarf an digital gestützter Koordination. Der Ausbildungsträger\label{term:ausbildungstraeger} behält seine Verantwortung, während die Schule mit dem LMS einen Teil der laufenden Abstimmung, Dokumentation und Begleitung operativ bearbeitet. Ein digitales System kann Nachweise, Zeitstände und Rückmeldungen sichtbar bündeln und damit Aufgaben übernehmen, die analog deutlich aufwendiger zu organisieren wären. In diesem Sinne lässt sich das hier beschriebene LMS als sachgerechte Infrastruktur zur Erfüllung schulischer Aufgaben verstehen.

### 3.1.2 Didaktisch-strukturelle Verortung {#sec:DidaktischeVerortung}

Aufbauend auf der rechtlich-funktionalen Rahmung wird die Schule im vorliegenden Untersuchungsfall als normativ verantwortliche Instanz und als didaktisch gestaltende Organisation verstanden. Das LMS übernimmt in dieser Perspektive die Funktion einer didaktischen Infrastruktur, die Lernhandlungen über Lernorte hinweg ordnet, synchronisiert und anschlussfähig macht. Damit wird die in \hyperref[sec:Bildungswiss-Verortung]{Abschnitt~2.2} entwickelte Perspektive auf Bildung als Wirkgefüge im institutionellen Vollzug konkret. Entscheidend ist die Kopplung von Aufgabenlogik, Rückmeldung, Sichtbarkeit, Zeitstruktur und Rollen.

Table: Konsequenzen für das LMS innerhalb der rechtlich-funktionalen Rahmung \label{tab:lms-konsequenzen}

| Stichwort                                                                           | Erklärung                                                                                              | Quellenverweis                                                                    |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Verantwortung der Schule für Lernorttransfer\label{term:lernorttransfer}                                        | LMS als systemisches Steuerungsinstrument innerhalb der schulischen Gesamtverantwortung.               | § 5 (3) @bundesrepublik_deutschland_gesetz_2023; § 2 (1-3) @bmg_ausbildungs-_2023 |
| Aktive Begleitung durch Schule                                                      | LMS muss Funktionen für Reflexion, Kommunikation und Dokumentation der Praxisbegleitung bereitstellen. | § 2 (3) @bmg_ausbildungs-_2023                                                    |
| Strukturierte Zusammenarbeit zwischen Schule und praktischer Ausbildungseinrichtung | Erfordert Kommunikations- und Kooperationsfunktionen zwischen Schule und Praxispartnern.               | § 5 (3) @bundesrepublik_deutschland_gesetz_2023; § 2 (2-3) @bmg_ausbildungs-_2023 |
| Rechtsverbindlichkeit                                                               | LMS-Einsatz muss mit normativen Vorgaben vereinbar sein und Nachweismöglichkeiten bieten.              | § 11 @bundesrepublik_deutschland_gesetz_2023; Einleitung @bmg_ausbildungs-_2023   |
| Pädagogisch-didaktischer Anspruch steigt                                            | Komplexe didaktische Szenarien müssen abbildbar sein (z. B. Kompetenzraster, ePortfolio etc.).         | § 4 @bundesrepublik_deutschland_gesetz_2023; Anlage 1 @bmg_ausbildungs-_2023      |
| Qualitätssicherung durch digitale Unterstützung                                     | Die normativen Vorgaben betonen Ausbildungsqualität, Praxisbegleitung und die Verzahnung von Theorie und Praxis. Ein LMS kann diese Anforderungen durch nachvollziehbare Dokumentation und abgestimmte Abläufe unterstützen. | Seiten 44-45 [@bundesgesundheitsministerium_referentenentwurf_2012]                 |

\tabsubcaption{Konsequenzen der rechtlich-funktionalen Rahmung für die LMS-Architektur. Zusammengeführt sind zentrale normative Anforderungen (u.a. NotSanG und Ausbildungs-/Prüfungsrahmen) und daraus abgeleitete Funktions- und Strukturbedarfe des Systems (Koordination der Lernorte, Dokumentation/Nachweis, Kommunikation, Qualitätssicherung).}

Die schulisch-organisationale Einbettung präzisiert diese Funktion weiter. Der Träger bleibt für die Gesamtverantwortung der Ausbildung zuständig, die Schule verantwortet die Koordination der Lernorte und die didaktische Ausgestaltung der Lernprozesse, und die Praxisakteure in Lehrrettungswache sowie Krankenhaus sind als ko-produzierende Lernortpartner eingebunden. Im LMS wird diese Mehr-Akteurs-Struktur operativ sichtbar, indem Zuständigkeiten, Kommunikationswege, Nachweise und Rückmeldeschleifen in einer gemeinsamen Arbeitsumgebung zusammengeführt werden. Die Architektur bildet Inhalte ab und organisiert Verantwortungsbeziehungen entlang curricularer und organisatorischer Anforderungen.

Für den Untersuchungsfall ist zusätzlich die High-Responsibility-Team-(HRT)-Logik der Notfallversorgung konstitutiv. Entscheidungen erfolgen unter Zeitdruck, mit potenziell gravierenden Fehlerfolgen und hoher Interdependenz zwischen professionellen Rollen. Daraus ergibt sich didaktisch eine doppelte Anforderung. Erstens müssen Handlungssituationen transferfähig auf reale Lagen ausgerichtet sein; zweitens muss Rückkopplung so gestaltet werden, dass Unsicherheit, Fehlentscheidungen und Koordinationsprobleme lernwirksam bearbeitet werden können. Das LMS fungiert hier als strukturgebende Umgebung, in der Kompetenzaufbau, Lernorttransfer und reflexive Verarbeitung kritischer Entscheidungssituationen systematisch gekoppelt werden. Diese Kontextlogik begründet den Übergang zu Abschnitt~\hyperref[sec:Entwicklung-Einbettung]{3.2}, in dem die konkrete Systementwicklung aus dieser Mehrfachanforderung heraus rekonstruiert wird.

## 3.2 Entwicklung und Einbettung des LMS {#sec:Entwicklung-Einbettung}

Die Entwicklung und Einbettung des hier untersuchten Learning Management Systems erfolgte als systematische Auseinandersetzung mit den Herausforderungen einer digital gestützten Ausbildung im Gesundheitswesen. Die Konzeption entstand aus der Verbindung theoretischer Überlegungen, eigener empirischer Arbeiten sowie konkreter institutioneller Anforderungen im Rahmen der Einführung der dreijährigen Ausbildung von Notfallsanitäter\*innen.

Die folgenden Abschnitte zeichnen nach, wie sich das System von den ersten konzeptionellen Gedanken (\hyperref[sec:Entstehung-Konzept]{Abschnitt 3.2.1}) über die schulische Implementierung (\hyperref[sec:Implementierung-Schule]{Abschnitt 3.2.2}) und dynamische Weiterentwicklung (\hyperref[sec:Weiterentwicklung-extern]{Abschnitt 3.2.3}) bis zur empirischen Evaluation (\hyperref[sec:Evaluation-Reflexion]{Abschnitt 3.2.4}) konstituierte.

### 3.2.1 Entstehungskontext und konzeptionelle Grundlagen {#sec:Entstehung-Konzept}

Eine wichtige konzeptionelle Grundlage des hier untersuchten Learning Management Systems liegt in eigenen Vorarbeiten zu Einflussfaktoren nachhaltigen Wissensmanagements in digitalen Kollaborationsarrangements [@hanisch_nachhaltiges_2017]. Diese Vorarbeiten werden hier nur in dem Umfang aufgegriffen, in dem sie für die Herleitung des Forschungsgegenstands relevant sind.

Für die vorliegende Dissertation sind diese Ergebnisse als Vorbefunde bedeutsam, weil sie Hinweise darauf gaben, welche Faktoren beim Aufbau des Learning-Management-Systems besonders berücksichtigt werden mussten. Sichtbarkeit und Verfügbarkeit von Ergebnissen, die Wahrnehmbarkeit von Struktur sowie die tatsächliche Möglichkeit zu kollaborativer Interaktion erwiesen sich dabei als konstruktiv relevante Gesichtspunkte [@hanisch_nachhaltiges_2017, Kapitel 3.4; @hanisch_nachhaltiges_2017, Kapitel 3.5].

Die Voruntersuchung weist damit keine Wirksamkeit des späteren LMS nach. Sie bildet eine wesentliche Grundlage für seine Konzeption. Für die Dissertation folgt daraus die Forschungslogik, den Blick auf das daraus hervorgegangene LMS als Wirkgefüge zu richten. Der analytische Fokus liegt auf den Bedingungen, unter denen die Verschränkung von Zeit, Struktur und Interaktion im LMS lernförderlich wird oder an welchen Stellen sich Entkopplungen zeigen.

Für die Rahmung dieser Ergebnisse muss berücksichtigt werden, dass die zugrunde liegende Untersuchung im Rahmen eines sechswöchigen Kursformats stattfand, das auf die staatliche Prüfung vorbereitete und sich deutlich vom Format einer dreijährigen Ausbildung unterscheidet. Die Kritik der Teilnehmenden bezog sich mehrfach auf fehlende zeitliche Transparenz im Lernarrangement, insbesondere hinsichtlich der Verfügbarkeit gemeinsamer Arbeitsergebnisse. Hier zeigt sich, dass Zeit zugleich didaktischer und organisatorisch relevanter Faktor für nachhaltiges Lernen ist. Ein weiterer Befund betrifft die geringe Wirkung struktureller Einflussfaktoren, die darauf zurückzuführen sein könnte, dass die Teilnehmenden keine reale Anwendung strukturierter digitaler Werkzeuge erfahren hatten. Ihnen fehlte die Möglichkeit, mit kollaborativen Tools tatsächlich zu arbeiten. Eine bloße Vorstellung davon reichte nicht aus, um deren Wirksamkeit einzuschätzen. Auch die Interaktion wurde eher als wünschenswerte Möglichkeit denn als gelebte Praxis beschrieben. Eigene Beobachtungen legen nahe, dass Teilnehmende Interaktion vor allem im Sinne einer expertengeleiteten Selbstvergewisserung verstehen, beispielsweise in einer Rückkopplung mit Prüfenden [@hanisch_nachhaltiges_2017, Seite 18–19].

Die Ergebnisse der Voruntersuchung machten damit sichtbar, an welchen Stellen das damalige Setting die Bedeutung dieser Faktoren nur unzureichend erkennen ließ. Für die Konzeption des hier untersuchten Learning-Management-Systems war deshalb entscheidend, genau diese Punkte gezielt in die Weiterentwicklung aufzunehmen.

### 3.2.2 Implementierung in der schulseitigen Praxis {#sec:Implementierung-Schule}

Die konkrete Implementierung des hier untersuchten Learning Management Systems erfolgte ab dem Jahr 2016 im Zuge der Einführung der dreijährigen Ausbildung zur Notfallsanitäterin bzw. zum Notfallsanitäter an einer Rettungsdienstschule in Nordrhein-Westfalen. Aus der vorherigen Rettungsassistentenausbildung heraus bot sich damit erstmals die Möglichkeit, die Durchführung der Ausbildung auch digital zu gestalten. Zur Umsetzung gehörten die Abbildung der geltenden Lehrpläne und die systematische Nutzung von Wikis zur Sicherung von Gruppenarbeitsergebnissen, gerade vor dem Hintergrund der zuvor beschriebenen Untersuchungsergebnisse. Entscheidend für die Einführung eines Learning Management Systems war die Verbindung aus systematischem digitalem Zugang, persönlichen didaktischen Erfahrungen und der Erwartung, nachhaltige Kompetenzentwicklung strukturell unterstützen zu können. Die Rahmenbedingungen erwiesen sich insofern als günstig, als eine hohe institutionelle Offenheit für digitale Lernprozesse mit einem spürbaren persönlichen Engagement seitens der Lehrkräfte und der Schulleitung zusammenfiel.

Die heute untersuchte Architektur ist aus zwei Moodle-Instanzen heraus rekonstruierbar. Die ältere Instanz enthält die ursprüngliche H-NFS-Struktur im Format tabellarisch gegliederter Themenbereiche, die spätere Instanz führt diese Logik als NFS-H-Struktur in einer stärker standardisierten Kursarchitektur weiter. Damit liegt der Forschungsgegenstand als Konzept und als sichtbare Entwicklungslinie vor. Aus einer ersten digitalen Umsetzung beruflicher Handlungssituationen entstand eine institutionell verstetigte Architektur, in der curriculare Kurse, Kohortenkurse, Aufgaben, Rückmeldungen und organisatorische Steuerung systematisch gekoppelt sind.

Diese Entwicklung zeigt eine Drift, die während der Dissertationsarbeit am Gegenstand selbst sichtbar wurde. Drift meint hier die fortlaufende Verschiebung eines lebenden Learning-Management-Systems unter didaktischen, organisatorischen und technischen Bedingungen. Der lesende Moodle-Live-Abgleich vom 03.05.2026 weist diese Verschiebung direkt an den beiden Instanzen aus.

Table: Forschungsgegenständliche Drift der Moodle-Architektur \label{tab:moodle-drift}

| Beobachtungsdimension | Ältere Moodle-Instanz | Aktuelle Moodle-Instanz | Bedeutung für den Forschungsgegenstand |
|---|---|---|---|
| Kursformat | 32 produktive Handlungssituationen im Format `tabtopics` | 32 produktive Handlungssituationen im Format `topics` | Die Kurslogik verschiebt sich von einer stärker registerartigen Oberfläche zu einer standardisierten Abschnittslogik. |
| Standardisierte Abschnitte | Einführung, Ressourcen, Aufgaben, weiterführende Quellen, Lounge und Feedback in allen 32 Kursen; Kursorganisation in 27 Kursen | Einführung, Ressourcen, Aufgaben, weiterführende Quellen, Lounge, Feedback und Kursorganisation in allen 32 Kursen | Organisation wird in der aktuellen Instanz durchgängig als Bestandteil der Handlungssituation geführt. |
| Aufgabenmodule | 788 `assign`-Aktivitäten in H-01 bis H-31; H-06 enthält 14 Aufgabenmodule | 993 `assign`-Aktivitäten in NFS-H-01 bis NFS-H-32; NFS-H-01 bis NFS-H-31 umfassen 952 Aufgabenmodule, NFS-H-32 ergänzt 41 Aufgabenmodule zur Prüfungsvorbereitung | Die Aufgabenarchitektur wurde in den fortgeführten Handlungssituationen sichtbar ausgebaut und bleibt zugleich in derselben curricularen Kurslogik organisiert. NFS-H-32 erweitert die Architektur um eine eigenständige Prüfungsvorbereitungsstruktur. |
| Ergebnissicherung | In H-NFS-01 als eigener Bereich mit Wiki und Glossar sichtbar | In den NFS-H-Handlungssituationen stärker als Querschnitt über Aufgaben, Foren, Datenbanken und Feedback angelegt; in kohortenspezifischen und individuellen Räumen bleiben Wiki, Glossar und E-Portfolio als Ergebnis-, Begriffs- und Entwicklungsräume erhalten | Ergebnissicherung wandert von einem einzelnen sichtbaren Ablageort in eine verteilte Kopplungsfunktion des Systems. |
| Synchrone Kommunikation | BigBlueButton in allen 32 Handlungssituationen vorhanden | Kein BigBlueButton-Baustein in den 32 NFS-H-Handlungssituationen; synchrone Konnektivität ist perspektivisch über Microsoft Teams nach dem Moodle-5-Update vorgesehen | Die aktuelle Kursarchitektur betont asynchrone, dokumentierbare und kursnah wiederauffindbare Bearbeitungsspuren und hält synchrone Kommunikation als integrierbare Anschlussfunktion offen. |
| Datenbanklogik | Eine Datenbankaktivität in den 32 Handlungssituationen | 33 Datenbankaktivitäten in den 32 Handlungssituationen | Dokumentation, Nachverfolgung und strukturierte Rückmeldung werden stärker in die Kursarchitektur eingebaut. |

\tabsubcaption{Lesender Moodle-Live-Abgleich der älteren und der aktuellen Moodle-Instanz am 03.05.2026. Personenbezogene Daten wurden nicht übernommen; ausgewertet wurden Kursformate, Abschnittslogik und Aktivitätstypen der produktiven Handlungssituationen.}

Initiativ in der Umsetzung war unter anderem die Verbindung eigener Studienleistungen im Bereich der Bildungswissenschaft an der FernUniversität in Hagen mit den curricularen Anforderungen vor Ort. Die FernUniversität hatte sich im Rahmen ihrer Lehre in den pädagogischen Feldern der Förderung digitaler Lehr-Lern-Formate verpflichtet, was eine hohe Affinität zu digitalen Medien im Ausbildungskontext begünstigte. Die Ausgangslage war dabei unter anderem durch die Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter sowie den Rahmenlehrplan Nordrhein-Westfalen geprägt. Aufgrund divergierender Anforderungen in diesen Dokumenten wurde ein schulinterner Lehrplan entworfen, der beide Vorgaben integrieren und curricular anschlussfähig machen sollte. In dieser Struktur wurde das Learning Management System verankert. Die Einführung erfolgte schrittweise, wobei zunächst grundlegende Funktionen im Vordergrund standen – insbesondere der Aufbau von Foren zur Begleitung von Handlungssituationen\label{term:handlungssituationen} sowie die Nutzung der Wiki-Funktionalität zur Strukturierung kollaborativer Aufgabenbearbeitung (\hyperref[sec:A-5]{Anhang „Übersicht Berufliche Handlungssituationen“}).

Als besonders hilfreich erwiesen sich die in den Jahren 2016 und 2017 regelmäßig durchgeführten sechswöchigen Vorbereitungskurse auf die staatliche Prüfung. Diese zeichneten sich durch eine hohe Zahl an Teilnehmenden und eine dadurch bedingte intensive Belastungssituation aus, in der das System auf seine technische und didaktische Belastbarkeit hin überprüft werden konnte. Die Erfahrungen aus diesen Kursen flossen unmittelbar in die Weiterentwicklung ein und ermöglichten eine erste fundierte Rückmeldung zur Frage, inwieweit digitale Systeme zur Begleitung, Strukturierung und Auswertung von Lernprozessen in hochverdichteten Ausbildungskontexten beitragen können.

### 3.2.3 Weiterentwicklung durch externe Anforderungen {#sec:Weiterentwicklung-extern}

Mit Beginn der pandemischen Lage im Frühjahr 2020 wurden auch für die Ausbildung in den Gesundheitsfachberufen einschneidende Maßnahmen erlassen. Der Erlass des Ministeriums für Arbeit, Gesundheit und Soziales des Landes Nordrhein-Westfalen sah eine Einstellung des regulären Unterrichtsbetriebs an Rettungsdienstschulen vor und empfahl zugleich die Entwicklung und Umsetzung digitaler Lehrformate zur Sicherung der Ausbildungskapazität [@schnabelin_masnahmen_2020]. Die bundesweite Verordnung zur Sicherung der Ausbildungen in den Gesundheitsfachberufen (EpiGesAusbSichV\label{term:epigesausbsichv}) konkretisierte wenig später, dass digitale Formate sowohl für den theoretischen als auch den praktischen Unterricht zulässig seien und entsprechend von den Schulen umgesetzt werden sollten [@bmg_verordnung_2020, § 2].

Die durch die COVID-19-Pandemie ausgelöste Umstellung auf digitalen Unterricht stellte auch für die hier untersuchte Schule eine Zäsur dar. Vor diesem Hintergrund wurde das bereits bestehende Learning Management System kurzfristig zur zentralen digitalen Infrastruktur weiterentwickelt. Wie @huber_covid-19_2020 im Rahmen des Schul-Barometers zeigen, waren insbesondere fehlende digitale Kompetenzen, unzureichende technische Ausstattung und mangelnde systemische Koordination zentrale Herausforderungen für viele Bildungseinrichtungen im deutschsprachigen Raum [@huber_covid-19_2020, Seite 30]. An der hier untersuchten Bildungseinrichtung konnte auf eine bereits zuvor begonnene Systemstruktur zurückgegriffen werden (Abschnitt~\hyperref[sec:Implementierung-Schule]{3.2.2}). Die pandemiebedingte Anforderung beschleunigte Nutzung und Systemanpassung zugleich. Für den produktiven Bereich NFS-H-01 bis NFS-H-31 sind 952 live gezählte Aufgabenmodule dokumentiert; NFS-H-32 ergänzt diese Kursarchitektur als Prüfungsvorbereitungsstruktur mit 41 weiteren Aufgabenmodulen. Insgesamt weist die aktuelle Instanz damit 993 Aufgabenmodule in 32 Handlungssituationen auf (\hyperref[sec:A-5]{Anhang „Übersicht Berufliche Handlungssituationen“}). Dies war insofern möglich, als die Entwicklung des Curriculums der Ausbildung von Notfallsanitäterinnen und Notfallsanitätern bereits durch die im vorherigen Kapitel beschriebenen Grundgedanken als digitale Realisierung mitgedacht wurde.

Rückblickend kann abgeleitet werden, dass die pandemiebedingten Einschränkungen als Katalysator für die vollständige Entfaltung des zuvor konzipierten Zusammenspiels aus Studienleistungen, Curriculumentwicklung und LMS-Aufbau wirkten. Viele Bildungseinrichtungen standen vor der Herausforderung, kurzfristig digitale Übergangslösungen zu implementieren @huber_covid-19_2020; hier konnte auf eine bereits didaktisch durchdachte und technisch vorbereitete Infrastruktur zurückgegriffen werden [@huber_covid-19_2020, Seite 34]. Die durch die Pandemie entstandene Notwendigkeit, sämtliche Lernprozesse digital zu strukturieren, wurde zu einer Gelegenheit, in der das Potenzial des bereits vorhandenen Learning Management Systems sichtbar wurde. Die zuvor entwickelten Konzepte, Funktionen und strukturellen Entscheidungen konnten unter Realbedingungen erprobt, ausgeweitet und im laufenden Betrieb angepasst werden. Dieser Prozess ließ bereits erste Elemente einer systemischen Verstetigung erkennen.

Die retrospektive Einordnung dieser Weiterentwicklung verdeutlicht der Vergleich mit den Ergebnissen von @gachanja_e-learning_2021, die in ihrer Untersuchung die Pandemie als Übergangs- und Bewährungsphase, die Rolle bestehender Infrastruktur sowie die Institutional Readiness als Voraussetzung für gelingendes E-Learning betrachteten. In ihrer Studie zur Implementierung eines E-Learning-Kurses im medizinischen Bildungsbereich zeigen die Forschenden, dass der Übergang in digitale Lernsettings unter Krisenbedingungen oft zu Überlastung, technischen Ausfällen und geringer Beteiligung führt. Entscheidend für das Gelingen sei weniger die eingesetzte Plattform als vielmehr die institutionelle Vorbereitung und strukturelle Stabilität. Diese Beobachtungen lassen sich rückblickend auch für das hier untersuchte System bestätigen [@gachanja_e-learning_2021, Seite 3, 6].
Ein Vergleich zwischen den präventiven Gegebenheiten und den retrospektiven Erkenntnissen verdeutlicht \hyperref[tab:lms-entwicklung]{Tabelle~\ref{tab:lms-entwicklung}}.

Table: Retrospektiver Vergleich der LMS-Entwicklung \label{tab:lms-entwicklung}

| Aspekt              | @gachanja_e-learning_2021                                                       | Hanisch (eig. Darstellung)                                                       |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Ausgangspunkt       | Unerwartete Umstellung auf E-Learning aufgrund pandemischer Vorgaben        | Bereits bestehendes LMS wird unter Pandemiebedingungen ausgebaut                 |
| Technische Ausstattung | Mangelhaft, v.a. Internetzugang und Serverleistung                         | Vollständige curricular-integrierte LMS-Struktur vorhanden                       |
| Systemstruktur      | Learning-Management-System ad hoc eingesetzt, mit starker Abhängigkeit vom Präsenzbetrieb       | Learning-Management-System bereits inhaltlich und organisatorisch vorbereitet                        |
| Herausforderungen    | Überforderung, fehlende Prüfungsformate, geringe Interaktion                | NFS-H-01 bis NFS-H-32 mit insgesamt 993 Aufgabenmodulen; darin NFS-H-01 bis NFS-H-31 mit 952 Aufgabenmodulen und NFS-H-32 als Prüfungsvorbereitungsstruktur mit 41 Aufgabenmodulen; Ergebnissicherung als verteilte Spur über Aufgaben, Foren, Datenbanken, Feedback, Wiki/Glossar in kohortenspezifischen Kursen und individuelle bzw. kohortenspezifische E-Portfolio-Anschlüsse |
| Ergebnisbewertung   | LMS als Notlösung ohne nachhaltige Wirkung                                  | LMS als systemische Infrastruktur mit Verstetigungspotenzial                     |
| Schlüsselbedingung  | „Institutional readiness“ erforderlich für Erfolg                           | Vorbereitung ab 2016 als Fundament nicht-planbarer pandemischer Handlungsfähigkeit |

\tabsubcaption{Retrospektiver Vergleich der pandemiebedingten LMS-Umstellung (Literaturbefund) mit der dokumentierten Systementwicklung im Rahmen der Notfallsanitäter-Ausbildung (2016--2023). Die Gegenüberstellung fokussiert Ausgangspunkt, Infrastrukturvoraussetzungen, Herausforderungen und Bewertung und dient der Einordnung der Pandemie als Katalysator bereits vorbereiteter Systemarchitektur.}

Während das bei @gachanja_e-learning_2021 untersuchte E-Learning-Modell unter Bedingungen einer ad-hoc eingeführten digitalen Infrastruktur umgesetzt wurde, basierte das hier untersuchte System auf einem längerfristig entwickelten, curricular integrierten und technisch stabilen Ansatz. Die Gegenüberstellung macht damit plausibel, warum institutionelle Vorbereitung, systemische Vordisposition und die frühzeitige Einbettung digitaler Lernprozesse für die Funktionsfähigkeit eines Learning Management Systems unter Belastungsbedingungen bedeutsam sind. Zugleich zeigt sich ein Unterschied in der Einordnung der Systeme. Während @gachanja_e-learning_2021 das LMS als temporäre Notlösung beschreiben, war das hier untersuchte System bereits vor der Krise als Teil der schulischen Infrastruktur angelegt.

Damit die hier geschilderte Nutzung auch außerhalb von Krisensituationen ihr Potenzial dauerhaft entfalten kann, wurden im hier beschriebenen Learning Management System turnusmäßig Evaluations- und Reflexionsschleifen eingeführt [@jutte_professionalitatsentwicklung_2025]. Ziel dieser Maßnahme war diejenigen Verbesserungspotenziale zu identifizieren, die bereits durch kleinste Anpassungen wirksam werden konnten.

### 3.2.4 Evaluation und Reflexion {#sec:Evaluation-Reflexion}

Bereits in der hier mehrfach zitierten studentischen Ausgangsuntersuchung wurde versucht, die Wirkung des eingesetzten Learning Management Systems in Anlehnung an das vierstufige Evaluationsmodell nach @kirkpatrick_evaluating_1998 zu evaluieren. Das Modell mit den Ebenen Reaktion, Lernen, Verhalten und Ergebnisse kann als Standardrahmen zur Bewertung von Trainingsmaßnahmen betrachtet und grundsätzlich auch auf Bildungsmaßnahmen in Heilberufen übertragen werden [@hanisch_nachhaltiges_2017, Seite 13]. Das Kirkpatrick-Modell\label{term:kirkpatrick-modell} wurde auf die Evaluation digital gestützter Gruppenarbeitsprozesse angewendet. Die Ergebnisse zeigten, dass die dort untersuchten Einflussfaktoren, insbesondere Zeit, Struktur und Interaktion, den vier Stufen nicht trennscharf zugeordnet werden konnten. Die Untersuchung verlagerte den Schwerpunkt daher von einer stufenbasierten Lernbewertung zu einer inhaltsbezogenen Wirkungsperspektive, bei der die nachhaltige Sicherung von Lernergebnissen im Mittelpunkt stand [@hanisch_nachhaltiges_2017, Seite 13–14, 20].

Aus dieser methodischen Einschränkung ergibt sich der Bedarf nach einem Instrument, das Ergebnis- und Gestaltungsmerkmale von Trainingssituationen gemeinsam erfassen kann. Das Training Evaluation Inventory (TEI)\label{term:tei} nach @ritzmann_training_2014 wurde deshalb als geeignetes Folgeinstrument identifiziert und in die Ausbildungskonzeption integriert. Das TEI schließt an die evaluative Grundfrage nach Trainingseffekten an und ergänzt sie um die systematische Erfassung von Designmerkmalen. Für den Untersuchungsrahmen dieses Kapitels liegt sein Nutzen darin, dass die in den Handlungssituationen des LMS angelegten didaktischen Kopplungen und die wahrgenommenen Trainingseffekte in einer gemeinsamen Auswertungslogik beobachtbar werden.

Das TEI ist für den organisationalen Alltag praktikabel angelegt und umfasst in der Validierungsfassung zehn Skalen mit insgesamt 53 Items. Die beiden zentralen Dimensionen sind wahrgenommene Trainingseffekte und didaktische Merkmale des Trainingsdesigns. Diese Kombination ermöglicht die gemeinsame Erfassung von Ergebnis- und Gestaltungsdimensionen eines Trainings. Die Skalen zu Lernfreude, Nützlichkeit, Wissenszuwachs, Einstellung und Transfer erfassen kognitive und affektive Wirkungen. Die Designskalen beruhen auf den didaktischen Prinzipien Problemorientierung, Aktivierung, Demonstration, Anwendung und Integration. Diese Fünf-Punkte-Struktur folgt den Überlegungen von Merrill (2002) und erlaubt Rückschlüsse darauf, unter welchen Designbedingungen Trainingsmaßnahmen als wirksam eingeschätzt werden. In der Validierungsstudie erweisen sich insbesondere die Skalen „Demonstration“, „Anwendung“ und „Integration“ als stärkste Prädiktoren positiver Trainingseffekte. Die regelmäßige Anwendung des TEI nach jeder Handlungssituation im hier betrachteten LMS macht diesen Zusammenhang als Rückmeldeschleife nutzbar. Sie verbindet summative Bewertung und formative Rückkopplung auf Mikroebene. Die erhobenen Daten erlauben es, die Gestaltung einzelner Handlungssituationen gezielt anzupassen und schrittweise zu verbessern. Evaluation wird damit integraler Bestandteil der Systementwicklung. Die Autor\*innen betonen selbst: „Evaluating the design features of training is important to shed light on the reasons why certain training outcome effects were produced“ [@ritzmann_training_2014, Seite 47] [@ritzmann_training_2014, Seite 43, 48, 62].

Für die vorliegende Arbeit liegt eine bereinigte Folge aggregierter Moodle-Exporte pro Handlungssituation (`Evaluation-01`…`Evaluation-32`) vor. Diese operative Moodle-Fassung umfasst je 46 Fragen. Sie wird damit als feldbezogene Implementierung des TEI geführt. Die Validierungsfassung mit 53 Items bleibt der Referenzrahmen. Insgesamt enthalten die Exporte 843 ausgefüllte Feedbacks. Die Rücklaufzahl variiert zwischen 4 und 58 ausgefüllten Feedbacks pro Handlungssituation [@hanisch-johannsen_tei-feedback_2025].

Der Moodle-Abgleich bestätigt die architektonische Verankerung dieser Evaluationslogik. In der aktuellen Instanz ist der Abschnitt „Feedback“ in allen 32 Handlungssituationen vorhanden. Das Inventar weist 37 Feedback-Aktivitäten aus; 36 davon tragen die Bezeichnung „eigene Evaluation“ oder eine entsprechende Variantenbezeichnung. Die Abweichung gegenüber den 32 Auswertungsexporten erklärt sich aus alten, doppelten oder zusätzlichen Evaluationsaktivitäten in einzelnen Handlungssituationen. Für die Dissertation werden deshalb die 32 bereinigten aggregierten Exporte als Auswertungsgrundlage geführt.

Neben dieser standardisierten Evaluation ist eine weitere Rückkopplungsspur in die Handlungssituationen eingelassen. In allen 32 Handlungssituationen der aktuellen Instanz findet sich eine Datenbank-Aktivität mit der Bezeichnung „Wünsche, Ideen, Gedanken, Anregungen, Fehler“. Während das TEI die wahrgenommenen Trainingseffekte und Designmerkmale strukturiert erhebt, eröffnet diese Datenbank einen niedrigschwelligen Ort für situative Rückmeldungen aus der laufenden Nutzung. Fehler, Anregungen und Verbesserungsideen werden dadurch bereits handlungssituationsbezogen an der Stelle dokumentierbar, an der sie auftreten. Für das hier rekonstruierte Wirkgefüge ist diese zweite Spur bedeutsam, weil sie Rückmeldung als operative Mitgestaltung des digitalen Bildungsraums lesbar macht.

Die exemplarische Verteilung der Rückläufe ist in \hyperref[tab:tei-ruecklaeufe]{Tabelle~\ref{tab:tei-ruecklaeufe}} dargestellt.

Table: TEI-Rückläufe pro Handlungssituation \label{tab:tei-ruecklaeufe}

| Evaluationsexport | Rücklauf n (ausgefüllte Feedbacks) | Items im Export |
| --- | ---: | ---: |
| `Evaluation-01` | 33 | 46 |
| `Evaluation-12` | 58 | 46 |
| `Evaluation-19` | 4 | 46 |

\tabsubcaption{Beispielhafte Darstellung der Rückläufe der bereinigten TEI-orientierten Moodle-Exporte pro Handlungssituation. Insgesamt liegen 32 Exporte mit je 46 Fragen und 843 ausgefüllten Feedbacks vor.}

Ein wesentlicher Vorteil liegt in der Organisations- und Teilnehmendenfreundlichkeit des Instruments. Das TEI kann innerhalb der Ausbildungsstruktur angewendet werden, wobei die Bearbeitungsdauer im Durchschnitt weniger als zehn Minuten beträgt. Dadurch wird eine regelmäßige und belastungsarme Anwendung auch im stark getakteten Ausbildungsgeschehen möglich. Zudem wurde das TEI so konzipiert, dass es direkt nach einem Trainingselement eingesetzt werden kann. Damit ist das Instrument an die Struktur der Handlungssituationen im Learning Management System anschlussfähig. Die empirisch belegte interne Konsistenz der Skalen (Cronbachs α = .73–.89) und die faktorenanalytisch abgesicherte Skalenstruktur bestätigen die methodische Qualität [@ritzmann_training_2014, Seite 49, 55].

Mit der theoretischen Fundierung, empirischen Absicherung und praxisorientierten Anwendbarkeit stellt das TEI ein wissenschaftlich tragfähiges Instrument für die Evaluation in gesundheitsberuflichen Ausbildungsgängen dar. Insgesamt ist die regelmäßige Anwendung des TEI hier als strukturierte Reflexionsinstanz im digitalen Bildungsraum zu verstehen. Sie dient der Sicherung lernprozessbegleitender Qualität, der gezielten Optimierung didaktischer Maßnahmen und der empirisch belastbaren Beobachtung einzelner Handlungssituationen. Das Learning Management System wird dadurch auch als Evaluationsträger und didaktisches Analysewerkzeug wirksam und trägt den besonderen Anforderungen der Ausbildung in den Heilberufen Rechnung.

Der in Abschnitt~\hyperref[sec:Evaluation-Reflexion]{3.2.4} beschriebene TEI-Einsatz ist damit Teil der laufenden Qualitätssicherung und zugleich eine feldnahe Rückkopplungsspur. Er liefert pro Handlungssituation Rückmeldungen zu Designmerkmalen und wahrgenommenen Effekten und macht so die Ebene sichtbar, auf der didaktische Passungen, Irritationen und wahrgenommene Wirkungen zuerst erkennbar werden [@ritzmann_training_2014]. Die Simulation in Abschnitt~\hyperref[sec:Simulation-Kompetenzentwicklung]{4.4} greift diese lokale Ebene auf und übersetzt sie in eine zeitliche Verlaufsperspektive, in der modelliert wird, wie sich Koppelungen über mehrere Schritte hinweg stabilisieren oder entkoppeln können [@hanisch-johannsen_simulation_2025]. Beide Zugänge sind methodisch anschlussfähig. Das TEI beschreibt lokale Rückmeldungen im Feld; die Simulation prüft modellhaft, wie sich solche lokalen Rückmeldungen unter Zeitbedingungen zu unterschiedlichen Dynamiken der Kompetenzentwicklung verdichten könnten [@ritzmann_training_2014; @hanisch-johannsen_simulation_2025].

Perspektivisch ist diese Verschränkung als iterativer Kreislauf gedacht. Pro Handlungssituation werden Eingangsparameterstände (Design-/Kontextmerkmale) explizit geführt, TEI‑Rückmeldungen und ergänzende LMS‑Analytiken liefern heuristische Ableitungen zu Bruchstellen, Passungen und Verlaufstypiken, und die Simulation wird dadurch schrittweise dateninformiert ergänzt und in Folge‑Läufen gezielt variiert.

## 3.3 Technische Architektur {#sec:TechnischeArchitektur}

Der folgende Abschnitt beschreibt die technische Architektur des Learning-Management-Systems als infrastrukturelle Bedingung des untersuchten Wirkgefüges. Technik trägt dabei Verfügbarkeit, Sichtbarkeit, Rollenlogik, Rückkopplung und Integration. Technische Entscheidungen sind deshalb für den Forschungsgegenstand relevant, weil didaktische und organisationale Funktionen nur dann stabil wirksam werden können, wenn sie auch betrieblich getragen sind. Die Architektur hat sich im Verlauf des Systems mehrfach verändert. Diese Veränderungen folgten den wachsenden Anforderungen aus Ausbildung, institutioneller Einbettung und alltäglicher Nutzung.

### 3.3.1 Einordnung: Technik als infrastrukturelle Bedingung des Wirkgefüges {#sec:TechnischeArchitektur-Einordnung}

Die technische Architektur des hier untersuchten Learning-Management-Systems ist als infrastrukturelle Grundlage zu verstehen, die didaktische Konzepte und organisationale Anforderungen überhaupt erst dauerhaft betreibbar macht. Sie trägt die im vorherigen Abschnitt beschriebene didaktische Struktur mit, ohne selbst schon mit Didaktik gleichgesetzt zu werden. Sichtbarkeit von Lernspuren, stabile Erreichbarkeit, Rollensteuerung, Freischaltungen, Rückmeldungen und die Kopplung weiterer Systeme bilden daher Voraussetzungen dafür, dass der digitale Bildungsraum im Ausbildungsalltag verlässlich funktioniert.

Mit @dyrna_methoden_2021 lässt sich das Setup begrifflich in Infrastruktur und Bildungswerkzeuge unterscheiden. Zur Infrastruktur gehören hier Serverbetrieb, Speicher, Netzwerk und Übertragung. Das Learning-Management-System fungiert als zentraler Lernraum, der Cloudspeicher als kollaborativer Arbeits- und Dateiraum, das E‑Portfolio als Raum für Dokumentation, Reflexion und Artefaktorganisation. Diese Unterscheidung ist für die vorliegende Darstellung wichtig, weil Infrastrukturentscheidungen nicht mit didaktischen Methoden verwechselt werden sollen. Die technische Architektur bildet die Betriebsgrundlage, die Bildungswerkzeuge konkretisieren darauf die pädagogischen Funktionen.

Hosting- und Betriebsanforderungen sind in diesem Zusammenhang Voraussetzungen dafür, dass das LMS als verlässlicher Bildungsraum überhaupt tragfähig wird. Ein System, das curriculare Steuerung, Rückmeldeschleifen, Lernpfade, Ergebnissicherung und Kommunikationsprozesse dauerhaft tragen soll, ist auf kontinuierliche Verfügbarkeit, belastbare Erreichbarkeit und einen stabilen Betriebsmodus angewiesen. Dazu gehören laufendes Monitoring, eine nachvollziehbare Update- und Bugfix-Logik sowie Backup- und Wiederherstellungsverfahren, die Ausfälle technisch begrenzen und den Verlust didaktisch relevanter Lernspuren verhindern. Ebenso gehört dazu eine Infrastruktur, die Lastspitzen, wachsende Nutzerzahlen und unterschiedliche Zugriffssituationen auffangen kann, ohne dass Navigation, Rückmeldung oder Bearbeitung instabil werden. In der Literatur zu datenbezogenen Bildungsumgebungen wird entsprechend betont, dass solche Systeme effizient, verantwortungsvoll und qualitätsgesichert betrieben werden sollten [@tzimas_literature_2023].

Hinzu treten Anforderungen an Datenschutz, Sicherheit und Integrationsfähigkeit. Für das hier untersuchte System ist entscheidend, dass Serverbetrieb, Zertifikate, Datenspeicherung und Zugriffsschutz so organisiert sind, dass ein datenschutzgerechter und institutionell anschlussfähiger Betrieb möglich bleibt. Das betrifft die sichere Verarbeitung personenbezogener Daten ebenso wie die Frage, ob Kursverwaltung, Rollenlogiken, Freischaltungen, Feedbackprozesse und Schnittstellen zu weiteren Systemen dauerhaft mitgeführt werden können. Gerade für datenbezogene Bildungsumgebungen verweisen neuere Arbeiten darauf, dass Transparenz, Kontrolle über Daten, sichere Speicherung und nachvollziehbare Nutzungslogiken zentrale Bedingungen für Vertrauen und Akzeptanz darstellen [@karimov_ethical_2024; @yan_evidencebased_2024]. Auch responsive Nutzung gehört in diesem Zusammenhang zur Benutzerfreundlichkeit und zur Betriebsfähigkeit des Lernraums, weil Lernhandlungen im Feld auf unterschiedliche Geräte, Orte und Zeitfenster verteilt sind. Hosting erscheint damit als dienende Infrastruktur. Zugleich trägt es die Reichweite und Stabilität der didaktischen Architektur mit, weil deren Kopplungslogik nur dann wirksam werden kann, wenn die technischen Voraussetzungen für Sichtbarkeit, Rückmeldung, Integration und verlässlichen Zugriff dauerhaft gesichert sind.

### 3.3.2 Epoche I: Eigenbetrieb im Heimnetzwerk (NAS-basierte Infrastruktur) {#sec:TechnischeArchitektur-Epoche-I}

Die erste technische Architektur wurde 2016 im Eigenbetrieb als NAS-basierte Heimnetzwerk-Lösung aufgebaut. Für die frühe Entwicklungsphase war das funktional, weil sich damit Kursverwaltung, Materialbereitstellung und digitale Kommunikation mit begrenzten Mitteln überhaupt erst realisieren ließen. Die Stärke dieser Phase lag vor allem in der Möglichkeit, die didaktische Grundidee unter realen Bedingungen zu erproben und schrittweise auszubauen.

Gleichzeitig markierte diese Architektur die Grenzen eines frühen Prototyps. Mit steigenden Nutzerzahlen, wachsender Datenmenge und komplexeren Anforderungen an Verfügbarkeit und Sicherheit wurde sichtbar, dass die Infrastruktur für einen dauerhaft tragfähigen Ausbildungsbetrieb zu schmal ausgelegt war. Gerade daran zeigt sich die Funktion dieser ersten Epoche. Sie machte die digitale Lernumgebung praktisch möglich und legte zugleich offen, welche infrastrukturellen Bedingungen für institutionelle Verstetigung später nachgezogen werden mussten.

### 3.3.3 Epoche II: Professionalisierung durch externe Hosting- und Servicepartner {#sec:TechnischeArchitektur-Epoche-II}

Mit der Pandemie und der damit verbundenen Ausweitung digitaler Lehre veränderten sich die infrastrukturellen Anforderungen grundlegend. Die zuvor tragfähige Eigenlösung genügte den Ansprüchen an Skalierbarkeit, Verfügbarkeit und Sicherheit nicht mehr. Im Jahr 2020 wurde das System daher in eine professionell gehostete Betriebsform überführt. Dieser Schritt ist für den Forschungsgegenstand deshalb bedeutsam, weil sich hier zeigt, dass didaktische Kontinuität im Ausbildungsalltag auf belastbare Betriebsbedingungen angewiesen ist. Verfügbarkeit, stabile Erreichbarkeit und ein verlässlicher Sicherheitsrahmen wurden nun selbst zu Voraussetzungen der Lernorganisation.

Parallel dazu wurde die Systemlandschaft funktional ausdifferenziert. Das Kursverwaltungsprogramm übernahm Verwaltungs- und Organisationsaufgaben, das Learning-Management-System trug die Lernplattformlogik, der Cloudspeicher die Datei- und Arbeitsorganisation. Damit entstand eine gekoppelte Infrastruktur, in der verschiedene Systeme jeweils eigene Aufgaben übernehmen und zugleich aufeinander bezogen bleiben.

Die Systeme Kursverwaltungsprogramm, Learning-Management-System, Cloudspeicher und E‑Portfolio sind über Schnittstellen und getrennte Betriebsumgebungen gekoppelt. Das erhöht den Koordinationsaufwand und erlaubt zugleich eine funktionale Trennung von Kursverwaltung, Lernraum, Datei- und Artefaktorganisation. Für das hier untersuchte LMS ist diese Verteilung ein prägendes Architekturmerkmal. Sie bestimmt mit, wie Rollen, Zugriffe, Freischaltungen und Datenflüsse organisiert werden können. Die Programm- und Aufgabenarchitektur ist in \hyperref[fig:fg-organisationsarchitektur-lms]{Abbildung~\ref{fig:fg-organisationsarchitektur-lms}} schematisch dargestellt.

\input{08 Metaquellen/08-01 Abbildungen/prozesse/lms-organisationsarchitektur.tex}

In dieser Professionalisierungsphase verdichtet sich zugleich eine zentrale Einsicht des Untersuchungsfalls. Technische Architektur muss hier drei Logiken gleichzeitig tragen. Sie muss Compliance und Datenschutz absichern, organisatorische Steuerung ermöglichen und didaktische Funktionen wie Lernpfade, Rückmeldungen oder Freischaltungen stabil betreiben. Gerade diese Mehrfachbindung macht verständlich, weshalb Infrastrukturentscheidungen im vorliegenden System nicht isoliert betrachtet werden können. Sie sind an Funktions- und Qualitätsansprüche rückgebunden, die aus Ausbildungsvollzug, institutioneller Verantwortung und didaktischer Gestaltung zugleich hervorgehen.

Technisch wird das Learning-Management-System in dieser Phase als webbasierte Applikation in einer LAMP-Umgebung betrieben. Für die vorliegende Arbeit ist diese Standardkonfiguration relevant, weil sie eine stabile Vermittlung zwischen Benutzeranfragen, Anwendungslogik und Datenbank ermöglicht. Genau diese Vermittlung ist für den Bildungsraum bedeutsam, weil darüber Zugriffe, Bearbeitungen, Freischaltungen und Rückmeldungen verlässlich verarbeitet werden. Die Interaktion zwischen Benutzenden, Webserver und Datenbank ist in \hyperref[fig:fg-user-server-interaktion]{Abbildung~\ref{fig:fg-user-server-interaktion}} skizziert.

Hinzu kommt eine rechtlich und organisatorisch relevante Ebene der Nachvollziehbarkeit. Log-Protokolle machen Systemzugriffe und Bearbeitungsvorgänge dokumentierbar. Im Ausbildungskontext ist das ein Administrationsaspekt und kann Teil einer Nachweislogik werden, die bei Rückfragen, Konflikten oder prüfungsbezogenen Klärungen bedeutsam ist.

\input{08 Metaquellen/08-01 Abbildungen/prozesse/lms-user-server-interaktion.tex}

Im September 2021 waren im digitalen Bildungsraum mehrere hundert Teilnehmende eingetragen, ohne dass diese gleichzeitig auf alle Systeme zugreifen. Die folgenden Kennzahlen zeigen deshalb, mit welcher infrastrukturellen Reserve der Betrieb zu diesem Zeitpunkt getragen wurde.

Die zusammengefassten Werte sind in \hyperref[tab:technische-kennzahlen-platon]{Tabelle~\ref{tab:technische-kennzahlen-platon}} dokumentiert.

Table: Technische Kennzahlen der gekoppelten Systemumgebung \label{tab:technische-kennzahlen-platon}

|                  | Learning-Management-System  | Cloudspeicher | E-Portfolio  |
|------------------|----------|------------|----------|
| Anzahl CPU-Kerne | 4 Stück  | 8 Stück    | 4 Stück  |
| Arbeitsspeicher  | 8 GB RAM | 32 GB RAM  | 8 GB RAM |
| Datenspeicher    | 500 GB   | 1 TB       | 512 GB   |
| Taktung          | 2,7 GHz  | 4,2 GHz    | —        |

\tabsubcaption{Gegenüberstellung der technischen Kennzahlen (CPU-Kerne, Arbeitsspeicher, Datenspeicher, Taktung) der eingesetzten Systemkomponenten Learning-Management-System, Cloudspeicher und E-Portfolio in der gekoppelten Betriebsumgebung.}

Die Tabelle ist vor diesem Hintergrund vor allem als Relation von Last, Verfügbarkeit und Nutzbarkeit zu lesen. Maßgeblich ist die Frage, ob die Systemauslegung stabile Zugriffszeiten, verlässliche Bearbeitbarkeit und kontinuierliche Rückkopplung auch unter erhöhter Last sichern kann. Wo diese Bedingungen nicht gegeben sind, entstehen technische Störungen mit didaktischen Folgen. In der Folge entstehen Unterbrechungen von Lernhandlungen, Verzögerungen in Rückmeldeschleifen und Unsicherheiten in organisatorischen Abläufen. Die technischen Rahmenbedingungen sind damit auch deshalb relevant, weil sie die didaktische Tragfähigkeit des Systems unmittelbar mitbestimmen.

### 3.3.4 Epoche III: Stabilisierungs- und Verstetigungsphase {#sec:TechnischeArchitektur-Epoche-III}

Die dritte Entwicklungsphase ist durch Stabilisierung, Verstetigung und institutionelle Einpassung geprägt. Nachdem in der Professionalisierungsphase vor allem die akute Sicherung von Verfügbarkeit, Sicherheit und Betriebsfähigkeit im Vordergrund stand, verschiebt sich der Schwerpunkt nun auf konsistenten Regelbetrieb. Für den Forschungsgegenstand ist diese Phase deshalb bedeutsam, weil technische Infrastruktur hier als dauerhaft mitlaufende Voraussetzung eines etablierten Bildungsraums erscheint.

Mit dieser Verstetigung verändern sich auch die Anforderungen an die technische Architektur. Entscheidend ist nun, dass das System erreichbar bleibt und dass Rollenlogiken, Freischaltungen, Rückmeldestrukturen, Kurskopien, Prüfungsorganisation und Schnittstellen im Alltag verlässlich funktionieren. Stabilität zeigt sich damit an Serverlaufzeiten, Reaktionsgeschwindigkeit und an der Frage, ob didaktische und organisationale Routinen ohne ständige technische Sonderlösungen getragen werden können. Gerade in dieser Phase wird sichtbar, dass Infrastruktur dann tragfähig ist, wenn sie im Hintergrund bleibt und gleichwohl die Sichtbarkeit, Nachvollziehbarkeit und Koordination des Ausbildungsvollzugs dauerhaft sichert.

Die Bezeichnung dieser Phase als Verstetigungsphase verweist zudem auf eine veränderte Systemrolle. Das LMS wird Teil des regulären Ausbildungsbetriebs. Die technische Architektur muss deshalb Anschlussfähigkeit in mehrere Richtungen sichern, nämlich zur Kursverwaltung, zu kooperativen Arbeitsräumen, zur Dokumentation individueller Lernspuren und zu den organisatorischen Vollzügen von Praxisbegleitung und Prüfung. Unter diesen Bedingungen gewinnt die Frage nach verantwortlichem Betrieb, datenschutzgerechter Verarbeitung, Updatefähigkeit und institutioneller Zuständigkeit weiter an Gewicht, wie dies auch für datenbezogene Bildungsumgebungen und qualitätsgesicherte eLearning-Strukturen beschrieben wird [@tzimas_literature_2023; @karimov_ethical_2024; @peters_referenzhandbuch_2016].

### 3.3.5 Vergleichende Einordnung der Entwicklungsphasen {#sec:VergleichendeEntwicklungsphasen}

Die drei Entwicklungsphasen markieren unterschiedliche Modi, in denen das System auf wachsende didaktische und institutionelle Anforderungen antwortet. Die erste Phase des Eigenbetriebs steht für Ermöglichung unter knappen Bedingungen. Sie schafft den Raum, in dem die digitale Grundidee praktisch erprobt werden kann, und bleibt in Verfügbarkeit, Sicherheit und Skalierbarkeit begrenzt. Die zweite Phase reagiert auf diese Grenzen mit Professionalisierung. Infrastruktur wird nun so ausgebaut, dass steigende Nutzerzahlen, stärkere organisatorische Kopplungen und eine komplexere Systemlandschaft getragen werden können. Die dritte Phase verschiebt den Fokus schließlich auf Stabilisierung und Verstetigung. Technik muss nun leistungsfähig sowie im Regelbetrieb verlässlich, anschlussfähig und institutionell eingebettet sein.

Vergleichbar werden die Phasen vor allem über ihre jeweilige Funktion für das Wirkgefüge. In Phase I dominiert die Ermöglichungsfunktion. In Phase II tritt die Absicherungs- und Integrationsfunktion hinzu. In Phase III rückt die Verstetigungsfunktion in den Vordergrund. Mit jeder Phase wächst damit der Grad, in dem technische Architektur digitale Lehre unterstützt und curriculare Steuerung, Rollenlogik, Prüfungsorganisation, Dokumentation und Rückkopplung als zusammenhängende Struktur mitträgt.

Für den Forschungsgegenstand ist dieser Vergleich deshalb relevant, weil sich daran die Eigenlogik des Systems ablesen lässt. Das LMS entwickelt sich entlang der Frage, welche Infrastruktur jeweils nötig ist, um einen digitalen Bildungsraum im Ausbildungsalltag tragfähig zu machen. Die technische Architektur folgt damit keiner autonomen Techniklogik. Sie verdichtet vielmehr jene Anforderungen, die aus didaktischer Gestaltung, normativer Rahmung und institutioneller Verantwortung an den Betrieb des Systems herangetragen werden. In diesem Sinn bilden die drei Phasen zusammen die infrastrukturelle Vorgeschichte der in Abschnitt~\hyperref[sec:DidaktischeArchitektur]{3.4} beschriebenen didaktischen Architektur.

## 3.4 Didaktische Architektur als Lernumgebung {#sec:DidaktischeArchitektur}

Aufbauend auf dem in Abschnitt~\hyperref[sec:Kontext-FG]{3.1} beschriebenen Entstehungskontext sowie den in Abschnitt~\hyperref[sec:Entwicklung-Einbettung]{3.2} weitergeführten Entwicklungsschritten wird im Folgenden die didaktische Architektur des Learning-Management-Systems vorgestellt. Diese Konzeption zielte auf eine digitale Struktur, die rechtliche Anforderungen der Ausbildung ebenso aufnimmt wie die didaktischen Prinzipien systemisch fundierter Kompetenzentwicklung. In dieser Phase entstand auch die in \hyperref[fig:fg-didaktische-systemstruktur]{Abbildung~\ref{fig:fg-didaktische-systemstruktur}} gezeigte Skizze zur didaktischen Systemstruktur. Sie hält einen frühen Stand der Überlegungen fest, aus denen später eine funktionsfähige und kohärente Lernumgebung hervorging.

An dieser Stelle wechselt die Darstellung von der Entstehung des Systems zu seiner inneren Lernlogik. Der Blick richtet sich darauf, wie die Ausbildung im System geordnet wird und wie aus rechtlichen Vorgaben, Lernfeldern, Aufgaben, Rückmeldungen und Ergebnisspuren ein wiedererkennbarer Bildungsraum entsteht.
	 
Die Skizze dient im Folgenden als Referenzstruktur. Sie macht sichtbar, welche Architekturannahmen (Lernorte, Kurslogik, Aufgabenstruktur, Rückkopplung) den späteren Ausführungen zugrunde liegen, ohne bereits Details der späteren Umsetzung vorwegzunehmen.

![Frühe Konstruktionsskizze der didaktischen Systemstruktur.](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/lms-konstruktionsskizze.png>){#fig:fg-didaktische-systemstruktur}

\figsubcaption{Eingescanntes Original einer frühen handschriftlichen Konzeptskizze aus der frühen Entwurfsphase des LMS. Sie zeigt erste Überlegungen zu Lernorten, Kurslogik, Aufgabenstruktur und Rückkopplung, die im weiteren Kapitel zur didaktischen Lernumgebung ausgearbeitet werden.}

Die Skizze hält den konzeptionellen Ausgangspunkt des hier beschriebenen Learning Management Systems fest. Sie zeigt erste Überlegungen zur Verschränkung von Lernorten, Selbststeuerung und Aufgabenstruktur als Grundlage einer systemisch-konstruktivistisch orientierten Ausbildungsarchitektur.

Die Skizze bildete das konzeptionelle Fundament der ersten Entwicklungsphase und visualisiert die Idee, innerhalb eines digitalen Bildungsraums Handlungssituationen, Lernorte und Kursorganisation so miteinander zu verbinden, dass eine strukturierte und individuelle Kompetenzentwicklung möglich wird. Besonders herauszustellen ist dabei die Trennung zwischen inhaltlicher Struktur und organisatorischer Kurslogik, wodurch eine hohe Flexibilität bei gleichzeitiger Kohärenz erreicht werden sollte. Die frühe Berücksichtigung aller drei Lernorte sowie die intendierte Rückführung kursinterner Erkenntnisse in die übergeordneten Lerneinheiten legen den systemischen Anspruch dieser Struktur offen [@hanisch_wirkgefuge_2022, Abschnitt 2.3].

### 3.4.1 Konzeptionelle Grundkonstruktion {#sec:Grundkonstruktion}

Am Anfang stand die Idee eines Ausbildungswegs, der fachliche Entwicklung, Haltung und berufliche Identitätsbildung in einer strukturierten Abfolge zusammenführt. Als philosophische Leitfigur dieser Weglogik diente dabei die Vorstellung des Weges als bewusst zu gestaltender Entwicklungs- und Handlungsform (i.A.a. [@miyamoto_buch_2005, Seite 64–69]). Die bildungswissenschaftliche und curriculare Ausarbeitung dieser Leitfigur erfolgte anschließend im Rückgriff auf den Rahmenlehrplan NRW\label{term:rahmenlehrplan-nrw} zur Ausbildung von Notfallsanitäter\*innen, insbesondere auf dessen Gliederung in zehn Lernfelder [@mgpa_nrw_rahmenlehrplan_2016, Seite 3]. Aus dieser Verbindung von philosophischer Leitidee und curricularer Struktur entstand die didaktische Grundkonstruktion des Learning Management Systems. Der Lernprozess wird damit als sequenziell angelegte, zugleich durchlässige Trajektorie organisiert, die curricular vorgegeben ist und im System adaptiv geführt werden kann. Diese Pfadidee wird modellbasiert als Trajektorie visualisiert (\hyperref[fig:fg-trajektorie]{Abbildung~\ref{fig:fg-trajektorie}}; zur theoretischen Rahmung Abschnitt~\hyperref[sec:Systemisch-konstruktivistische-Theorie]{2.2.3}).

![Trajektorie der Handlungssituationen im LMS.](<08 Metaquellen/08-01 Abbildungen/didaktik/ontologisch-systemische-trajektorie_konstruktivistisch-standardlernender.png>){#fig:fg-trajektorie}

\figsubcaption{Beispielprofil. Die Abbildung visualisiert das LMS als Pfad durch Handlungssituationen: Lernen wird als sequenzielle, rückkopplungsfähige Prozessarchitektur modelliert.}

Das Learning Management System übersetzt diese Grundidee in eine digitale Architektur, in der curriculare Kompetenzziele, handlungsleitende Aufgaben und Lernortbezüge systematisch aufeinander bezogen werden. Die im Lehrplan als „erwünschte Wirkung“ beschriebenen Kompetenzziele wurden dafür in ein eigenes Kompetenzraster überführt und mit den in Abschnitt~\hyperref[sec:Implementierung-Schule]{3.2.2} beschriebenen Aufgabenformaten verknüpft. So entstand eine Struktur, in der Lernhandlungen, Sichtbarkeit von Ergebnissen und Rückkopplung innerhalb eines durchgängigen pädagogischen Pfads organisiert werden.

Das didaktisch-digitale Fundament bilden 32 curricular-inhaltliche Kurse, die als Handlungssituationen die Lernfelder des Rahmenlehrplans abbilden, sowie kohortenspezifische Ausbildungskurse, in denen organisatorische Informationen, kursinterne Arbeitsergebnisse und Prüfungsbezüge gebündelt werden. Ergänzend besteht eine Vorlagenlogik, über die Handlungssituationen reproduzierbar angelegt und in neue Kursstände überführt werden können. Diese Trennung hält die inhaltliche Struktur stabil und erlaubt zugleich, Lernende bei unterschiedlichen Verläufen, Wiederholungen oder Unterbrechungen an ihren fachlichen Stand anzuschließen, ohne die Kohärenz des Gesamtsystems aufzugeben.

Die konzeptionelle Grundstruktur des LMS wird in \hyperref[fig:modell_LMS]{Abbildung~\ref{fig:modell_LMS}} als Schema visualisiert.

\input{08 Metaquellen/08-01 Abbildungen/prozesse/lms-modell.tex}

Die Struktur trennt curricular-inhaltliche Handlungssituationen ($n = 32$) von kohortenspezifischen Ausbildungskursen und Vorlagenkursen. Daraus ergibt sich eine flexible, zugleich kohärente Lernumgebung, in der Erfahrungen, Arbeitsergebnisse und organisatorische Prozesse in die übergeordnete Handlungsebene rückgebunden werden können. Zugleich bezieht die Architektur alle drei Lernorte der Ausbildung ein, also Lehrrettungswache, Notfallsanitäterschule und Krankenhaus (§ 3 i.V.m. Anlage 1-3 NotSan-APrV\label{term:notsan-aprv}, 2023). Die beteiligten Akteur\*innen\label{term:akteure} werden damit in eine gemeinsame Kursstruktur eingebunden, in der fachliche Begleitung, organisatorische Steuerung und Rückmeldung zusammengeführt werden.

\hyperref[fig:modell_LMS]{Abbildung~\ref{fig:modell_LMS}} macht diese integrative Grundstruktur anschaulich. Im Zentrum steht die wechselseitige Beziehung von Handlungssituationen als curricular-didaktischen Strukturelementen und Ausbildungskursen als organisatorischen Einheiten. Die inneren Bereiche Result, Communication und Organization markieren die operative Ebene des Systems. Hier werden Arbeitsergebnisse gesichert, Rückmeldungen geführt, Zuständigkeiten sichtbar gemacht und Abläufe strukturiert. Die äußeren Bereiche Content und Lernorte bezeichnen die beiden Bezugsrahmen, aus denen die Handlungssituationen gespeist werden und an die sie Ergebnisse zurückgeben. Sichtbar wird damit eine Architektur, in der Stabilität, Adaptivität und Lernort-Transfer zugleich organisiert sind.

Die Überführung dieser Überlegungen in die Kursansicht zeigt \hyperref[fig:fg-kursansicht]{Abbildung~\ref{fig:fg-kursansicht}}. Dort wird sichtbar, welche standardisierte Kursstruktur Lernhandlungen, Navigation und Rückkopplung im System technisch stützt. Die Darstellung stammt aus der eigenen LMS-Instanz, die als technisches Fundament des hier beschriebenen Learning Management Systems dient.

![Exemplarische Kursansicht im Learning Management System.](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/lms-kursansicht-1.png>){#fig:fg-kursansicht}

\figsubcaption{Die Abbildung zeigt die standardisierte Container-Navigation (links) sowie den inhaltsseitigen Aufbau (Kursdetails, Ressourcen etc.) als operatives Abbild der beschriebenen didaktischen Architektur.}

Die Darstellung zeigt die standardisierte Containerstruktur mit den Bereichen Einführung, Ressourcen, Aufgaben, weiterführende Quellen, Lounge, Feedback und Kursorganisation sowie den jeweils zugeordneten Aktivitäten und Materialien. Die ältere Entwicklungsstufe enthielt zusätzlich einen eigenen Bereich Ergebnissicherung, der in der aktuellen Struktur der Handlungssituationen vor allem funktional in Aufgaben, Foren, Datenbanken und Feedback weitergeführt wird. Wiki und Glossar bleiben ergänzend in kohortenspezifischen Kursen als Räume für Ergebnissynthese und Begriffsarbeit erhalten. Das E-Portfolio schließt eher individuell beziehungsweise kohortenspezifisch an diese Spuren an. Diese Struktur stellt sicher, dass alle Handlungssituationen in derselben Logik gebaut sind. Dadurch werden Navigation, Dokumentation und Kommunikation für Lernende und Lehrende zuverlässig wiedererkennbar.

### 3.4.2 Didaktisch-architektonische Umsetzung {#sec:DidaktischeUmsetzung}

Die didaktisch-architektonische Umsetzung folgt einer standardisierten Containerstruktur, die alle Handlungssituationen in derselben Grundform gliedert und dennoch Anpassungen im konkreten Kursverlauf zulässt. In der aktuellen Moodle-Instanz bilden Einführung, Ressourcen, Aufgaben, weiterführende Quellen, Lounge, Feedback und Kursorganisation die wiederkehrende Abschnittslogik. Die ältere Moodle-Instanz zeigt daran anschließend, wie Ergebnissicherung zunächst als eigener Bereich sichtbar geführt wurde. In den aktuellen Handlungssituationen wird sie stärker als Querschnittsfunktion realisiert; in kohortenspezifischen Kursen bleiben Wiki und Glossar zusätzlich als Orte der Ergebnissynthese und Begriffsarbeit erhalten. Breiter dargestellt werden deshalb jene Bereiche, in denen sich die Kopplung von Aufgabenlogik, Ergebnissicherung, Rückmeldung und organisatorischer Steuerung besonders deutlich zeigt.

**Integrative Wirkung der Containerstruktur**

Die Container sind mehr als eine Menüstruktur. In der Nutzung ordnen sie Lernhandlungen, weil sie Orientierung, Wissensaneignung, Aufgabenbearbeitung, Ergebnissicherung, Reflexion, soziale Einbindung, Feedback und Organisation in eine wiederkehrende Abfolge bringen. Gerade diese Wiederholung reduziert Suchaufwand und stabilisiert Erwartungshorizonte. Lernende können sich dadurch im Kurs sicher bewegen, Schwerpunkte setzen und individuelle wie kollektive Lernpfade ausbilden (im Abschnitt \hyperref[sec:Gefuegeperspektive-FG]{Begriffsrahmung: Gefügeperspektive auf die LMS-Architektur}).

Die Verknüpfung der Container mit der in \hyperref[sec:Begriffe-Wirkung-Gefuege]{Abschnitt~2.2.4} entwickelten Begriffsarchitektur macht die didaktische Architektur anschlussfähig an den Theorieteil. Lernprozesse werden hier als rekursive Kopplung von Orientierung, Aufgabenbearbeitung, Ergebnissicherung, Rückmeldung und Organisation verstanden. Ergebnisse aus einer Phase werden als Ressourcen für die nächste genutzt, Feedback wird als Systeminformation geführt, und Organisation sichert die Stabilität der Prozesse (Abschnitt~\hyperref[sec:Evaluation-Reflexion]{3.2.4}).

Diese Containerarchitektur ist als eigene Entwicklungsleistung zu verstehen. Sie ist aus der praktischen Implementierung (Abschnitt~\hyperref[sec:Implementierung-Schule]{3.2.2} bis \hyperref[sec:Weiterentwicklung-extern]{3.2.3}), aus begleitender Evaluation (Abschnitt~\hyperref[sec:Evaluation-Reflexion]{3.2.4}) und aus der theoretischen Rahmung (\hyperref[sec:Theorieteil]{Kapitel 2}) hervorgegangen. Entscheidend ist dabei die explizite Kopplung von didaktischer Steuerung, Dokumentation und Rückmeldung. Genau diese Kopplungslogik wird in \hyperref[sec:Diskussion-Interdependenz]{Kapitel 6.3.1} wieder aufgegriffen.

**Einführung**

Die Einführung rahmt jede Handlungssituation und bildet die Schwelle zwischen organisatorischer Orientierung und inhaltlicher Arbeit. Sie macht sichtbar, welche Inhalte die jeweilige Lerneinheit umfasst, wie sie in die Ausbildung eingeordnet ist und welche Erwartungen an Kommunikation, Mitarbeit und Ergebnissicherung geknüpft sind. Im Learning-Management-System wird diese Funktion vor allem über Textseiten und ein Ankündigungsforum umgesetzt, also über Formate, die Verbindlichkeit herstellen, ohne den Einstieg bereits mit Arbeitsaufträgen zu überladen. Für NFS‑H‑01 ist das besonders wichtig, weil die erste Woche zugleich in die Ausbildung, in den digitalen Lernraum und in die soziale Logik der Kohorte einführt. Genau hier zeigt sich auch die Grenze des Containers. Reine Orientierungstexte reichen nicht aus, wenn Wochenstruktur, Kommunikationswege und technische Grundhandlungen nicht früh mit eingeübt werden. Die Einführung ist daher die erste Setzung jener Kopplungsordnung, die den weiteren Kurs trägt (\hyperref[sec:Emotionen]{Abschnitt~2.1.2}; \hyperref[sec:SystemischeDynamik]{Abschnitt~2.5}; Abschnitt~\hyperref[sec:DidaktischeVerortung]{3.1.2}).

**Ressourcen**

Der Ressourcencontainer bündelt jene Materialien, die für Aufgabenbearbeitung, Praxisbezug und wiederkehrende Orientierung gebraucht werden. Er ist damit der Wissensraum, auf den die weiteren Lernhandlungen immer wieder zurückgreifen. Verzeichnisse, Dateilisten und Linksammlungen im Learning-Management-System eignen sich dafür, weil sie Bestände stabil halten und zugleich aktualisierbar machen. Für den Untersuchungsfall ist das wesentlich, weil Verfügbarkeit und Wiederauffindbarkeit von Materialien bereits in den Vorarbeiten als kritische Bedingung für nachhaltige Wissensprozesse sichtbar wurden (Abschnitt~\hyperref[sec:Entstehung-Konzept]{3.2.1}). In NFS‑H‑01 wird dieser Bereich deshalb als Grundlagenraum angelegt, der gemeinsame Bezugspunkte für den Ausbildungsstart schafft und den unterschiedlichen Vorwissensständen der Lernenden Rechnung trägt. Seine Stärke liegt in dieser Entlastungsfunktion. Seine Schwäche zeigt sich dort, wo Sammlung in bloße Ablage kippt. Didaktisch wirksam wird der Container erst dann, wenn Materialien auf Aufgaben, Ergebnissicherung und Prüfungsvorbereitung zurückbezogen bleiben und über ihre bloße Verfügbarkeit hinaus genutzt werden (\hyperref[sec:Bildungswiss-Verortung]{Abschnitt~2.2}; Abschnitt~\hyperref[sec:Pruefungsarchitektur]{3.4.3}).

Gerade hier zeigt sich die Bereitstellung zentraler Lernmaterialien in strukturierter Form. Die Materialien orientieren sich an curricularen Kompetenzanforderungen und bilden die inhaltliche Grundlage für die Bearbeitung der Aufgaben innerhalb der jeweiligen Handlungssituation.

**Aufgaben**

**Didaktische Funktion im Gesamtlernprozess**

Der Aufgabencontainer ist das Herzstück des kompetenzorientierten Lernprozesses. Er operationalisiert die curricularen Anforderungen in konkrete, handlungsorientierte Aufgabenstellungen, die sowohl individuelle als auch kollaborative Bearbeitung fördern. Durch die gezielte Verwendung von Operatoren und die Anbindung an reale Problemstellungen wird der Aufbau von Fach-, Handlungs- und Reflexionskompetenz unterstützt. Die Aufgaben dienen als "Lernmotor" und strukturieren die individuelle und gemeinsame Auseinandersetzung mit den Ausbildungsinhalten.

**Theoriekonzeptionelle Referenz**

Der Aufgabencontainer bildet die zentrale Kopplungsstelle zwischen curricularer Anforderung, subjektbezogener Verarbeitung und sichtbarer Bearbeitung. Hier werden Lernpfade, Aufgabenformate, Operatorik, Peer-Feedback und Ergebnissicherung aufeinander bezogen. Anschlussfähig wird der Container dadurch, dass Aufgaben Inhalte, Bearbeitung, Rückmeldung, Unsicherheit, Motivation und Kompetenzzuschreibung in einen gemeinsamen Verlauf bringen (\hyperref[sec:Emotionen]{Abschnitt~2.1.2}; \hyperref[sec:Bildung-Kompetenz]{Abschnitt~2.2.2}; \hyperref[sec:SystemischeDynamik]{Abschnitt~2.5}).

**Technische Umsetzung im Learning-Management-System**

Im Aufgabencontainer wird eine Kombination aus Aufgabenmodulen, Foren und Abstimmungen genutzt, weil damit Bearbeitung, Austausch und Selbstorganisation in einem sichtbaren Prozess zusammenlaufen. Aufgabenmodule sichern Abgabe, Fristen und Bewertung. Foren tragen Diskussion und Peer-Rückmeldung, Abstimmungen machen Arbeitsverteilung und Zuständigkeiten transparent. Diese technische Kopplung ist im Untersuchungsfall zentral, weil der Aufgabencontainer die Schnittstelle zwischen curricularer Vorgabe, kooperativer Bearbeitung und späterer Ergebnissicherung bildet (Abschnitt~\hyperref[sec:Grundkonstruktion]{3.4.1}).

**Limitationen und Weiterentwicklungspotenziale**

Risiken liegen in Überstrukturierung und Unschärfe. Zu viele oder zu komplexe Aufgaben können überfordern, unklare Operatorik erzeugt Unsicherheit und Passivität. Hinzu kommen technische Hürden, wenn mehrere Module gleichzeitig bedient werden müssen. Weiterentwicklung liegt deshalb in passgenauer Operatorlogik, tragfähigen Kriterien und in abgestuften Bearbeitungsformaten, die mit wachsender Kompetenz anspruchsvoller werden. Ergänzend können automatisierte Rückmeldungen oder Analytiken helfen, Überlastung früh zu erkennen und Unterstützung gezielt anzubieten (Abschnitt~\hyperref[sec:Evaluation-Reflexion]{3.2.4}).
Die Aufgabenstellungen werden durch didaktisch begründete Operatoren formuliert, die eine transparente und kompetenzorientierte Anforderungsstruktur gewährleisten und sich an der Kompetenzstufung orientieren. Im Beispielkurs wird erkennbar, wie die Aufgaben zugleich eigenständige Auseinandersetzung mit fachlichen Inhalten und kooperative Bearbeitungsformen ermöglichen. Ergänzt wird diese Struktur durch ein Bearbeitungsforum, das den Austausch von Ideen fördert und Reflexionsprozesse anregt.

**Umsetzung in NFS‑H‑01**

NFS‑H‑01 nutzt den Aufgabencontainer in besonderer Weise als „Einstiegsdidaktik“. Die erste Woche ist darauf ausgerichtet, die Lernenden in die Logik des Ausbildungsgangs und in die Logik des digitalen Lernraums einzuarbeiten. Dazu werden unterschiedliche Aufgabenformate bewusst kombiniert. Eine formale Abgabe (z. B. der „eLebenslauf“) trainiert den technischen und prozessualen Abgabeweg, ohne dass inhaltliche Komplexität den Prozess überlagert. Gleichzeitig werden thematische Aufgabenblöcke gesetzt, die den Blick auf das Ausbildungsziel (rechtliche und curriculare Verortung) und auf Grundlagen wissenschaftlichen Arbeitens (Quellenvalidität, argumentatives Begründen, Strukturieren) lenken. Dass diese Bereiche durch Abstimmungen („Aufgabenverteilung …“) und Diskussionsforen flankiert werden, ist didaktisch nicht zufällig. Die Abstimmungen stärken Selbstorganisation und Sichtbarkeit der Arbeitsverteilung, während die Foren die Erwartung früh stabilisieren, dass Lernen in diesem Setting als begründetes Austauschen, Mitargumentieren und gemeinsames Klären organisiert ist. Der Aufgabencontainer ist damit ein Inhaltscontainer. Er ist zugleich ein sozialer und prozessualer Trainingsraum, der die späteren Handlungssituationen vorbereitet.

**Didaktische Besonderheiten/Herausforderungen**

Im Aufgabencontainer entscheidet sich die Anschlussfähigkeit häufig an Transparenz. Verbindliche Abgabezeitpunkte, nachvollziehbare Kriterien (inkl. Operatorlogik) und Regeln für Peer‑Rückmeldung machen kooperative Arbeit weniger zufallsabhängig und sichern, dass Austausch fachlich begründet erfolgt.

**Funktion im Gesamtsystem**

Der Aufgabencontainer ist damit die zentrale Kopplungsstelle zwischen curricularer Vorgabe, lernprozessualer Bearbeitung und späterer Ergebnissicherung. Er organisiert die lernleitende Sequenz, erzeugt Anlässe für Austausch und legt die Grundlage dafür, dass Ergebnisse überhaupt dokumentierbar und rückkoppelbar werden.

Beispielhafte Aufgabenformate zur Bearbeitung beruflicher Handlungssituationen werden hier in ihrer Anlage erkennbar. Operatoren und strukturierte Aufgabenbereiche ermöglichen eine kompetenzorientierte Formulierung und eine praxisnahe Umsetzung curricularer Anforderungen.
Die lernleitenden Aufgaben sind inhaltlich eng mit den bereitgestellten Ressourcen verknüpft, was in der Regel durch die Quellenangaben bei der Aufgabendarlegung gewährleistet wird. Eine beispielhafte Aufgabenstellung findet sich in der beruflichen Handlungssituation 1 „Einführung in die Berufsausbildung Notfallsanitäter“ bei @hanisch-johannsen_nfs-h-01_2025.
„Beschreibe bitte die Maßnahmen, die du eigenverantwortlich als Notfallsanitäter:in durchführen musst, vor allem in Bezug auf die Anforderungen des Notfallsanitätergesetzes §4 und der Ausbildungs- und Prüfungsverordnung für Notfallsanitäter:innen (Anlage 1). Denke dabei an die Ausbildungsziele als Notfallsanitäter:in.
Bitte nenne die Quellen, die du zur Bearbeitung verwendet hast.“
Inhaltliche Ergebnisse und die dazugehörigen Erkenntnisse aus der Bearbeitung der Aufgaben werden in der Ergebnissicherung zusammengeführt und für alle weiteren Bearbeitungsschritte kuratiert.

**Ergebnissicherung**

**Didaktische Funktion im Gesamtlernprozess**

Die Ergebnissicherung ist der zentrale Reflexions- und Dokumentationsraum, in dem individuelle und kollaborative Lernergebnisse sichtbar und nachnutzbar gemacht werden. Sie ermöglicht die Reflexion von Lernfortschritten, die Konsolidierung von Wissen und die Vorbereitung von Transferleistungen. Durch die kontinuierliche Ergebnissicherung wird nachhaltiges Wissensmanagement gefördert und die Grundlage für formative Evaluation und rekursive Lernprozesse geschaffen.

**Theoriekonzeptionelle Referenz**

Theoriekonzeptionell ist die Ergebnissicherung der Ort, an dem Bearbeitungsspuren in anschlussfähige Lern- und Reflexionsartefakte überführt werden. Sie verbindet individuelle und kollaborative Lernwege, macht Zwischenergebnisse sichtbar und schafft Material für weitere Rückkopplung. In den Handlungssituationen operationalisieren vor allem Aufgaben, Foren, Datenbanken und Feedback diese Kopplungsordnung. In den kohortenspezifischen Kursen übernehmen Wiki und Glossar zusätzlich die Funktion, Ergebnisse kollaborativ zu verdichten und zentrale Begriffe gemeinsam zu sichern. Das E-Portfolio führt diese Spuren eher individuell beziehungsweise kohortenspezifisch weiter und macht längerfristige Entwicklungsverläufe dokumentierbar. Damit bleiben Ergebnisse für spätere Aufgaben, Feedback und Kompetenzzuschreibungen verfügbar (\hyperref[sec:Emotionen]{Abschnitt~2.1.2}; \hyperref[sec:Bildungswiss-Verortung]{Abschnitt~2.2}).

**Technische Umsetzung im Learning-Management-System**

Die Auswahl von Foren, Datenbanken, Wikis und Glossaren als Formate für die Ergebnissicherung ist didaktisch motiviert und auf unterschiedliche Kurslogiken verteilt. In den Handlungssituationen erlauben Foren die Präsentation und Diskussion von Ergebnissen; Datenbanken bieten strukturierte Ablagemöglichkeiten für Einsatzberichte, Fehlermeldungen, Anregungen und praktische Lernnachweise. In den kohortenspezifischen Kursen ermöglichen Wikis die kollaborative, versionierbare Dokumentation von Lernergebnissen, während Glossare Begriffsarbeit strukturieren und die Entwicklung einer gemeinsamen Fachsprache fördern. Im Vergleich zu Einzelabgaben oder statischen Textseiten fördern diese Formate die Sichtbarkeit, Nachvollziehbarkeit und Wiederverwendbarkeit von Ergebnissen.

**Limitationen und Weiterentwicklungspotenziale**

Risiken liegen vor allem in Fragmentierung. Wenn Ergebnisse in Abgaben, Forenthreads und persönlichen Notizen zerfallen, verlieren sie Anschlussfähigkeit für spätere Aufgaben, Prüfungsbezug und Transfer. Hinzu kommt eine Einstiegshürde, wenn kollaborative Tools ungeübt sind und die Ergebnissicherung als zusätzlicher Aufwand erlebt wird. Weiterentwicklung liegt deshalb in einer nachvollziehbaren Ergebnislogik, die feste Orte, einfache Routinen und sichtbare Rückkopplungen verbindet, etwa durch automatisierte Übernahmen aus Aufgabenmodulen, Feedback- und Bewertungsfunktionen oder übersichtliche Dashboards. Didaktisch wird Ergebnissicherung dann wirksam, wenn sie als Teil der Lernkette geführt wird, nicht als nachträgliche Ablage (Abschnitt~\hyperref[sec:Entstehung-Konzept]{3.2.1} sowie Abschnitt~\hyperref[sec:E-Portfolio]{3.6}).

**Umsetzung in NFS‑H‑01**

Im Kurs NFS‑H‑01 wird diese Logik bereits im Aufgabenbereich explizit angekündigt („Denkt daran, eure Ergebnisse … festzuhalten“) und damit als Erwartungshorizont gesetzt, auch wenn die Ergebnissicherungspraktiken in der Einführungswoche noch stärker einübend als ausdifferenziert angelegt sind. Dieser frühe Verweis ist didaktisch bedeutsam. Er verschiebt die Aufmerksamkeit von der Einzelleistung hin zu einer dokumentierten Ergebnislogik, die im Verlauf der Ausbildung zunehmend professionalisiert wird (Verdichtung, Nachvollziehbarkeit, Wiederauffindbarkeit, Wiederverwendbarkeit). Ergebnissicherung fungiert dabei zugleich als Brücke zwischen individueller Bearbeitung und kollektiver Lernorganisation. Sie macht sichtbar, was gelernt wurde, und sie schafft Anschlussstellen für spätere Rückfragen, Prüfungslogik und Transferdiskussionen.

**Didaktische Besonderheiten/Herausforderungen**

Ergebnissicherung bleibt nur dann mehr als ein Postulat, wenn sie in der Kursansicht als sichtbarer Arbeitsort geführt wird, etwa als Kursbuch, Wiki, Glossar, Präsentationsbereich, Datenbank oder E-Portfolio-Anschluss, und dadurch im Arbeitsprozess der Lernenden tatsächlich „mitläuft“. Ohne diese Sichtbarkeit drohen Ergebnisse in Aufgabenabgaben, Forenthreads oder persönlichen Notizen zu fragmentieren und verlieren ihre Anschlussfähigkeit.

**Technische Umsetzung**

Die Ergebnissicherung ist über standardisierte Elemente umgesetzt, die je nach Handlungssituation und kohortenspezifischem Kurs unterschiedlich verortet sind. Dazu zählen die folgenden Elemente.
Aus Datenschutzgründen werden konkrete Kurskennungen in den folgenden Beispielen als „Beispielkurs“ neutralisiert.

- **Kursbuch** (Forum) zur fortlaufenden, kursbezogenen Dokumentation und Reflexion.
- **Wiki** in kohortenspezifischen Kursen zur kollaborativen Ergebnissynthese und gemeinsamen Verdichtung von Lernergebnissen.
- **Glossar** in kohortenspezifischen Kursen zur strukturierten Begriffsarbeit und zur Konsolidierung zentraler Terminologie.
- **Präsentation** (Forum) zur Bereitstellung, Diskussion und Weiterentwicklung von Präsentationsergebnissen.
- **Einsatzberichte** (Datenbank) zur systematischen Sammlung, Auswertung und Rückbindung beruflicher Fallberichte.
- **Invasive Maßnahmen** (Datenbank) zur dokumentierten Sammlung und Vergleichbarkeit praktischer Maßnahmen und Lernnachweise.

Gerade die Datenbanken zu Einsatzberichten und invasiven Maßnahmen erweitern die Ergebnissicherung um eine Lernort-Transferfunktion. Reale Einsatzberichte können dort so dokumentiert werden, dass sie für spätere schulische Aktivitäten wiederaufgenommen und fachlich bearbeitet werden können. Praxisanleitende, Lernende und Lehrkräfte können die Einträge kommentieren. Dadurch entsteht eine gemeinsame Reflexionsspur, in der berufliche Erfahrung, praktische Anleitung und schulische Bearbeitung aufeinander bezogen bleiben. Der Lernorttransfer erhält damit eine dokumentierbare und kommentierbare Praxisfallspur in der Systemarchitektur. Für die spätere Bearbeitung der Handlungssituationen bedeutet das, dass reale Einsatzerfahrungen als konservierte Fälle in den digitalen Bildungsraum zurückgeführt und dort mit der schulischen Lernlogik verbunden werden können.

**Funktion im Gesamtsystem**

Die Ergebnissicherung ist damit Abschluss einer Handlungssituation und Teil eines zyklischen und systemisch eingebetteten Lernprozesses.

Exemplarisch treten hier zentrale Elemente der Ergebnissicherung in der Verbindung von Handlungssituationen und kohortenspezifischen Kursen hervor. Datenbanken, Foren und Feedback sichern handlungssituationsbezogene Spuren; Wiki und Glossar in den kohortenspezifischen Kursen dienen der kollaborativen Dokumentation und Strukturierung von Lernergebnissen. Diese Aktivitäten stehen gemeinsam für die systematische Umsetzung der in \hyperref[sec:Entwicklung-Einbettung]{Abschnitt 3.2} empirisch begründeten Forderung nach zeitnaher, zugänglicher und formativ nutzbarer Ergebnissicherung im digitalen Bildungsraum.

Die Ergebnissicherung stellt damit die didaktische Umsetzung der aus vorherigen Untersuchungen hervorgegangenen Forderung dar, Evaluationsergebnisse umzusetzen und einzubetten. Sie implementiert ein standardisiertes Vorgehen, das die Erkenntnisse von @hanisch_nachhaltiges_2017 auf Seite 19–20 berücksichtigt.

**Weiterführende Quellen**

Der Container „Weiterführende Quellen“ erweitert den curricularen Kern um einen Raum für Vertiefung, Transfer und wissenschaftsorientiertes Arbeiten. Seine Funktion geht über zusätzliche Literaturhinweise hinaus. Er trägt im System die Anforderung mit, Lerninhalte und berufliches Handeln an den aktuellen Stand von Wissenschaft und Technik rückzubinden. Gerade im gesundheitsberuflichen Feld gehört diese Rückbindung zur fachlichen und professionellen Plausibilität des Curriculums.

In NFS‑H‑01 ist dieser Bereich als kuratierte Startstruktur mit Leitlinienverzeichnissen, Fachgesellschaften, Datenbanken und ausgewählten Onlineportalen angelegt. Hinzu kommt das Forum „Aktuelle Literatur“, in dem analysierte neue Quellen eingestellt und für die weitere Bearbeitung verfügbar gemacht werden. Der Container bildet damit eine Brücke zwischen den im Kurs bereitgestellten Grundlagen und jener fortlaufenden Aktualisierung, die für evidenzorientiertes Arbeiten notwendig ist. Lernende sollen hier Quellen finden und zugleich sehen, wie Aktualisierung, Einordnung und Begründung im digitalen Bildungsraum praktisch organisiert werden.

Ein möglicher Einwand gegenüber wiederverwendbaren Aufgaben betrifft die Gefahr fachlicher Veraltung. Im untersuchten System wird diese Gefahr über eine zweite Aktualisierungsschicht bearbeitet. Die Aufgaben stabilisieren den didaktischen Ausgangspunkt der Handlungssituationen. Der Abschnitt „Weiterführende Quellen“ hält die fachliche, rechtliche und curriculare Rückbindung beweglich. Der Moodle-Abgleich zeigt dafür in allen 32 Handlungssituationen ein Forum mit der Bezeichnung „Aktuelle Literatur“. Dort werden wissenschaftliche Beiträge, Leitlinien und Studienberichte nach Kernthemen, rettungsdienstlicher Relevanz, Ausbildungsimplikationen und Zuordnung zur jeweiligen Handlungssituation erschlossen. Die zugrunde liegende Auswertungslogik bindet diese Beiträge an NotSanG, NotSan-APrV, Rahmenlehrplan, NRW-Ausführungsbestimmungen und lokale Kompetenzbezüge zurück. Damit bleibt der Startpunkt der Lernhandlung wiedererkennbar, während fachliche Aktualisierung über Quellenarbeit, Kommentierung und curriculare Einordnung in die Bearbeitung einwandert.

Seine Stärke liegt damit in der Anschlussfähigkeit an Aufgaben, Begründungen und Transferleistungen. Seine Grenze zeigt sich dort, wo Aufnahme, Kommentierung und Validierung von Quellen unklar bleiben. Ohne erkennbare Kriterien droht der Bereich unübersichtlich zu werden oder Aktualität mit fachlicher Belastbarkeit zu verwechseln. Didaktisch tragfähig wird der Container deshalb erst dann, wenn die Quellenarbeit ausdrücklich an die Aufgabenlogik und an die rechtlich-funktionale Rahmung des Ausbildungsgangs rückgebunden bleibt (\hyperref[sec:SystemischeDynamik]{Abschnitt 2.5}; Abschnitt~\hyperref[sec:Grundkonstruktion]{3.4.1}; Abschnitt~\hyperref[sec:RechtlicheRahmung]{3.1.1}).

**Lounge**

Die Lounge ist der informelle Sozialraum des Systems. In NFS‑H‑01 wird sie über den „Kaffeeklatsch“ und den „Expertenchat“ realisiert. Ihre Funktion liegt weniger in zusätzlichem Inhalt als in der Stabilisierung von Kohorte, Nachfragen und niedrigschwelliger Klärung. In der älteren Instanz war synchrone Kommunikation zusätzlich über BigBlueButton in den Handlungssituationen angelegt. In der aktuellen Instanz ist diese Funktion nicht mehr als BigBlueButton-Baustein in den 32 NFS-H-Handlungssituationen sichtbar; perspektivisch soll synchrone Konnektivität nach dem Moodle-5-Update über Microsoft Teams eingebunden werden. Gerade im Ausbildungsbeginn reduziert die Lounge die Schwelle, sich überhaupt am digitalen Kursgeschehen zu beteiligen. Pädagogisch relevant wird sie dort, wo informeller Austausch Reibungen auffängt, Zugehörigkeit stützt und fachliche Aufgabenbearbeitung entlastet. Fehlende Kommunikationsregeln können diesen Bereich unübersichtlich machen oder in konkurrierende Kanäle zerfallen lassen (\hyperref[sec:Bildungswiss-Verortung]{Abschnitt~2.2}; \hyperref[sec:SystemischeDynamik]{Abschnitt~2.5}).

**Feedback**

**Didaktische Funktion im Gesamtlernprozess**

Der Feedback-Container ist die zentrale Instanz für formative Evaluation, Selbstreflexion und systemische Rückkopplung. Er ermöglicht die kontinuierliche Überprüfung der Qualität der Lernumgebung und der Lernprozesse, die Steuerung individueller und kollektiver Entwicklung sowie die iterative Weiterentwicklung der Lernarchitektur. Durch die systematische Integration von Feedback wird Lernen als rekursiver Prozess operationalisiert, in dem Rückmeldungen als Ressource für Optimierung und Innovation genutzt werden.

**Theoriekonzeptionelle Referenz**

Feedback ist die zentrale Rückkopplungsstelle zwischen subjektiver Erfahrung, Aufgabenbearbeitung und Systementwicklung. Es macht sichtbar, wie Anforderungen erlebt werden, welche Irritationen entstehen, wo Orientierung fehlt und an welchen Stellen Kursstruktur oder Unterstützung angepasst werden müssen. Damit verbindet der Feedback-Container die emotions- und bedürfnisbezogenen Trägervariablen aus \hyperref[sec:PadagogischPsychologischeGrundannahmen]{Abschnitt~2.1} mit der systemischen Dynamik des digitalen Bildungswirkgefüges in \hyperref[sec:SystemischeDynamik]{Abschnitt~2.5}.

**Technische Umsetzung im Learning-Management-System**

Die Verwendung von Feedback-Aktivitäten (TEI-orientiert), offenen Einreichkanälen und Umfragen ist didaktisch begründet. Feedback-Aktivitäten ermöglichen strukturierte, vergleichbare Rückmeldungen. Offene Kanäle fördern niedrigschwellige, spontane Rückmeldungen. Umfragen ermöglichen qualitative Vertiefung. Gegenüber informellen Feedback-Formaten (z. B. E-Mail) erhöhen diese Aktivitäten Transparenz, Aggregierbarkeit und die Möglichkeit, Rückmeldungen systematisch in die Weiterentwicklung zu integrieren.

**Limitationen und Weiterentwicklungspotenziale**

Limitationen liegen in Feedbackmüdigkeit, Oberflächlichkeit und fehlender Konsequenz. Wenn Rückmeldungen ohne sichtbare Veränderung bleiben, sinkt Beteiligung. Technisch wird das Problem verstärkt, wenn Auswertung und Rückspiegelung an die Lernenden zu aufwendig sind. Weiterentwicklung bedeutet daher wenige, eindeutig platzierte Feedbackpunkte mit transparenter Rückmeldung, ergänzt um automatisierte Auswertung und einfache Visualisierungen. Feedback wird als Prozess dann tragfähig, wenn Rückmeldungen als Dialog geführt und als Systeminformation in Kursanpassungen übersetzt werden (Abschnitt~\hyperref[sec:Evaluation-Reflexion]{3.2.4} sowie Abschnitt~\hyperref[sec:Simulation-Kompetenzentwicklung]{4.4}).

**Umsetzung in NFS‑H‑01**

Für NFS‑H‑01 wird diese Rückkopplungslogik als „Startsignal“ der lernenden Organisation gesetzt. Bereits in der Einführungswoche wird sichtbar gemacht, dass Rückmeldung als erwartete Lern- und Systeminformation verstanden wird. Die TEI‑orientierte Feedbackaktivität liefert dabei standardisierte Datenpunkte, die über einzelne Eindrücke hinaus vergleichbar werden. Der offene Einreichkanal hält niederschwellige, situative Rückmeldungen fest. Die qualitative Umfrage erschließt jene Erfahrungsebene, die in Skalen nur begrenzt abbildbar ist (Engagement, Distanz, Irritation, Überraschung). Entscheidend ist dabei weniger die einzelne Frage als die ritualisierte Praxis. Durch die wiederholte, kursintegrierte Nutzung wird Evaluation zu einem Teil der Kurslogik und nicht zu einem nachgeschalteten Qualitätsmanagement.

**Technische Umsetzung**

Somit ist der Bereich als Kombination aus strukturiertem Kursfeedback (orientiert am TEI) und offenen Einreichmöglichkeiten umgesetzt, sodass sowohl standardisierte Indikatoren als auch qualitative Eindrücke erfasst werden. Standardisierte Elemente sind dabei die folgenden.

- **eigene Evaluation (NFS-H-01)** (Feedback) als TEI-orientiertes Kursfeedback zur Erfassung wahrgenommener Trainingseffekte und didaktischer Qualität.
- **Feedback einreichen** als offener Kanal zur niederschwelligen Rückmeldung außerhalb der standardisierten Items.
- **Feedback für uns (NFS-H-01)** (Umfrage) als qualitative Erhebung mit verpflichtenden Reflexionsfragen („Antworten einreichen“, kursseitig mit Aggregation/Anzeige der Rückläufe).

Die Umfrage „Feedback für uns (z. B. NFS-H-01)“ ist als kurze, retrospektive Reflexion angelegt und umfasst verpflichtend zu beantwortende Leitfragen.

1. Wann haben Sie sich in diesem Kurs als Lernende*r am meisten engagiert?
2. Wann hatten Sie als Lernende*r zu diesem Kurs die meiste Distanz?
3. Welche Aktivität im Forum fanden Sie besonders bestätigend oder hilfreich?
4. Welche Aktivität im Forum fanden Sie besonders merkwürdig oder verwirrend?
5. Was hat Sie am meisten überrascht?

**Funktion im Gesamtsystem**

Damit wird sichergestellt, dass neben der quantitativen Erfassung auch qualitative Eindrücke und Reflexionen systematisch dokumentiert und für die Weiterentwicklung genutzt werden können.

**Kursorganisation**

Nach Aufgaben, Quellen, Ergebnissicherung und Feedback wird die Kursorganisation als jene Ebene sichtbar, auf der Rollen, Rechte, Abläufe und Verantwortlichkeiten zusammengeführt werden.

**Didaktische Funktion im Gesamtlernprozess**

Der Kursorganisations-Container ist das Rückgrat der administrativen, rechtlichen und prozessualen Steuerung des Lernraums. Er sichert Transparenz, Nachvollziehbarkeit und Effizienz der organisatorischen Abläufe und richtet den Fokus der Lernenden auf die Inhalte aus, indem er administrative Reibungsverluste minimiert. Durch die Trennung von inhaltlichen und organisatorischen Prozessen wird Klarheit geschaffen und die Selbstorganisation der Lernenden gefördert.

**Theoriekonzeptionelle Referenz**

Die Kursorganisation ist das Element, das die Funktionsfähigkeit und Kohärenz des Systems gewährleistet. Sie macht Zuständigkeiten, Termine, Regeln, Rollen und Abläufe sichtbar und trägt damit jene organisationale Rahmung, die in \hyperref[sec:SystemischeDynamik]{Abschnitt~2.5} als Bedingung stabiler Kopplung beschrieben wird. Als Bindeglied zwischen Struktur und Prozess verhindert sie, dass Lernhandlungen, Rückmeldungen und Nachweise in unverbundene Einzelspuren zerfallen.

**Technische Umsetzung im Learning-Management-System**

Die Kombination aus Datenbanken, Foren, Textseiten und Abstimmungen ist didaktisch und organisatorisch motiviert. Datenbanken ermöglichen strukturierte, versionierbare Ablage und Nachverfolgung (z. B. Einverständniserklärungen, Materialverwaltung). Foren sichern Transparenz und Dokumentation von Abstimmungsprozessen. Textseiten bieten Templates und standardisierte Informationsbereiche. Abstimmungen ermöglichen schnelle, nachvollziehbare Entscheidungen. Gegenüber informellen Kommunikationswegen (z. B. E-Mail) werden Nachvollziehbarkeit und Rollensteuerung deutlich verbessert.

**Limitationen und Weiterentwicklungspotenziale**

Limitationen ergeben sich aus der Komplexität von Rechten und Sichtbarkeit. Wenn Rollenlogik und Zugriff nicht sauber gesetzt sind, entstehen Intransparenz, unbeabsichtigte Offenheit oder Datenschutzprobleme. Gleichzeitig besteht die Gefahr, dass Organisation den Lernprozess überlagert, wenn zu viele administrative Abläufe im Vordergrund stehen. Weiterentwicklung liegt deshalb in transparenten Rollenmodellen, nachvollziehbarer Sichtbarkeitslogik und in Automatisierungen, die Reibung reduzieren, etwa Erinnerungen, Workflows oder Dashboards. Organisation wird dann als Ermöglichungsstruktur erkennbar, wenn sie die rechtlich-funktionalen Anforderungen absichert und zugleich Lernhandlungen entlastet (Abschnitt~\hyperref[sec:RechtlicheRahmung]{3.1.1} sowie Abschnitt~\hyperref[sec:TechnischeArchitektur]{3.3}).

**Umsetzung in NFS‑H‑01**

In NFS‑H‑01 wird diese Trennung konkret, indem organisatorische Verbesserungsvorschläge und Fehlermeldungen als eigene Datenbank geführt werden („Wünsche, Ideen, Gedanken, …“). Redaktionelle Abstimmungen sind in ein gesondertes, rollenbasiert geschütztes Forum ausgelagert. Dadurch entsteht eine doppelte Ordnung. Lernende können Hinweise und Optimierungsideen sichtbar einbringen, ohne dass sie in fachlichen Diskussionen verloren gehen. Die redaktionelle Verantwortung (z. B. Anpassung von Aufgaben, Texten, Materialien) bleibt dort steuerbar, wo sie sinnvollerweise liegt. Die Advance‑Organizer‑Textseiten (z. B. „Ausbildungsziel“, „Wissenschaftliches Arbeiten“) und die Materialverzeichnisse (Informationsblätter, Unterrichtsmaterial) sind Ablageorte und Standardisierungsinstrumente. Sie sichern Wiedererkennbarkeit von Kurskommunikation, reduzieren Interpretationsspielräume und machen wichtige Dokumente „kursnah“ auffindbar. Gerade die im Kursdump sichtbaren Einschränkungen („fehlende Gruppierung“) verweisen auf einen zentralen Punkt. Sichtbarkeit ist hier didaktische Infrastruktur. Wo Rollen- und Gruppenlogik nicht sauber gesetzt ist, entsteht unbeabsichtigte Intransparenz (Material verschwindet) oder ungewollte Offenheit (Abstimmungen, redaktionelle Prozesse). Der Kursorganisationscontainer ist damit der Ort, an dem sich technische Rechteverwaltung unmittelbar in pädagogische Steuerbarkeit übersetzt.

**Technische Umsetzung (Beispielkurs)**

Operationalisiert wird dies über standardisierte Bausteine. Dazu zählen die folgenden.

- **Einverständniserklärungen** als Datenbank zur dokumentierten Ablage und Nachverfolgbarkeit von Einwilligungen sowie zugehöriger Rückmeldeschleifen.
- **Gebrauchsmaterial** als Datenbank zur Sammlung, Verwaltung und Aktualisierung kursbezogener Materialien (z. B. Verbrauchs- und Arbeitsmittel).
- **Wünsche, Ideen, Gedanken, Anregungen, Fehler** als Datenbank für kontinuierliche Verbesserungsvorschläge, Fehlermeldungen und Optimierungsideen im Sinne einer lernenden Organisation.
- **Kursorganisation** als Forum zur allgemeinen Abstimmung organisatorischer Fragen.
- **Redaktionelle Abstimmung** als rollenbasiert eingeschränktes Forum zur inhaltlich-redaktionellen Koordination, ergänzt um **Advance Organizer Vorlage (Textseite)** als strukturiertes Template für einheitliche Kurskommunikation und Ankündigungen.
- **Praxisbegleitung** als rollenbasiert eingeschränktes Forum (Praxisanleitung) zur Begleitung und Auswertung von Praxisbegleitgesprächen, ergänzt um einen **zusätzlichen Praxisbegleitungsblock** als Abstimmungselement, das abhängig von Rollenbedingungen Entscheidungen und Terminabsprachen technisch unterstützt.
- **Rund um die staatliche Prüfung** als organisatorische Sammelkategorie, insbesondere mit **Prüfungsorganisation** als rollenbasiert eingeschränktem Forum (Prüfende) zur Vor- und Nachbereitung, sowie den Textseiten **Gruppen- und Stationsverteilung**, **Prüfungsablauf** und **Prüfungsausschuss** zur verbindlichen, kursweit referenzierbaren Bereitstellung prüfungsrelevanter Informationen.

**Funktion im Gesamtsystem**

Die konsequente Rollen- und Sichtbarkeitssteuerung (z. B. Lehrende/Dozent*in/Praxisanleitung/Prüfende) erfüllt dabei zwei Funktionen. Erstens werden organisatorische Prozesse dort transparent gemacht, wo sie für Lernende handlungsrelevant sind (z. B. Ablauf- und Verteilungsinformationen), und zweitens werden sensible Abstimmungs- und Prüfungsprozesse systemseitig vor unberechtigtem Zugriff geschützt. Insgesamt ermöglicht der Container „Kursorganisation“ damit eine Trennung von Lern- und Verwaltungslogik, ohne die kursinterne Kohärenz des digitalen Bildungsraums zu beeinträchtigen.

### 3.4.3 Prüfungsarchitektur {#sec:Pruefungsarchitektur}

Die Prüfungsarchitektur ist im untersuchten LMS Teil der didaktischen und organisatorischen Grundkonstruktion. Prüfungsrelevante Anforderungen werden über Aufgabenlogik, Ergebnissicherung, Rückmeldestrukturen und Rollensteuerung kontinuierlich mitgeführt. Damit folgt der Abschnitt einem Verständnis digitaler Lernumgebungen, in dem Plattform, Organisation und Qualitätssicherung als zusammenhängende Struktur betrachtet werden (@peters_referenzhandbuch_2016).

Im Untersuchungsfall ist diese Prüfungslogik in drei Ebenen des Systems eingelassen. Erstens ist die Prüfungsvorbereitung curricular fest verankert. Wie der Übersicht der Handlungssituationen im Anhang zu entnehmen ist, ist mit `NFS-H-32` eine eigene Handlungssituation „Vorbereitung auf die Notfallsanitäterprüfung“ angelegt (\hyperref[sec:A-5]{Anhang „Übersicht Berufliche Handlungssituationen“}). Prüfungsvorbereitung erscheint damit als regulärer Teil der didaktischen Architektur. Sie ist in dieselbe Containerlogik eingebunden wie die übrigen Handlungssituationen und wird dadurch mit Ressourcen, Aufgaben, Ergebnissicherung und Rückmeldung verschränkt.

Zweitens wird Prüfungsrelevanz im Aufgabenbereich und in der Ergebnissicherung thematisch und strukturell vorbereitet. Aufgabenformate, Operatoren und Bearbeitungsanforderungen gewöhnen an dokumentierte Bearbeitung, an begründete Entscheidungen, an transparente Kriterien und an die Rückbindung von Ergebnissen an vorgegebene Anforderungen. Die Ergebnissicherung schließt daran an, indem sie Bearbeitungsspuren, Verdichtungen und wiederverwendbare Nachweise erzeugt, die über die einzelne Lernsituation hinaus anschlussfähig bleiben. Rückmeldung erscheint in diesem Zusammenhang als mitlaufende Struktur der Bearbeitung, was sich auch in anderen Bildungssettings als tragfähige Prozesslogik beschreiben lässt (@pieper_lehrkraft-feedback_2023).

Drittens umfasst die Prüfungsarchitektur auch organisationale und operative Vollzugsanteile. Der Bereich Kursorganisation trägt diese Seite des Systems mit, weil dort Sichtbarkeiten, Zugriffsrechte, Verteilungslogiken und organisatorische Zuständigkeiten systematisch geführt werden. In Abschnitt~\hyperref[sec:DidaktischeUmsetzung]{3.4.2} wurde dies bereits an der Sammelkategorie „Rund um die staatliche Prüfung“ mit Prüfungsorganisation, Gruppen- und Stationsverteilung, Prüfungsablauf und Prüfungsausschuss sichtbar gemacht. Prüfungsorganisation ist damit im Learning-Management-System selbst verankert. Soweit schriftliche Prüfungsanteile im Untersuchungsfall systembasiert im Learning-Management-System durchgeführt werden, reicht diese Integration über die Vorbereitung hinaus bis in den Prüfungsvollzug. Für den weiteren Diskurs zum digitalen Prüfungswesen ist dabei relevant, dass digitale Prüfungsdurchführung als an den Ausbildungsvollzug rückgebundene Praxis verstanden werden sollte (@hollmann_prufungswesen_2021).

Für die rechtlich-funktionale Rahmung aus Abschnitt~\hyperref[sec:RechtlicheRahmung]{3.1.1} ist das bedeutsam, weil Prüfungen an dieselbe Koordinations- und Organisationsverantwortung rückgebunden bleiben wie der übrige Ausbildungsvollzug. Das LMS bildet jene Infrastruktur, in der Prüfungsvorbereitung, prüfungsrelevante Bearbeitungen, Ergebnissicherungen und organisatorische Abstimmungen nachvollziehbar zusammenlaufen. Die Prüfungsarchitektur bildet damit die Schnittstelle zwischen curricularer Ordnung, dokumentierter Lernbearbeitung und rechtlich gebundener Nachweislogik. Vor diesem Hintergrund wird im folgenden Abschnitt die curriculare Struktur des digitalen Bildungsraums quantitativ beschrieben.

### 3.4.4 Deskriptive Struktur der curricularen Architektur {#sec:CurriculareStruktur}

Dieser Abschnitt beschreibt die curriculare Struktur des digitalen Bildungsraums „NFS-H“ in quantitativer Form. Ausgewiesen werden Verteilungen nach Themenbereichen und Kompetenzfeldern sowie ergänzende Kennwerte wie Kursdauer und Aufgabenanzahl. Hinzu kommen Visualisierungen, die die Kursstruktur entlang der in der NotSan-APrV vorgegebenen Bezugsgrößen dokumentieren.

**Datengrundlage und Zielsetzung**

Die Auswertung beschreibt die 32 digital abgebildeten Handlungssituationen des Systems („NFS-H-Kurse“) entlang der Anlage 1 NotSan-APrV. Im Mittelpunkt stehen die Zuordnung zu Themenbereichen und Kompetenzfeldern, die Verteilung der Kursanteile sowie zusammenfassende Kennwerte der Kursstruktur. Der Abschnitt dokumentiert zunächst, wie sich die curriculare Architektur des digitalen Bildungsraums in quantitativer Hinsicht anhand der in dieser Arbeit vorgenommenen Auswertung darstellt [@hanisch-johannsen_systematische_2025].

**Analytisches Vorgehen**

Die 32 Kurse wurden automatisiert mit Python und Pandas ausgewertet. Als Referenzbasis dienen die APrV-Kürzel aus der Datei `lms-verteilung.xlsx`. Jedes Kürzel wurde anhand der Datei `APrV-Kuerzel_zu_Kompetenzbereichen.csv` einem der drei Themenbereiche `medizinisch`, `rettungsdienstlich` oder `bezugswissenschaftlich` sowie einem von vier Kompetenzfeldern `fachlich`, `sozial`, `personal` oder `methodisch` zugeordnet. Diese Zuordnung orientiert sich an der Struktur der NotSan-APrV [@bundesgesundheitsministerium_referentenentwurf_2012, Seite 47]. Für jede Handlungssituation wurden die relativen Anteile dieser Kürzel berechnet und daraus die jeweils dominierenden Bereiche abgeleitet [@hanisch-johannsen_systematische_2025].

Ergänzend wurden der Zusammenhang zwischen Aufgabenanzahl und Kursdauer berechnet, Verteilungen nach Themenbereichen über Mittelwert, Median und Standardabweichung beschrieben sowie die Ergebnisse in Boxplots, Vergleichsdiagrammen und zwei Clusterdarstellungen aufbereitet. Diese Darstellungen eröffnen eine zusätzliche Sicht auf Ähnlichkeiten und Unterschiede der Kursprofile im Raum der Themenanteile.

**Ergebnisse im Überblick**

Die Auswertung der 32 Kurse liefert zunächst Kennzahlen zur inhaltlichen Gewichtung nach Themenbereichen.

- Bezugswissenschaftlich: 12 Kurse, Ø Dauer = 21,3 Tage, Ø Aufgaben = 25,6
- Medizinisch: 12 Kurse, Ø Dauer = 27,2 Tage, Ø Aufgaben = 32,8
- Rettungsdienstlich: 6 Kurse, Ø Dauer = 57,0 Tage, Ø Aufgaben = 38,7
- Einführung/Prüfung (Sonderkategorie): 2 Kurse, Ø Dauer = 23,5 Tage, Ø Aufgaben = 30,5

Die folgenden Kennwerte eröffnen einen Vergleich mit der normativen Stundenverteilung der Anlage 1 NotSan-APrV (\hyperref[fig:fg-aprv-themenbereiche]{Abb.~\ref{fig:fg-aprv-themenbereiche}}).

- Rettungsdienstlich: 47 % (APrV) vs. empirisch Ø 57,0 Tage (höchster Kursmittelwert)
- Medizinisch: 27 % (APrV) vs. Ø 27,2 Tage (nächsthöherer Mittelwert)
- Bezugswissenschaftlich: 26 % (APrV) vs. Ø 21,3 Tage

Auch die Verteilung der Kompetenzbereiche ist als Gegenüberstellung zur normativen Referenz ausgewiesen (\hyperref[fig:fg-aprv-kompetenzbereiche]{Abb.~\ref{fig:fg-aprv-kompetenzbereiche}} sowie \hyperref[fig:fg-vergleich-kompetenzgewichtung]{Abb.~\ref{fig:fg-vergleich-kompetenzgewichtung}}). Die Aufgabenverteilung nach Themenbereich ist in \hyperref[fig:fg-aufgaben-pro-themenbereich]{Abbildung~\ref{fig:fg-aufgaben-pro-themenbereich}} visualisiert; die Kursdauerverteilung nach Themenbereich in \hyperref[fig:fg-kursdauer-pro-themenbereich]{Abbildung~\ref{fig:fg-kursdauer-pro-themenbereich}}.

Ergänzend lässt sich die Struktur der 32 Kurse als mehrdimensionaler Raum der Themenanteile `medizinisch`, `rettungsdienstlich` und `bezugswissenschaftlich` darstellen. \hyperref[fig:fg-kmeans-themenanteile]{Abbildung~\ref{fig:fg-kmeans-themenanteile}} zeigt eine Gruppierung der Kursprofile im dreidimensionalen Anteilsraum. \hyperref[fig:fg-dendrogramm-themenanteile]{Abbildung~\ref{fig:fg-dendrogramm-themenanteile}} ergänzt diese Darstellung um eine hierarchische Sicht auf thematische Nähe und Distanz.

Die erste Darstellung bündelt die Kursprofile im Anteilsraum. So wird erkennbar, ob einzelne Kurse als Randfälle oder Übergänge zwischen Themenprofilen erscheinen.

![K-Means-Clusteranalyse der Kursanteile nach Themenbereichen.](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/kmeans_cluster_anteile_notsan-aprv-vergleich.png>){#fig:fg-kmeans-themenanteile}

\figsubcaption{3D-Darstellung der 32 Kurse im Raum der Themenanteile (medizinisch, rettungsdienstlich, bezugswissenschaftlich) mit farblicher Zuordnung der k-means-Cluster; die Grafik verdeutlicht, wie sich Kurse anhand ihrer normativ codierten Themenprofile im Anteilsraum zu Gruppen bündeln.}

Die Projektion verdeutlicht, wie sich die Kursanteile im dreidimensionalen Raum verteilen und welche Kursprofile dabei näher beieinanderliegen.

Das Dendrogramm ergänzt diese Sicht um eine hierarchische Gruppierung. Erkennbar wird, in welchen Abständen Kurse zusammengeführt werden und an welchen Stellen sich größere Gruppen abzeichnen.

![Dendrogramm der Kursanteile nach Themenbereichen.](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/dendrogramm_cluster_anteile_notsan-aprv-vergleich.png>){#fig:fg-dendrogramm-themenanteile}

\figsubcaption{Hierarchische Clusterstruktur der Kursanteile (Ward-Linkage) als Ähnlichkeitsbaum; die Höhe der Verknüpfungen (Distanz) markiert, welche Kurse thematisch nahe beieinanderliegen und wo sich größere Gruppen entlang der Themenprofile bilden.}

Zusammen zeigen beide Visualisierungen die Kursprofile einmal als Gruppierung im Anteilsraum und einmal als abgestufte Ähnlichkeitsstruktur.

![Anteil der Themenbereiche nach NotSan-APrV (eigene Darstellung).](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/anteil-der-themenbereiche-nach-aprv_notsan-aprv-vergleich.png>){#fig:fg-aprv-themenbereiche}

\figsubcaption{Normative Referenzverteilung der drei Themenbereiche (medizinisch, rettungsdienstlich, bezugswissenschaftlich) gemäß Anlage 1 NotSan-APrV; dient als Ausgangspunkt für den empirischen Abgleich mit der im digitalen Curriculum realisierten Struktur.}

\hyperref[fig:fg-aprv-themenbereiche]{Abbildung~\ref{fig:fg-aprv-themenbereiche}} visualisiert die prozentuale Verteilung der inhaltlichen Themenbereiche gemäß Anlage 1 der Ausbildungs- und Prüfungsverordnung für Notfallsanitäter\*innen (NotSan-APrV). Diese drei Themenbereiche – medizinisch (27 %), rettungsdienstlich (47 %) und bezugswissenschaftlich (26 %) – bilden die normative Grundlage des theoretischen und praktischen Unterrichts über 1.920 Stunden [@bundesgesundheitsministerium_referentenentwurf_2012, Seiten 44, 47]. Der größte Anteil entfällt auf rettungsdienstliche Inhalte. Der medizinische Bereich umfasst diagnostische und pathophysiologische Anteile, bezugswissenschaftliche Inhalte etwa Kommunikation, Recht oder Psychologie.

![Anteil der Kompetenzbereiche nach NotSan-APrV (eigene Darstellung).](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/anteil-der-kompetenzbereiche-nach-aprv_notsan-aprv-vergleich.png>){#fig:fg-aprv-kompetenzbereiche}

\figsubcaption{Normative Referenzgewichtung der Kompetenzbereiche (fachlich, sozial, personal, methodisch) gemäß NotSan-APrV; dient als Referenzrahmen für die empirisch rekonstruierte Kompetenzzuordnung des digitalen Curriculums.}

\hyperref[fig:fg-aprv-kompetenzbereiche]{Abbildung~\ref{fig:fg-aprv-kompetenzbereiche}} zeigt, bezogen auf den Gesamtumfang der Ausbildung, die in der NotSan-APrV verankerte Kompetenzgewichtung. Die vier Kompetenzbereiche – fachlich (24 %), sozial (15 %), personal (11 %) und methodisch (50 %) – definieren die Zielstruktur beruflicher Handlungskompetenz im Rettungsdienst [@bundesgesundheitsministerium_referentenentwurf_2012, Seite 47]. Der hohe Anteil methodischer Kompetenzen wird in der normativen Verteilung sichtbar ausgewiesen. Fachliche, soziale und personale Anteile ergänzen diesen Schwerpunkt um Wissen, Interaktionsfähigkeit und Reflexionsfähigkeit.

![Vergleich der Themengewichtung von NotSan-APrV und Curriculum.](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/vergleich-themengewichtung-aprv-schatzung-vs-nfs-h-lehrplan_notsan-aprv-vergleich.png>){#fig:fg-vergleich-themengewichtung}

\figsubcaption{Gegenüberstellung der normativen Themengewichtung (NotSan-APrV) mit der empirisch rekonstruierten Verteilung im digitalen Curriculum (NFS-H).}

Die Balkengrafik in \hyperref[fig:fg-vergleich-themengewichtung]{Abbildung~\ref{fig:fg-vergleich-themengewichtung}} stellt die normativ vorgegebene Verteilung der Themenbereiche gemäß NotSan-APrV der empirisch rekonstruierten Verteilung im digitalen Curriculum „NFS-H“ gegenüber [@bundesgesundheitsministerium_referentenentwurf_2012, Seiten 44, 47].

![Vergleich der Kompetenzgewichtung von NotSan-APrV und Curriculum.](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/vergleich-kompetenzgewichtung-aprv-schatzung-vs-nfs-h-lehrplan_notsan-aprv-vergleich.png>){#fig:fg-vergleich-kompetenzgewichtung}

\figsubcaption{Gegenüberstellung der normativen Kompetenzgewichtung (NotSan-APrV) mit den empirisch rekonstruierten Anteilen im digitalen Curriculum.}

\hyperref[fig:fg-vergleich-kompetenzgewichtung]{Abbildung~\ref{fig:fg-vergleich-kompetenzgewichtung}} stellt die normativen Vorgaben der NotSan-APrV den empirisch ermittelten Anteilen im Curriculum gegenüber [@bundesgesundheitsministerium_referentenentwurf_2012, Seite 47].

![Verteilung der Aufgaben pro Themenbereich (eigene Darstellung).](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/verteilung-der-aufgaben-pro-themenbereich_notsan-aprv-vergleich.png>){#fig:fg-aufgaben-pro-themenbereich}

\figsubcaption{Boxplot der Aufgabenanzahl je Kurs, gruppiert nach Themenbereichen (medizinisch, rettungsdienstlich, bezugswissenschaftlich sowie Einführung/Prüfung); zeigt Median, Streuung und Ausreißer als Indikatoren für die interne Differenzierung der Aufgabenlast.}

Die Boxplot-Darstellung in \hyperref[fig:fg-aufgaben-pro-themenbereich]{Abbildung~\ref{fig:fg-aufgaben-pro-themenbereich}} zeigt die Anzahl der Aufgaben in den 32 Kursen, gruppiert nach den Bezugskategorien (medizinisch, rettungsdienstlich, bezugswissenschaftlich sowie Einführung/Prüfung) [@bundesgesundheitsministerium_referentenentwurf_2012, Seiten 44–45]. Dargestellt sind Median, Streuung und Ausreißer pro Kategorie.

![Verteilung der Kursdauer pro Themenbereich (eigene Darstellung).](<08 Metaquellen/08-01 Abbildungen/LMS-Abbildungen/verteilung-der-kursdauer-pro-themenbereich_notsan-aprv-vergleich.png>){#fig:fg-kursdauer-pro-themenbereich}

\figsubcaption{Boxplot der Kursdauer (in Tagen) je Kurs, gruppiert nach Themenbereichen; zeigt Median, Streuung und Ausreißer als Indikatoren für die zeitliche Allokation und die interne Varianz der Kurslogik.}

Die Boxplot-Darstellung in \hyperref[fig:fg-kursdauer-pro-themenbereich]{Abbildung~\ref{fig:fg-kursdauer-pro-themenbereich}} visualisiert die Dauer der 32 Kurse in Tagen, differenziert nach den vier Bezugskategorien [@bundesgesundheitsministerium_referentenentwurf_2012, Seiten 44–45]. Dargestellt sind Median, Streuung und Ausreißer pro Kategorie.

Die Einordnung der in diesem Abschnitt dokumentierten Kennwerte erfolgt im Ergebniskapitel (Abschnitt~\hyperref[sec:CurricularesAlignment]{5.1.1}).

## 3.5 Operative Architektur als Arbeits- und Lernumgebung {#sec:OperativeArchitektur}

Die operative Architektur erweitert die didaktische Architektur um jene Funktionen, die im Ausbildungsalltag Lernprozesse, Koordination, Übersicht und Arbeitsorganisation tragen. Für Lehrkräfte ist das System damit didaktisches Werkzeug und zugleich Arbeitsmittel. Zwei Studien markieren dafür einen knappen Vergleichsrahmen. Sie zeigen, dass digitale Systeme auch für administrative, organisatorische und arbeitsplatzbezogene Zwecke genutzt werden können, bleiben im Aufbau jedoch deutlich schmaler als der hier beschriebene Untersuchungsfall.

@brandic_asynchroner_2024 beschreiben die Entwicklung eines asynchronen Moodle-Kurses für das fachliche Onboarding administrativen Personals an der Universität Wien. Ziel ist eine zeitlich flexible, selbstgesteuerte Schulung, die den Einstieg in zentrale IT-Systeme der Universität erleichtert. Der Kurs arbeitet mit strukturierten Lerneinheiten, H5P-Elementen, Videos und Aufgaben und ist als autodidaktischer Lernpfad angelegt [@brandic_asynchroner_2024, Seite 22–24].

Für den hier verfolgten Zusammenhang ist an dieser Studie vor allem interessant, dass das Learning-Management-System als operatives Arbeitsmittel in einem eng umrissenen Anwendungsszenario eingesetzt wird. Im Vergleich zum hier beschriebenen System bleibt der Kurs jedoch auf ein einzelnes Onboarding-Format bezogen und ist nicht auf eine curricular durchgearbeitete Mehrjahresstruktur ausgerichtet.

@nwosu_digitalisation_2024 akzentuieren die administrative Seite noch deutlicher. Im Mittelpunkt stehen Digitalisierungsprozesse der Bildungsverwaltung, Fragen von Effizienz, Steuerung und Produktivität sowie die organisatorischen Voraussetzungen digitaler Systeme [@nwosu_digitalisation_2024, Seite 3–5]. Lehr- und Lernprozesse werden mitgeführt und erscheinen vor allem unter dem Gesichtspunkt verbesserter Administration.

Im Vergleich dazu ist das hier betrachtete Learning Management System als pädagogisch fundierte und operativ nutzbare Struktur angelegt. Organisation und Lehre greifen darin in derselben Systemarchitektur ineinander. Die Containerstruktur für die Handlungssituationen rahmt Lernprozesse und unterstützt zugleich Kurskoordination, Aufgabenverteilung und Rückmeldung. Kursadministration, Nutzerverwaltung, Terminplanung und Kommunikationswerkzeuge sind deshalb Teil des operativen Zuschnitts des Systems. Die beiden Studien markieren dafür hilfreiche Vergleichspunkte. @brandic_asynchroner_2024 zeigen ein begrenztes Onboarding-Format, @nwosu_digitalisation_2024 einen stärker administrativ gerahmten Digitalisierungsansatz. Der hier untersuchte Fall führt curriculare Logik, operative Nutzung und didaktische Architektur in einem gemeinsamen Rahmen zusammen.

## 3.6 Exkurs: E-Portfolio als Reflexions- und Transferinstrument {#sec:E-Portfolio}

Das E-Portfolio ist im hier untersuchten System Teil der operativen Architektur des digitalen Bildungsraums. Technisch ist es als eigenständiges Bildungswerkzeug realisiert und steht damit neben Learning-Management-System, Cloudspeicher und den weiteren Systemkomponenten der in Abschnitt~\hyperref[sec:TechnischeArchitektur]{3.3} beschriebenen Infrastruktur. Pädagogisch entspricht es einem Raum, in dem individuelle Lernspuren, Praxisbezüge und längerfristige Entwicklungsverläufe zusammengeführt werden können, wie dies auch für E-Portfolios als Bindeglied zwischen Hochschule, Studierenden und Praxis beschrieben wird [@hess_e-portfolios_2024]. Seine Funktion geht über diese technische Zuordnung hinaus. Im Zusammenspiel mit den Aufgabencontainern, den Formen der Ergebnissicherung und den Rückmeldelogiken der Kurse übernimmt das E-Portfolio eine eigene pädagogische Rolle. Es ist dabei eher individuell beziehungsweise kohortenspezifisch angebunden. Es nimmt Artefakte, Zwischenergebnisse, Reflexionen und Nachweise auf und führt sie in einen Zusammenhang, der über die einzelne Handlungssituation hinausreicht.

Didaktisch lässt sich diese Rolle in drei eng miteinander verbundenen Funktionen beschreiben. Erstens dient das E-Portfolio der Dokumentation. Lernprodukte, Einsatzberichte, Rückmeldungen und ausgewählte Bearbeitungsergebnisse werden in einer Form gesammelt, die Wiederauffindbarkeit und Nachvollziehbarkeit über einzelne Kursräume oder Abgabezeitpunkte hinaus sichert. Zweitens fungiert es als Reflexionsraum. Die im Lernprozess entstandenen Artefakte werden dort in ihrer Entstehung, ihrer Qualität und ihrer Bedeutung für weitere Lernschritte thematisierbar. Dass digitale Portfolioformate genau diese Verbindungslinien zwischen einzelnen Inhalten, Rückmeldungen und Entwicklungsschritten sichtbar machen können, beschreiben auch @mrohs_digitale_2023 für das digitale Feedback-Portfolio. Drittens übernimmt das E-Portfolio eine Transferfunktion. Es verbindet Ergebnisse aus einzelnen Handlungssituationen und kohortenspezifischen Kurszusammenhängen mit späteren Anforderungen, macht Entwicklungslinien sichtbar und schafft Anschlussstellen zwischen kurzfristiger Aufgabenbearbeitung und längerfristiger beruflicher Bildung. Für gesundheitsberufliche Kontexte ist diese Brückenfunktion zwischen Theorie, Praxis und digitalem Lernen auch von @schwanke_einsatz_2023 ausdrücklich hervorgehoben worden.

In erwachsenen- und weiterbildungswissenschaftlicher Lesart wird diese Funktion noch präziser. Reflexives Lernen setzt an Erfahrungen an und verbindet berufliches Handeln mit wissenschaftlicher Deutung, sodass Professionalitätsentwicklung als Wechselbezug von Praxis, Wissen und Selbstbeobachtung möglich wird. Genau diese Struktur bildet das E-Portfolio im untersuchten System ab. Einsatzberichte, Aufgabenprodukte, Rückmeldungen und Praxisreflexionen werden dort gesammelt und zugleich als Anlässe für Distanzierung, Neubewertung und berufliche Weiterentwicklung verfügbar. [@jutte_professionalitatsentwicklung_2025, Seiten 6 und 8-10]

Gerade diese dritte Funktion ist für die Systemarchitektur bedeutsam. Im Learning-Management-System werden Aufgaben bearbeitet, Rückmeldungen gegeben, Diskussionen geführt und Ergebnisse in den jeweiligen Containern sichtbar gemacht (Abschnitt~\hyperref[sec:DidaktischeArchitektur]{3.4}). Das E-Portfolio setzt an diesem Punkt an und führt die Strukturen als Fortsetzungsraum der Lernaktivitäten weiter. Was in Aufgabenmodulen, Foren, Wikis, Glossaren oder Datenbanken zunächst handlungssituationsbezogen entsteht, kann dort in eine individuelle und zugleich längerfristige Form überführt werden. Damit verschiebt sich der Blick vom isolierten Kursergebnis auf eine verdichtete Lernbiografie, in der Zusammenhänge zwischen Lernschritten, Praxisbezügen und Rückmeldungen erkennbar bleiben.

Für die im Ergebniskapitel später aufgegriffene Kompetenzperspektive ist dieses Arrangement anschlussfähig, ohne sie hier bereits vorwegzunehmen. Das E-Portfolio schafft einen Raum, in dem Kompetenzentwicklung dokumentiert, reflektiert und plausibilisiert werden kann. Sichtbar werden dort Leistungen, Verdichtungen, Überarbeitungen, Rückbezüge und Übergänge zwischen verschiedenen Anforderungssituationen. Im Wirkgefüge des untersuchten digitalen Bildungsraums übernimmt das E-Portfolio damit eine vermittelnde Funktion. Es koppelt operative Lernprozesse an längerfristige Selbstbeobachtung und macht aus verteilten Lernspuren eine Form, in der Entwicklung über einzelne Kurse hinaus lesbar wird.

Mit dieser Gegenstandsbeschreibung sind jene Ebenen bestimmt, an denen die Arbeit im nächsten Schritt methodisch ansetzt. Kapitel \hyperref[sec:Methodologie]{4} übersetzt die theoretische Rahmung und die hier rekonstruierte Architektur in ein forschungsfragengeleitetes Methodendesign, das die weiteren Analysen trägt.
