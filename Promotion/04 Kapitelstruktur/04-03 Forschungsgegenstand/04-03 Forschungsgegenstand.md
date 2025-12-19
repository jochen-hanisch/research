\newpage

# 3 Beschreibung des Forschungsgegenstandes {#sec:Forschungsgegenstand}

Kapitel 3 beschreibt Entstehung, Kontext und Architektur des untersuchten LMSs. Es konkretisiert damit die in \hyperref[sec:Theorieteil]{Kapitel 2} entwickelten theoretischen Überlegungen für den spezifischen Anwendungsfall und bereitet die spätere Ergebnisdarstellung in \hyperref[sec:Ergebnisse]{Kapitel 5} vor.

Die hier dargestellte Architektur und ihre rechtlich-didaktische Verortung werden in \hyperref[sec:Diskussion-Interdependenz]{Kapitel 6.3.1} in den Interdependenzrahmen eingeordnet und bilden eine der empirischen Grundlagen für die manifestartige Verdichtung in \hyperref[sec:Conclusio-Manifest]{Kapitel 7}.

Folgerung für die Darstellung
Konsequenzen klar zweiteilig gliedern:
(a) rechtlich-funktional,
(b) didaktisch-strukturell
Learning Management System (LMS) = Schnittstelle zwischen Norm und Didaktik

## 3.1 Kontext des Forschungsgegenstandes {#sec:Kontext-FG}

### 3.1.1 Rechtlich-funktionale Rahmung {#sec:RechtlicheRahmung}

Das hier zu beschreibende LMS (LMS) wird im Rahmen in der Lehre der durch die europäische Richtlinie 2005/36/EG reglementierten Gesundheitsberufe, insbesondere in der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern, eingesetzt. Der Begriff der Gesundheitsberufe ist nicht definiert und fasst alle Berufe zusammen, deren Tätigkeitsfeld im Wesentlichen im Gesundheitssektor angesiedelt ist. Für einen Teil dieser Berufe sind Ausbildung und Prüfung gesetzlich geregelt; diese Berufe stehen im Mittelpunkt der hier angestellten Betrachtungen und werden den reglementierten Berufen, und damit der Gesetzgebungskompetenz des Bundes zugeordnet. Die reglementierten Heilberufe fassen Berufe zusammen, deren Tätigkeiten insbesondere heilende und medizinisch-assistierende Anteile als charakteristisches Merkmal aufweisen. Aus der staatlichen Zuordnung folgt, dass die Führung der Berufsbezeichnung entweder durch eine Approbation oder durch eine behördliche Erlaubnis auf Antrag erworben werden kann. [@bundesgesundheitsministerium_gesundheitsberufe_2025]

Im Anwendungsfeld der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern sowie die Erlaubnis zum Führen der Berufsbezeichnung unterliegt der o.a. staatlichen Regelung. Maßgeblich verantwortlich für die gesetzeskonforme Umsetzung ist nach § 5 Abs. 3 Satz 4 NotSanG die Schule, in deren Gesamtverantwortung die „Organisation und Koordination des theoretischen und praktischen Unterrichts und der praktischen Ausbildung entsprechend dem Ausbildungsziel“ [@bundesrepublik_deutschland_gesetz_2023, § 5 (3) Satz 4] liegt. Die genaue Bedeutung dieses Auftrages verdeutlichen Dielmann & Malottke [@dielmann_notfallsanitatergesetz_2017, Seite 137-138] in ihrem Kommentar und bieten damit eine zentrale normierte Grundlage zur Herleitung der Rolle eines LMS innerhalb der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern.

Den Kommentatoren nach obliegt der Schule zwar die Gesamtverantwortung zur Organisation und Koordination des Unterrichtes und der praktischen Ausbildung, jedoch ist diese Verantwortlichkeit nicht auf die gesamte Ausbildung übertragbar. Diese liegt beim Träger der Ausbildung und muss auch von ihm wahrgenommen werden. Das Ziel der Organisation und Koordination ist demzufolge die sinnvolle, strukturierte Verzahnung der Lernorte Lehrrettungswache, Schule und Krankenhaus entlang des gesetzlich vorgegebenen Ausbildungsziels gem. § 4 NotSanG [@bundesrepublik_deutschland_gesetz_2023, § 4]. Infolgedessen steht die Schule in der Verantwortung der Koordination mit gleichzeitigem Ausschluss der hoheitlichen Deutung. Demnach kann die Schule gestalterisch tätig sein, jedoch ist diese Gestaltung nicht als autonom anzusehen. [@dielmann_notfallsanitatergesetz_2017, Seite 137-138]

Die Konsequenzen des Einsatzes eines LMS können entlang der Dimensionen Werkzeugfunktion, Kohärenzsicherung und Abgrenzung schulischer und trägerschaftlicher Verantwortung weiter differenziert werden.
Aufgrund der Koordinations- und Organisationsverantwortung der Schule lässt sich aus den bisherigen Überlegungen ableiten, dass das hier behandelte Lernmanagementsystem als das gesetzlich geforderte Steuerungsinstrument angesehen werden kann, das zur Umsetzung der gesetzlichen Verpflichtung geeignet erscheint. Erst die nachvollziehbare und standardisierte Zusammenführung von Kursen, Kalendern, Lernfortschritten, Aufgaben und Einsatzberichten in E-Portfolios\label{term:e-portfolio} innerhalb einer digitalen Struktur kann die Ausbildungsabschnitte und unterschiedlichen Lernorte strukturell miteinander verknüpfen. Ergänzend bildet die Integration von Fallbearbeitungen, Praxisreflexionen sowie zeitunabhängigen, dokumentierten Reflexionsprozessen das didaktische Gerüst, das die Koordination zwischen den Lernorten sowie den theoretischen und praktischen Ausbildungsanteilen systematisch stützt. Unter diesen Voraussetzungen ist das LMS ein operationalisiertes Werkzeug zur Wahrnehmung der schulischen Verantwortung zur Koordination und Organisation.

In den o.a. Ausführungen wird die Notwendigkeit verwiesen, individuelle Ausbildungspläne so zu gestalten, dass Rahmenlehrpläne bzw. die rechtlichen Ausbildungsbestimmungen umgesetzt werden können. Ableitend davon, ergibt sich die Verpflichtung zur Kohärenz von Rahmenlehrplan, Stundenplan und Einsatzplan sowie deren inhaltlichen Anteile zueinander. Das LMS muss folglich in der Lage sein, die einzelnen Elemente individuell und lernortspezifisch aufeinander abzustimmen. Damit fungiert das LMS als strukturelles Bindeglied zwischen Theorie (Stundenplan), Praxis (Einsatzorte) und Individualisierung (Ausbildungspläne) und verfügt über die Möglichkeit, diese disjunkten Elemente über Planungs- und Synchronisationsfunktionen miteinander zu verbinden.

Wenn Schule nicht die insgesamte Ausbildungsverantwortung übernimmt, sondern der Ausbildungsträger\label{term:ausbildungstraeger} sich ihrer als Erfüllungsgehilfin bedient, ergibt sich daraus im rechtlichen Sinne eine funktionale Verpflichtung zum Einsatz eines digitalen Koordinations- und Organisationsinstruments. Der Ausbildungsträger bleibt nach obiger Lesart haftungsrechtlich in der Verantwortung und durch den Einsatz des LMS durch die Schule übernimmt diese einen Teil genau dieser Verantwortlichkeit, ohne gleichzeitig selbst in die Trägerrolle zu wechseln. Durch den Einsatz eines digitalen Systems können alle rechtlich geforderten Dokumentations- und Nachweispflichten beispielsweise durch Logfiles, Beitragszeiten in Foren und Berichtsabfragen auch in Echtzeit gewährleistet werden. Hierin unterscheidet sich ein LMS signifikant von anderen analogen oder konventionellen Lösungen.
Der bisherigen Argumentation folgend ist der Einsatz des hier beschriebenen LMS als ausbildungsrechtlich notwendige Infrastruktur zur Erfüllung schulischer Aufgaben zu verstehen. Die gesetzlich übertragene Verantwortung zur Koordination und Organisation der Ausbildung von Notfallsanitäterinnen und Notfallsanitätern lässt sich ohne ein entsprechendes System kaum mehr realisieren, insbesondere unter Berücksichtigung heutiger Möglichkeiten im digitalen Bildungsraum.

### 3.1.2 Didaktisch-strukturelle Verortung {#sec:DidaktischeVerortung}

Hier weiter mit Argumentation aus \hyperref[sec:Bildungswiss-Verortung]{Kapitel 2.1} fortführend.

Didaktische Rahmung
Schule = nicht nur juristische Instanz, sondern auch didaktisches Konstrukt
LMS = didaktische Infrastruktur, um Lernprozesse zwischen den Lernorten kohärent zu verknüpfen
Anschluss an Theoriekapitel (-> Bildung als Wirkgefüge / digitale Dispositive / Lernraumlogiken)

Table: Konsequenzen für das LMS innerhalb der rechtlich-funktionalen Rahmung \label{tab:lms-konsequenzen}

| Stichwort                                                                           | Erklärung                                                                                              | Quellenverweis                                                                    |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Verantwortung der Schule für Lernorttransfer\label{term:lernorttransfer}                                        | LMS als systemisches Steuerungsinstrument innerhalb der schulischen Gesamtverantwortung.               | § 5 (3) @bundesrepublik_deutschland_gesetz_2023; § 2 (1-3) @bmg_ausbildungs-_2023 |
| Aktive Begleitung durch Schule                                                      | LMS muss Funktionen für Reflexion, Kommunikation und Dokumentation der Praxisbegleitung bereitstellen. | § 2 (3) @bmg_ausbildungs-_2023                                                    |
| Strukturierte Zusammenarbeit zwischen Schule und praktischer Ausbildungseinrichtung | Erfordert Kommunikations- und Kooperationsfunktionen zwischen Schule und Praxispartnern.               | § 5 (3) @bundesrepublik_deutschland_gesetz_2023; § 2 (2-3) @bmg_ausbildungs-_2023 |
| Rechtsverbindlichkeit                                                               | LMS-Einsatz muss mit normativen Vorgaben vereinbar sein und Nachweismöglichkeiten bieten.              | § 11 @bundesrepublik_deutschland_gesetz_2023; Einleitung @bmg_ausbildungs-_2023   |
| Pädagogisch-didaktischer Anspruch steigt                                            | Komplexe didaktische Szenarien müssen abbildbar sein (z. B. Kompetenzraster, ePortfolio etc.).         | § 4 @bundesrepublik_deutschland_gesetz_2023; Anlage 1 @bmg_ausbildungs-_2023      |
| Qualitätssicherung durch digitale Unterstützung                                     | LMS muss evaluierbare und standardisierte Prozesse zur Qualitätssicherung ermöglichen.                 | Seite  44-45 @bundesgesundheitsministerium_referentenentwurf_2012                 |
| Anschlussfähigkeit an akademische Systeme                                           | LMS sollte Anschlussfähigkeit an hochschulische Systeme und Studiengänge berücksichtigen.              | @bundesgesundheitsministerium_gesundheitsberufe_2025                              |

