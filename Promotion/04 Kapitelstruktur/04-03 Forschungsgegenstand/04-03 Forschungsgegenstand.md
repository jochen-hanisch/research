\newpage

# 3 Beschreibung des Forschungsgegenstandes {#sec:3}

Kapitel 3 beschreibt Entstehung, Kontext und Architektur des untersuchten Learning-Management-Systems. Es konkretisiert damit die in \hyperref[sec:2]{Kapitel 2} entwickelten theoretischen Überlegungen für den spezifischen Anwendungsfall und bereitet die spätere Ergebnisdarstellung in \hyperref[sec:5]{Kapitel 5} vor.

Folgerung für die Darstellung
Konsequenzen klar zweiteilig gliedern:
(a) rechtlich-funktional,
(b) didaktisch-strukturell
LMS = Schnittstelle zwischen Norm und Didaktik


## 3.1 Kontext des Forschungsgegenstandes {#sec:3-1}

### 3.1.1 Rechtlich-funktionale Rahmung {#sec:3-1-1}

Das hier zu beschreibende Learning Management System wird im Rahmen in der Lehre der durch die europäische Richtlinie 2005/36/EG reglementierten Gesundheitsberufe, insbesondere in der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern, eingesetzt. Der Begriff der Gesundheitsberufe ist nicht definiert und fasst alle Berufe zusammen, deren Tätigkeitsfeld im Wesentlichen im Gesundheitssektor angesiedelt ist. Für einen Teil dieser Berufe sind Ausbildung und Prüfung gesetzlich geregelt; diese Berufe stehen im Mittelpunkt der hier angestellten Betrachtungen und werden den reglementierten Berufen, und damit der Gesetzgebungskompetenz des Bundes zugeordnet. Die reglementierten Heilberufe fassen Berufe zusammen, deren Tätigkeiten insbesondere heilende und medizinisch-assistierende Anteile als charakteristisches Merkmal aufweisen. Aus der staatlichen Zuordnung folgt, dass die Führung der Berufsbezeichnung entweder durch eine Approbation oder durch eine behördliche Erlaubnis auf Antrag erworben werden kann. [@bundesgesundheitsministerium_gesundheitsberufe_2025]

Im Anwendungsfeld der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern sowie die Erlaubnis zum Führen der Berufsbezeichnung unterliegt der o.a. staatlichen Regelung. Maßgeblich verantwortlich für die gesetzeskonforme Umsetzung ist nach § 5 Abs. 3 Satz 4 NotSanG die Schule, in deren Gesamtverantwortung die „Organisation und Koordination des theoretischen und praktischen Unterrichts und der praktischen Ausbildung entsprechend dem Ausbildungsziel“ [@bundesrepublik_deutschland_gesetz_2023, § 5 Abs. 3 Satz 4] liegt. Die genaue Bedeutung dieses Auftrages verdeutlichen Dielmann & Malottke [@dielmann_notfallsanitatergesetz_2017, S. 137–138] in ihrem Kommentar und bieten damit eine zentrale normierte Grundlage zur Herleitung der Rolle eines Learning Management Systems innerhalb der Ausbildung und Prüfung von Notfallsanitäterinnen und Notfallsanitätern.

Den Kommentatoren nach obliegt der Schule zwar die Gesamtverantwortung zur Organisation und Koordination des Unterrichtes und der praktischen Ausbildung, jedoch ist diese Verantwortlichkeit nicht auf die gesamte Ausbildung übertragbar. Diese liegt beim Träger der Ausbildung und muss auch von ihm wahrgenommen werden. Das Ziel der Organisation und Koordination ist demzufolge die sinnvolle, strukturierte Verzahnung der Lernorte Lehrrettungswache, Schule und Krankenhaus entlang des gesetzlich vorgegebenen Ausbildungsziels gem. § 4 NotSanG [@bundesrepublik_deutschland_gesetz_2023, § 4]. Infolgedessen steht die Schule in der Verantwortung der Koordination mit gleichzeitigem Ausschluss der hoheitlichen Deutung. Demnach kann die Schule gestalterisch tätig sein, jedoch ist diese Gestaltung nicht als autonom anzusehen. [@dielmann_notfallsanitatergesetz_2017, S. 137–138]

