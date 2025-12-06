\newpage

# 1	Einleitung und theoretischer Rahmen {#sec:Einleitung}

Die aktuellen Novellierungen in der Ausbildung der Gesundheitsberufe\label{term:gesundheitsberufe} zielen darauf ab, nicht nur die gesetzlichen Rahmenbedingungen für Gesundheitsberufe anzupassen, sondern die Kompetenzanforderungen zu erweitern und zu präzisieren. So wird besonderer Wert auf die Förderung fachspezifischer, sozialer und methodischer Kompetenzen gelegt, die sich an den wachsenden Herausforderungen im Gesundheitswesen orientieren. Dies spiegelt sich sowohl in den neuen Ausbildungsrichtlinien als auch in den erweiterten Kompetenzprofilen der jeweiligen Berufsgruppen wider [@pflegekammer_nrw_weiterbildungsordnung_2023; @bundesrepublik_deutschland_gesetz_2023].

- Erkenntnisinteresse skizzieren (Kapitel 1.1).
- Forschungsstand und Forschungslücke prägnant benennen.
- Herleitung der Forschungsfragen vorbereiten.
- Methodische Vorüberlegungen andeuten (Kapitel 1.2).

## 1.1 Erkenntnisinteresse, Problemstellung und Relevanz {#sec:Erkenntnisinteresse-Komplex}

Die Ausbildung im Rettungsdienst wurde durch das Gesetz über den Beruf der Notfallsanitäterin und des Notfallsanitäters (NotSanG)\label{term:notsang} zum 01.01.2014 gem. § 5 (1) NotSanG [-@bundesrepublik_deutschland_gesetz_2023] von einer zweijährigen zu einer dreijährigen Qualifikation geändert. Der Gesetzgeber transformierte hierdurch die Tätigkeit weg von einem Assistenzberuf hin zu einer beruflichen Qualifikation, in deren Mittelpunkt das kompetenzorientierte und selbstverantwortliche Handeln nach § 4 NotSanG [-@bundesrepublik_deutschland_gesetz_2023] als Ausbildungsziel definiert wurde. Der Referentenentwurf [-@bundesgesundheitsministerium_referentenentwurf_2012] zum NotSanG verdeutlicht die intendierte Absicht [@bundesgesundheitsministerium_referentenentwurf_2012, Seite 44-45]: Die Auszubildenden sollen insbesondere interdisziplinäre Fachlichkeit erlangen, die zur selbstständigen Lösung aller berufsrelevanter Handlungen sowie deren kritischen und selbstreflektiven Ergebnisbeurteilungen notwendig erscheinen.

#todo Definition von NotSanG bzw. NotSan (Erstnennung) ergänzen, Verweis auf Anhang Begriffe setzen.

Um insbesondere den anerkennungsrechtlichen Erfordernissen aus § 6 (2) 1 [-@bundesrepublik_deutschland_gesetz_2023], namentlich dem "Vorhandensein der für die Ausbildung erforderlichen Räume und Einrichtungen sowie ausreichender Lehr- und Lernmittel" [@bundesrepublik_deutschland_gesetz_2023] gerecht zu werden, ist in der Ausbildung von Notfallsanitäterinnen und Notfallsanitäter\label{term:notfallsan} die Verwendung eines digitalen Learning Management System (LMS)\label{term:lms} implentiert, welches die Bereitstellung von Lernmaterialien, die Unterstützung kollaborativer Lernprozesse und die Förderung selbstorganisierter Kompetenzentwicklung ermöglicht [@moodle_pty_ltd_was_2019].

Die Grundlage zur Konzeption der benutzen LMS-Architektur findet sich in einer Vorarbeit, die sich insbesondere mit der nachhaltigen, digitalen Sicherung von selbstorganisierten Gruppenarbeitsergebnissen beschäftigte [@hanisch_nachhaltiges_2017]. Diesen Erkenntnissen zur Folge, sind die Faktoren

