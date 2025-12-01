## **Kompetenzentwicklung in High Responsibility Teams (HRT), speziell für Notfallsanitäter**

## **Ziel**
Entwicklung einer Referenzkurve, die eine idealtypische Kompetenzentwicklung für Notfallsanitäter darstellt, basierend auf der Kompetenzdefinition und den Charakteristika von HRT.

## **Hintergrund:**
- **Kompetenzdefinition**: „Kompetenz im Kontext von High Responsibility Teams ist die individuelle Bereitschaft, Operationen auf ausbildungsrechtlichen Grundlagen zu planen, deren Wirkung zu angemessenem und brauchbarem Handeln führt, um Transformationsbarrieren vom unerwünschten zum erwünschten Zustand zu überwinden.“ (Hanisch, 2023, S. 81)
- **Charakteristika von HRT**: Notfallsanitäter in HRT zeichnen sich durch irreversiblen Handlungen, potenzielle Gefahr für Dritte, Verantwortung für das Leben anderer und die Notwendigkeit, Handlungen nicht unterbrechen zu können, aus.

## **Beobachtungen:**
Zusätzliche dynamische Faktoren basierend auf Beobachtungen:
- **Verständnis der Didaktik**: Nach einer moderaten Steigung, Integration einer initialen Verzögerung in der Kompetenzentwicklung, da die Auszubildenden ca. 5 bis 6 Quartale benötigen, um die Didaktik der Ausbildung vollständig zu verstehen.
- **Stagnation in den ersten Quartalen**: Modelliere eine Phase der Stagnation oder leichten Rückgangs der Kompetenzentwicklung in den ersten 4 bis 6 Quartalen.
- **Plateauphase**: Nach etwa 10 Quartalen erreicht die Kompetenzentwicklung ein Plateau.
- **Motivationsknick**: Implementiere einen "Knick" in der Motivation beim Übergang vom zweiten zum dritten Ausbildungsjahr.
- **Steigerung in den letzten Quartalen**: Eine gesteigerte Kompetenzentwicklung in den letzten beiden Quartalen, insbesondere während der Prüfungsvorbereitung.

## Verwende dabei die folgenden Wahrscheinlichkeitsverteilungen für die entsprechenden Variablen:
### **Weibull-Verteilung**
- für die Modellierung der allgemeinen Entwicklung von Kompetenzen über die Zeit. Setze spezifische Form- und Skalenparameter, um unterschiedliche Entwicklungsmuster zu simulieren.

### **Normalverteilung**
- **Individuelle Lerngeschwindigkeit und Aufnahmefähigkeit (ILG)**: Grundlegende Fähigkeit zum Erlernen neuer Kompetenzen.
- **Selbstreflexions- und Selbstkritikfähigkeit (SRSK)**: Fähigkeit zur Reflexion über das eigene Handeln.
- **Emotionale Stabilität und Stressbewältigung (ESS)**: Wichtig für die effektive Ausübung des Berufs unter Stress.
- **Anpassungsfähigkeit an wechselnde Situationen (AWSA)**: Flexibilität in unterschiedlichen Einsatzbedingungen.
- **Problemlösungsfähigkeiten und Entscheidungsfindung (PLE)**: Anwendung algorithmenbasierter Handlungen.
- **Konfliktlösungs- und Kooperationsfähigkeit (KKF)**: Wichtig für Teamarbeit und Konfliktbewältigung.
- **Anwendung standardisierter medizinischer Verfahren (ASMV)**: Anwendung standardisierter Verfahren in der Notfallmedizin.

### **Beta-Verteilung**
- **Motivation und Engagement für den Beruf (MEB)**: Hohe Motivation und Engagement für den Beruf.
- **Kommunikations- und Teamarbeitsfähigkeit (KTF)**: Teamorientierte Fähigkeiten in der notfallmedizinischen Versorgung.
- **Empathie und Patientenbetreuung (EPB)**: Berücksichtigung der Patientenperspektive.
- **Berücksichtigung persönlicher und situativer Umstände (BPSU)**: Anpassung des Handelns an Patientenumstände.

### **Poisson-Verteilung**
- **Unerwartete Ereignisse**: Erfassung seltener, unvorhersehbarer Ereignisse, für das Auftreten persönlicher Ereignisse (PE): während der Ausbildung. Bestimme die Rate λ (Lambda) für die Häufigkeit dieser Ereignisse. Datenbasis für die persönlichen Ereignisse:
	- Familiäre Ereignisse (PFE): 12,5%
	- Bedeutende Lebensveränderungen (PLE): 8,33%
	- Finanzielle Veränderungen (PFV): 20,83%
	- Gesundheitliche Veränderungen (PGV): 12,5%
	- Soziale Ereignisse (PSE): 41,67%
	- Persönliche Erfolge/Herausforderungen (PEE): 4,17%

### **Wechselwirkungen zwischen den Variablen**:
- **Wechselwirkung zwischen ILG (Individuelle Lerngeschwindigkeit und Aufnahmefähigkeit) und ASMV (Anwendung standardisierter medizinischer Verfahren)**:
	- Eine höhere ILG könnte die Fähigkeit zur schnellen Aneignung und effizienten Anwendung standardisierter medizinischer Verfahren verbessern.
- **Interaktion zwischen ESS (Emotionale Stabilität und Stressbewältigung) und BPSU (Berücksichtigung persönlicher und situativer Umstände)**:
	- Starke ESS unterstützt die Fähigkeit, in herausfordernden Situationen empathisch und patientenorientiert zu handeln, was für die adäquate Berücksichtigung persönlicher und situativer Umstände der Patienten essenziell ist.