Die Konsequenzen des Einsatzes eines Learning-Management-Systems können entlang der Dimensionen Werkzeugfunktion, Kohärenzsicherung und Abgrenzung schulischer und trägerschaftlicher Verantwortung weiter differenziert werden.
Aufgrund der Koordinations- und Organisationsverantwortung der Schule lässt sich aus den bisherigen Überlegungen ableiten, dass das hier behandelte Lernmanagementsystem als das gesetzlich geforderte Steuerungsinstrument angesehen werden kann, das zur Umsetzung der gesetzlichen Verpflichtung geeignet erscheint. Erst die nachvollziehbare und standardisierte Zusammenführung von Kursen, Kalendern, Lernfortschritten, Aufgaben und Einsatzberichten in E-Portfolios innerhalb einer digitalen Struktur kann die Ausbildungsabschnitte und unterschiedlichen Lernorte strukturell miteinander verknüpfen. Ergänzend bildet die Integration von Fallbearbeitungen, Praxisreflexionen sowie zeitunabhängigen, dokumentierten Reflexionsprozessen das didaktische Gerüst, das die Koordination zwischen den Lernorten sowie den theoretischen und praktischen Ausbildungsanteilen systematisch stützt. Unter diesen Voraussetzungen ist das LMS ein operationalisiertes Werkzeug zur Wahrnehmung der schulischen Verantwortung zur Koordination und Organisation.

In den o.a. Ausführungen wird die Notwendigkeit verwiesen, individuelle Ausbildungspläne so zu gestalten, dass Rahmenlehrpläne bzw. die rechtlichen Ausbildungsbestimmungen umgesetzt werden können. Ableitend davon, ergibt sich die Verpflichtung zur Kohärenz von Rahmenlehrplan, Stundenplan und Einsatzplan sowie deren inhaltlichen Anteile zueinander. Das LMS muss folglich in der Lage sein, die einzelnen Elemente individuell und lernortspezifisch aufeinander abzustimmen. Damit fungiert das Learning Management System als strukturelles Bindeglied zwischen Theorie (Stundenplan), Praxis (Einsatzorte) und Individualisierung (Ausbildungspläne) und verfügt über die Möglichkeit, diese disjunkten Elemente über Planungs- und Synchronisationsfunktionen miteinander zu verbinden.

Wenn Schule nicht die insgesamte Ausbildungsverantwortung übernimmt, sondern der Ausbildungsträger sich ihrer als Erfüllungsgehilfin bedient, ergibt sich daraus im rechtlichen Sinne eine funktionale Verpflichtung zum Einsatz eines digitalen Koordinations- und Organisationsinstruments. Der Ausbildungsträger bleibt nach obiger Lesart haftungsrechtlich in der Verantwortung und durch den Einsatz des LMS durch die Schule übernimmt diese einen Teil genau dieser Verantwortlichkeit, ohne gleichzeitig selbst in die Trägerrolle zu wechseln. Durch den Einsatz eines digitalen Systems können alle rechtlich geforderten Dokumentations- und Nachweispflichten beispielsweise durch Logfiles, Beitragszeiten in Foren und Berichtsabfragen auch in Echtzeit gewährleistet werden. Hierin unterscheidet sich ein Learning Management System signifikant von anderen analogen oder konventionellen Lösungen.
Der bisherigen Argumentation folgend ist der Einsatz des hier beschriebenen Learning Management Systems als ausbildungsrechtlich notwendige Infrastruktur zur Erfüllung schulischer Aufgaben zu verstehen. Die gesetzlich übertragene Verantwortung zur Koordination und Organisation der Ausbildung von Notfallsanitäterinnen und Notfallsanitätern lässt sich ohne ein entsprechendes System kaum mehr realisieren, insbesondere unter Berücksichtigung heutiger Möglichkeiten im digitalen Bildungsraum.

### 3.1.2 Didaktisch-strukturelle Verortung {#sec:3-1-2}

Hier weiter mit Argumentation aus \hyperref[sec:2-1]{Kapitel 2.1} fortführend.

