---
author: Jochen Hanisch-Johannsen
title: Kognitivismus
created: 2024-10-02
updated: 2024-10-13
tags:
  - "#Kognition"
  - "#Lernprozess"
  - "#Didaktik"
  - "#Lernmethoden"
  - "#Konstruktivismus"
  - "#Metakognition"
  - "#Wissensverarbeitung"
project: 
type:
  - Theoretische Notiz
publish: false
---
# 1 Definition

Der **kognitivistische Ansatz** betont die Rolle interner kognitiver Prozesse wie Wahrnehmung, Gedächtnis, Problemlösung und Informationsverarbeitung im Lernprozess. Lernen wird als aktiver und strukturierter Prozess verstanden, bei dem Lernende neue Informationen mit ihrem bestehenden Wissensbestand verknüpfen und diese durch Anwendung kognitiver Strategien integrieren. Die Instruktion zielt darauf ab, diese Prozesse durch geeignete didaktische Methoden wie Visualisierungen, Analogien und Strukturierung von Lerninhalten zu unterstützen. Im Vergleich zum Konstruktivismus ist der Kognitivismus stärker strukturiert, ermutigt jedoch auch zu selbstgesteuertem Lernen und Problemlösung.

# 2 Herleitung

## 2.1 Grundprinzipien des kognitivistischen Ansatzes

Die Basis des kognitivistischen Ansatzes liegt in den folgenden Grundprinzipien:

- **Informationsverarbeitung**: Lernen wird als Aufnahme, Verarbeitung und Speicherung von Informationen verstanden. Lernende agieren als aktive Teilnehmer, die neue Informationen in ihr bestehendes Wissensnetzwerk integrieren.

- **Wissensorganisation**: Wissen ist strukturiert und wird in Form von Schemata oder mentalen Modellen gespeichert. Diese helfen den Lernenden, neue Informationen logisch zu organisieren und zu speichern.

- **Kognitive Strategien**: Der Ansatz betont die Bedeutung von Lernstrategien wie Wiederholung, Elaboration und Visualisierung, die Lernende einsetzen, um Informationen effektiver zu verarbeiten.

- **Metakognition**: Metakognitive Fähigkeiten – das Bewusstsein und die Kontrolle über die eigenen Lernprozesse – sind entscheidend für das effektive Lernen. Lernende, die ihre eigenen Denkprozesse verstehen und steuern können, lernen effizienter.

## 2.2 Mathematische Modellierung des kognitivistischen Ansatzes

Der kognitivistische Ansatz kann durch mathematische Modelle beschrieben werden, um die Dynamik der Wissensverarbeitung und den Einfluss kognitiver Strategien auf das Lernen zu analysieren.

### 2.2.1 Modellierung der Wissensverarbeitung

1. **Definition der Variablen**

    - $K(t)$: Wissensstand einer Person zum Zeitpunkt $t$.
    - $E(t)$: Erfahrungsvariablen, die den Einfluss neuer Erlebnisse und Interaktionen auf den Wissensstand beschreiben.
    - $M(t)$: Metakognitive Variablen, die den Grad der Reflexion und Kontrolle über die eigenen Lernprozesse anzeigen.
    - $S(t)$: Einsatz kognitiver Strategien (z.B. Wiederholung, Visualisierung).

2. **Funktionen und Parameter**

   Die Veränderung des Wissensstands über die Zeit kann durch die folgende Gleichung beschrieben werden:

   $$
   K(t+1) = K(t) + \Delta t \cdot \left( \alpha \cdot E(t) + \beta \cdot S(t) + \gamma \cdot M(t) \right)
   $$

   Hierbei:

   - $\alpha$: Gewichtungsfaktor für den Einfluss von Erfahrungen.
   - $\beta$: Gewichtungsfaktor für den Einfluss kognitiver Strategien.
   - $\gamma$: Gewichtungsfaktor für den Einfluss metakognitiver Prozesse.
   - $K(t+1)$: Wissensstand der Person zum Zeitpunkt $t+1$.
   - $\Delta t$: Zeitintervall.

3. **Metakognitive Steuerung**

   Metakognitive Steuerung kann modelliert werden, um zu zeigen, wie Lernende ihre eigenen kognitiven Prozesse regulieren:

   $$
   M(t+1) = M(t) + \delta \cdot (K_{ziel}(t) - K(t))
   $$

   Hier gibt $K_{ziel}(t)$ das angestrebte Wissensniveau an und $\delta$ beschreibt die Anpassungsrate durch Reflexion.

4. **Dynamik der kognitiven Strategien**

   Der Einsatz kognitiver Strategien kann durch eine eigene Differentialgleichung beschrieben werden, die die Entwicklung und den Einsatz dieser Strategien modelliert:

   $$
   \frac{dS}{dt} = f(K(t), M(t), E(t))
   $$

   Diese Gleichung zeigt, wie sich der Einsatz von Strategien über die Zeit in Abhängigkeit vom Wissensstand und metakognitiven Variablen verändert.