-  Zeitpunkt der Erfassung und Verfügbarkeit: $\beta = 1{,}213$, $\Delta = 0{,}213$ sowie $\beta = 0{,}251$, $\Delta = 0{,}749$,
-  Struktur des digitalen Systems: $\beta = 2{,}372$, $\Delta = 1{,}372$ und
-  Interaktion der Akteurinnen: $\beta = 0{,}151$, $\Delta = 0{,}849$

für die nachhaltige Sicherung der selbstorganisierten Gruppenarbeitsergebnisse förderlich [@hanisch_nachhaltiges_2017, Abbildung 2]. Die in der Studienleistung gewonnenen Ergebnisse nahmen auf die Gestaltung und Nutzung der digitalen Lernumgebung Moodle® in der Einrichtung erheblichen Einfluss. Der Aufbau der technischen Architektur wurde extern als studentischer Projektauftrag in Zusammenarbeit mit der Notfallsanitäterschule durch eine Studierende der Bildungswissenschaft während ihres Praktikums im Wintersemester 2016/2017 betreut. Die hier vorgestellte Erweiterung und Weiterentwicklung des LMS resultierte aus der pandemischen Situation ab März 2020, in der die Ausbildung von Notfallsanitäterinnen und Notfallsanitätern zunächst kaum mehr in Präsenzunterrichten durchführbar erschien. Aus der vorherigen intensiven Nutzung des LMS durch die Auszubildenden, war die Verschränkung zwischen Fern- und Präsenzunterricht eine Herausforderung, die in Summe innerhalb von drei Monaten durch die Umsetzung der inhaltlichen und organisatorischen Ergänzungen auf Grundlage des Curriculums in das bestehende digitale System bewältigt wurde.

### 1.1.1 Erkenntnisinteresse {#sec:Erkenntnisinteresse}

Im Anwendungsfeld einer Ausbildungseinrichtung wird die Ausbildung von Notfallsanitäterinnen und Notfallsanitätern (NFS, NotSan) seit Beginn des ersten Jahrgangs im März 2017 durchgeführt. Im Zuge der Konzeption beruflich-currikulater Berufsbildung im Kontext von High Responsibility Teams (HRT)\label{term:hrt} in den Gesundheitsberufen, wurde direkt zu Beginn eine digitale Lernumgebung in Form eines LMS implementiert. Dieses System dient nicht nur der Bereitstellung von Lernmaterialien, sondern auch der Unterstützung kollaborativer Lernprozesse und der Förderung selbstorganisierter Kompetenzentwicklung. Erste Evaluationen deuten darauf hin, dass das LMS einen signifikanten Einfluss auf die Lernprozesse und die Kompetenzentwicklung der Studierenden hat. Allerdings bleiben die zugrunde liegenden Wirkmechanismen und Interaktionen zwischen den technologischen, didaktischen und sozialen Komponenten weitgehend unklar.
#todo Prüfen, ob HRT, LMS und digitaler Bildungsraum ausreichend definiert und im Anhang verlinkt sind.

Das zentrale Erkenntnisinteresse dieser Forschungsarbeit besteht darin, das Wirkgefüge\label{term:wirkgefege} eines eingesetzten LMS im digitalen Bildungsraum\label{term:digitaler-bildungsraum} der Gesundheitsberufe systematisch zu analysieren. Im Mittelpunkt steht die Frage, wie Lern-, Handlungs- und Kompetenzentwicklungsprozesse durch das Zusammenspiel technologischer, didaktischer und sozialer Mechanismen beeinflusst werden und welche emergenten Muster sich dabei ausbilden – gerade weil Gesundheitsberufe zwischen engen regulatorischen Vorgaben, multiprofessionellen Lernsettings und hohen Anforderungen an dokumentierte Kompetenzentwicklung vermittelt werden müssen [@hanisch_notfallsanitater_2020; @pentzold_praxis_2018].

