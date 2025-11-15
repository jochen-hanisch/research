# Analyse und Herleitung des Bildungswirkgefüges in Moodle auf Basis von Kompetenz- und TEI-Daten

## 1. Einleitung

Die Analyse von Lernprozessen erfordert ein tiefgehendes Verständnis der individuellen Kompetenzentwicklung. Bisherige Methoden der Lernkontrolle basieren oft auf statischen Evaluationsverfahren oder isolierten Kompetenzmessungen, die lediglich punktuelle Einblicke in den Lernfortschritt ermöglichen. Durch die Kombination objektiver Fortschrittsdaten aus Moodle mit subjektiven Einschätzungen der Lernenden aus den TEI-Daten kann ein dynamisches Modell erstellt werden, das sowohl die langfristige Entwicklung als auch kurzfristige Veränderungen sichtbar macht. Das daraus entstehende Bildungswirkgefüge stellt eine umfassende Methode dar, um Lernprozesse in Echtzeit zu überwachen, Unsicherheiten zu identifizieren und adaptive Maßnahmen für die individuelle Lernförderung zu entwickeln.

## 2. Der Bildungswirkfaktor als zentrale Messgröße der Kompetenzentwicklung

Der Bildungswirkfaktor $ν$ beschreibt die langfristige Entwicklung der Kompetenz eines Lernenden. Er setzt sich aus zwei Hauptkomponenten zusammen: dem objektiven Lernfortschritt, der sich aus den in Moodle markierten Aufgaben ableitet, und der subjektiven Wahrnehmung des Kompetenzzuwachses, die durch die TEI-Daten erfasst wird.

Die formale Definition des Bildungswirkfaktors lautet:

$$
ν = \left(\frac{\text{abgeschlossene Aufgaben}}{\text{Gesamtaufgaben}}\right) \times \left(\frac{\text{Subjective Knowledge Gain}}{\max(\text{Perceived Difficulty}, 1)}\right)
$$

Die erste Komponente des Bildungswirkfaktors beschreibt den **objektiven Fortschritt**, indem das Verhältnis zwischen den abgeschlossenen Aufgaben und der Gesamtanzahl der Aufgaben berechnet wird. Diese Metrik ermöglicht eine klare Quantifizierung des individuellen Lernstandes. Die zweite Komponente basiert auf der subjektiven Wahrnehmung der Lernenden. Hierbei wird das Verhältnis zwischen dem subjektiv wahrgenommenen Wissenszuwachs und der wahrgenommenen Schwierigkeit des Lernmaterials betrachtet. Dieser Wert zeigt, ob Lernende ihre Kompetenzentwicklung als positiv oder negativ erleben.

Ein steigender Bildungswirkfaktor deutet auf eine erfolgreiche Kompetenzentwicklung hin. Ein stagnierender oder sinkender Wert kann hingegen darauf hinweisen, dass Lernende Schwierigkeiten haben oder sich unsicher fühlen. Durch die kontinuierliche Berechnung dieses Faktors lässt sich die Kompetenzentwicklung systematisch überwachen.

## 3. Der Bildungswirkindikator als Frühwarnsystem

Während der Bildungswirkfaktor die allgemeine Entwicklung der Kompetenz misst, beschreibt der Bildungswirkindikator $ι$ die Dynamik dieser Entwicklung. Der Bildungswirkindikator ist die erste Ableitung des Bildungswirkfaktors und gibt damit die Änderungsrate der Kompetenzentwicklung an:

$$
ι = \frac{dν}{dt}
$$

Ein positiver Wert für $ι$ bedeutet, dass sich der Bildungswirkfaktor beschleunigt und Lernende in kurzer Zeit deutliche Fortschritte machen. Ein negativer Wert zeigt hingegen eine Verlangsamung oder Stagnation des Lernprozesses an. 

Die kontinuierliche Berechnung des Bildungswirkindikators erlaubt es, Lernentwicklungen frühzeitig zu erkennen. Während der Bildungswirkfaktor über längere Zeiträume hinweg gemessen wird, kann der Bildungswirkindikator bereits bei den ersten Anzeichen einer Veränderung Hinweise auf sich anbahnende Lernschwierigkeiten oder besonders erfolgreiche Lernphasen geben.

