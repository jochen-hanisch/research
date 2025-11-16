\newpage

# 1	Einleitung und theoretischer Rahmen {#sec:1}

Die aktuellen Novellierungen in der Ausbildung der Gesundheitsberufe zielen darauf ab, nicht nur die gesetzlichen Rahmenbedingungen für Gesundheitsberufe anzupassen, sondern die Kompetenzanforderungen zu erweitern und zu präzisieren. So wird besonderer Wert auf die Förderung fachspezifischer, sozialer und methodischer Kompetenzen gelegt, die sich an den wachsenden Herausforderungen im Gesundheitswesen orientieren. Dies spiegelt sich sowohl in den neuen Ausbildungsrichtlinien als auch in den erweiterten Kompetenzprofilen der jeweiligen Berufsgruppen wider [@pflegekammer_nrw_weiterbildungsordnung_2023; @bundesrepublik_deutschland_gesetz_2023].

## 1.1	Erkenntnisinteresse, Problemstellung und Relevanz {#sec:1-1}

Die Ausbildung im Rettungsdienst wurde durch das Gesetz über den Beruf der Notfallsanitäterin und des Notfallsanitäters (NotSanG) zum 01.01.2014 gem. § 5 (1) NotSanG [-@bundesrepublik_deutschland_gesetz_2023] von einer zweijährigen zu einer dreijährigen Qualifikation geändert. Der Gesetzgeber transformierte hierdurch die Tätigkeit weg von einem Assistenzberuf hin zu einer beruflichen Qualifikation, in deren Mittelpunkt das kompetenzorientierte und selbstverantwortliche Handeln nach § 4 NotSanG [-@bundesrepublik_deutschland_gesetz_2023] als Ausbildungsziel definiert wurde. Der Referentenentwurf [-@bundesgesundheitsministerium_referentenentwurf_2012] zum NotSanG verdeutlicht die intendierte Absicht [@bundesgesundheitsministerium_referentenentwurf_2012, Seite 44-45]: Die Auszubildenden sollen insbesondere interdisziplinäre Fachlichkeit erlangen, die zur selbstständigen Lösung aller berufsrelevanter Handlungen sowie deren kritischen und selbstreflektiven Ergebnisbeurteilungen notwendig erscheinen.

Um insbesondere den anerkennungsrechtlichen Erfordernissen aus § 6 (2) 1 [-@bundesrepublik_deutschland_gesetz_2023], namentlich dem "Vorhandensein der für die Ausbildung erforderlichen Räume und Einrichtungen sowie ausreichender Lehr- und Lernmittel"  [@bundesrepublik_deutschland_gesetz_2023] gerecht zu werden, ist in der Ausbildung von Notfallsanitäterinnen und Notfallsanitäter die Verwendung eines digitalen Learning-Management-Systems (LMS) implentiert, welches die Bereitstellung von Lernmaterialien, die Unterstützung kollaborativer Lernprozesse und die Förderung selbstorganisierter Kompetenzentwicklung ermöglicht [@moodle_pty_ltd_was_2019].

Die Grundlage zur Konzeption der benutzen LMS-Architektur findet sich in einer Vorarbeit, die sich insbesondere mit der nachhaltigen, digitalen Sicherung von selbstorganisierten Gruppenarbeitsergebnissen beschäftigte [@hanisch_nachhaltiges_2017]. Diesen Erkenntnissen zur Folge, sind die Faktoren

-   Zeitpunkt der Erfassung und Verfügbarkeit: $\beta = 1{,}213$, $\Delta = 0{,}213$ sowie $\beta = 0{,}251$, $\Delta = 0{,}749$,
-   Struktur des digitalen Systems: $\beta = 2{,}372$, $\Delta = 1{,}372$ und
-   Interaktion der Akteurinnen: $\beta = 0{,}151$, $\Delta = 0{,}849$

für die nachhaltige Sicherung  der selbstorganisierten Gruppenarbeitsergebnisse förderlich [@hanisch_nachhaltiges_2017, Abbildung 2]. Die  in der Studienleistung gewonnenen Ergebnisse nahmen auf die Gestaltung und Nutzung  der digitalen Lernumgebung Moodle® in der Einrichtung erheblichen  Einfluss. Der Aufbau der technischen Architektur wurde als studentischer Projektauftrag  in Zusammenarbeit mit dem BZ durch eine Studierende der FernUniversität in Hagen  während ihres Praktikums im Wintersemester 2016/2017 abgeleitet und geplant. Die hier  vorgestellte Erweiterung und Weiterentwicklung des LMS resultierte aus der pandemischen Situation ab März 2020, in der die Ausbildung von Notfallsanitäterinnen und Notfallsanitätern zunächst kaum mehr in Präsenzunterrichten durchführbar erschien. Aus  der vorherigen intensiven Nutzung des LMS durch die Auszubildenden, war die Verschränkung zwischen Fern- und Präsenzunterricht eine Herausforderung, die in Summe  innerhalb von drei Monaten durch die Umsetzung der inhaltlichen und organisatorischen  Ergänzungen auf Grundlage des Curriculums in das bestehende digitale System bewältigt wurde.