Von besonderem Interesse ist, wie Akteurinnen, d.h. Lernende, Lehrende und Organisationen, das LMS interpretieren, nutzen und in ihre eigenen Selbstorganisations- und Entscheidungsprozesse integrieren. Damit richtet sich das Erkenntnisinteresse nicht auf die isolierte Bewertung einzelner Funktionen des LMS, sondern auf die Aufklärung der kausalen Interdependenzen, die zwischen System, Akteurinnen\label{term:akteure} und digitalen Infrastrukturen entstehen [@parker_negotiating_2024; @van_niekerk_addressing_2025]. Der Fokus richtet sich hierbei vertiefend  auf Akteure, die im Kontext von High Responsibility Teams (HRT) agieren, da diese durch ihre komplexen Arbeitsanforderungen und die Notwendigkeit zur schnellen, fundierten Entscheidungsfindung besondere Herausforderungen an die Kompetenzentwicklung stellen [@hagemann_trainingsentwicklung_2011; @hagemann_high_2011; @ritzmann_training_2014].

Im Rahmen dieses Forschungsansatzes wird infolgedessen davon ausgegangen, dass die Anwendung der systemisch‑konstruktivistischer Theorie nicht nur für die curriculare Gestaltung und Durchführung von Lernprozessen relevant sein könnte, sondern für die Architektur und den Betrieb von Learning‑Management‑Systemen unverzichtbar ist. Daher wird untersucht, inwiefern die LMS‑Struktur, ihre Nutzungsdynamiken und die durch sie erzeugten Rückkopplungen Aufschluss darüber geben, wie Kompetenzen im digitalen Bildungsraum entstehen und stabilisiert werden.

Dieser Arbeit liegt damit ein doppelt gerichtetes Erkenntnisinteresse zugrunde. Einerseits sollen die beobachtbaren Wirkmechanismen systematisch identifiziert und theoretisch erklärbar gemacht, andererseits sollen daraus prospektive Einsichten gewonnen werden, die eine gezielte Gestaltung zukünftiger Bildungsräume ermöglichen. In diesem Sinne betrachtet diese Arbeit zu den retrospektiven Analysen bestehender Effekte und erweitert diese um die Entwicklung einer theoretisch fundierten Grundlage für prognostische Aussagen zu gewünschten Wirkungen.

### 1.1.2 Problemstellung {#sec:Problemstellung}

Text

### 1.1.3 Thematische Relevanz {#sec:Themenrelevanz}

Text

## 1.2 Forschungsfragen und methodische Vorüberlegungen {#sec:Forschungsfragen-Methodik}

Text

### 1.2.1 Zugrundliegende Vermutungen {#sec:Vermutungen}

Text

### 1.2.2 Ziel der Forschung {#sec:Zielsetzung}

Transdisziplinäre Zielsetzung unter Berücksichtigung medizinischer und bildungswissenschaftlicher Aspekte.

## 1.3 Stand der Forschung und Forschungslücke {#sec:Forschungsstand}

- [ ] Überblick über die bisherigen Studien und relevante Literatur zum Thema.
- [ ] legt den Stand der Forschung dar und entwickelt die Fragestellung. 

Die Untersuchung legt nahe, dass künftige Forschungen sich verstärkt auf die Analyse der Lernaktivitäten und deren Auswirkungen auf die Lernenden konzentrieren sollten. Die Autoren betonen insbesondere die Notwendigkeit, zukünftige Forschungsarbeiten darauf auszurichten, wie unterschiedliche CBL-Methoden in spezifischen medizinischen Bildungskontexten wirksam eingesetzt werden können.