## 4. Die Unschärferelation als Indikator für Lernunsicherheiten

Die Unschärferelation im Bildungswirkgefüge beschreibt den Zusammenhang zwischen emotionaler und kognitiver Unsicherheit. Diese Unsicherheiten beeinflussen die Kompetenzentwicklung erheblich und können durch folgende Beziehung mathematisch beschrieben werden:

$$
ΔE \cdot ΔK = C
$$

Hierbei steht $ΔE$ für die emotionale Unsicherheit und $ΔK$ für die kognitive Unsicherheit. Die Konstante $C$ gibt an, inwiefern Unsicherheit systematisch auftritt.

Die emotionale Unsicherheit $ΔE$ ergibt sich aus der Differenz zwischen der wahrgenommenen Schwierigkeit und dem subjektiv eingeschätzten Nutzen eines Kurses:

$$
ΔE = \text{Perceived Difficulty} - \text{Perceived Usefulness}
$$

Die kognitive Unsicherheit $ΔK$ beschreibt die Abweichung zwischen dem objektiven Lernfortschritt und der subjektiven Wahrnehmung des Wissenszuwachses:

$$
ΔK = \left| \left(\frac{\text{abgeschlossene Aufgaben}}{\text{Gesamtaufgaben}}\right) - \left(\frac{\text{Subjective Knowledge Gain}}{\max(\text{Perceived Difficulty}, 1)}\right) \right|
$$

Ein hohes Produkt von $ΔE$ und $ΔK$ zeigt an, dass Lernende in einer Phase hoher Unsicherheit sind. Niedrige Werte deuten auf eine gefestigte Kompetenzentwicklung hin. Die Unschärferelation ermöglicht eine genauere Einschätzung, wann Lernende zusätzliche Unterstützung oder gezielte Interventionen benötigen.

## 5. Wendepunkte in der zweiten Ableitung des Bildungswirkindikators als Marker für Lernphasenwechsel

Neben der ersten Ableitung des Bildungswirkfaktors kann auch die zweite Ableitung des Bildungswirkindikators berechnet werden, um abrupte Lernphasenwechsel zu erkennen:

$$
\frac{d^2ι}{dt^2}
$$

Ein Wendepunkt in der zweiten Ableitung bedeutet, dass sich die Dynamik des Lernprozesses abrupt verändert. Ein positiver Wendepunkt zeigt an, dass sich Lernende nach einer schwierigen Phase stabilisieren und schneller Fortschritte machen. Ein negativer Wendepunkt weist darauf hin, dass der Lernprozess sich verlangsamt oder eine Unsicherheitsphase eintritt.

Durch die Identifikation dieser Wendepunkte können gezielte Maßnahmen eingeleitet werden, bevor sich Lernschwierigkeiten verfestigen.

## 6. Die Rolle der Moodle-Aufgaben und TEI-Items im Bildungswirkgefüge

Die Berechnung des Bildungswirkfaktors basiert auf einer Kombination objektiver Moodle-Daten und subjektiver TEI-Items.

**Moodle-Daten und ihre Zuordnung:**

- „Kann ich“-Markierung: Subjektiv wahrgenommener Kompetenzzuwachs
- Abgeschlossene Aufgaben pro Kurs: Objektive Kompetenzentwicklung
- Verhältnis von abgeschlossenen zu Gesamtaufgaben: Fortschrittsanzeige
- Anzahl der Klicks auf eine Aufgabe: Indikator für Unsicherheiten
- Zeit bis zur „Kann ich“-Markierung: Reflexionsprozess

**TEI-Items und ihre Zuordnung:**

- „Ich habe den Eindruck, mein Wissen hat sich langfristig erweitert.“: Subjektive Kompetenzentwicklung
- „Ich werde mir die neuen Themen gut merken können.“: Sicherheitsgefühl im Lernprozess
- „Die Inhalte waren verständlich.“: Wahrgenommene Schwierigkeit
- „Ich finde das Training nützlich für meinen Beruf.“: Wahrgenommene Relevanz
- „Ich werde das Gelernte im beruflichen Alltag anwenden.“: Transfer des Gelernten

## 7. Fazit