```{=latex}
\tabsubcaption{Konsequenzen der rechtlich-funktionalen Rahmung für die LMS-Architektur. Zusammengeführt sind zentrale normative Anforderungen (u.a. NotSanG und Ausbildungs-/Prüfungsrahmen) und daraus abgeleitete Funktions- und Strukturbedarfe des Systems (Koordination der Lernorte, Dokumentation/Nachweis, Kommunikation, Qualitätssicherung).}
```


Weiter mit Schule

Weiter mit HRT

#todo (#37) Platzhalter-Notizen („Weiter mit …“) durch ausformulierte Abschnitte ersetzen: (a) schulische/organisationale Einbettung (Träger, Schule, Lernorte, Verantwortlichkeiten) und (b) HRT-spezifische Anforderungen (Entscheidungsdruck, Fehlerfolgen, Kompetenz-/Transferlogik) als Begründung der besonderen Kontextbedingungen des Untersuchungsfalls.




## 3.2 Entwicklung und Einbettung des LMS {#sec:Entwicklung-Einbettung}

Die Entwicklung und Einbettung des hier untersuchten Learning Management Systems erfolgte nicht als Reaktion auf äußere Anforderungen, sondern als systematische Auseinandersetzung mit den Herausforderungen einer digital gestützten Ausbildung im Gesundheitswesen. Die Konzeption entstand aus der Verbindung theoretischer Überlegungen, eigener empirischer Arbeiten sowie konkreter institutioneller Anforderungen im Rahmen der Einführung der dreijährigen Ausbildung von Notfallsanitäter*innen.
Die folgenden Abschnitte zeigen, wie sich das System von den ersten konzeptionellen Gedanken (3.2.1) über die schulische Implementierung (3.2.2) und dynamische Weiterentwicklung (3.2.3) bis zur empirischen Evaluation (3.2.4) konstituierte.

### 3.2.1 Entstehungskontext und konzeptionelle Grundlagen {#sec:Entstehung-Konzept}

#todo (#38) Redundanz vermeiden! Nur auf eigene Arbeiten beziehen, die in Kapitel 2 nicht behandelt wurden. 

Zentrale wissenschaftliche und konzeptionelle Grundlagen des hier untersuchten Learning Management Systems sind Ergebnisse aus eigenen Untersuchungen, inwiefern Einflussfaktoren Zeit, Struktur und Interaktion Effekte auf nachhaltiges Wissensmanagement durch Kollaborationstools haben, die anhand von selbstorganisierten Gruppenarbeitsergebnissen in der Qualifikation von Notfallsanitäterinnen und Notfallsanitätern evaluiert wurden [@hanisch_nachhaltiges_2017].

#todo (#39) Vor Finalisierung: RH1–RH3 klar als Hypothesen/Vorbefunde aus der Vorarbeit (nicht als Hypothesen der Dissertation) markieren; im Fließtext stärker die daraus abgeleitete Begründung für die Dissertation (Mechanismen/Wirkgefüge im LMS) betonen und ggf. Ergebnisse/Schlussfolgerungen vor die Hypothesenliste ziehen, um Verwirrung zu vermeiden.

In den eigenen Untersuchungen wurden drei Hypothesen geprüft, die sich auf die Effekte der Einflussfaktoren Zeit, Struktur und Interaktion auf nachhaltiges Wissensmanagement durch Kollaborationstools beziehen. Grundannahme war, dass Lernen in der Qualifikation von Notfallsanitäterinnen und Notfallsanitätern autopoietisch und selbstorganisiert verläuft (s. \hyperref[sec:Systemisch-konstruktivistische-Theorie]{Kapitel 2.1.2}), und dass insbesondere die zeitliche Verfügbarkeit von Lernergebnissen entscheidend für deren nachhaltige Aneignung ist [@hanisch_nachhaltiges_2017, Kapitel 3.4, Abbildung 2]:

- RH1, die zeitliche Erfassung und Verfügbarkeit betreffend, konnte deutlich bestätigt werden. Der höchste Effekt wurde für die Variable PV1b (Verfügbarkeit) mit einem Regressionskoeffizienten von β = -1,213 nachgewiesen.
- RH2 zur Struktur zeigte eine sehr hohe Korrelation (r = .942), der Einfluss auf das nachhaltige Wissensmanagement erwies sich jedoch als statistisch unplausibel hoch (β = 2,372) und wurde daher verworfen.
- Zwar wies die kollaborative Interaktion (RH3) die stärkste Korrelation mit dem Kriterium auf (r = .953), hatte jedoch mit β = .151 einen nur geringen Einfluss.

Die Ergebnisse der Hypothesenprüfung zeigen eine differenzierte Wirkung der untersuchten Einflussfaktoren auf nachhaltiges Wissensmanagement. Mit der zeitlichen Verfügbarkeit von Gruppenarbeitsergebnissen (RH1) als stärkstem Prädiktor lässt sich die Annahme bestätigen, dass das Wann der Ergebnissicherung ein zentraler Gelingensfaktor für nachhaltige Wissensprozesse ist. Die Verwerfung der Hypothese zur Sicherungsstruktur (RH2) deutet darauf hin, dass Strukturmerkmale zwar als relevant wahrgenommen, aber offenbar nicht lernwirksam erlebt wurden. Auch wenn die kollaborative Interaktion (RH3) die höchste Korrelation mit dem Kriterium aufwies, blieb ihr tatsächlicher Einfluss begrenzt. Dies ist möglicherweise die Folge fehlender Erfahrung oder unzureichender Umsetzung [@hanisch_nachhaltiges_2017, Kapitel 3.5].

+++++

Für die Rahmung dieser Ergebnisse muss berücksichtigt werden, dass die zugrunde liegende Untersuchung im Rahmen eines sechswöchigen Kursformats stattfand, das auf die staatliche Prüfung vorbereitete und sich deutlich vom Format einer dreijährigen Ausbildung unterscheidet. Die Kritik der Teilnehmenden bezog sich mehrfach auf die fehlende zeitliche Transparenz im Lernarrangement – insbesondere hinsichtlich der Verfügbarkeit gemeinsamer Arbeitsergebnisse. Hier zeigt sich, dass Zeit nicht nur ein didaktischer, sondern auch ein organisatorisch relevanter Faktor für nachhaltiges Lernen ist. Ein weiterer Blickwinkel ist die geringe Wirkung struktureller Einflussfaktoren, die darauf zurückzuführen sein könnte, dass die Teilnehmenden keine reale Anwendung strukturierter digitaler Werkzeuge erfahren hatten. Ihnen fehlte die Möglichkeit, mit kollaborativen Tools tatsächlich zu arbeiten – eine bloße Vorstellung davon reichte nicht aus, um deren Wirksamkeit einzuschätzen. Auch die Interaktion wurde weniger als gelebte Praxis, denn als wünschenswerte Möglichkeit beschrieben. Eigene Beobachtungen legen nahe, dass Teilnehmende Interaktion vor allem im Sinne einer expertengeleiteten Selbstvergewisserung verstehen, bspw. in einer Rückkopplung mit Prüfenden [@hanisch_nachhaltiges_2017, Seite 18–19].

Die Ergebnisse machen damit deutlich, dass die untersuchten Wirkfaktoren nicht methodisch irrelevant, sondern strukturell untererfüllt waren. Für die Konzeption und Konstruktion des hier untersuchten Learning-Management-Systems war es daher zentral, die identifizierten Kritikpunkte systematisch in die Weiterentwicklung einzubeziehen.

### 3.2.2 Implementierung in der schulseitigen Praxis {#sec:Implementierung-Schule}

Die konkrete Implementierung des hier untersuchten Learning Management Systems erfolgte ab dem Jahr 2016 im Zuge der Einführung der dreijährigen Ausbildung zur Notfallsanitäterin bzw. zum Notfallsanitäter an einer Rettungsdienstschule in Nordrhein-Westfalen. Im Unterschied zur vorherigen Rettungsassistentenausbildung bot sich hier erstmals die Möglichkeit, die Durchführung der Ausbildung auch digital zu gestalten. Zur Umsetzung gehörten einerseits die Abbildung der geltenden Lehrpläne, andererseits die systematische Nutzung von Wikis zur Sicherung von Gruppenarbeitsergebnissen, gerade vor dem Hintergrund der zuvor beschriebenen Untersuchungsergebnisse. Entscheidend für die Einführung eines Learning Management Systems war dabei nicht allein das Ziel, einen systematischen digitalen Zugang zu schaffen, sondern auch die persönlichen didaktischen Erfahrungen, die den Einsatz solcher Systeme im Sinne einer nachhaltigen Kompetenzentwicklung als sinnvoll erscheinen ließen. Die Rahmenbedingungen erwiesen sich insofern als günstig, als nicht nur eine hohe institutionelle Offenheit für digitale Lernprozesse, sondern auch ein spürbares persönliches Engagement seitens der Lehrkräfte und der Schulleitung gegeben war.

Initiativ in der Umsetzung war unter anderem die Verbindung eigener Studienleistungen im Bereich der Bildungswissenschaft an der FernUniversität in Hagen mit den curricularen Anforderungen vor Ort. Die FernUniversität hatte sich im Rahmen ihrer Lehre in den pädagogischen Feldern der Förderung digitaler Lehr-Lern-Formate verpflichtet, was eine hohe Affinität zu digitalen Medien im Ausbildungskontext begünstigte. Die Ausgangslage war dabei unter anderem durch die Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter sowie den Rahmenlehrplan Nordrhein-Westfalen geprägt. Aufgrund divergierender Anforderungen in diesen Dokumenten wurde ein schulinterner Lehrplan entworfen, der beide Vorgaben integrieren und curricular anschlussfähig machen sollte. In dieser Struktur wurde das Learning Management System verankert. Die Einführung erfolgte schrittweise, wobei zunächst grundlegende Funktionen im Vordergrund standen – insbesondere der Aufbau von Foren zur Begleitung von Handlungssituationen\label{term:handlungssituationen} sowie die Nutzung der Wiki-Funktionalität zur Strukturierung kollaborativer Aufgabenbearbeitung (\hyperref[sec:A-5]{Anhang A‑5}).

Als besonders hilfreich erwiesen sich die in den Jahren 2016 und 2017 regelmäßig durchgeführten sechswöchigen Vorbereitungskurse auf die staatliche Prüfung. Diese zeichneten sich durch eine hohe Zahl an Teilnehmenden und eine dadurch bedingte intensive Belastungssituation aus, in der das System auf seine technische und didaktische Belastbarkeit hin überprüft werden konnte. Die Erfahrungen aus diesen Kursen flossen unmittelbar in die Weiterentwicklung ein und ermöglichten somit eine erste fundierte Rückmeldung zur Frage, inwieweit digitale Systeme zur Begleitung, Strukturierung und Auswertung von Lernprozessen in hochverdichteten Ausbildungskontexten beitragen können.

### 3.2.3 Weiterentwicklung durch externe Anforderungen {#sec:Weiterentwicklung-extern}