- **Beziehung zwischen MEB (Motivation und Engagement für den Beruf) und AWSA (Anpassungsfähigkeit an wechselnde Situationen und Anforderungen)**:
	- Ein hohes Maß an MEB fördert die Bereitschaft, sich an verschiedene situative Bedingungen anzupassen und fortlaufend neues Wissen zu erwerben.
- **Zusammenhang zwischen KTF (Kommunikations- und Teamarbeitsfähigkeit) und KKF (Konfliktlösungs- und Kooperationsfähigkeit)**:
	- Effektive KTF verbessert die Fähigkeit zur Konfliktlösung und Kooperation im Team, was wiederum für eine effiziente Teamarbeit in Notfallsituationen entscheidend ist.
- **Wechselwirkung zwischen EPB (Empathie und Patientenbetreuung) und ASMV/BPSU**:
	- Hohe EPB unterstützt die adäquate Anwendung medizinischer Verfahren unter Berücksichtigung individueller Patientenbedürfnisse und situativer Umstände.

## **Simulationsparameter:**
- **Anzahl der Simulationsläufe:**
	- Für normal- und Beta-verteilte Variablen wurde eine gute Konvergenz der Mittelwerte und Varianzen im Bereich von 10.000 bis 25.000 Durchläufen beobachtet.
	- Für Poisson-verteilte Variablen zeigte sich ebenfalls eine stabile Konvergenz im gleichen Durchlaufbereich.
- **Anfangskompetenzniveau:**
	- Hintergrundinformationen:
		- **Ausbildungsumfang**: Notfallsanitäterausbildung umfasst insgesamt 4600 Stunden, während die Rettungssanitäterausbildung 520 Stunden umfasst.
		- **Annahme**: Das Kompetenzniveau eines vollständig ausgebildeten Notfallsanitäters entspricht auf der Skala einem Wert von 10.
	- Bestimmung des Anfangskompetenzniveaus:
		- Unter Berücksichtigung des Verhältnisses der Ausbildungsstunden, schätze das Anfangskompetenzniveau der als Rettungssanitäter qualifizierten Teilnehmer auf der Skala von 0-10.
		- **Berücksichtigung individueller Unterschiede**: Erwäge, dass die Kompetenzniveaus individuell variieren können, basierend auf persönlichen Erfahrungen und Fähigkeiten.
		- **Integration in die Simulation**: Nutze diese Einschätzung als Ausgangspunkt für die weitere Entwicklung in der Monte Carlo Simulation.
- **Integration von Feedback-Schleifen:**
	- Dynamische Anpassung der Kompetenzentwicklung basierend auf Erfahrungen und Feedback.
	- Messung und Anpassung der Parameter im Laufe der Zeit.
	- Die oben genannten Beobachtungen werden berücksichtigt.
- **Integration der Zeitachse in die Simulation:**
	- **Monatliche Simulation**: Die Simulation soll in monatlichen Intervallen durchgeführt werden, um die kontinuierliche Entwicklung der Kompetenzen und die Auswirkungen von Erfahrungen und Feedback-Schleifen präzise abzubilden.
	- **Quartalsweise Darstellung der Ergebnisse**:
		- Die Ergebnisse der Simulation werden quartalsweise dargestellt, um einen klaren Überblick über die Kompetenzentwicklung im Zeitverlauf zu bieten. Dies entspricht vier Quartalen pro Ausbildungsjahr.
		- Jedes Quartal repräsentiert eine aggregierte Darstellung der monatlichen Entwicklungen und Veränderungen in den Kompetenzen der Notfallsanitäter.
		- **Gesamtdauer der Simulation**:
		- Die Simulation deckt den gesamten Zeitraum der Notfallsanitäterausbildung ab, welcher insgesamt drei Jahre (drei Ausbildungsjahre) umfasst.
		- Dies ermöglicht es, die vollständige Entwicklung der Kompetenzen von Anfang bis Ende der Ausbildung zu verfolgen und zu analysieren.
		- Das Kompetenzniveau (y-Achse) soll auf eine Nominalskala in den Grenzen 0 bis 10 bezogen werden.

## Darstellung:
- Die Beschriftung der x-Achse soll „Quartal“ sein.
- Die Beschriftung der y-Achse soll „Niveau“ sein.
- Die Skalierung der x-Achse soll in Quartalsschritten sein.
- Die Skalierung der y-Achse soll auf einer dimensionslosen Nominalskala 0 bis 10 sein.
- Beide Ursprünge der x- und y-Achse sollen einem Koordinatensystem gleichen.    passt grundsätzlich, jedoch wächst die Kurve zu steil und in einer zu kurzen Zeit an. Nochmal meine Beobachtungen, ich beschreibe diese in absoluter Zeit zur Gesamtausbildungsdauer von 36 Monaten:

- - moderate bis höhere Steigerung in der ersten 3-4 Monaten, da Auszubildende sich freuen 
- - eher weniger Steigung, da Ernüchterung, dass die Ausbildung nicht nur Medizin beinhaltet, 
- - nach ca. 12 - 18 Monaten haben die Auszubildenden das System verinnerlicht, bis dahin gibt es ein auf und ab
- - Hiernach eine Plateau Phase, die bis ca. zweites Drittel dauert und irgdwo dort einen signifikanten Knick erhält.
- - dieser Knick hält ca. 2-3 Monate an und baut sich moderat wieder auf 
- - ca. 2 Monate vor Ausbildungsende gibt es noch mal einen Signifikanten Anstieg de Komentenz durch die intensive  Prüfungsvorbereitung