Das Bildungswirkgefüge bietet ein umfassendes Modell zur Messung und Analyse der Kompetenzentwicklung. Es kombiniert objektive Lernfortschritte mit subjektiven Unsicherheiten und ermöglicht eine adaptive Steuerung von Lernprozessen. Der Bildungswirkfaktor beschreibt den langfristigen Fortschritt, während der Bildungswirkindikator frühzeitig Veränderungen anzeigt. Die Unschärferelation hilft, Unsicherheiten zu identifizieren, und Wendepunkte in der zweiten Ableitung signalisieren kritische Lernphasenwechsel. Durch die Integration von Moodle-Aufgaben und TEI-Daten kann dieses Modell zur kontinuierlichen Lernüberwachung und zur gezielten Unterstützung von Lernenden eingesetzt werden.

# Simulation der Umsetzung

```python

import numpy as np

import matplotlib.pyplot as plt

from scipy.signal import find_peaks

  
# Beispielhafte Moodle- & TEI-Daten (Simulation mit 32 Handlungssituationen)

completed_tasks = np.random.randint(5, 20, 32) # Abgeschlossene Aufgaben

total_tasks = np.full(32, 20) # Gesamtaufgaben pro Kurs

perceived_difficulty = np.random.uniform(1, 5, 32) # Subjektive Schwierigkeit (TEI)

knowledge_gain = np.random.uniform(1, 5, 32) # Subjektives Lernwachstum (TEI)

  

# Berechnung von Bildungswirkfaktor ν (objektive Kompetenz + subjektive Einschätzung)

bildungswirkfaktor = (completed_tasks / total_tasks) * (knowledge_gain / np.maximum(perceived_difficulty, 1))

  

# Berechnung des Bildungswirkindikators ι (1. Ableitung von ν)

bildungswirkindikator = np.gradient(bildungswirkfaktor)

  

# Berechnung der Unsicherheitsrelation ΔE ⋅ ΔK = C

delta_e = perceived_difficulty - knowledge_gain # Emotionale Unsicherheit

delta_k = np.abs((completed_tasks / total_tasks) - (knowledge_gain / np.maximum(perceived_difficulty, 1))) # Kognitive Unsicherheit

c_values = delta_e * delta_k # Unschärferelation

  

# Bestimmung der Wendepunkte, Minima & Maxima

maxima_nu, _ = find_peaks(bildungswirkfaktor)

minima_nu, _ = find_peaks(-bildungswirkfaktor)

maxima_iota, _ = find_peaks(bildungswirkindikator)

minima_iota, _ = find_peaks(-bildungswirkindikator)

  

# Dashboard-Visualisierung

plt.figure(figsize=(12, 6))

  

# Bildungswirkfaktor & Bildungswirkindikator

plt.subplot(2, 2, 1)

plt.plot(bildungswirkfaktor, label="Bildungswirkfaktor (ν)", marker="o", color="purple")

plt.plot(bildungswirkindikator, label="Bildungswirkindikator (ι)", linestyle="--", color="orange")

plt.scatter(maxima_nu, bildungswirkfaktor[maxima_nu], color="green", label="Regeneration")

plt.scatter(minima_nu, bildungswirkfaktor[minima_nu], color="red", label="Prävention")

plt.legend()

plt.title("Bildungswirkfaktor & Bildungswirkindikator")

  

# Unschärferelation ΔE ⋅ ΔK = C

plt.subplot(2, 2, 2)

plt.plot(c_values, label="C (Unsicherheitsrelation)", color="teal")

plt.axhline(np.mean(c_values), linestyle="--", color="black", label="Erwartungswert")

plt.legend()

plt.title("Unschärferelation (ΔE⋅ΔK≥C)")

  

# Kumulative Kompetenz

plt.subplot(2, 2, 3)

plt.plot(np.cumsum(bildungswirkfaktor), label="Kumulative Kompetenz", color="purple", linewidth=2)

plt.fill_between(range(32), np.cumsum(bildungswirkfaktor), alpha=0.3, color="cyan")

plt.legend()

plt.title("Kumulative Kompetenz")

  

# Histogramm der Kompetenzentwicklung

plt.subplot(2, 2, 4)

plt.hist(bildungswirkfaktor, bins=10, color="brown", alpha=0.5, label="Histogramm")

plt.legend()

plt.title("Histogramm, Dichte & KDE")

  

plt.tight_layout()

plt.show()

```