### 1.1.1	Erkenntnisinteresse {#sec:1-1-1}

Eine anonymisierte Ausbildungseinrichtung führt die Ausbildung von Notfallsanitäterinnen und Notfallsanitätern (NFS, NotSan) seit Beginn des ersten Jahrgangs im März 2017 durch. Im Zuge der Konzeption beruflich-currikulater Berufsbildung im Kontext von High Responsibility Teams (HRT) in den Gesundheitsberufen, wurde direkt zu Beginn eine digitale Lernumgebung in Form eines Learning-Management-Systems (LMS) implementiert. Dieses System dient nicht nur der Bereitstellung von Lernmaterialien, sondern auch der Unterstützung kollaborativer Lernprozesse und der Förderung selbstorganisierter Kompetenzentwicklung. Erste Evaluationen deuten darauf hin, dass das LMS einen signifikanten Einfluss auf die Lernprozesse und die Kompetenzentwicklung der Studierenden hat. Allerdings bleiben die zugrunde liegenden Wirkmechanismen und Interaktionen zwischen den technologischen, didaktischen und sozialen Komponenten weitgehend unklar.

Das zentrale Erkenntnisinteresse dieser Forschungsarbeit besteht darin, das Wirkgefüge eines eingesetzten Learning-Management-Systems (LMS) im digitalen Bildungsraum der Gesundheitsberufe systematisch zu analysieren. Im Mittelpunkt steht die Frage, wie Lern-, Handlungs- und Kompetenzentwicklungsprozesse durch das Zusammenspiel technologischer, didaktischer und sozialer Mechanismen beeinflusst werden und welche emergenten Muster sich dabei ausbilden – gerade weil Gesundheitsberufe zwischen engen regulatorischen Vorgaben, multiprofessionellen Lernsettings und hohen Anforderungen an dokumentierte Kompetenzentwicklung vermittelt werden müssen [@hanisch_notfallsanitater_2020; @pentzold_praxis_2018].

Von besonderem Interesse ist, wie Akteurinnen, d.h. Lernende, Lehrende und Organisationen, das LMS interpretieren, nutzen und in ihre eigenen Selbstorganisations- und Entscheidungsprozesse integrieren. Damit richtet sich das Erkenntnisinteresse nicht auf die isolierte Bewertung einzelner Funktionen des LMS, sondern auf die Aufklärung der kausalen Interdependenzen, die zwischen System, Akteurinnen und digitalen Infrastrukturen entstehen [@parker_negotiating_2024; @van_niekerk_addressing_2025].

Im Rahmen dieses Forschungsansatzes wird davon ausgegangen, dass die Anwendung systemisch‑konstruktivistischer Theorie nicht nur für die curriculare Gestaltung und Durchführung von Lernprozessen relevant ist, sondern auch für die Architektur und den Betrieb von Learning‑Management‑Systemen. Es wird daher untersucht, inwiefern die LMS‑Struktur, ihre Nutzungsdynamiken und die durch sie erzeugten Rückkopplungen Aufschluss darüber geben, wie Kompetenzen im digitalen Bildungsraum entstehen und stabilisiert werden [@doring_forschungsmethoden_2023; @mey_qualitative_2010].

Die Arbeit verfolgt damit ein doppelt gerichtetes Erkenntnisinteresse: Einerseits sollen die beobachtbaren Wirkmechanismen systematisch identifiziert und theoretisch erklärbar gemacht werden; andererseits sollen daraus prospektive Einsichten gewonnen werden, die es ermöglichen, zukünftige Bildungsräume gezielt zu gestalten. In diesem Sinne geht es nicht nur um die retrospektive Analyse bestehender Effekte, sondern ebenso um die Entwicklung einer theoretisch fundierten Grundlage für prognostische Aussagen zu gewünschten Wirkungen [@reinders_uberblick_2022; @schnell_methoden_2013].

### 1.1.2	Problemstellung {#sec:1-1-2}



### 1.1.3	Thematische Relevanz {#sec:1-1-3}

## 1.2	Forschungsfragen und methodische Vorüberlegungen {#sec:1-2}

### 1.2.1	Zugrundliegende Vermutungen {#sec:1-2-1}

### 1.2.2	Ziel der Forschung {#sec:1-2-2}

Transdisziplinäre Zielsetzung unter Berücksichtigung medizinischer und bildungswissenschaftlicher Aspekte.