Mit Beginn der pandemischen Lage im Frühjahr 2020 wurden auch für die Ausbildung in den Gesundheitsfachberufen einschneidende Maßnahmen erlassen. Der Erlass des Ministeriums für Arbeit, Gesundheit und Soziales des Landes Nordrhein-Westfalen sah eine Einstellung des regulären Unterrichtsbetriebs an Rettungsdienstschulen vor und empfahl zugleich die Entwicklung und Umsetzung digitaler Lehrformate zur Sicherung der Ausbildungskapazität [@schnabelin_masnahmen_2020]. Die bundesweite Verordnung zur Sicherung der Ausbildungen in den Gesundheitsfachberufen (EpiGesAusbSichV\label{term:epigesausbsichv}) konkretisierte wenig später, dass digitale Formate sowohl für den theoretischen als auch den praktischen Unterricht zulässig seien und entsprechend von den Schulen umgesetzt werden sollten [@bmg_verordnung_2020, § 2].

Die durch die Covid-19-Pandemie ausgelöste Umstellung auf digitalen Unterricht stellte auch für die hier untersuchte Schule eine Zäsur dar. Vor diesem Hintergrund wurde das bereits bestehende Learning Management System kurzfristig zur zentralen digitalen Infrastruktur weiterentwickelt. Wie @huber_covid-19_2020 im Rahmen des Schul-Barometers zeigen, waren insbesondere fehlende digitale Kompetenzen, unzureichende technische Ausstattung und mangelnde systemische Koordination zentrale Herausforderungen für viele Bildungseinrichtungen im deutschsprachigen Raum [@huber_covid-19_2020, Seite 30]. Im Gegensatz dazu konnte an der hier untersuchten Bildungseinrichtung auf eine bereits zuvor begonnene Systemstruktur zurückgegriffen werden (vgl. \hyperref[sec:Implementierung-Schule]{Kapitel 3.2.2}). Die pandemiebedingte Anforderung beschleunigte dabei nicht nur die Nutzung, sondern erforderte eine konkrete Systemanpassung. Innerhalb kürzester Zeit wurden u.a. 848 Aufgaben in 32 Handlungssituationen digital strukturiert, veröffentlicht und zugewiesen. Dies war insofern nur möglich, da die Entwicklung des Curriculums der Ausbildung von Notfallsanitäterinnen und Notfallsanitätern bereits durch die im vorherigen Kapitel beschriebenen Grundgedanken als digitale Realisierung mitgedacht wurde.

Rückblickend kann abgeleitet werden, dass die pandemiebedingten Einschränkungen nicht Auslöser, sondern vielmehr Katalysator für die vollständige Entfaltung des zuvor konzipierten Geflechts aus studentischen Leistungen, Curriculumsentwicklung sowie der Anlage des Learning Management Systems waren. Während viele Bildungseinrichtungen vor der Herausforderung standen, kurzfristig digitale Übergangslösungen zu implementieren @huber_covid-19_2020, konnte auf eine bereits didaktisch durchdachte und technisch vorbereitete Infrastruktur zurückgegriffen werden [@huber_covid-19_2020, Seite 34]. Demnach zeigte die im Kontext der Pandemie entstandene Notwendigkeit, sämtliche Lernprozesse digital zu strukturieren, sich damit nicht als Störung, sondern als Gelegenheit, in der das volle Potenzial des bereits vorhandenen Learning Management Systems sichtbar wurde. Die zuvor entwickelten Konzepte, Funktionen und strukturellen Entscheidungen konnten unter Realbedingungen erprobt, ausgeweitet und im laufenden Betrieb angepasst werden. Dieser Prozess ließ bereits erste Elemente einer systemischen Verstetigung erkennen.

Die retrospektive Einordnung dieser Weiterentwicklung verdeutlicht der Vergleich mit den Ergebnissen von @gachanja_e-learning_2021, die in ihrer Untersuchung die Pandemie als Übergangs- und Bewährungsphase, die Rolle bestehender Infrastruktur sowie die Institutional Readiness als Voraussetzung für gelingendes E-Learning betrachteten. In ihrer Studie zur Implementierung eines E-Learning-Kurses im medizinischen Bildungsbereich zeigen die Forschenden, dass der Übergang in digitale Lernsettings unter Krisenbedingungen oft zu Überlastung, technischen Ausfällen und geringer Beteiligung führt. Entscheidend für das Gelingen sei weniger die eingesetzte Plattform als vielmehr die institutionelle Vorbereitung und strukturelle Stabilität. Diese Beobachtungen lassen sich rückblickend auch für das hier untersuchte System bestätigen [@gachanja_e-learning_2021, Seite 3, 6].
Ein Vergleich zwischen den präventiven Gegebenheiten und den retrospektiven Erkenntnissen verdeutlicht Tabelle \ref{tab:lms-entwicklung}.

Table: Retrospektiv-vergleichende Darstellung der LMS-Entwicklung im Kontext pandemischer Umstellungen \label{tab:lms-entwicklung}

| Aspekt              | @gachanja_e-learning_2021                                                       | Hanisch (eig. Darstellung)                                                       |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Ausgangspunkt       | Unerwartete Umstellung auf E-Learning aufgrund pandemischer Vorgaben        | Bereits bestehendes LMS wird unter Pandemiebedingungen ausgebaut                 |
| Technische Ausstattung | Mangelhaft, v.a. Internetzugang und Serverleistung                         | Vollständige curricular-integrierte LMS-Struktur vorhanden                       |
| Systemstruktur      | Moodle ad hoc eingesetzt, mit starker Abhängigkeit vom Präsenzbetrieb       | Moodle bereits inhaltlich und organisatorisch vorbereitet                        |
| Herausforderungen    | Überforderung, fehlende Prüfungsformate, geringe Interaktion                | 848 Aufgaben, 32 Handlungssituationen, Wikis und Foren produktiv nutzbar         |
| Ergebnisbewertung   | LMS als Notlösung ohne nachhaltige Wirkung                                  | LMS als systemische Infrastruktur mit Verstetigungspotenzial                     |
| Schlüsselbedingung  | „Institutional readiness“ erforderlich für Erfolg                           | Vorbereitung ab 2016 als Fundament nicht-planbarer pandemischer Handlungsfähigkeit |

```{=latex}
\tabsubcaption{Retrospektiver Vergleich der pandemiebedingten LMS-Umstellung (Literaturbefund) mit der dokumentierten Systementwicklung im Rahmen der Notfallsanitäter-Ausbildung (2016--2023). Die Gegenüberstellung fokussiert Ausgangspunkt, Infrastrukturvoraussetzungen, Herausforderungen und Bewertung und dient der Einordnung der Pandemie als Katalysator bereits vorbereiteter Systemarchitektur.}
```

Während das bei @gachanja_e-learning_2021 untersuchte E-Learning-Modell unter Bedingungen einer ad-hoc eingeführten digitalen Infrastruktur umgesetzt wurde, basierte das hier untersuchte System auf einem längerfristig entwickelten, curricular integrierten und technisch stabilen Ansatz. Die Gegenüberstellung macht deutlich, dass institutionelle Vorbereitung, systemische Vordisposition und die frühzeitige Einbettung digitaler Lernprozesse entscheidende Erfolgsfaktoren für die Funktionsfähigkeit eines Learning Management Systems unter Belastungsbedingungen darstellen. Besonders hervorzuheben ist dabei der Unterschied in der Bewertung der eingesetzten Systeme selbst. Während @gachanja_e-learning_2021 das LMS als temporäre Notlösung wahrgenommen haben, war das hier untersuchte System als integraler Bestandteil der schulischen Infrastruktur aufgebaut. Es zeigte seine Wirkungsfähigkeit zur Verstetigung über die Krise hinaus.

Damit die hier geschilderte Nutzung auch außerhalb von Krisensituationen ihr Potenzial dauerhaft entfalten kann, wurden im hier beschriebenen Learning Management System turnusmäßig Evaluations- und Reflexionsschleifen eingeführt. Ziel dieser Maßnahme war diejenigen Verbesserungspotenziale zu identifizieren, die bereits durch kleinste Anpassungen wirksam werden konnten.

### 3.2.4 Evaluation und Reflexion {#sec:Evaluation-Reflexion}

Bereits in der hier mehrfach zitierten studentischen Ausgangsuntersuchung wurde der Versuch unternommen, die Wirkung des eingesetzten Learning Management Systems mithilfe des Evaluating Training Programs nach @kirkpatrick_evaluating_1998 zu evaluieren [@kirkpatrick_evaluating_1998]. Das vierstufige Modell mit den Ebenen Zufriedenheit, Lernen, Verhalten und Ergebnisse kann als Standardrahmen zur Bewertung von Trainingsmaßnahmen betrachtet und grundsätzlich auch auf Bildungsmaßnahmen in Heilberufen übertragen werden [@hanisch_nachhaltiges_2017, Seite 13]. Kirkpatrick\label{term:kirkpatrick-modell}s Modell wurde auf die Evaluation digital gestützter Gruppenarbeitsprozesse angewendet. Die Ergebnisse zeigten jedoch, dass die dort untersuchten Einflussfaktoren, insbesondere Zeit, Struktur und Interaktion, nicht trennscharf den vier Stufen zugeordnet werden konnten. Die Untersuchung wurde daher von einer stufenbasierten Lernbewertung weg, hin zu einer inhaltsbezogenen Wirkungsperspektive verlagert, bei der die nachhaltige Sicherung von Lernergebnissen im Mittelpunkt stand [@hanisch_nachhaltiges_2017, Seite 13–14, 20].

Aus dieser methodischen Einschränkung heraus wurde das Training Evaluation Inventory (TEI) nach @ritzmann_training_2014 als weiterführendes, geeignetes Instrument identifiziert und in den Folgejahren in die Ausbildungskonzeption inhaltlich und didaktisch integriert. Das TEI greift zentrale Gedanken Kirkpatricks auf und überträgt diese auf Kontexte, in denen High-Responsibility-Teams trainieren und agieren. Zugleich verbindet es diese Überlegungen mit einem empirisch überprüfbaren Fragebogeninstrument. Damit stellt das TEI die bisher einzig bekannte, systematisch anschlussfähige Möglichkeit dar, die Wirkung der im Learning Management System abgebildeten Handlungssituationen differenziert zu evaluieren.

Die Anwendung des TEI soll im organisationalen Alltag praktikabel sein und umfasst zehn Skalen mit insgesamt 53 Items, die die beiden zentralen Dimensionen wahrgenommene Trainingseffekte sowie didaktische Merkmale des Trainingsdesigns einbeziehen. Diese Kombination ermöglicht einerseits den Output eines Trainings zu erfassen, andererseits dessen didaktische Wirksamkeit zu analysieren. Ein in dem Kontext dieses Kapitels bedeutender Vorteil des TEI liegt in der Verknüpfung von Ergebnis- und Prozessdimensionen. Die Skalen zu Lernfreude, Nützlichkeit, Wissenszuwachs, Einstellung und Transfer erlauben die Erfassung kognitiver und affektiver Wirkungen. Die Designskalen beruhen auf den didaktischen Prinzipien Problemorientierung, Aktivierung, Demonstration, Anwendung und Integration. Diese Fünf-Punkte-Struktur folgt den Überlegungen von Merrill (2002) und erlaubt Rückschlüsse darauf, inwiefern angebotene Trainingsmaßnahmen wirksam oder unwirksam sind. Hervorzuheben ist hierbei, dass laut den Ergebnissen der Validierungsstudie insbesondere die Skalen „Demonstration“, „Anwendung“ und „Integration“ die stärksten Prädiktoren für positive Trainingseffekte darstellen. Die regelmäßige Anwendung des TEI nach jeder Handlungssituation im hier betrachteten LMS bringt genau diesen Mehrwert zur Geltung: Sie ermöglicht ein kontinuierliches Rückmeldesystem, das nicht nur eine summative Bewertung, sondern auch eine formative Rückkopplung auf Mikroebene bereitstellt. Die erhobenen Daten erlauben es, die Gestaltung einzelner Handlungssituationen gezielt anzupassen und schrittweise zu verbessern. Evaluation wird damit integraler Bestandteil der Systementwicklung. Die Autor*innen betonen selbst: „Evaluating the design features of training is important to shed light on the reasons why certain training outcome effects were produced“ [@ritzmann_training_2014, Seite 47] [@ritzmann_training_2014, Seite 43, 48, 62].