Didaktische Rahmung
Schule = nicht nur juristische Instanz, sondern auch didaktisches Konstrukt
LMS = didaktische Infrastruktur, um Lernprozesse zwischen den Lernorten kohärent zu verknüpfen
Anschluss an Theoriekapitel (-> Bildung als Wirkgefüge / digitale Dispositive / Lernraumlogiken)

Table: Konsequenzen für das LMS innerhalb der rechtlich-funktionalen Rahmung \label{tab:lms-konsequenzen}

| Stichwort | Erklärung | Quellenverweis |
| --- | --- | --- |
| Verantwortung der Schule für Lernorttransfer | LMS als systemisches Steuerungsinstrument innerhalb der schulischen Gesamtverantwortung. | NotSanG, § 5 Abs. 3 [@bundesrepublik_deutschland_gesetz_2023]; NotSan-APrV, § 2 Abs. 1–3 [@bmg_ausbildungs-_2023] |
| Aktive Begleitung durch Schule | LMS muss Funktionen für Reflexion, Kommunikation und Dokumentation der Praxisbegleitung bereitstellen. | NotSan-APrV, § 2 Abs. 3 [@bmg_ausbildungs-_2023] |
| Strukturierte Zusammenarbeit zwischen Schule und praktischer Ausbildungseinrichtung | Erfordert Kommunikations- und Kooperationsfunktionen zwischen Schule und Praxispartnern. | NotSanG, § 5 Abs. 3 [@bundesrepublik_deutschland_gesetz_2023]; NotSan-APrV, § 2 Abs. 2–3 [@bmg_ausbildungs-_2023] |
| Rechtsverbindlichkeit | LMS-Einsatz muss mit normativen Vorgaben vereinbar sein und Nachweismöglichkeiten bieten. | NotSanG, § 11 [@bundesrepublik_deutschland_gesetz_2023]; NotSan-APrV, Einleitung [@bmg_ausbildungs-_2023] |
| Pädagogisch-didaktischer Anspruch steigt | Komplexe didaktische Szenarien müssen abbildbar sein (z. B. Kompetenzraster, ePortfolio etc.). | NotSanG, § 4 [@bundesrepublik_deutschland_gesetz_2023]; NotSan-APrV, Anlage 1 [@bmg_ausbildungs-_2023] |
| Qualitätssicherung durch digitale Unterstützung | LMS muss evaluierbare und standardisierte Prozesse zur Qualitätssicherung ermöglichen. | Referentenentwurf NotSan-APrV, S. 44–45 [@bundesgesundheitsministerium_referentenentwurf_2012, S. 44–45] |
| Anschlussfähigkeit an akademische Systeme | LMS sollte Anschlussfähigkeit an hochschulische Systeme und Studiengänge berücksichtigen. | Bundesgesundheitsministerium (Gesundheitsberufe) [@bundesgesundheitsministerium_gesundheitsberufe_2025] |


Weiter mit Schule

Weiter mit HRT




## 3.2 Entwicklung und Einbettung des Learning-Management-Systems {#sec:3-2}

### 3.2.1 Entstehungskontext {#sec:3-2-1}

### 3.2.2 Implementierung in der schulseitigen Praxis {#sec:3-2-2}

### 3.2.3 Weiterentwicklung durch externe Anforderungen {#sec:3-2-3}

### 3.2.4 Evaluation und Reflexion {#sec:3-2-4}

## 3.3 Didaktische Architektur als Learning-Environment {#sec:3-3}

### 3.3.1 Konzeptionelle Grundkonstruktion {#sec:3-3-1}

### 3.3.2 Didaktisch-architektonische Umsetzung {#sec:3-3-2}

### 3.3.3 Prüfungsarchitektur {#sec:3-3-3}

### 3.3.4 Statistische Analyse curriculare Struktur {#sec:3-3-4}

## 3.4 Operative Architektur als Arbeits- und Lernumgebung {#sec:3-4}

## 3.5 E-Portfolio als Reflexions- und Transferinstrument {#sec:3-5}

## 3.6 Technische Rahmenbedingungen {#sec:3-6}