> Der menschliche Bildungsprozess ist von einer ständigen Wechselwirkung zwischen grundlegenden emotionalen und kognitiven Bedürfnissen sowie den Unsicherheiten geprägt, die beim Lernen und der Kompetenzentwicklung auftreten. Bedürfnisse wie Bindung, Selbstwerterhöhung und die Vermeidung von Unlust bilden die Basis für eine dynamische Kausalkette, die das Lernverhalten antreibt. Aus den Bedürfnissen heraus entstehen Unsicherheiten im Lernprozess und in der Kompetenzmessung, die das Handeln der Lernenden prägen. Diese Handlungen zielen darauf ab, die Unsicherheiten zu verringern und das Bedürfnis nach Selbstverwirklichung zu befriedigen. In dieser kontinuierlichen Zirkulation beeinflussen sich Bedürfnisse, Konzepte und Handlungen wechselseitig und treiben den Lernprozess stetig voran.

### 1.3.1 Theoretische und empirische Vorüberlegungen {#sec:TheoretischeVoruberlegungen}

Text

### 1.3.2 Literaturrecherche {#sec:Literaturrecherche}

Die systematische Literatursuche orientiert sich an den Qualitätskriterien von Döring [@doring_forschungsmethoden_2023] und kombiniert das Suchnetzwerk nach @vom_brocke_standing_2015 mit einem mehrstufigen Dokumentationsprozess in Zotero und Obsidian. Ausgehend von den im Exposé [@hanisch_wirkgefuge_2022] abgeleiteten Suchclustern werden primäre Begriffe (z.B. „Learning Management System“, „digitaler Bildungsraum“, „Kompetenzentwicklung“) genutzt, um Quellen zu identifizieren, die unmittelbar den Forschungsgegenstand adressieren. Sekundäre Begriffe (z.B. „digital“, „blended“, „hybride Lernarrangements“) dienen der Kontextualisierung über didaktische und organisatorische Fragen der Lernraumgestaltung hinaus. Tertiäre Begriffe (z.B. „E-Learning“, „Online-Plattform“, „EdTech-Infrastruktur“, „Open-Source-Lernplattformen“) erschließen angrenzende technologische Rahmungen und Innovationspfade. Die Cluster werden mit 35 % (primär), 40 % (sekundär) bzw. 25 % (tertiär) gewichtet. Die prozentuale Gewichtung bestimmt zugleich die Mindestquote der zu sichtenden Trefferlisten: Primäre Kombinationen werden zu 80 % vollständig analysiert, sekundäre zu 50 %, tertiäre zu 15 %. Damit lässt sich das Spannungsfeld aus Vollständigkeit und Praktikabilität transparent steuern.

Die Suchanfragen werden entlang der sechs Schritte Festlegung von Suchbegriffen, Auswahl einschlägiger Datenbanken (u.a. Fachdatenbanken der Bildungswissenschaft und Medizin), Durchführung der Suchstrings, Sichtung und Strukturierung der Treffer, Dokumentation aller Entscheidungen sowie Analyse und Synthese der ausgewählten Literatur abgearbeitet. Jeder Schritt wird in Zotero als Memo protokolliert, sodass der Bezug zu den Gütekriterien Validität, Reliabilität und Transparenz jederzeit nachvollziehbar bleibt [@doring_forschungsmethoden_2023].

Konkrete Abfragen koppeln die Suchbegriffe mit Eintragstypen. Für „Learning Management System“ (Zeitschriftenartikel) liegen 68 Einträge vor, „Online Lernplattform“ liefert drei Einträge und „Digital Learning“ 289. Kleine Trefferlisten werden vollständig bearbeitet; bei umfangreichen Ergebnisräumen greift die oben beschriebene Quotierung. Die Bearbeitungstiefe wird über Tag-Kombinationen gesteuert: Jede ausgewertete Quelle erhält `Promotion:Literaturanalyse` plus genau eine argumentative Kategorie (`Promotion:Argumentation`, `Promotion:Kerngedanke`, `Promotion:Schlussfolgerung` oder `Promotion:Weiterführung`). Erst wenn die erforderliche Quote in einer Suchkombination mit entsprechenden Tags vermerkt ist, gilt der Suchraum als saturiert. Auf diese Weise lässt sich jederzeit nachverfolgen, welche Quelle bereits bewertet ist und wie sie in das Argumentationsgefüge der Arbeit einfließt.