Der vielleicht stärkste Vorteil liegt in der Organisations- und Teilnehmendenfreundlichkeit des Instruments. Wie oben dargestellt, kann das TEI innerhalb der Ausbildungsstruktur angewendet werden, wobei die Bearbeitungsdauer im Durchschnitt weniger als zehn Minuten beträgt; eine regelmäßige und belastungsarme Anwendung auch im stark getakteten Ausbildungsgeschehen wird somit eingeräumt. Zudem wurde das TEI so konzipiert, dass dieses direkt nach einem Trainingselement angewendet werden kann, also ein Umstand, der die Anschlussfähigkeit an die Struktur der Handlungssituationen im Learning Management System zusätzlich erhöht. Die empirisch belegte interne Konsistenz der Skalen (Cronbachs α = .73–.89) und die faktorenanalytisch abgesicherte Skalenstruktur bestätigen die methodische Qualität [@ritzmann_training_2014, Seite 49, 55].

Mit der theoretischen Fundierung, empirischen Absicherung und praxisorientierten Anwendbarkeit stellt das TEI ein wissenschaftlich tragfähiges Instrument für die Evaluation in gesundheitsberuflichen Ausbildungsgängen dar. Insgesamt soll die regelmäßige Anwendung des TEI hier als strukturierte Reflexionsinstanz im digitalen Bildungsraum verstanden werden, die die Sicherung einer hohen lernprozessbegleitend Qualität, Optimierung der notwendigen und hilfreichen didaktische Maßnahmen gezielt und zugleich empirisch belastbare Rückschlüsse auf die Wirkung einzelner Handlungssituationen zu ziehen. Das Learning Management System wird dadurch nicht nur als rechtliches, inhaltliches oder technisches Steuerungsinstrument verwendet, sondern auch als Evaluationsträger und didaktisches Analysewerkzeug wirksam und trägt zugleich den besonderen Anforderungen der Ausbildung in den Heilberufen Rechnung. 

## 3.3 Didaktische Architektur als Learning-Environment {#sec:DidaktischeArchitektur}

Aufbauend auf den in \hyperref[sec:Kontext-FG]{Abschnitt 3.1} beschriebenen Entstehungskontext sowie den in \hyperref[sec:Entwicklung-Einbettung]{Abschnitt 3.2} weitergeführten Entwicklungsschritten wird im Folgenden die didaktische Architektur des Learning-Management-Systems vorgestellt. Diese Konzeption beabsichtigte eine digitale Struktur zu schaffen, die nicht nur rechtliche Anforderungen der Ausbildung abbildet, sondern auch die didaktischen Prinzipien systemisch fundierter Kompetenzentwicklung integriert. In dieser Phase entstand auch die in Abbildung 1 gezeigte Skizze zur didaktischen Systemstruktur, die den Anspruch veranschaulicht, aus ersten Überlegungen zur digitalen Unterstützung eine funktionsfähige und kohärente Lernumgebung zu entwickeln.
	 
Die Skizze dient im Folgenden als Referenzstruktur: Sie macht sichtbar, welche Architekturannahmen (Lernorte, Kurslogik, Aufgabenstruktur, Rückkopplung) den späteren Ausführungen zugrunde liegen, ohne bereits Details der späteren Umsetzung vorwegzunehmen.

Abbildung 1: Frühe Skizze zur didaktischen Systemstruktur (eig. Darstellung, 2016)

+++++ Abbildung 1 hier einfügen +++++

#todo (#40) Abbildung 1 ersetzen: tatsächliche Grafikdatei/Scan einbinden (inkl. Quelle/Datum), konsistente Caption + Subcaption (Was wird gezeigt? Warum ist sie für den Forschungsgegenstand relevant?).

Visualisiert wird der konzeptionelle Ausgangspunkt des hier beschriebenen Learning Management Systems. Die Skizze zeigt erste Überlegungen zur Verschränkung von Lernorten, Selbststeuerung und Aufgabenstruktur als Grundlage einer systemisch-konstruktivistisch orientierten Ausbildungsarchitektur.

Die Skizze bildete das konzeptionelle Fundament der ersten Entwicklungsphase und visualisiert die Idee, innerhalb eines digitalen Bildungsraums Handlungssituationen, Lernorte und Kursorganisation so miteinander zu verbinden, dass eine strukturierte und individuelle Kompetenzentwicklung möglich wird. Besonders herauszustellen ist dabei die Trennung zwischen inhaltlicher Struktur und organisatorischer Kurslogik, wodurch eine hohe Flexibilität bei gleichzeitiger Kohärenz erreicht werden sollte. Die frühe Berücksichtigung aller drei Lernorte sowie die intendierte Rückführung kursinterner Erkenntnisse in die übergeordneten Lerneinheiten legen den systemischen Anspruch dieser Struktur offen [@hanisch_wirkgefuge_2022, Abschnitt 2.3].

### 3.3.1 Konzeptionelle Grundkonstruktion {#sec:Grundkonstruktion}

Anfangs stand weniger ein fertiges Konzept als vielmehr die Idee eines Weges, der, inspiriert von der Vorstellung, eine Ausbildung zu entwickeln, die mit Haltung, Struktur und kontinuierlicher Entfaltung nicht nur Inhalte vermittelt, sondern berufliche Identität formt (i.A.a. [@miyamoto_buch_2005, Seite 64–69]). Diese Idee eines strukturierten und durchlässigen Pfads wurde zur Grundlage der didaktischen Systemstruktur und damit zur Ausgangsbasis für die Architektur des Learning Management Systems. Die Konzeption der Handlungssituationen als Kurseinheiten im LMS orientiert sich inhaltlich und strukturell am Rahmenlehrplan NRW\label{term:rahmenlehrplan-nrw} zur Ausbildung von Notfallsanitäter*innen, insbesondere an dessen systematischer Gliederung in insgesamt 10 Lernfelder [@mgpa_nrw_rahmenlehrplan_2016, Seite 3]. Diese Lernfelder beschreiben konkrete berufliche Anforderungen und bilden den Kern einer kompetenzorientierten Ausbildung, die durch die hier entwickelte, digitale Struktur diese Logik in ein modular aufgebautes, sequenziell organisiertes Kurssystem überträgt. So entstehen Handlungssituationen, die, ähnlich wie Etappen auf einem Weg, den Lernprozess begleiten, strukturieren und situativ adaptierbar machen Diese Vorstellung wird in Abbildung X („Trajektorie“) simuliert und visuell aufgegriffen (vgl. \hyperref[sec:Systemisch-konstruktivistische-Theorie]{Abschnitt 2.1.2}).
In dieser Form ist das Learning Management System nicht nur ein digitales Abbild der Ausbildung, sondern die konkrete Umsetzung eines pädagogischen Weges, der systemisch gedacht, curricular verankert und lernprozessbezogen gestaltet ist. Auf Grundlage der in \hyperref[sec:Bildungswiss-Verortung]{Abschnitt 2.1} dargestellten didaktischen Paradigmen wurden zunächst die im Lehrplan als „erwünschte Wirkung“ bezeichneten Kompetenzbeschreibungen in das Kompetenzraster des Learning Management Systems übertragen. Darauf aufbauend erfolgte die systematische Zuordnung der in \hyperref[sec:Implementierung-Schule]{Abschnitt 3.2.2} erwähnten handlungsleitenden Aufgaben, die bereits im Lehrplan mediendidaktisch formuliert vorlagen, zu den jeweiligen Handlungssituationen innerhalb der Kursstruktur. Auf diese Weise entstand eine digitale Architektur, die curriculare Kompetenzziele mit konkreten Lernhandlungen verbindet – strukturiert, adressierbar und systematisch verknüpft mit den drei Lernorten Schule, Lehrrettungswache und Krankenhaus.
Das didaktisch-digitale Fundament des hier skizzierten Learning Management Systems bilden 32 Kurse, die, wie Abbildung 2 verdeutlicht, als „Handlungssituationen im Gesundheitswesen“ die gesamten inhaltlichen Dimensionen der Lernfelder des Rahmenlehrplans NRW abbilden. Ergänzend wird pro Ausbildungskurs eine kursinterne Umgebung zur Verfügung gestellt, in der die individuellen Erkenntnisse und Arbeitsergebnisse der jeweiligen Kohorte gesichert und dokumentiert werden können. Besonders an dieser Organisationsform ist die bewusste Trennung zwischen inhaltlicher Struktur und organisatorischer Kurslogik, wodurch eine hohe Flexibilität entsteht, innerhalb derer Lernende bei der Absolvierung oder Wiederholung einzelner Ausbildungsabschnitte gezielt an ihre individuellen fachlich-inhaltlichen Lernstände anknüpfen können, ohne die Kohärenz der Gesamtstruktur zu verlieren.

Die konzeptionelle Grundstruktur des LMS wird in Abb.~\ref{fig:modell_LMS} als Schema visualisiert.

\begin{figure}[H]
\centering
\begin{tikzpicture}[
  node distance=1.4cm and 2.0cm,
  process/.style={rectangle, rounded corners, draw, align=center, minimum width=3.4cm, minimum height=1.1cm, fill=gray!10},
  flow/.style={-Stealth, thick}
]
\node[process] (curriculum) {Handlungssituationen\\(32 curriculare Einheiten)};
\node[process, right=of curriculum, xshift=1.4cm] (lms) {LMS-Kern\\Kurse, Ressourcen, Aufgaben, Feedback};
\node[process, right=of lms, xshift=1.4cm] (cohort) {Ausbildungskurse\\(3 Kohortenräume)};
\node[process, above=of lms] (content) {Content\\Fachliteratur, Medien};
\node[process, below=of lms] (lernorte) {Lernorte\\Schule, Lehrrettungswache, Krankenhaus};

\draw[flow] (curriculum) -- node[above, align=center]{curriculare Struktur} (lms);
\draw[flow] (lms) -- node[above, align=center]{Umsetzung \& Steuerung} (cohort);
\draw[flow, bend left=18] (cohort) to node[above]{Erkenntnisse, Feedback} (curriculum);
\draw[flow, bend left=18] (curriculum) to node[below]{Aufgaben, Standards} (cohort);
\draw[flow] (content) -- node[right]{Materialien} (lms);
\draw[flow] (lernorte) -- node[right]{Praxisimpulse} (lms);
\draw[flow, dashed] (lernorte) -- node[below, align=center]{Koordination} (cohort);
\draw[flow, dashed] (lernorte) -- node[below, align=center]{Anforderungen} (curriculum);
\end{tikzpicture}
\caption{Systemisches Modell des eingesetzten Learning Management Systems mit Rückkopplung zwischen curricularen Handlungssituationen, LMS-Kern und kohortenspezifischen Ausbildungskursen.}
\label{fig:modell_LMS}
\end{figure}