### Beispiel: Modellierung der Wissensverarbeitung

Ein einfaches Beispielmodell beschreibt den Wissensaufbau eines Schülers in Abhängigkeit von seinen Erfahrungen ($E$), den kognitiven Strategien ($S$) und der metakognitiven Steuerung ($M$):

$$
K(t+1) = K(t) + \Delta t \cdot (0,4 \cdot E(t) + 0,3 \cdot S(t) + 0,3 \cdot M(t))
$$

Hierbei:

- $E(t)$: Anzahl und Qualität der neuen Lernerfahrungen.
- $S(t)$: Häufigkeit und Intensität der eingesetzten kognitiven Strategien.
- $M(t)$: Reflexions- und Steuerungsrate.

## 2.3 Anwendungen des kognitivistischen Ansatzes

- **Kognitive Karten**: Lehrkräfte nutzen Diagramme und Mindmaps, um komplexe Informationen zu strukturieren und Lernenden zu helfen, Beziehungen zwischen Konzepten visuell zu erkennen und zu verstehen.

- **Entdeckendes Lernen**: Lernende werden ermutigt, durch geleitete Entdeckung und Exploration Wissen selbst zu erschließen, wobei die Lehrkraft als Facilitator dient.

- **Simulationen und Modellierung**: Durch den Einsatz von Simulationen können Lernende komplexe Systeme und Prozesse in einem kontrollierten Umfeld erkunden, was das Verständnis und die Anwendung von theoretischem Wissen erleichtert.

## 2.4 Mögliche Auswirkungen des kognitivistischen Ansatzes

- **Verbesserte Problemlösungsfähigkeiten**: Lernende entwickeln ein tiefes Verständnis der Materie und sind in der Lage, Wissen auf neue Probleme und Situationen anzuwenden.

- **Förderung selbstgesteuerten Lernens**: Durch den Einsatz metakognitiver Strategien können Lernende effektiver selbstgesteuert lernen und ihre Lernprozesse optimieren.

- **Anpassungsfähigkeit**: Lernende, die kognitive Strategien beherrschen, sind besser in der Lage, sich an verschiedene Lernsituationen und Herausforderungen anzupassen.

- **Herausforderungen in der Umsetzung**: Die Umsetzung kognitivistischer Methoden erfordert oft umfangreiche Planung und Ressourcen, was eine Herausforderung für Bildungseinrichtungen darstellen kann.

# 3 Folgerungen

- **Integration von kognitiven und metakognitiven Strategien**: Der kognitivistische Ansatz fordert eine stärkere Integration kognitiver und metakognitiver Strategien, um die Selbstregulation der Lernenden zu fördern.

- **Strukturierte und kontextbezogene Vermittlung von Wissen**: Wissen sollte strukturiert und in einem sinnvollen Kontext präsentiert werden, um die kognitive Verarbeitung zu erleichtern.

- **Förderung der Reflexion**: Lernende sollten dazu angehalten werden, regelmäßig über ihre eigenen Lernprozesse zu reflektieren.

# 4 Implikationen

- **Bildungs- und Trainingsprogramme**: Der kognitivistische Ansatz erfordert eine Neugestaltung von Bildungs- und Trainingsprogrammen, um die kognitive und metakognitive Entwicklung der Lernenden zu unterstützen.

- **Adaptive Lehrstrategien**: Die Berücksichtigung von individuellen Unterschieden im Wissenserwerb und der Anwendung kognitiver Strategien führt zu einer flexiblen Gestaltung von Lehrstrategien.

- **Bewertungsmethoden**: Traditionelle Prüfungen sollten um metakognitive Reflexionsaufgaben ergänzt werden, um die Tiefe des Verständnisses zu erfassen.

# 5 Zusammenfassung

Der **kognitivistische Ansatz** beschreibt ein Lernmodell, das auf der Grundlage interner kognitiver Prozesse basiert. Der Schwerpunkt liegt auf der Verarbeitung, Organisation und Speicherung von Informationen durch den Lernenden. Anwendungen finden sich in der Entwicklung kognitiver Karten, entdeckendem Lernen und Simulationen. Der Ansatz fördert tiefes Verständnis, Problemlösungsfähigkeiten und selbstgesteuertes Lernen, erfordert jedoch eine durchdachte Gestaltung der Lernumgebung.

# Quelle(n)

- Anderson, J. R. (1983). *The Architecture of Cognition*. Harvard University Press.
- Ausubel, D. P. (1968). *Educational Psychology: A Cognitive View*. Holt, Rinehart & Winston.
- Bruner, J. S. (1966). *Toward a Theory of Instruction*. Harvard University Press.
- Mayer, R. E. (2002). *Rote versus Meaningful Learning*. Educational Psychologist, 41, 13–17.
- Piaget, J. (1954). *The Construction of Reality in the Child*. Basic Books.