Die Auswahlkriterien sind projektspezifisch operationalisiert und in den Arbeitsunterlagen hinterlegt:

Table: Auswahlkriterien der Literaturrecherche \label{tab:auswahlkriterien_literaturrecherche}

| Kriterium | Begründung | Bemerkung |
| --- | --- | --- |
| Aktualität | Normative Entwicklungen (z.B. NotSanG-Novellierungen) verlangen Quellen mit unmittelbarem Bezug zum Untersuchungszeitraum. | Fokus auf Publikationen ab 2014, sofern Klassiker nicht zwingend notwendig sind. |
| Art der Quelle (Übersichtsartikel, Metaanalysen, Monografien, Sammelbände, Zeitschriftenbeiträge, Studien, Klassiker) | Nur wissenschaftliche Publikationen sichern die geforderte Güte und trennen Fachliteratur von populären Darstellungen. | Datenbankauswahl richtet sich nach Disziplin (Bildungswissenschaft, Medizin, Bildungstechnologie). |
| Subjektive Relevanz / systematische Einordnung | Jede Quelle wird hinsichtlich ihres Beitrags zur Argumentation auf einer Skala von 1–10 bewertet (1 = „Hauch einer Relevanz“, 10 = „totale Relevanz“). | Die Relevanzbewertung wird zusammen mit der Tag-Kombination dokumentiert. |

Die Tabelle bündelt damit die Auswahlkriterien, die bei jeder Suchkombination geprüft werden, bevor die Quelle in Zotero markiert und in MAXQDA weiterverarbeitet wird. Sie stellt die direkte Verbindung zum Suchnetzwerk her, weil die Kriterien bestimmen, welche Treffer aus den primären, sekundären und tertiären Clustern in die detaillierte Analyse überführt werden.

Die beschriebenen Schritte – Suchnetzwerk, prozentuale Gewichtung, Tag-basierte Nachverfolgung und transparente Kriterien – gewährleisten, dass relevante Quellen systematisch identifiziert, kategorisiert und priorisiert werden. Gleichzeitig entsteht eine belastbare Dokumentationsgrundlage, die eine spätere Aktualisierung oder Replikation der Literaturrecherche ohne Medienbruch erlaubt.

### 1.3.3 Identifikation der Forschungslücke {#sec:Forschungslucke}

Eine der dem Untersuchungsgegenstand am nächsten kommenden Studien stammt von Fonseca et al. [-@fonseca_collaborative_2024]. Diese Untersuchung zeigt, dass digitale Communities of Practice (CoPs) eine zentrale Rolle für den Erfolg kollaborativer Lernökosysteme spielen. Erfolgreiche Collaborative Learning Ecosystems (CESs) zeichnen sich durch klare Kommunikationsstrukturen, dynamische soziale Interaktionen sowie flexible Lerntechnologien aus. Die Studie liefert konkrete Designprinzipien, die zur Entwicklung nachhaltiger digitaler Lernräume genutzt werden können. Auf dieser Grundlage wird ein neues Modell für digitale Lernökosysteme entwickelt, das kollaborative Lernprozesse mit technologischen und sozialen Aspekten verbindet. (@fonseca_collaborative_2024, Seite 130, 134, 137)