Die Struktur trennt curricular-inhaltliche Handlungssituationen ($n = 32$) von kohortenspezifischen Ausbildungskursen ($n = 3$). Diese Trennung ermöglicht eine flexible, aber kohärente Lernumgebung, in der individuelle Erkenntnisse aus kursinternen Prozessen systematisch in die übergeordnete Handlungsebene zurückgeführt werden können.

Durch diese Gestaltung verbinden alle drei an der Ausbildung beteiligten Lernorte (Lehrrettungswache, Notfallsanitäterschule und Krankenhaus) gemäß der Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter in den Kursen der Handlungssituationen als interne und externe Akteure (§ 3 i.V.m. Anlage 1-3 NotSan-APrV\label{term:notsan-aprv}, 2023). Auf diese Weise wird die Gesamtheit der Personen, die eine unmittelbare Verantwortung für die Begleitung der jeweiligen Schülerinnen und Schüler übernommen haben, in alle Kurse eingetragen. Infolgedessen stehen für die inhaltlich-fachliche Ausbildung mehr Ressourcen zur Verfügung. Zugleich kann die administrativ-organisatorische Ressourcenbereitstellung bewusst pro Ausbildungskurs erfolgen. Ferner ist die zur Verfügungstellung passender Inhalte möglich, die nur einen Ausbildungskurs betreffen. Die Erkenntnisse aus den Arbeitsergebnissen der kursinternen Aufgabenbearbeitung fließen wiederum in die jeweilige Handlungssituation zurück. Damit entsteht eine hohe Durchlässigkeit von Erfahrungen und Erkenntnissen – sowohl in Richtung eines spezifischen Kurses als auch in Richtung der übergeordneten Handlungssituationen. Die Möglichkeit der Anwendung liegt in der Gestaltung von Rahmenbedingungen, die den unmittelbaren Lernort-Transfer (Lehrrettungswache – Notfallsanitäterschule – Krankenhaus) durch die Verschränkung der Lernorte sowie den damit verknüpften Erfahrungsaustausch und Erkenntnisgewinn systematisch sicherstellen.
Abbildung 3 visualisiert die integrative Architektur des hier beschriebenen Learning Management Systems. Im Zentrum steht die funktionale Verknüpfung zweier Struktureinheiten: Handlungssituationen als inhaltlich-didaktische Strukturelemente (untere Ebene) und Ausbildungskurse als organisatorisch-administrative Einheiten (obere Ebene). Beide Einheiten sind nicht hierarchisch, sondern wechselseitig bezogen. Inhalte und Erkenntnisse aus den kursinternen Lernprozessen fließen in die Handlungssituationen zurück, während die Handlungssituationen den curricularen Rahmen für die Ausbildungskurse bilden. Diese Rückkopplung wurde in den vorhergehenden Abschnitten als Durchlässigkeit zwischen Struktur- und Anwendungsebene beschrieben.

Abbildung 3:  Integrative Architektur des Learning Management Systems (eig. Darstellung).

+++++ Abbildung 3 hier einfügen +++++

Die Handlungssituationen (n = 32) bilden die curricular-inhaltliche Struktur gemäß Rahmenlehrplan NRW ab und bestehen aus standardisierten didaktischen Containern (Einführung, Ressourcen, Aufgaben, weiterführende Quellen, Lounge, Feedback, Organisation). Die Ausbildungskurse (n = 3) dienen der kohortenspezifischen Organisation und individuellen Ergebnissicherung. Content und Lernorte wirken wechselseitig auf die Handlungssituationen ein und sichern die curricular verankerte Theorie-Praxis-Verknüpfung im digitalen Raum.

Jede Handlungssituation besteht aus einem wiederkehrenden Satz von didaktisch strukturierten Containern: Einführung, Ressourcen, Aufgaben, weiterführende Quellen, Lounge, Feedback und Organisation. Diese Container wurden hier bereits als das organisationale, digitale Fundament, und damit als Trägerelemente der Aufgabenlogik beschrieben und bilden die standardisierte Grundlage für die Bearbeitung durch die Lernenden. Die Ausbildungskurse dagegen dienen der kohortenspezifischen Dokumentation, Reflexion und Organisation und sind der Ort für kursinterne Bearbeitung, individuelle Ergebnisfesthaltung und administrative Steuerung.
Die äußeren Bereiche, Content auf der linken und Lernorte auf der rechten Seite, bilden die beiden zentralen Bezugsrahmen des digitalen Bildungsraums. Content umfasst bspw. Fachliteratur, Theoriegrundlagen und didaktische Ressourcen, Lernorte stehen für die in § 3 i.V.m. Anlage 1–3 NotSan-APrV festgelegten Ausbildungseinrichtungen Lehrrettungswache, Notfallsanitäterschule und Krankenhaus. Die Pfeilführung in der Abbildung verdeutlicht, dass beide Bereiche nicht statisch sind, sondern aktiv in die Handlungssituationen hineinwirken und gleichzeitig von dort Erkenntnisse und Rückmeldungen zurückerhalten – ein zentrales Prinzip des hier beschriebenen Lernraums.
Anhand von Abbildung 4 lässt sich die exemplarische Anwendung der zuvor beschriebenen didaktischen Architektur verdeutlichen, in der die theoretischen Überlegungen in die Kursansicht überführt wurden, die allen im Rahmen der beruflichen Qualifikation genutzten Kurse zugrunde liegt.

Die folgende Abbildung verdeutlicht als Dokumentation die operativen Rahmenbedingungen des Wirkgefüges und Sie zeigt, welche standardisierte Kursstruktur Lernhandlungen, Navigation und Rückkopplung im System notwednigerweise technisch ermöglichend berücksichtig werden müssen. Ursprung dieser Darstellung ist die eigene Moodle-Instanz, die als technisches Fundament des hier beschriebenen Learning Management Systems dient.

Abbildung 4: Exemplarische Kursansicht im Learning Management System (eigene Moodle-Instanz)

#todo (#41) Abbildung 4 hier einfügen

Die Darstellung zeigt die standardisierte Containerstruktur, bestehend aus den Bereichen Einführung, Ressourcen, Aufgaben, Ergebnissicherung, weiterführende Quellen, Lounge, Feedback und Organisation mit den jeweils zugeordneten Aktivitäten und Materialien. Diese Struktur dient der konsistenten Gestaltung aller Handlungssituationen.

Sichtbar werden die strukturierten Inhaltsbereiche, die für alle Kurse einheitlich implementiert wurden und den Rahmen für lernprozessbegleitende Navigation, Dokumentation und Kommunikation bilden.

### 3.3.2 Didaktisch-architektonische Umsetzung {#sec:DidaktischeUmsetzung}

Die didaktische Umsetzung innerhalb des Learning Management Systems erfolgt auf Basis einer modularen Containerstruktur, die in sämtlichen Handlungssituationen identisch aufgebaut ist und sowohl Orientierung als auch didaktische Kohärenz gewährleisten soll. Diese Struktur basiert auf sieben wiederkehrenden Inhaltsbereichen, die den curricularen Anforderungen der Ausbildung entsprechen und zugleich eine lernlogische Sequenz abbilden. Im Folgenden werden diese zentralen Container exemplarisch dargestellt.
Einführung
Die Einführung dient der strukturellen Rahmung jeder Handlungssituation. Hier werden zentrale Informationen zur Kursleitung, zur Zielstellung der Lerneinheit sowie zur curricularen Verortung innerhalb der Ausbildung bereitgestellt. Ergänzt werden diese Angaben durch Hinweise auf spezifische Aufgabenformate, organisatorische Besonderheiten oder den Stellenwert der Einheit im Gesamtkontext der beruflichen Qualifikation. Dier Bereich vermittelt den Lernenden eine erste inhaltliche Orientierung, schafft Ziel- und Aufgabenklarheit und ermöglicht einen sicheren Einstieg in die digitale Lernsituation. Die Einführung ist damit zugleich das Begrüßungs-, Struktur- und Verortungsmodul, welches den Übergang zwischen physischer und digitaler Lernwelt begleitet.

Abbildung 5: LMS Kurs Einführung (eig. Darstellung)

#todo (#42): Abbildung einfügen prüfen

Die Abbildung zeigt die strukturelle Umsetzung des Containers „Einführung“, der grundlegende Informationen zur Kursleitung, Zielstellung und Orientierung innerhalb des Ausbildungsgangs bereitstellt.

Abbildung 5 zeigt exemplarisch die Umsetzung des Einführungskontextes innerhalb des Learning Management Systems. Sichtbar sind Begrüßungstext, Verantwortlichkeiten, sowie erste Hinweise auf den thematischen Zuschnitt und die Bedeutung der Einführungseinheit.
Ressourcen
Der Container in Abbildung 6 stellt zentrale Materialien zur Verfügung, die für die inhaltliche Bearbeitung der Aufgabenstellungen erforderlich sind. Dazu zählen grundlegende Fachliteratur, Orientierungshilfen, strukturelle Vorlagen, externe Verlinkungen und thematisch einschlägige Hintergrundmaterialien. Die Auswahl erfolgt dabei gezielt auf Grundlage curricular definierter Kompetenzanforderungen und orientiert sich an der im Rahmenlehrplan vorgesehenen inhaltlichen Tiefe der jeweiligen Lerneinheit.

Abbildung 6: LMS Kurs Ressourcen (eig. Darstellung)

#todo (#43): Abbildung einfügen prüfen

Die Abbildung zeigt die Bereitstellung zentraler Lernmaterialien in strukturierter Form. Die Materialien orientieren sich an curricularen Kompetenzanforderungen und bilden die inhaltliche Grundlage für die Bearbeitung der Aufgaben innerhalb der jeweiligen Handlungssituation.

