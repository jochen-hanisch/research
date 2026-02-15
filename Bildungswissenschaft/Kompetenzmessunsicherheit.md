---
title: Kompetenzmessunsicherheit
tags:
  - Begriff
  - Definition
  - Research
  - Kompetenz
  - "#Kompetenzmessunsicherheit"
  - "#Bildungsforschung"
  - "#Evaluationsmethoden"
  - "#Kompetenzentwicklung"
  - "#Psychologie"
  - "#Messunsicherheit"
  - "#StatistischeAnalyse"
  - "#Bildungsvalidität"
created: 2024-10-01
updated: 2024-10-17
author: Jochen Hanisch-Johannsen
publish: false
type:
  - Wissenschaftliche Notiz
---

# 1 Definition

Die Kompetenzmessunsicherheit beschreibt die Unsicherheiten und Abweichungen bei der Erfassung und Bewertung von Kompetenzen. Sie ist ein Maß für die Präzision und Genauigkeit der eingesetzten Bewertungsinstrumente und Methoden. Der Begriff wird in Bildungs- und Evaluationskontexten verwendet, um die Verlässlichkeit und Aussagekraft von Kompetenzmessungen zu bestimmen. Die Kompetenzmessunsicherheit kann aus zufälligen Messfehlern, systematischen Verzerrungen oder methodischen Schwächen resultieren.
Sie ist neben der [[Kompetenzentwicklungsunsicherheit]] das zweite Element der [[Kompetzenzunsicherheit]].

# 2 Herleitung

## 2.1 Technische Perspektive

Aus technischer Sicht bezieht sich die Kompetenzmessunsicherheit auf die Standardabweichung und statistische Messfehler, die bei wiederholten Messungen derselben Kompetenz auftreten können. Sie wird durch die Standardabweichung $\sigma(K)$ berechnet:

$$ \sigma(K) = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left(K_i - \overline{K}\right)^2} $$

wobei:

- $N$ die Anzahl der Messungen,
- $K_i$ der gemessene Kompetenzwert und
- $\overline{K}$ der Mittelwert aller gemessenen Kompetenzwerte ist.

### Erweiterung und Beweis der Standardabweichung

Die Standardabweichung $\sigma$ ist ein Maß für die Streuung der Messwerte um den Mittelwert. Je größer die Standardabweichung, desto weiter sind die einzelnen Messwerte vom Mittelwert entfernt. Der Mittelwert $\overline{K}$ wird als:

$$ \overline{K} = \frac{1}{N} \sum_{i=1}^{N} K_i $$

berechnet. Die Standardabweichung $\sigma(K)$ ist dann die Quadratwurzel der mittleren quadratischen Abweichung der Messwerte von diesem Mittelwert.

## 2.2 Systemische Perspektive

In einem systemischen Kontext umfasst die Kompetenzmessunsicherheit kumulative Effekte aus der Messunsicherheit der Umwelt, der subjektiven Einschätzung der Bewertenden sowie methodischen Verzerrungen. Die Gesamtunsicherheit lässt sich als Summe der Varianzen der Einflussfaktoren darstellen:

$$ \sigma^2_{\text{gesamt}} = \sigma^2_{\text{Umwelt}} + \sigma^2_{\text{Messung}} + \sigma^2_{\text{Beobachter}} $$

### Herleitung und Erläuterung der Varianzaddition

Die Varianzaddition ist ein Prinzip aus der Statistik, das besagt, dass die Gesamtvarianz eines Systems als Summe der Varianzen der einzelnen unabhängigen Faktoren berechnet werden kann. Für die Kompetenzmessung bedeutet dies, dass die Gesamtunsicherheit aus der Summe der Umgebungsunsicherheiten ($\sigma_{\text{Umwelt}}$), der Messunsicherheiten ($\sigma_{\text{Messung}}$) und der Beobachtungsunsicherheiten ($\sigma_{\text{Beobachter}}$) besteht. Die Formel zur Addition der Varianzen lautet:

$$ \sigma^2_{\text{gesamt}} = \sum_{i=1}^{m} \sigma^2_{i} $$

wobei $m$ die Anzahl der unabhängigen Varianzquellen darstellt.

## 2.3 Mathematische Perspektive

Die Kompetenzmessunsicherheit steht in direkter Beziehung zur Unsicherheit in der [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung]] $\Delta E$ und der Unsicherheit in der Kompetenzmessung $\Delta K$. Diese Kopplung wird durch den [[Dynamischer Unsicherheitswert|dynamischen Unsicherheitswert]] beschrieben:

$$ \Delta E \cdot \Delta K \geq C $$

wobei:

- $\Delta E$ die Unsicherheit in der [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung]],
- $\Delta K$ die Unsicherheit in der Messung und
- $C$ der dynamische Unsicherheitswert ist, der die Abhängigkeit der beiden Variablen beschreibt.

### Beweis und Anwendung des dynamischen Unsicherheitswerts

Der dynamische Unsicherheitswert $C$ zeigt an, dass die Produktunsicherheit zweier abhängiger Variablen $\Delta E$ und $\Delta K$ niemals kleiner als ein bestimmter Wert sein kann. Für den Kontext der Kompetenzmessung bedeutet dies, dass eine hohe Unsicherheit in der [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung]] nur dann akzeptabel ist, wenn die Messunsicherheit entsprechend klein ist und umgekehrt. Der dynamische Unsicherheitswert $C$ wird in der Simulation als Maß für die Stabilität der Kopplung zwischen $\Delta E$ und $\Delta K$ berechnet.

## 2.4 Mathematische Interpretation

Bei einer hohen Standardabweichung $\sigma(K)$ sind die Messungen so weit gestreut, dass eine eindeutige Bewertung der Kompetenzen erschwert wird. Eine Reduktion der Standardabweichung ist nur durch Optimierung der Messbedingungen möglich. Auch die Minimierung der Varianzquellen $\sigma_{\text{Umwelt}}, \sigma_{\text{Messung}}, \sigma_{\text{Beobachter}}$ führt zu einer stabileren und objektiveren Kompetenzmessung.

# 3 Folgerungen

- Aspekt 1: Eine hohe Kompetenzmessunsicherheit kann zu Fehlinterpretationen der Kompetenzen führen und den tatsächlichen Lernerfolg verzerrt darstellen.
- Aspekt 2: Die Reduktion der Kompetenzmessunsicherheit durch standardisierte Messverfahren erhöht die Objektivität und Validität der Ergebnisse.
- Aspekt 3: Eine zu hohe Kompetenzmessunsicherheit kann die Aussagekraft von Kompetenzentwicklungen beeinträchtigen und notwendige Anpassungen im Lernprozess erschweren.

# 4 Zusammenfassung

Die Kompetenzmessunsicherheit beschreibt die Präzision und Verlässlichkeit von Kompetenzmessungen und beeinflusst die Interpretation von Kompetenzentwicklungen. Sie wird in Bildungs- und Evaluationsprozessen angewendet und ist entscheidend für die Objektivität und Validität der Bewertungen. Mathematisch lässt sie sich durch die Standardabweichung und den [[Dynamischer Unsicherheitswert|dynamischen Unsicherheitswert]] darstellen. Der Begriff trägt dazu bei, die Qualität von Bildungsprozessen zu sichern und mögliche Verzerrungen in der Kompetenzdiagnostik zu identifizieren. Eine detaillierte mathematische Analyse zeigt, dass die Kompetenzmessunsicherheit durch die Varianzaddition berechnet werden kann, während der dynamische Unsicherheitswert die Grenzen der Kopplung von [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung]] und Messunsicherheit aufzeigt.

# Quelle(n)

- AERA, APA, & NCME. (2014). _Standards for Educational and Psychological Testing_. American Educational Research Association.
- Messick, S. (1995). Validity of psychological assessment: Validation of inferences from persons’ responses and performances as scientific inquiry into score meaning. _American Psychologist, 50_(9), 741–749. doi:10.1037/0003-066X.50.9.741
- Kane, M. T. (2013). Validating the Interpretations and Uses of Test Scores. _Journal of Educational Measurement, 50_(1), 1–73. doi:10.1111/jedm.12000
- Schmitt, N., & Kunce, C. (2002). Measurement error in psychological research: Lessons from 26 research scenarios. _Psychological Methods, 7_(3), 306–324. doi:10.1037/1082-989X.7.3.306
- Fischer, G. N., & Riedl, A. (2018). Psychometrische Verfahren zur Kompetenzmessung: Ein Überblick. In _Kompetenzentwicklung in Unternehmen_ (S. 103–132). Springer VS.
- Lienert, G. A., & Raatz, U. (1998). _Testaufbau und Testanalyse_. Beltz.
- Wittmann, W. W. (1988). Multivariate reliability theory: Principles of symmetry and successful validation strategies. In H. Wainer & S. Messick (Eds.), _Principles of modern psychological measurement_ (pp. 183–208). Erlbaum.