Während die genannte Untersuchung wertvolle Erkenntnisse über die Bedeutung von Communities of Practice (CoPs) und Collaborative Learning Ecosystems (CESs) liefert, fehlt in der bisherigen Forschung eine systemische Erklärung der Wirkmechanismen digitaler Bildungsräume. Die bisherigen Studien konzentrieren sich primär auf die empirische Analyse einzelner Erfolgsfaktoren und Designprinzipien, ohne die kausalen Interdependenzen zwischen den beteiligten Elementen umfassend zu modellieren.
Die vorliegende Forschungsarbeit schließt diese Lücke, indem sie das Wirkgefüge eines LMS in der medizinischen Lehre systemisch analysiert. Im Gegensatz zu bestehenden Studien, die digitale Lernräume als Sammlung von Einzelfaktoren betrachten, wird in dieser Untersuchung ein holistisches Modell entwickelt, das nicht nur beschreibt, was funktioniert, sondern wie die verschiedenen Elemente eines digitalen Bildungsraumes interagieren und sich wechselseitig beeinflussen. Ein entscheidender Unterschied zur bisherigen Forschung ist der systemtheoretische Ansatz, der die Identifikation emergenter Strukturen und autopoietischer Stabilisierungseffekte innerhalb digitaler Lernumgebungen ermöglicht. Während empirische Studien bereits Hinweise auf erfolgreiche kollaborative Lernmodelle liefern, fehlt eine tiefgehende Analyse der zugrunde liegenden Kausalketten, die diese Erfolgsfaktoren miteinander verbinden.

Diese Arbeit setzt an dieser Stelle an, indem sie ein systemisches Modell des digitalen Bildungsraums entwickelt und untersucht, welche strukturellen Bedingungen die nachhaltige Wirksamkeit eines LMS beeinflussen. Durch diese systemische Perspektive wird nicht nur die bestehende Forschung ergänzt, sondern auch eine theoretische Grundlage geschaffen, um digitale Bildungsräume nicht nur retrospektiv zu bewerten, sondern auch prospektiv zu gestalten. Dies erlaubt eine Ableitung fundierter Gestaltungsrichtlinien für zukünftige Bildungsumgebungen, die auf einer systemisch erklärbaren Wechselwirkung zwischen technologischen, sozialen und didaktischen Faktoren basieren.

## 1.4 Herleitung Haupt- und Unterforschungsfragen {#sec:FU-Herleitung}

Wissenschaftliche und praxisorientierte Erkenntnisinteressen.

Die bisherigen LMS-Erfahrungen erklären das beobachtete Wirkungspotenzial, nicht jedoch die dahinterliegenden Mechanismen. Gerade weil Gesundheitsberufe einer engen Regulierung unterliegen und digitale Bildungsräume für High Responsibility Teams besondere Anforderungen stellen, braucht es eine systemische Analyse, die technologische, didaktische und soziale Faktoren als Wirkgefüge fasst. Leitend ist die Annahme, dass das systemisch-konstruktivistische Theoriegebäude nicht nur curriculare Entscheidungen, sondern ebenso die Architektur und den Betrieb eines LMS begründet – und damit Prognosen künftiger Wirkungen ermöglicht. Aus dieser Annahme lassen sich keine klassischen, theorieabgeleiteten Hypothesen formulieren [@doring_forschungsmethoden_2023, Seite 146]; stattdessen wird eine forschungsfragengeleitete Struktur entwickelt.

Die handlungsleitende Hauptforschungsfrage (FH) lautet:

„Wie ist das Wirkgefüge des angewendeten LMS auf Akteure im digitalem Bildungsraum von Gesundheitsberufen gestaltet?“ \label{fh}

Die Forschungsfrage ist bewusst eng gefasst, weil ein bestehendes LMS im realen Betrieb untersucht wird. Ihre Syntax wird entlang der zentralen Begriffe operationalisiert: Das Medientool (LMS) wirkt im digitalen Bildungsraum auf Akteurinnen, die in Gesundheitsberufen handeln; zu analysieren ist das Wirkgefüge und dessen Gestaltung [@schnell_methoden_2013, Seite 7].