Aus didaktischer Perspektive erfüllen die Ressourcen zwei Funktionen. Einerseits stehen sie als inhaltlicher Ausgangspunkt für die selbstständige Aufgabenbearbeitung, andererseits ermöglichen sie eine inhaltlich fundierte Auseinandersetzung mit den relevanten berufspraktischen Themen. Insofern korrespondieren die Ressourcen in direkter Linie zur Prüfungsvorbereitung und markieren den Bereich, in dem aus curricularer Tiefe prüfungsrelevante Breite wird. Die Relevanz dieser Materialien ergibt sich insbesondere aus der in \hyperref[sec:Pruefungsarchitektur]{Abschnitt 3.3.3} beschriebenen Konzeption der Aufgabenformate, die sich wiederum an dem in \hyperref[sec:RechtlicheRahmung]{Abschnitt 3.1.1} dargestellte Ausbildungsziel orientiert. Demzufolge trägt die geplante Bereitstellung dieser Ressourcen dazu bei, sowohl Transparenz über zu erwerbende Kompetenzen herzustellen als auch die strukturelle Prüfungsrelevanz für die Auszubildenden nachvollziehbar zu gestalten.
Aufgaben
Als didaktisches Kernstück jeder Handlungssituation im Learning Management System bauen die Aufgaben stets auf den rechtlich vorgegebenen Ausbildungsinhalten auf und werden aus diesen grundsätzlich abgeleitet. Sie sind handlungsorientiert formuliert, werden durch die Nutzung der Einsatzberichte (vgl. \hyperref[sec:E-Portfolio]{Abschnitt 3.5}) auf konkrete berufliche Problemstellungen bezogen und greifen die Struktur der jeweiligen Lernsituation auf, wie sie durch die curricularen Vorgaben der Ausbildungs- und Prüfungsverordnung sowie den Rahmenlehrplan definiert ist. Infolgedessen ermöglichen die Aufgaben eine direkte Verknüpfung zwischen beruflicher Handlungspraxis und digitaler Aufgabenbearbeitung; ein zentraler Aspekt, der im Bereich des Feedbacks durch die eigene Evaluation (vgl. \hyperref[sec:Evaluation-Reflexion]{Abschnitt 3.2.4}) aufgegriffen wird.
Die Aufgabenstellungen werden durch didaktisch begründete Operatoren formuliert, die eine transparente und kompetenzorientierte Anforderungsstruktur gewährleisten und sich an der Kompetenzstufung orientieren. Die Aufgaben, wie sie in Abbildung 7 präsentiert werden, sind so gestaltet, dass sie sowohl die eigenständige Auseinandersetzung mit fachlichen Inhalten als auch kooperative Bearbeitungsformen der Akteure ermöglichen. Zudem wird dieser Abschnitt durch ein Bearbeitungsforum ergänzt, das den Austausch von Ideen fördert und Reflexionsprozesse anregt.

Abbildung 7: LMS Kurs Aufgaben (eig. Darstellung)

#todo (#44): Abbildung einfügen prüfen

Die Abbildung zeigt beispielhafte Aufgabenformate zur Bearbeitung beruflicher Handlungssituationen. Operatoren und strukturierte Aufgabenbereiche ermöglichen eine kompetenzorientierte Formulierung und eine praxisnahe Umsetzung curricularer Anforderungen.
Die lernleitenden Aufgaben sind inhaltlich eng mit den bereitgestellten Ressourcen verknüpft, was in der Regel durch die Quellenangaben bei der Aufgabendarlegung gewährleistet wird. Eine beispielhafte Aufgabenstellung lautet bspw. in der beruflichen Handlungssituation 1: Einführung in die Berufsausbildung Notfallsanitäter (Hanisch-Johannsen [@hanisch-johannsen_nfs-h-01_2025]):
„Beschreibe bitte die Maßnahmen, die du eigenverantwortlich als Notfallsanitäter:in durchführen musst, vor allem in Bezug auf die Anforderungen des Notfallsanitätergesetzes §4 und der Ausbildungs- und Prüfungsverordnung für Notfallsanitäter:innen (Anlage 1). Denke dabei an die Ausbildungsziele als Notfallsanitäter:in.
Bitte nenne die Quellen, die du zur Bearbeitung verwendet hast.“
Inhaltliche Ergebnisse und die dazugehörigen Erkenntnisse aus der Bearbeitung der Aufgaben werden in der Ergebnissicherung zusammengeführt und für alle weiteren Bearbeitungsschritte kuratiert.
Ergebnissicherung
Die Ergebnissicherung ist der didaktisch-strukturelle Abschluss jeder Handlungssituation im Learning Management System. Sie ist die Schnittstelle zwischen Lernprozess, Reflexion und systemischer Rückmeldung. Häufig als Aktivitäten von Wikis, Glossaren oder Präsentationen konzipiert, werden hier Arbeitsergebnisse aus den Lernphasen dokumentiert, verdichtet und für anschließende Lernprozesse zugänglich gemacht. Perspektivisch ist eine Ausweitung der Ergebnissicherung über Jahrgänge hinweg vorgesehen, um die Reflexionsprozesse kohortenübergreifend zu fördern und das Prinzip einer lernenden Organisation strukturell zu implementieren. Die empirische Bedeutung dieser Ergebnisse wurde bereits in Abschnitt 3.2 ausführlich dargestellt. Dort konnte auf Basis der eigenen Evaluation [@hanisch_nachhaltiges_2017] gezeigt werden, dass insbesondere der Zeitpunkt der Erfassung und Verfügbarkeit einen signifikanten Einfluss auf die Nachhaltigkeit des Wissensmanagements hat. Darüber hinaus wurde deutlich, dass strukturierte, interaktive und reflexive Formate der Ergebnissicherung nicht nur dokumentieren, sondern aktiv zur Kompetenzentwicklung beitragen. Die Ergebnissicherung wie in Abbildung 8 dargestellt, ist somit nicht bloß Abschluss einer Handlungssituation, sondern Teil eines zyklischen und systemisch eingebetteten Lernprozesses.

Abbildung 8: LMS Kurs Ergebnissicherung (eig. Darstellung)

#todo (#45): Abbildung einfügen prüfen

Die Darstellung zeigt die zentralen Elemente der Ergebnissicherung in einem Handlungssituationskurs: ein Wiki und ein Glossar dienen der kollaborativen Dokumentation und Strukturierung von Lernergebnissen. Beide Aktivitäten stehen exemplarisch für die systematische Umsetzung der in Abschnitt 3.2 empirisch begründeten Forderung nach zeitnaher, zugänglicher und formativ nutzbarer Ergebnissicherung im digitalen Bildungsraum.

Die Ergebnissicherung stellt damit die didaktische Umsetzung der aus vorherigen Untersuchungen hervorgegangenen Forderung dar, Evaluationsergebnisse umzusetzen und einzubetten. Sie implementiert ein standardisiertes Vorgehen, das die Erkenntnisse von Hanisch [@hanisch_nachhaltiges_2017, Seite 19–20] berücksichtigt.

Weiterführende Quellen

Dieser Container bietet zusätzliche Materialien, die das Verständnis vertiefen, den Kontext erweitern oder das Wissen ergänzen. Er zielt darauf ab, die Lernsituation über den unmittelbaren Aufgabenhorizont hinaus zu öffnen. Die weiterführenden Quellen sind bislang jedoch noch unzureichend ausgearbeitet und müssen in Funktion sowie didaktischer Ausrichtung systematisch neu organisiert werden. Wie in Abbildung 9 aufgezeigt, soll jene Aktivitäten und Materialien sammeln, die über die curricular angebundenen Ressourcen hinausgehen. Während die Ressourcen auf verpflichtende, direkt zugeordnete Inhalte fokussieren, enthalten die weiterführenden Quellen kontextualisierende, aktualisierende oder reflexionsfördernde Inhalte, die eigenständige Wissensprozesse anregen und vertiefen. Damit wird sichergestellt, dass einerseits aktuelle, wissenschaftlich begründete Literatur zur Verfügung steht und andererseits Transferleistungen möglich werden, die im Sinne der NotSan-APrV  den Anforderungen in besonderem Maß entsprechen (§ 8 NotSan-APrV, 2023). Diese Verankerung ist insbesondere mit Blick auf prüfungsrelevante Anforderungen von Bedeutung. Die Bereitstellung aktueller, evidenzbasierter und interdisziplinärer Quellen eröffnet Lernenden die Möglichkeit, über den Pflichtstoff hinausgehende Leistungen zu erbringen, d.h. als ein zentrales Kriterium für die Erreichung der Bestnote. Gleichzeitig adressiert dieser Bereich Anforderungen an Transferkompetenz und wissenschaftliches Arbeiten, die explizit als „allgemein“ anerkannter Stand „rettungsdienstlicher, medizinischer und weiterer bezugswissenschaftlicher Erkenntnisse“ (§ 2 NotSan-APrV, 2023) gefordert werden.

#todo (#46): die neue Entwicklung einführen, d.h. das Forum etc.

Abbildung 9: LMS Kurs Weiterführende Quellen (eig. Darstellung)

#todo (#47): Abbildung einfügen prüfen

Der Container „Weiterführende Quellen“ enthält eine strukturierte Sammlung ergänzender Literatur, Datenbanken und wissenschaftlicher Ressourcen zur Vertiefung und Kontextualisierung der Lerninhalte. Die Auswahl umfasst fachliche Leitlinien, Verzeichnisse medizinischer Fachgesellschaften, Plattformen für wissenschaftliches Arbeiten sowie kuratierte Blogs und evidenzbasierte Onlineportale. Die Liste ist dynamisch angelegt und kann im Sinne einer lernenden Organisation durch die Lernenden fortlaufend erweitert werden. Ziel ist die Förderung wissenschaftsorientierter Transferleistungen im Sinne einer prüfungsrelevanten Vertiefung gemäß § 8 NotSan-APrV.

Einschränkend muss derzeit konstatiert werden, dass bislang noch kein schlüssiges Verfahren vorliegt, um zu bestimmen, welche Quellen in diesen Container aufgenommen werden oder unter welchen Bedingungen dies ggf. im Peer-Review-Verfahren erfolgt. Die Herausforderung der Zukunft besteht darin, klare Kriterien zu entwickeln und ein transparentes Verfahren zur evidenten Integration solcher Quellen zu etablieren.
Der Container weiterführende Quellen trägt somit zur Erweiterung des individuellen Lernhorizonts bei und bewirkt zugleich eine strukturelle Voraussetzung für eine differenzierte Leistungsbewertung im Sinne evidenzbasierten Handelns.

Lounge
Als digitaler Kommunikationsraum stellt die Lounge einen informellen Austauschbereich dar, in dem Fragen, Hinweise, aber auch erfahrungsbasierte Reflexionen unter den Lernenden und Lehrenden geteilt werden können. Die Lounge ist als niedrigschwelliger Einstiegspunkt in kooperatives Lernen gedacht. Hier das prägnante Beispile, weshalb die Ahrl von Begriffen bedeutsam erscheint: Lounge erzeugt Assoziationen, die in dder Wahrnemungspsychologie ableitbare Wirkungen erzeugt (vgl. \hyperref[sec:PadagogischPsychologischeGrundannahmen]{Abschnitt 2.2}).
Feedback und Evaluation
Dieser Bereich unterstützt bei der formativen Rückmeldung. Im LMS ist hierfür ein Kursfeedback- bzw. Evaluationsbereich vorgesehen, der sich am Training Evaluation Inventory (TEI)\label{term:tei} als strukturiertem Rahmen orientiert und Rückmeldungen sowohl zur didaktischen Gestaltung als auch zu wahrgenommenen Trainingseffekten ermöglicht. Der Feedbackbereich eröffnet zudem offene Rückmeldungen zur jeweiligen Handlungssituation.

Alle hier dargestellten Elemente sind zudem mit dem Kompetenzraster verbunden, welches

#todo (#48): Kompetenzraster ausführlich beschreiben.

Diese Verbindung stellt sicher, dass alle didaktischen Maßnahmen und curricularen Strukturen systematisch auf die im Kompetenzraster definierten Lernziele ausgerichtet sind.


### 3.3.3 Prüfungsarchitektur {#sec:Pruefungsarchitektur}

Text

### 3.3.4 Statistische Analyse curriculare Struktur {#sec:CurriculareAnalyse}

