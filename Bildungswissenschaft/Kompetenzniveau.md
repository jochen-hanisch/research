---
author: Jochen Hanisch-Johannsen
title: Kompetenzniveau
created: 2024-10-17
updated: 2024-10-17
tags:
  - "#Kompetenz"
  - "#Kompetenzentwicklung"
  - "#Lernprozess"
  - "#Bildungsforschung"
  - "#Kompetenzniveau"
  - "#Lernsimulationen"
project: Bildungsraum-Analyse
type:
  - Wissenschaftliche Notiz
publish:
---

# 1 Definition

Das Kompetenzniveau beschreibt den aktuellen Entwicklungsstand einer Fähigkeit oder Fertigkeit, den eine Person oder ein Lernender zu einem bestimmten Zeitpunkt erreicht hat. Es handelt sich um eine dynamische Größe, die sich durch verschiedene Faktoren wie Lernen, Übung, Motivation und äußere Einflüsse (z. B. persönliche Ereignisse) kontinuierlich verändert. In der Bildung wird das Kompetenzniveau häufig in Stufen oder Skalen gemessen, um den Fortschritt oder Entwicklungsbedarf zu bestimmen.

Im Kontext von Simulationen oder Modellen beschreibt das Kompetenzniveau eine numerische Darstellung der Lernentwicklung über die Zeit und zeigt an, wie sich die Kompetenzen eines Lernenden während eines Simulationsdurchlaufs verändern.

# 2 Herleitung

## 2.1 Kompetenzen und Kompetenzniveaus

### 2.1.1 Kompetenzmessung

Das Kompetenzniveau basiert auf der Fähigkeit, die Kompetenzen einer Person in einem bestimmten Bereich zu erfassen und zu bewerten. Diese Bewertung kann durch verschiedene Methoden erfolgen, darunter formale Tests, Selbstbeurteilungen oder Beobachtungen. Das im Code verwendete Kompetenzniveau wird numerisch dargestellt, um die Entwicklung der Kompetenz eines Lernenden im Zeitverlauf zu modellieren. Der Startwert der Kompetenz wird zu Beginn der Simulation festgelegt (im Beispiel: `start_kompetenz`), und dieses Niveau wird über mehrere Quartale hinweg simuliert.

### 2.1.2 Dynamische Entwicklung

Kompetenzniveaus verändern sich im Verlauf des Lernprozesses. Im vorliegenden Code wird das Kompetenzniveau in jedem Quartal durch eine Kombination von Faktoren wie Bereitschaftssteigerung, Motivation, Neugier und der Gesamtauswirkung persönlicher Ereignisse (PE) angepasst. Diese Dynamik spiegelt die kontinuierliche Veränderung des Lernfortschritts wider. Das Ziel der Simulation besteht darin, die Entwicklung der Kompetenz in Abhängigkeit von diesen Faktoren zu modellieren.

### 2.1.3 Grenzen der Entwicklung

In der Simulation wird das Kompetenzniveau durch die Funktion `np.clip()` auf einen Maximalwert von 10 begrenzt, um zu verhindern, dass das Kompetenzniveau über ein realistisches Maß hinaus ansteigt. Dies zeigt, dass das Kompetenzniveau in diesem Modell eine feste Obergrenze hat, die den maximalen Kompetenzstand eines Lernenden darstellt.

### 2.1.4 Einflussfaktoren

Die Simulation berücksichtigt verschiedene Einflussfaktoren, die das Kompetenzniveau beeinflussen:

- **Bereitschaftssteigerung**: Die Anpassung der Bereitschaft zum Lernen oder zur Kompetenzsteigerung in jedem Quartal.
- **Motivation**: Der individuelle Motivationswert, der in jedem Quartal variiert.
- **Neugier**: Der Einfluss der Neugier auf den Lernprozess und die Kompetenzentwicklung.
- **Persönliche Ereignisse (PE)**: Individuelle Erlebnisse und Ereignisse, die den Lernverlauf und die Bereitschaft, sich neuen Inhalten zu widmen, beeinflussen.

# 3 Folgerungen

- **Dynamik der Kompetenzentwicklung**: Die Entwicklung des Kompetenzniveaus ist dynamisch und hängt von einer Vielzahl von Faktoren ab. Diese Unsicherheiten machen es schwer vorherzusagen, wie sich das Kompetenzniveau in einem festen Zeitrahmen entwickeln wird.
  
- **Interdependenz der Faktoren**: Die Anpassung des Kompetenzniveaus hängt stark von externen Faktoren wie Motivation und Bereitschaft ab, aber auch von der individuellen Neugier und den Auswirkungen persönlicher Ereignisse.

# 4 Implikationen

- **Lernsimulationen und adaptive Lernsysteme**: Lernplattformen und Simulationen müssen in der Lage sein, die Vielzahl an Einflussfaktoren zu berücksichtigen, die das Kompetenzniveau beeinflussen. Dies zeigt die Notwendigkeit für adaptive Systeme, die auf die unterschiedlichen Bedürfnisse und Lernverläufe der Lernenden eingehen.

# 5 Zusammenfassung

Das Kompetenzniveau beschreibt den Entwicklungsstand der Kompetenzen eines Lernenden. Es ist eine dynamische Größe, die von kognitiven, emotionalen und sozialen Faktoren beeinflusst wird und durch externe Ereignisse weiter modifiziert werden kann. In der Simulation dient das Kompetenzniveau als zentrale Kennzahl zur Bewertung des Lernfortschritts, wobei es durch verschiedene Faktoren wie Bereitschaftssteigerung, Motivation, Neugier und persönliche Ereignisse beeinflusst wird. Der Bildungsprozess ist somit eine komplexe Wechselwirkung aus verschiedenen Variablen, die die Kompetenzentwicklung in einem festgelegten Zeitraum beeinflussen.

# Quelle(n)

- Hanisch-Johannsen, J. (2024). _Simulation Bildungswirkgefüge_ (Version 1.3.5) [Python].