Aus der FH werden sieben Forschungsunterfragen (FU1–FU7)\label{term:forschungsunterfrage} abgeleitet, die das Wirkgefüge in adressierbare Teilaspekte zerlegen und zugleich die Methodenwahl strukturieren (\hyperref[tab:methoden_FU]{Tabelle 4}):

- FU1: Akzeptanz und Nützlichkeit des LMS aus Sicht der Nutzenden (Metaanalyse, Umfrage).
- FU2a/FU2b: Wirkung auf Lernende bzw. Lehrende (Evaluation nach Kirkpatrick, Gruppeninterviews).
- FU3: Didaktische und technologische Merkmale des Systems (theoretische Rekonstruktion der Architektur).
- FU4a/FU4b: Bildungswissenschaftliche und technisch-gestalterische Wirkmechanismen (Inhaltsanalyse, Eye-Tracking, Simulation).
- FU5: Möglichkeiten und Grenzen des angewandten Modells (Qualitative Inhaltsanalyse, SWOT).
- FU6: LMS als Kompetenzerwerbssystem (systemische Kopplung von Kompetenzmodellen und LMS-Struktur).
- FU7: Erweiterung von Kausalgesetzen im digitalen Bildungsraum (Grounded-Theory-gestützte Theorieentwicklung).

Die Abfolge der Unterforschungsfragen folgt der in Abbildung \ref{fig:fu-sequenz} skizzierten Logik: Von der Bedeutung (FU1) über beobachtete Effekte (FU2a/FU2b) und deren Effektfaktoren zur Konzeption (FU3), flankiert von Möglichkeiten und Mechanismen (FU4a/FU4b), bis hin zu Kompetenzen und Kausalgesetzen (FU6/FU7), die schließlich das Wirkgefüge der Hauptfrage adressieren. Damit ist die Sequenz zugleich thematische Landkarte und methodische Prozessführung.

\begin{figure}[h]
\centering
\begin{tikzpicture}[every node/.style={rectangle, draw, rounded corners, align=center, minimum width=3.4cm, minimum height=1.1cm}, node distance=2.2cm]
  \node (bedeutung) at (0,2.2) {Bedeutung\\(FU1)};
  \node (effekte) at (0,0) {Effekte\\(FU2a/FU2b)};
  \node (faktoren) at (0,-2.2) {Effektfaktoren};

  \node (moglichkeiten) at (4.4,2.2) {Möglichkeiten\\(FU5)};
  \node (mechanismen) at (4.4,0) {Mechanismen\\(FU4a/FU4b)};
  \node (konzeption) at (4.4,-2.2) {Konzeption\\(FU3)};

  \node (kompetenzen) at (8.8,2.2) {Kompetenzen\\(FU6)};
  \node (kausal) at (8.8,0) {Kausalgesetze\\(FU7)};
  \node (wirkgefuge) at (8.8,-2.2) {Wirkgefüge};

  \draw[->, thick] (bedeutung) -- (effekte);
  \draw[->, thick] (effekte) -- (faktoren);
  \draw[->, thick] (moglichkeiten) -- (mechanismen);
  \draw[->, thick] (mechanismen) -- (konzeption);
  \draw[->, thick] (kompetenzen) -- (kausal);
  \draw[->, thick] (kausal) -- (wirkgefuge);

  \draw[->, thick] (bedeutung) -- (moglichkeiten);
  \draw[->, thick] (effekte) -- (mechanismen);
  \draw[->, thick] (faktoren) -- (konzeption);
  \draw[->, thick] (moglichkeiten) -- (kompetenzen);
  \draw[->, thick] (mechanismen) -- (kausal);
  \draw[->, thick] (konzeption) -- (wirkgefuge);
\end{tikzpicture}
\caption{Abfolge der Forschungsunterfragen: von Bedeutung und Effekten über Mechanismen und Konzeption hin zu Kompetenzen, Kausalgesetzen und Wirkgefüge.}
\label{fig:fu-sequenz}
\end{figure}