Dieser Abschnitt ist als empirischer Kurzbeitrag im Stil wissenschaftlicher Studien angelegt und analysiert die curriculare Struktur des digitalen Bildungsraums „NFS-H“ mit dem Ziel, die empirische Nachvollziehbarkeit, interne Konsistenz und regulatorische Anschlussfähigkeit des Kursplans quantitativ zu überprüfen. Damit wird gezeigt, dass der zugrunde liegende Lehrplan nicht nur konzeptionell schlüssig, sondern auch datenbasiert strukturiert ist. Die vorliegende Analyse orientiert sich eng an zentralen Prinzipien der Curriculumsforschung. Sie greift das Konzept des Curriculum Alignment\label{term:curriculum-alignment} (Biggs, 1996, S. 360–361) auf, das die Passung zwischen Lernzielen, Prüfungsanforderungen und curricularer Struktur thematisiert. Darüber hinaus folgt sie dem Ansatz des Programmatic Assessment\label{term:programmatic-assessment} (vgl. [@van_der_vleuten_model_2012], Abschnitt „Principles of assessment“), der die Konsistenz über multiple curriculare Elemente hinweg betont. Schließlich wird durch die systematische Quantifizierung didaktischer Strukturen ein Beitrag zur datenbasierten Modellierung von Bildungsarchitekturen geleistet. Die methodische Umsetzung über algorithmische Kürzelzuordnung, statistische Auswertung und Visualisierung stellt einen erweiterten Zugang dar, um curriculare Kohärenz empirisch zu fundieren, was insbesondere im Kontext digitaler Bildungsräume im Gesundheitswesen bedeutsam erscheint.

Zielstellung

Die statistische Analyse untersucht, inwiefern das hinterlegte Curriculum durchgängig den Anforderungen an Validität, Reliabilität und Konsistenz genügt. Die 32 digital abgebildeten Handlungssituationen („NFS-H-Kurse“) werden entlang der Anlage 1 NotSan-APrV strukturell ausgewertet. Im Fokus stehen dabei die empirische Zuordnung zu Themenbereichen und Kompetenzfeldern, die Vergleichbarkeit mit den APrV-Vorgaben sowie die statistische Konsistenz der curricularen Struktur. (Hanisch-Johannsen, 2025c)

Methodik

Die 32 Kurse sind automatisiert mit Python und Pandas analysiert worden. Die APrV-Kürzel aus der Datei ‚lms-verteilung.xlsx‘ dienen dabei als Referenzbasis. Jedes dieser Kürzel ist anhand der Datei ‚APrV-Kuerzel_zu_Kompetenzbereichen.csv‘ eindeutig einem der drei Themenbereiche (medizinisch, rettungsdienstlich, bezugswissenschaftlich) und einem von vier Kompetenzfeldern (fachlich, sozial, personal, methodisch) zugeordnet (i.A.a. Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 47). Für jede Handlungssituation wurden die relativen Anteile der Kürzel berechnet und der jeweils dominierende Bereich daraus abgeleitet. (Hanisch-Johannsen, 2025c)

Berechnung und Visualisierung

Als Analyseschritte folgten:

1.	Ermittlung der Korrelation zwischen Aufgabenanzahl und Kursdauer (r = 0,66) zur Prüfung innerer Konsistenz.
2.	Gruppierung nach Themenbereich: Mittelwert, Median und Standardabweichung für Aufgabenanzahl und Dauer.
3.	Kompetenzbereichszuordnung auf Basis aggregierter Kürzelverteilung.
4.	Visualisierung der Verteilungen über Boxplots.
5.	Vergleich zwischen APrV-Vorgaben und empirischer Struktur durch Gegenüberstellung in Säulen- und Tortendiagrammen.

Ergebnisse

Die statistische Analyse der 32 Kurse liefert differenzierte Kennzahlen zur inhaltlichen Gewichtung nach Themenbereichen:

•	Bezugswissenschaftlich: 13 Kurse, Ø Dauer = 21,3 Tage, Ø Aufgaben = 21,7
•	Medizinisch: 12 Kurse, Ø Dauer = 27,2 Tage, Ø Aufgaben = 26,8
•	Rettungsdienstlich: 7 Kurse, Ø Dauer = 57,0 Tage, Ø Aufgaben = 33,3
•	Einweisung/Prüfung (Sonderkategorie): 2 Kurse, getrennt ausgewertet

Diese Ergebnisse zeigen eine auffällige inhaltliche Kongruenz mit der Stundenverteilung der Anlage 1 NotSan-APrV (vgl. Abbildung 8):

•	Rettungsdienstlich: 47 % (APrV) vs. empirisch Ø 57,0 Tage (höchster Kursmittelwert)
•	Medizinisch: 27 % (APrV) vs. Ø 27,2 Tage (nächsthöherer Mittelwert)
•	Bezugswissenschaftlich: 26 % (APrV) vs. Ø 21,3 Tage

Auch die Verteilung der Kompetenzbereiche (vgl. Abbildung 9) wurde rekonstruiert und grafisch aufbereitet. Die direkte Gegenüberstellung der empirischen Anteile mit der APrV-Gewichtung ist in Abbildung 10 und Abbildung 11) als Balkendiagramm dargestellt. Die Aufgabenverteilung (Ø 21,7 / 26,8 / 33,3) wurde in Abbildung 12 visualisiert und die Dauerverteilung findet sich in Abbildung 13.

Abbildung 10: Anteil der Themenbereiche nach APrV (eig. Darstellung)

#todo (#49): Abbildung einfügen

Die Abbildung  visualisiert die prozentuale Verteilung der inhaltlichen Themenbereiche gemäß Anlage 1 der Ausbildungs- und Prüfungsverordnung für Notfallsanitäter*innen (NotSan-APrV). Diese drei Themenbereiche – medizinisch (27 %), rettungsdienstlich (47 %) und bezugswissenschaftlich (26 %) – bilden die normative Grundlage des theoretischen und praktischen Unterrichts über 1.920 Stunden (Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 44, 47). Der größte Anteil entfällt auf rettungsdienstliche Inhalte, was den praktischen Handlungsschwerpunkt des Berufsbildes reflektiert. Der medizinische Bereich steht für die Anwendung pathophysiologischer und diagnostischer Kenntnisse, während bezugswissenschaftliche Inhalte (z. B. Psychologie, Kommunikation, Recht) die theoretische Fundierung ergänzen. Die Darstellung dient als Referenzwert für den Abgleich mit der empirischen Struktur des digitalen Curriculums.

Abbildung 11: Anteil der Kompetenzbereiche nach APrV (eig. Darstellung)

#todo (#50): Abbildung einfügen

Die Abbildung  zeigt, bezogen auf den Gesamtumfang der Ausbildung, die in der NotSan-APrV verankerte Kompetenzgewichtung. Die vier Kompetenzbereiche – fachlich (24 %), sozial (15 %), personal (11 %) und methodisch (50 %) – definieren die Zielstruktur beruflicher Handlungskompetenz im Rettungsdienst (Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 47). Der besonders hohe Anteil methodischer Kompetenzen spiegelt die Bedeutung strukturierter Vorgehensweisen, Entscheidungsalgorithmen und standardisierter Handlungsroutinen im beruflichen Alltag wider. Fachliche, soziale und personale Anteile ergänzen diesen Schwerpunkt um domänenspezifisches Wissen, Interaktionsfähigkeit und individuelle Reflexionsfähigkeit. Die Darstellung dient als normativer Referenzrahmen zur Bewertung des digital abgebildeten Curriculums im Hinblick auf seine kompetenzorientierte Ausrichtung.

Abbildung 12: Vergleich Themengewichtung APrV-Schätzung vs. NFS-H-Lehrplan (eig. Darstellung)

#todo (#51): Abbildung einfügen

Die Balkengrafik  kontrastiert die normativ vorgegebene Verteilung der Themenbereiche gemäß NotSan-APrV mit der empirisch erhobenen Verteilung im digitalen Curriculum „NFS-H“. Während die APrV eine Gewichtung von 47 % rettungsdienstlich, 27 % medizinisch und 26 % bezugswissenschaftlich vorgibt (Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 44, 47), zeigt die Umsetzung im Curriculum eine nahezu deckungsgleiche Relation (Ø Kursdauer: 57,0 / 27,2 / 21,3 Tage). Die hohe Übereinstimmung verdeutlicht, dass die digitale Bildungsarchitektur nicht nur formal regelkonform ist, sondern auch inhaltlich anschlussfähig zur gesetzlichen Grundlage gestaltet wurde. Damit wird eine zentrale Voraussetzung für die curriculare Validität erfüllt.

Abbildung 13: Kompetenzgewichtung APrV-Schätzung vs. NFS-H-Lehrplan (eig. Darstellung)

#todo (#52): Abbildung einfügen

Die Abbildung  vergleicht die vier Kompetenzbereiche fachlich, sozial, personal und methodisch hinsichtlich ihres relativen Anteils an der curricularen Kursdauer. Die normativen Vorgaben der NotSan-APrV (z. B. 50 % methodisch, 24 % fachlich) werden den empirisch ermittelten Anteilen im Curriculum gegenübergestellt. Die Daten zeigen, dass die Gewichtung der Kompetenzbereiche im digitalen Lehrplan des „NFS-H“ weitgehend der gesetzlich intendierten Verteilung (Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 47) entspricht. Die methodische Dominanz in beiden Perspektiven legt nahe, dass die Ausbildung nicht nur auf inhaltliche Vermittlung, sondern auch auf handlungsbezogene Umsetzung im Sinne einer professionellen Handlungskompetenz zielt. Die Parallelität unterstützt somit die Annahme einer curriculären Implementierung.

Abbildung 14: Verteilung der Aufgaben pro Themenbereich (eig. Darstellung)

#todo (#53): Abbildung einfügen

Die Boxplot-Darstellung  zeigt die Anzahl der Aufgaben in den 32 Kursen, gruppiert nach den Bezugskategorien (Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 44–45) medizinisch, rettungsdienstlich, bezugswissenschaftlich sowie Einführung/Prüfung. Erkennbar ist, dass die rettungsdienstlichen Kurse mit einem Median von über 30 Aufgaben eine deutlich höhere Aufgabenlast aufweisen als die anderen Bereiche. Die bezugswissenschaftlichen Module liegen im unteren Bereich, während medizinische Kurse ein mittleres Aufgabenvolumen abbilden. Die geringe Streuung innerhalb der Themenbereiche und die ausgeprägte Differenzierung zwischen ihnen weisen auf eine strukturierte und differenzierte didaktische Konzeption hin.

Abbildung 15: Verteilung der Kursdauer pro Themenbereich (eig. Darstellung)

#todo (#54): Abbildung einfügen

Die Boxplot-Darstellung  visualisiert die Dauer der 32 Kurse in Tagen, differenziert nach den vier Bezugskategorien (Referentenentwurf des Bundesministeriums für Gesundheit: Ausbildungs- und Prüfungsverordnung für Notfallsanitäterinnen und Notfallsanitäter, 2012, S. 44–45). Auffällig ist der signifikant höhere Medianwert der rettungsdienstlichen Kurse (Ø 57 Tage), was den inhaltlich-praktischen Anforderungen dieses Bereichs entspricht. Medizinische und bezugswissenschaftliche Kurse weisen deutlich kürzere und zugleich eng beieinanderliegende Dauerverteilungen auf. Die Einführung und Prüfung bilden als Sonderkategorie zwei randständige Ausreißer mit jeweils kurzer Laufzeit. Insgesamt belegt die Verteilung eine hohe curriculare Abstimmung hinsichtlich zeitlicher Allokation und thematischer Komplexität.