### 1.2.3	Herleitung Haupt- und Unterforschungsfragen {#sec:1-2-3}

Wissenschaftliche und praxisorientierte Erkenntnisinteressen.

**Herleitung**

> Wie beschrieben, fehlt eine Untersuchung der Wirkfaktoren, weshalb die bisherigen Ergebnisse unter Einsatz des LMS erzielt werden konnten. Diese Wirkfaktoren können als Herleitung und Begründung des Forschungsvorhabens dienen. Die zugrundeliegende Vermutung ist, dass die konsequente Anwendung des systemisch-konstruktivistischen Theoriegebäudes nicht nur bei der curricularen Konzeption oder bei der Durchführung von Lehrveranstaltungen, sondern gerade auch bei der Entwicklung einer Learning-Management-System-Architektur die beobachtbare Wirkung nicht nur erklärt, sondern darüber hinaus, Prognosen von zukünftigen gewünschten Wirkungen ermöglicht. Die Vermutung ist weiterhin, dass alle notwendigen Theorien und Erklärungen bereits in den unterschiedlichsten Wissenschaftsdisziplinen vorhanden sind. Aus den hier genannten Vermutungen lassen sich seriös kaum Forschungshypothesen ableiten, die definitionsgemäß auf bestehende Theorien aufbauen [@doring_forschungsmethoden_2023, Seite 146]. Die handlungsleitende Hauptforschungsfrage (FH) kann demnach wie folgt gestellt werden:

„Wie ist das Wirkgefüge des angewendeten Learning-Management-Systems auf Akteure im digitalem Bildungsraum von Gesundheitsberufen gestaltet?“ \label{fh}

> Die Forschungsfrage ist absichtlich eng gefasst, da ein bestehendes Learning-Management-System betrachtet wird. Weiterhin besteht die aufgrund einer weit gefassten Begriffsauslegung die Notwendigkeit, die Forschungsfrage in ihrer Syntax zu entfalten Insbesondere kommt der Operationalisierung eine wesentliche Bedeutung zu: die beobachtbaren Indikatoren werden dem theoretischem Begriff zugeordnet [@schnell_methoden_2013, Seite 7]. Ziel und Zweck der Forschungsfrage ist die Betrachtung der Anwendung des eingesetzten Medientools LMS (Seite 7) im digitalem Bildungsraum (Seite 6, 5). Als zentraler Begriff, der zu operationalisieren ist, steht das Wirkgefüge (Seite 6) im Fokus. Der Kontext, in dem die Bearbeitung stattfindet, ist in den Gesundheitsberufen (Seite 7) zu finden, in dessen Kontext Akteure (Seite 7) agieren. Zur Operationalisierung wurde der Begriff der Gestaltung ausgewählt.

Die detaillierte Zuordnung der Forschungsunterfragen (FU1–FU7) zu den eingesetzten Methoden sowie den jeweiligen Erfüllungskriterien ist in Kapitel 4.2 <<<VERWEIS>>> (Forschungsdesign und Datenerhebung) dargestellt.


## 1.3 Stand der Forschung und Forschungslücke {#sec:1-3}

- [ ] Überblick über die bisherigen Studien und relevante Literatur zum Thema.
- [ ] legt den Stand der Forschung dar und entwickelt die Fragestellung. 

Die Untersuchung legt nahe, dass künftige Forschungen sich verstärkt auf die Analyse der Lernaktivitäten und deren Auswirkungen auf die Lernenden konzentrieren sollten. Die Autoren betonen insbesondere die Notwendigkeit, zukünftige Forschungsarbeiten darauf auszurichten, wie unterschiedliche CBL-Methoden in spezifischen medizinischen Bildungskontexten wirksam eingesetzt werden können.

> Der menschliche Bildungsprozess ist von einer ständigen Wechselwirkung zwischen grundlegenden emotionalen und kognitiven Bedürfnissen sowie den Unsicherheiten geprägt, die beim Lernen und der Kompetenzentwicklung auftreten. Bedürfnisse wie Bindung, Selbstwerterhöhung und die Vermeidung von Unlust bilden die Basis für eine dynamische Kausalkette, die das Lernverhalten antreibt. Aus den Bedürfnissen heraus entstehen Unsicherheiten im Lernprozess und in der Kompetenzmessung, die das Handeln der Lernenden prägen. Diese Handlungen zielen darauf ab, die Unsicherheiten zu verringern und das Bedürfnis nach Selbstverwirklichung zu befriedigen. In dieser kontinuierlichen Zirkulation beeinflussen sich Bedürfnisse, Konzepte und Handlungen wechselseitig und treiben den Lernprozess stetig voran.

### 1.3.1	Theoretische und empirische Vorüberlegungen {#sec:1-3-1}