Der hier skizzierte Entwicklungspfad folgt einer deduktiv gestützten Progression von Akzeptanz über Effekte und Mechanismen hin zu Kompetenz- und Kausalannahmen. FU1 knüpft an Akzeptanz- und Nutzungsrahmen an [@doring_forschungsmethoden_2023, Kapitel 6.1] und legitimiert die Frage nach Bedeutung und Nützlichkeit im Anwendungsfeld. FU2a/FU2b greifen die Wirkung auf Lernende und Lehrende auf, angelehnt an Evaluationslogiken nach Kirkpatrick und TEI [@kirkpatrick_evaluating_1998; @ritzmann_tei_2020], und bieten dadurch die Möglichkeit einer belastbaren Evaluation. FU3–FU4b werden durch systematische Inhaltsanalyse und UI-/Eye-Tracking-Ansätze abgeleitet, die Mechanismen und gestalterische Faktoren sichtbar machen [@mey_qualitative_2010; @mayring_neuere_2008; @lewandowska_realeye_2020; @kaduk_webcam_2023] und Rückschlüsse auf die Erkenntnisse der vorangegangenen Evaluation zulassen. FU5 adressiert Möglichkeiten und Grenzen, gestützt durch literaturbasierte SWOT-Analysen [@niederberger_swot-analyse_2015]; in der Folge kann die Einordnung der Bedeutsamkeit im Kontext der bisherigen Ergebnisse überhaupt erst vorgenommen und damit der Rahmen beschrieben werden. Der abschließende Schritt ist die systemtheoretische Einordnung über Kausalitätsbeziehungen, um Ziele zu beschreiben und das Wirkgefüge zu begründen [@glasersfeld_radikaler_2008, Seite 127-129; @reich_systemisch-konstruktivistische_2010, Seite 118-119; @siebert_padagogischer_2003, Seite 74-78; @baraldi_operationbeobachtung_2019, Seite 125].

Die detaillierte Zuordnung dieser Unterfragen zu den Datenerhebungen und Erfüllungskriterien erfolgt in Kapitel 4.2; die interdependente Argumentation wird in \hyperref[sec:Diskussion-Interdependenz]{Kapitel 6.3.1} aufgegriffen und in \hyperref[sec:Conclusio-Manifest]{Kapitel 7} manifestartig verdichtet.

#todo Kurzhinweis auf Eye-Tracking-Design (Remote, Bildexport-only, FU-gekoppeltes 7-Schritte-Raster) einfügen, Verweis auf Abschnitt 4.2.4.

## 1.5 Aufbau der Arbeit {#sec:Aufbau-Arbeit}

Die Struktur des vorliegenden Forschungsprojekts weist aufgrund der transdisziplinären Ausrichtung zwischen Bildungswissenschaft und Medizin eine besondere Komplexität auf, da verschiedene Disziplinen integriert und unterschiedliche wissenschaftliche Anforderungen berücksichtigt werden müssen. Um dieser Herausforderung gerecht zu werden, folgt der strukturelle Aufbau der Arbeit einer konsequenten Verschränkung der formalen Anforderungen sowohl der medizinischen als auch der kultur- und sozialwissenschaftlichen Rahmenbedingungen. Dies ermöglicht eine umfassende Bearbeitung des Themas, die den jeweiligen spezifischen Gegebenheiten beider Disziplinen gerecht wird.

Zum Abschluss der Einleitung folgt ein kurzer Überblick über die nachfolgenden Kapitel: Kapitel 2 entfaltet den theoretischen Hintergrund und klärt zentrale Begriffe; Kapitel 3 beschreibt den Forschungsgegenstand und die Ausgangslage. Kapitel 4 erläutert das methodische Vorgehen, Kapitel 5 präsentiert die Ergebnisse, Kapitel 6 diskutiert deren Einordnung und Kapitel 7 bündelt die Schlussfolgerungen mit einem Ausblick auf weitere Forschungsperspektiven.