Diese Übereinstimmungen belegen, dass der Aufbau des Curriculums nicht nur konzeptionell plausibel, sondern auch statistisch nachvollziehbar ist.

Bewertung

Die curriculare Struktur des digitalen Bildungsraums NFS-H erfüllt zentrale Anforderungen an Qualität und Transparenz:

•	Die mittlere Kursdauer ist innerhalb der Kategorien homogen (SD jeweils < 28 Tage), mit klarer Abgrenzung zwischen den Bereichen.
•	Der hohe Anteil rettungsdienstlicher Module (Ø 57 Tage) korrespondiert exakt mit dem APrV-Anteil von 47 %.
•	Die Zuordnung der Inhalte auf Basis systematisch codierter APrV-Kürzel vermeidet subjektive Verzerrungen.
•	Die Korrelation zwischen Kursdauer und Aufgabenanzahl (r = 0,66) weist auf eine innere Konsistenz der Lernstruktur hin.

Somit ist belegt, dass der untersuchte Bildungsraum sowohl reliabel (Wiederholbarkeit der Muster), valide (inhaltliche Deckung mit normativen Grundlagen) als auch konsistent (strukturelle Kohärenz zwischen Plan und Umsetzung) aufgebaut ist. Die Ergebnisse erlauben darüber hinaus eine operationalisierte Bewertung digitaler Curricula auf Grundlage regulatorischer Anforderungen. Zudem zeigen die dargestellten Ergebnisse eine hohe strukturelle Konsistenz des untersuchten Curriculums und spiegeln in ihrer quantitativen Ausprägung die gesetzlich intendierte Bildungslogik der NotSan-APrV wider. Auf diese Weise ergibt sich eine direkte Verbindung zwischen den empirisch beobachteten Anteilen und den Ausbildungszielen, die im Referentenentwurf von 2012 definiert wurden.

Die prozentuale Verteilung der Themenbereiche „medizinisch” (27 %), „rettungsdienstlich” (47 %) und „bezugswissenschaftlich” (26 %) im APrV-Grundlagenkorpus findet sich beinahe deckungsgleich in der realen Kursstruktur wieder (vgl. Abbildungen 8 und 10). Diese Übereinstimmung stützt die Annahme, dass das analysierte Curriculum den staatlich definierten Anspruch auf eine bedarfsorientierte Daseinsvorsorge (vgl. S. 44 NotSan-APrV) sowohl formal aufnimmt als auch in Kurslogik und Zeitstruktur operationalisiert und umsetzt. Auch die Auswertung der vier Kompetenzbereiche zeigt eine deutliche Parallelität zu den in der APrV formulierten Anforderungen (siehe Abbildungen 9 und 11). Die hohe Gewichtung methodischer Kompetenzen (50 %) und die Integration fachlicher, sozialer und personaler Aspekte verdeutlichen, dass die Ausbildung systematisch darauf ausgerichtet ist, die „zur Berufsausübung notwendige Handlungssicherheit“ (S. 47) zu vermitteln, inhaltlich und didaktisch sowie curricular. Die geringe Streuung innerhalb der Themenkategorien (SD < 28 Tage), die hohe Korrelation zwischen Kursdauer und Aufgabenanzahl (r = 0,66) sowie die klare Zuordenbarkeit der Inhalte über algorithmische APrV-Kürzel sprechen für einen systematisch konstruierten Lehrplan, der somit den regulatorischen Vorgaben formal, inhaltlich und strukturell entspricht.
Ausblick

Diese Analyse verdeutlicht exemplarisch, wie digitale Curricula im Gesundheitswesen systematisch und datenbasiert analysieren werden können. Die Verbindung zwischen regulatorischer Struktur (NotSan-APrV), inhaltlicher Codierung und quantitativer Auswertung liefert ein konsistentes Argument für die Validität digitaler Bildungsräume und deren Anschlussfähigkeit an curriculare Standards. Die Analyse ist ein methodischer Beitrag zur curricularen Forschung und belegt empirisch die Anschlussfähigkeit des digitalen Curriculums an die gesetzliche Struktur der NotSan-APrV. Die normative Fundierung wird mittels dieser Analyse statistisch nachgewiesen.

## 3.4 Operative Architektur als Arbeits- und Lernumgebung {#sec:OperativeArchitektur}

Die bestehende didaktische Architektur des Learning Management Systems kann zur Berücksichtigung des operativen Bereichs um die lernprozessbezogene Struktur erweitert werden. Einerseits basiert der Aufbau bereits auf einer Organisationsstruktur, die in der Lehre aktiv genutzt wird und daher unmittelbar anschlussfähig ist. Andererseits ermöglicht die komplementäre Benutzung durch Lehrkräfte im operativen Alltag, das System nicht nur als didaktisches Werkzeug, sondern auch als erlebbares Arbeitsmittel zu nutzen. So können Lehrkräfte die Vorteile und Begrenzungen des Systems direkt erfahren. Zur kontextuellen Einordnung dieser operativen Architektur des hier beschriebenen Learning Management Systems können weiterhin zwei Aufsätze als Referenzrahmen dienen. Beide Studien zeigen, dass digitale Systeme nicht nur für Lehr-Lern-Prozesse, sondern auch für administrative, organisatorische und arbeitsplatzbezogene Zwecke eingesetzt werden können. Gleichzeitig verdeutlichen die Arbeiten die Grenzen bestehender Ansätze, die sich hauptsächlich in ihrer strukturellen Tiefe und curricularen Integration unterscheiden.

@brandic_asynchroner_2024 beschreiben bspw. in ihrer Studie die Entwicklung eines asynchronen Moodle-Kurses für das fachliche Onboarding administrativen Personals an der Universität Wien. Ihre Absicht war, eine zeitlich flexible, selbstgesteuerte Schulung zu schaffen, die den Einstieg in zentrale IT-Systeme der Universität erleichtert. Der Kurs besteht aus strukturierten Lerneinheiten mit eingebetteten H5P-Objekten, Videos und reflexiven Aufgaben, wobei der Fokus auf der unmittelbaren Funktionsvermittlung liegt. Das zugrunde liegende didaktische Konzept basiert auf einer modularen Struktur mit asynchroner Kommunikation und Rückmeldemöglichkeiten, die eine individuelle Lerngeschwindigkeit ermöglichen sollen [@brandic_asynchroner_2024, Seite 22–24].

Obwohl @brandic_asynchroner_2024 die operative Nutzung eines Learning Management Systems beispielhaft belegen, bleibt die Struktur funktional begrenzt. Das untersuchte Kursformat stellt ein isoliertes Schulungsmodul dar, dem eine umfassendere curricular-systemische Einbettung fehlt. In der vorliegenden Evaluation wird die Moodle-Plattform als Träger einer Lernressource eingesetzt, jedoch mit der Einschränkung, dass sie nicht als strukturierendes Element eines organisationalen Bildungsraums fungiert. Der vorliegende Unterschied zum hier beschriebenen System ist in diesem Aspekt zu verorten. Während der Kurs bei @brandic_asynchroner_2024 als Tool für ein spezifisches Anwendungsszenario konzipiert wurde, das auf die administrative Zielgruppe ausgerichtet ist, versteht sich das hier beschriebene Learning Management System als strukturübergreifende, konsistente und reflexionsoffene Organisationsumgebung. In dieser arbeiten Lehrende, Lernende und Verwaltung in einer gemeinsamen Systemarchitektur.

Die Abgrenzung zum hier verfolgten Ansatz wird in der Studie von @nwosu_digitalisation_2024 noch deutlicher, in der die Digitalisierung der Bildungsverwaltung in Nigeria untersucht wird. Der Fokus liegt dabei nicht auf konkreten Plattformen, sondern auf der Entwicklung eines digitalen Bildungsmanagementsystems, das die Effizienz steigert, die Steuerung verbessert und die Rechenschaftslegung im staatlichen Schulwesen ermöglicht. Das System wird seitens der Autorenschaft als Instrument zur zentralen Kontrolle und Verwaltungsoptimierung beschrieben, weniger als didaktisch operierender Raum. Zwar betonen beide, dass Digitalisierung notwendig sei, um die Schulqualität zu sichern und organisatorischen Abläufe zu verbessern, doch die pädagogische Perspektive bleibt vollständig außen vor. Der Mensch erscheint darin als Verwaltungseinheit, nicht als lernende oder lehrende Person [@nwosu_digitalisation_2024, Seite 3–5].

Im Vergleich dazu ist der hier betrachtete Anteil des Learning Management Systems als pädagogisch fundierte, operativ nutzbare Struktur konzipiert. In diesem System stehen Organisation und Lehre nicht nebeneinander, sondern sind strukturell miteinander verbunden. Die Containerstruktur, die für alle Handlungssituationen gilt, bildet die Grundlage für die Lernprozesse und bietet gleichzeitig einen Rahmen für organisatorische Abstimmungen, Kurskoordination, Aufgabenverteilung und Rückmeldung. Somit fungiert das System als Verwaltungsinstrument und reflektierbarer Handlungsraum für alle Beteiligten, von der Kursleitung und den Lehrenden bis hin zu den Lernenden selbst. Im Kontext des Forschungsgegenstands veranschaulichen zwei Studien die Bandbreite bestehender Ansätze. @brandic_asynchroner_2024 beschreiben ein isoliertes, funktional begrenztes Lernmodul, während @nwosu_digitalisation_2024 ein zentralisiertes Verwaltungsinstrument skizzieren. Im Gegensatz dazu verfolgt das hier untersuchte System einen systemisch-strukturellen Ansatz, der pädagogische Architektur, operative Nutzung und curriculare Logik in einer konsistenten und integrativen Umgebung miteinander verbindet.

Bereits in der didaktischen Architektur finden organisatorische Elemente ihren Raum. Neben der in Abschnitt 3.3 beschriebenen Containerstruktur existieren weitere Funktionen, die den operativen Betrieb unterstützen. Dazu zählen u.a. die Kursadministration, die Nutzerverwaltung, die Terminplanung und die Kommunikationswerkzeuge. Diese Funktionen sind integraler Bestandteil des Systems und ermöglichen eine nahtlose Verbindung zwischen Lernprozessen und organisatorischen Abläufen. So können Lehrende beispielsweise Kursmaterialien bereitstellen, Aufgaben verwalten und Feedback geben, während gleichzeitig administrative Aufgaben wie Teilnehmermanagement, Fortschrittsüberwachung und Berichterstattung durchgeführt werden können. Diese duale Funktionalität trägt dazu bei, dass das Learning Management System nicht nur als didaktisches Werkzeug, sondern auch als operatives Arbeitsmittel genutzt wird.

## 3.5 E-Portfolio als Reflexions- und Transferinstrument {#sec:E-Portfolio}

## 3.6 Technische Rahmenbedingungen {#sec:TechnischeRahmen}

@dyrna_methoden_2021 als technische Klassifizierung