### 1.3.2	Literaturrecherche {#sec:1-3-2}

### 1.3.3	Identifikation der Forschungslücke {#sec:1-3-3}

Eine der dem Untersuchungsgegenstand am nächsten kommenden Studien stammt von Fonseca et al. [-@fonseca_collaborative_2024]. Diese Untersuchung zeigt, dass digitale Communities of Practice (CoPs) eine zentrale Rolle für den Erfolg kollaborativer Lernökosysteme spielen. Erfolgreiche Collaborative Learning Ecosystems (CESs) zeichnen sich durch klare Kommunikationsstrukturen, dynamische soziale Interaktionen sowie flexible Lerntechnologien aus. Die Studie liefert konkrete Designprinzipien, die zur Entwicklung nachhaltiger digitaler Lernräume genutzt werden können. Auf dieser Grundlage wird ein neues Modell für digitale Lernökosysteme entwickelt, das kollaborative Lernprozesse mit technologischen und sozialen Aspekten verbindet. (@fonseca_collaborative_2024, Seite 130, 134, 137)
Während die genannte Untersuchung wertvolle Erkenntnisse über die Bedeutung von Communities of Practice (CoPs) und Collaborative Learning Ecosystems (CESs) liefert, fehlt in der bisherigen Forschung eine systemische Erklärung der Wirkmechanismen digitaler Bildungsräume. Die bisherigen Studien konzentrieren sich primär auf die empirische Analyse einzelner Erfolgsfaktoren und Designprinzipien, ohne die kausalen Interdependenzen zwischen den beteiligten Elementen umfassend zu modellieren.
Die vorliegende Forschungsarbeit schließt diese Lücke, indem sie das Wirkgefüge eines Learning-Management-Systems (LMS) in der medizinischen Lehre systemisch analysiert. Im Gegensatz zu bestehenden Studien, die digitale Lernräume als Sammlung von Einzelfaktoren betrachten, wird in dieser Untersuchung ein holistisches Modell entwickelt, das nicht nur beschreibt, was funktioniert, sondern wie die verschiedenen Elemente eines digitalen Bildungsraumes interagieren und sich wechselseitig beeinflussen. Ein entscheidender Unterschied zur bisherigen Forschung ist der systemtheoretische Ansatz, der die Identifikation  emergenter Strukturen und autopoietischer Stabilisierungseffekte innerhalb digitaler Lernumgebungen ermöglicht. Während empirische Studien bereits Hinweise auf erfolgreiche kollaborative Lernmodelle liefern, fehlt eine tiefgehende Analyse der zugrunde liegenden Kausalketten, die diese Erfolgsfaktoren miteinander verbinden.
Diese Arbeit setzt an dieser Stelle an, indem sie ein systemisches Modell des digitalen Bildungsraums entwickelt und untersucht, welche strukturellen Bedingungen die nachhaltige Wirksamkeit eines LMS beeinflussen. Durch diese systemische Perspektive wird nicht nur die bestehende Forschung ergänzt, sondern auch eine theoretische Grundlage geschaffen, um digitale Bildungsräume nicht nur retrospektiv zu bewerten, sondern auch prospektiv zu gestalten. Dies erlaubt eine Ableitung fundierter Gestaltungsrichtlinien für zukünftige Bildungsumgebungen, die auf einer systemisch erklärbaren Wechselwirkung zwischen technologischen, sozialen und didaktischen Faktoren basieren.

## 1.4 Aufbau der Arbeit {#sec:1-4}

Die Struktur des vorliegenden Forschungsprojekts weist aufgrund der transdisziplinären Ausrichtung zwischen Bildungswissenschaft und Medizin eine besondere Komplexität auf, da verschiedene Disziplinen integriert und unterschiedliche wissenschaftliche Anforderungen berücksichtigt werden müssen. Um dieser Herausforderung gerecht zu werden, folgt der strukturelle Aufbau der Arbeit einer konsequenten Verschränkung der formalen Anforderungen sowohl der medizinischen als auch der kultur- und sozialwissenschaftlichen Rahmenbedingungen. Dies ermöglicht eine umfassende Bearbeitung des Themas, die den jeweiligen spezifischen Gegebenheiten beider Disziplinen gerecht wird.

Zum Abschluss der Einleitung folgt ein kurzer Überblick über die nachfolgenden Kapitel: Kapitel 2 entfaltet den theoretischen Hintergrund und klärt zentrale Begriffe; Kapitel 3 beschreibt den Forschungsgegenstand und die Ausgangslage. Kapitel 4 erläutert das methodische Vorgehen, Kapitel 5 präsentiert die Ergebnisse, Kapitel 6 diskutiert deren Einordnung und Kapitel 7 bündelt die Schlussfolgerungen mit einem Ausblick auf weitere Forschungsperspektiven.
