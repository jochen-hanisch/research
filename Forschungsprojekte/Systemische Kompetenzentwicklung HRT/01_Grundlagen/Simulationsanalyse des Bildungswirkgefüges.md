---
author: Jochen Hanisch-Johannsen
title: "Simulationsanalyse des Bildungswirkgefüges: Kompetenzentwicklung und Unsicherheitsrelationen"
updated: 2024-10-09
project: Wirkgefüge im digitalen Bildungsraum
---
# Kompetenzentwicklung und Unsicherheitsrelationen

Der gegebene Python-Code implementiert ein komplexes Modell zur Simulation und Visualisierung von Kompetenzentwicklungen in einem Bildungsprozess. Er umfasst zahlreiche Schritte zur Verarbeitung und Analyse von Daten. Nachfolgend eine detaillierte Interpretation der einzelnen Abschnitte:

## 1. Initialisierung und Importe

- Es werden eine Reihe von Bibliotheken importiert, darunter `numpy`, `pandas`, `scipy`, `plotly`, `matplotlib`, `networkx`und `datetime`. Diese sind erforderlich für:
    
    - Mathematische Berechnungen (z.B. `numpy`, `scipy`),
    - Datenmanipulation (z.B. `pandas`),
    - Plotting und Visualisierung (z.B. `plotly`, `matplotlib`, `seaborn`),
    - Netzwerkanalyse (z.B. `networkx`).
- **Farben-Definitionen** (`colors`): Die Farbpalette dient der einheitlichen Gestaltung der Visualisierungen.
#### **Struktur des Codes**

Der erste Abschnitt des Codes bereitet das Skript durch die Definition der genutzten Bibliotheken, das Setzen von Anzeigeoptionen und das Einrichten einer Farbpalette vor. Dieser Abschnitt bildet die Grundlage für die gesamte Simulation und die spätere Visualisierung.

#### **1.1. Import von Bibliotheken**

Der Import erfolgt in mehreren Schritten:

python

Code kopieren

`import os import numpy as np import pandas as pd from scipy.signal import find_peaks, savgol_filter from scipy.stats import gaussian_kde, norm, pearsonr from scipy.interpolate import interp1d import plotly.express as px import plotly.graph_objects as go from plotly.subplots import make_subplots import matplotlib.pyplot as plt import seaborn as sns import networkx as nx import datetime`

Die importierten Module lassen sich wie folgt kategorisieren:

1. **Standard-Module:**
    
    - `os`: Ermöglicht die Ausführung von Betriebssystemkommandos (hier genutzt, um das Terminal zu leeren).
    - `datetime`: Bietet Funktionen zur Arbeit mit Datums- und Zeitangaben.
2. **Numerische und statistische Berechnungen:**
    
    - `numpy` (`np`): Bietet mathematische Funktionen, wie Zufallszahlen, Mittelwerte, Standardabweichungen und lineare Algebra.
    - `scipy.signal`, `scipy.stats`, `scipy.interpolate`: Erweitert `numpy` um Funktionen zur Signalverarbeitung (`find_peaks`, `savgol_filter`), statistische Tests und Berechnungen (`norm`, `pearsonr`), sowie zur Interpolation (`interp1d`).
3. **Datenanalyse und Manipulation:**
    
    - `pandas` (`pd`): Zur Manipulation und Analyse von Daten, speziell für den Umgang mit Tabellenstrukturen (`DataFrames`).
4. **Visualisierung:**
    
    - `plotly`: Bibliothek für interaktive Visualisierungen (z.B. `go.Figure`, `make_subplots`).
    - `matplotlib` und `seaborn`: Matplotlib wird als universelle Visualisierungsbibliothek genutzt, während Seaborn darauf aufbaut und speziellere Funktionen bietet (z.B. zur Erstellung von Heatmaps).
5. **Netzwerkanalyse:**
    
    - `networkx`: Ermöglicht die Erstellung und Analyse von Netzwerkstrukturen (z.B. für die Visualisierung von Graphen).

#### **1.2. Leeren des Terminals**

python

Code kopieren

`# Terminal leeren os.system('cls' if os.name == 'nt' else 'clear')`

Je nach Betriebssystem (`os.name`) wird das Terminalfenster geleert:

- **Windows:** Der Befehl `cls` wird ausgeführt.
- **Unix/Linux/Mac:** Der Befehl `clear` wird verwendet.

Dies ist optional, um die Anzeige im Terminal zu bereinigen und die Übersichtlichkeit zu erhöhen.

#### **1.3. Anzeigeoptionen für `pandas`**

python

Code kopieren

`pd.set_option('display.max_columns', None) pd.set_option('future.no_silent_downcasting', True)`

- **`display.max_columns`:** Setzt die maximale Anzahl der Spalten auf `None`, um sicherzustellen, dass alle Spalten eines DataFrames angezeigt werden.
- **`future.no_silent_downcasting`:** Legt fest, dass bei bestimmten Operationen in Zukunft keine stillen Datentyp-Umwandlungen (z.B. von `float64` nach `float32`) erfolgen.

Diese Einstellungen beeinflussen, wie Daten im Terminal angezeigt werden.

#### **1.4. Definition einer benutzerdefinierten Farbpalette**

python

Code kopieren

`colors = {     "background": "#003366",     "text": "#333333",     "accent": "#663300",     "primaryLine": "#660066",     "secondaryLine": "#cc6600",     "depthArea": "#006666",     "brightArea": "#66CCCC",     "positiveHighlight": "#336600",     "negativeHighlight": "#990000",     "white": "#ffffff" }`

Eine zentrale Farbpalette (`colors`) wird erstellt. Dies erleichtert die spätere Farbwahl für Diagramme und stellt sicher, dass die Visualisierungen eine einheitliche Ästhetik haben.

- **Hauptfarben:**
    
    - `background`: Definiert die Hintergrundfarbe (#003366), ein dunkler Blauton.
    - `text`: Definiert die Textfarbe (#333333), ein dunkles Grau für Lesbarkeit.
- **Spezifische Farben:**
    
    - `accent`: Akzentfarbe (#663300), ein dunkler Orange-Braun-Ton.
    - `primaryLine` und `secondaryLine`: Farben für primäre und sekundäre Linien.
    - `positiveHighlight` und `negativeHighlight`: Farbmarkierungen zur Unterscheidung positiver (Grün) und negativer (Rot) Entwicklungen.
    - `depthArea` und `brightArea`: Farben für verschiedene Bereiche in Diagrammen.

Die Wahl von Farben wie `#660066` (Violett) und `#cc6600` (Orange) dient dazu, Kontraste hervorzuheben und bestimmte Aspekte optisch abzuheben.

### **Zusammenfassung:**

Der erste Abschnitt des Codes ist essenziell für das Einrichten der Arbeitsumgebung. Er stellt sicher, dass alle notwendigen Bibliotheken verfügbar sind und eine konsistente, übersichtliche Darstellung der Daten ermöglicht wird. Die benutzerdefinierte Farbpalette und die Anzeigeoptionen sind auf die folgenden Visualisierungen und Darstellungen abgestimmt.
## **2. Eingabeparameter**

- Die **Anzahl der Quartale** und **Durchläufe** wird festgelegt.
- `initial_neugier` und `start_kompetenz` bestimmen die Ausgangswerte für das Lernverhalten und die Kompetenz der Lernenden.
- `bereitschafts_steigerung_phase`: Die Bereitschaft des Lernenden variiert in verschiedenen Phasen des Lernprozesses. Dies wird durch zufällige Werte modelliert.
- **Persönliche Ereignisse (PE)** beeinflussen die Lernentwicklung, z.B. durch `PFE` (Persönlicher Fehlschlag extern), `PSE` (Stabilitätserfolg) und andere Kategorien.

Der zweite Abschnitt des Codes definiert zentrale Eingabeparameter, die für die Simulation und das Modell erforderlich sind. Diese Eingaben steuern das Verhalten des Modells, legen Anfangswerte fest und definieren Variablen, die während der Simulation angepasst werden.

#### **2.1. Definition von Kernparametern der Simulation**

python

Code kopieren

`quartale = 12 simulations_durchlaeufe = 250`

- **`quartale = 12`**: Legt die Anzahl der Quartale (Monate) für die Simulation fest, d. h. die gesamte Simulation deckt einen Zeitraum von 12 Quartalen ab.
- **`simulations_durchlaeufe = 250`**: Gibt die Anzahl der Wiederholungen (Simulationsdurchläufe) an. Jede Simulation startet mit denselben Anfangsbedingungen, kann jedoch aufgrund zufälliger Einflüsse unterschiedliche Ergebnisse liefern. Dies ermöglicht es, die Varianz und Stabilität des Modells zu analysieren.

#### **2.2. Ausgangswerte für Motivation und Kompetenz**

python

Code kopieren

`initial_neugier = 3.066  # aus 5DCR = 3.066 ; aus Näherung = 4.333 ; zur Demo = 5.000 start_kompetenz = 1.333  # aus KRI  = 4.733 ; aus APrVO = 1.133 ; zur Demo = 1.500`

- **`initial_neugier = 3.066`**: Der Anfangswert für die Neugier des Lernenden. Die Kommentare deuten auf verschiedene Referenzwerte (z. B. `5DCR`) hin, die zur Festlegung dieses Wertes herangezogen wurden.
- **`start_kompetenz = 1.333`**: Der Startwert für die Kompetenz des Lernenden. Auch hier gibt es verschiedene Quellen (z. B. `KRI` oder `APrVO`), die diesen Wert beeinflusst haben könnten.

Diese beiden Parameter sind entscheidend, da sie den Ausgangspunkt für die Simulation bilden. Die Werte sind so gewählt, dass sie eine Art Durchschnitt darstellen, basierend auf realen oder modellierten Daten.

#### **2.3. Standardabweichung der Bereitschaft**

python

Code kopieren

`bereitschafts_std = 0.5`

- Definiert die **Standardabweichung** für die Bereitschaftssteigerung des Lernenden. Eine höhere Standardabweichung führt zu einer größeren Streuung der Bereitschaftswerte, was in der Simulation zu mehr Unsicherheit und Schwankungen führt.

#### **2.4. Phasen der Bereitschaftssteigerung**

python

Code kopieren

`bereitschafts_steigerung_phase = {     'Anpassung': np.random.uniform(-0.05, 0),     'Verfestigung': np.random.uniform(0.05, 0.1),     'Wachstum': np.random.uniform(0.1, 0.15),     'Plateau': np.random.uniform(0.05, 0.1) }`

- Dieses Dictionary legt die **Bereitschaftssteigerung in verschiedenen Phasen** fest, wobei jede Phase einen bestimmten Bereich (Intervall) für die Zufallswerte definiert:
    - **`'Anpassung'`:** Zu Beginn (Anpassungsphase) wird die Bereitschaft leicht negativ oder bei Null gehalten (Intervall: `[-0.05, 0]`).
    - **`'Verfestigung'`:** Während der Verfestigungsphase ist die Steigerung der Bereitschaft positiv und liegt zwischen `0.05` und `0.1`.
    - **`'Wachstum'`:** Die Wachstumsphase weist eine deutliche Steigerung auf (`[0.1, 0.15]`).
    - **`'Plateau'`:** Am Ende (Plateauphase) ist die Steigerung ähnlich der Verfestigungsphase (`[0.05, 0.1]`).

Diese Phasen repräsentieren den typischen Verlauf einer Lernkurve, bei der nach einer anfänglichen Anpassung eine Phase der Stabilisierung und dann ein Wachstum folgt, bevor die Bereitschaftssteigerung wieder abnimmt.

#### **2.5. Parameter für die Auswirkungen von persönlichen Ereignissen**

python

Code kopieren

`pe_auswirkungen = {     'PFE': 0.1,                 # Persönlicher Fehlschlag extern      0.1     'PLE': 0.08,                # Persönlicher Leistungseinbruch      0.08     'PFV': 0.15,                # Persönlicher Fortschritt variabel   0.15     'PGV': 0.1,                 # Persönliches Großereignis variabel  0.1     'PSE': 0.2,                 # Persönlicher Stabilitätserfolg      0.2     'PEE': 0.05                 # Persönlicher Erfolg extern          0.05 }`

- Die **[[Persönliche Ereignisse]] (PE)** haben unterschiedliche Auswirkungen auf die Simulation:
    - **`PFE`:** Persönlicher Fehlschlag, der extern bedingt ist, führt zu einer negativen Auswirkung von `0.1`.
    - **`PLE`:** Persönlicher Leistungseinbruch hat eine negative Auswirkung von `0.08`.
    - **`PFV`:** Persönlicher Fortschritt, variabel, führt zu einer positiven Auswirkung von `0.15`.
    - **`PSE`:** Stabilitätserfolg ist ein positiver Faktor (`0.2`).
    - **`PEE`:** Persönlicher Erfolg, extern, hat den geringsten positiven Effekt (`0.05`).

Diese Kategorien wirken als **Stör- oder Verstärkungsfaktoren** und beeinflussen die Lern- und Kompetenzentwicklung. Durch Zufallszahlen in der Simulation wird eine realistische Variation in die Simulation eingebracht.

#### **2.6. Funktion zur Berechnung eines dynamischen Unsicherheitswerts**

python

Code kopieren

`def calculate_dynamic_C(delta_e, delta_k):     r, _ = pearsonr(delta_e, delta_k)     return abs(r) * (np.std(delta_e) * np.std(delta_k))`

- Diese Funktion berechnet einen **dynamischen Unsicherheitswert `C`**, der die Korrelation (`pearsonr`) zwischen `delta_e` (emotionaler Entwicklung) und `delta_k` (Kompetenzentwicklung) misst.
    - Der Pearson-Korrelationskoeffizient `r` gibt an, wie stark die beiden Variablen miteinander zusammenhängen.
    - Das Produkt der Standardabweichungen (`np.std(delta_e) * np.std(delta_k)`) wird mit dem Betrag von `r` multipliziert, um `C` zu berechnen.

Der [[Dynamischer Unsicherheitswert]] ($C$) dient als Maß für die **Gesamtunsicherheit**, die in der Simulation auftritt, und beeinflusst die Entscheidung, ob die Unsicherheitsrelation erfüllt ist.

#### **Zusammenfassung:**

Der zweite Abschnitt definiert die **Hauptparameter** und **Anfangsbedingungen**, die den gesamten Verlauf der Simulation beeinflussen. Die klare Struktur und die verschiedenen Stufen der Einflussfaktoren (z.B. `initial_neugier`, `pe_auswirkungen`) ermöglichen es, das Verhalten des Modells in verschiedenen Szenarien zu steuern. Dies macht diesen Abschnitt essenziell für die spätere Analyse und Visualisierung.
## **3. Funktionen zur Fluktuation und Verteilung**

- Funktionen wie `fluctuate_parameter`, `weibull_distribution`, `normal_distribution`, etc. definieren die statistischen Eigenschaften von Parametern.
- Eine Funktion zur Berechnung eines dynamischen Unsicherheitswertes `calculate_dynamic_C` basiert auf der Korrelation zwischen zwei Zeitreihen (`delta_e`, `delta_k`).

## **4. Simulation**

- Die Hauptsimulation führt mehrere Durchläufe durch, um die Kompetenzentwicklung und Neugier der Lernenden zu modellieren.
- **Schlüsselfunktionen** sind:
    - `simulate_motivation_neugier_modified`: Simuliert die Entwicklung der Motivation und Neugier eines Lernenden über eine bestimmte Anzahl von Monaten und Durchläufen.
    - `anpassung_der_bereitschaft`: Anpassung der Bereitschaftssteigerung je nach Quartal.
    - `gesamtauswirkung_pe`: Berechnet die Gesamtwirkung der PE auf die Entwicklung.

## **5. Berechnungen**

- Die Simulation erzeugt mehrere DataFrames (`simulations_ergebnisse_pe`, `bereitschaftssteigerungen`, `kompetenzniveaus_df`, etc.), die die Ergebnisse speichern.
- `pe_auswirkungen_list` speichert die PE-Wirkungen für jeden Durchlauf.

## **6. Statistische Analyse**

- Berechnung von **Mittelwerten**, **Standardabweichungen**, und **Medianen**.
- `korrelations_matrix_bereitschaft` und `korrelations_matrix_pe` berechnen die Korrelationsmatrix für Bereitschaft und PE-Auswirkungen.

## **7. Visualisierung**

- `fig_mc`, `fig_verhaeltnis`, `fig_summary`, `fig_bildungswirkgefuege`, etc., erstellen eine Vielzahl von Visualisierungen, darunter:
    - **Monte-Carlo-Simulation**: Zeigt die Simulationsergebnisse für mehrere Durchläufe.
    - **Korrelationen**: Visualisiert die Korrelationen der Simulationsergebnisse.
    - **Histogramme und Dichteverteilungen**: Analyse der Endkompetenzen.
    - **Sankey-Diagramme**: Zeigt den Fluss der Werte und Einflüsse zwischen verschiedenen Faktoren.
    - **3D-Visualisierung des Lernpfades** mit `networkx`: Die Position der Knoten wird durch Zufallswerte (`kognition_unsicherheit`, `emotion_unsicherheit`) bestimmt.

## **8. Dynamische Berechnung des Bildungswirkfaktors und Bildungswirkindikators**

- Der `bildungswirkfaktor` und `bildungswirkindikator` werden aus der Simulation abgeleitet und mittels erster und zweiter Ableitung analysiert.
- **Wendepunkte** in der Bildungseffektivität werden erkannt, um Empfehlungen für Maßnahmen abzuleiten (z.B. Interventionsbedarf).

## **9. Zusammenfassung**

Dieser Code bildet eine Simulation von Bildungsprozessen ab, die sowohl auf mathematischen Verteilungen als auch auf statistischen Methoden basiert. Die Ergebnisse werden in einer Vielzahl von dynamischen Visualisierungen dargestellt, um komplexe Zusammenhänge zu verdeutlichen.


# Code

```python
# =========================================
# Import
# -----------------------------------------

import numpy as np
import pandas as pd
from scipy.signal import find_peaks, savgol_filter
from scipy.stats import gaussian_kde, norm, pearsonr
from scipy.interpolate import interp1d
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)

# Benutzerdefinierte Farbpalette
colors = {
    "background": "#003366",
    "text": "#333333",
    "accent": "#663300",
    "primaryLine": "#660066",
    "secondaryLine": "#cc6600",
    "depthArea": "#006666",
    "brightArea": "#66CCCC",
    "positiveHighlight": "#336600",
    "negativeHighlight": "#990000",
    "white": "#ffffff"
}


# ========================================= 
# Eingaben
# -----------------------------------------

quartale = 12
simulations_durchlaeufe = 250

initial_neugier = 3.066    # aus 5DCR = 3.066 ; aus Näherung = 4.333 ; zur Demo = 5.000
start_kompetenz = 1.333    # aus KRI  = 4.733 ; aus APrVO = 1.133    ; zur Demo = 1.500

bereitschafts_std = 0.5

# Darstellung Lernort
bereitschafts_steigerung_phase = {
    'Anpassung': np.random.uniform(-0.05, 0),
    'Verfestigung': np.random.uniform(0.05, 0.1),
    'Wachstum': np.random.uniform(0.1, 0.15),
    'Plateau': np.random.uniform(0.05, 0.1)
}

# Darstellung Akteur
pe_auswirkungen = {
    'PFE': 0.1,                 # Persönlicher Fehlschlag extern      0.1
    'PLE': 0.08,                # Persönlicher Leistungseinbruch      0.08
    'PFV': 0.15,                # Persönlicher Fortschritt variabel   0.15
    'PGV': 0.1,                 # Persönliches Großereignis variabel  0.1
    'PSE': 0.2,                 # Persönlicher Stabilitätserfolg      0.2
    'PEE': 0.05                 # Persönlicher Erfolg extern          0.05
}

# C ist jetzt der dynamische Unsicherheitswert
def calculate_dynamic_C(delta_e, delta_k):
    r, _ = pearsonr(delta_e, delta_k)
    return abs(r) * (np.std(delta_e) * np.std(delta_k))

# ========================================= 
# Funktionen
# -----------------------------------------

# Relativer Zeitplan in Tagen
relative_schedule = [
    ("H-NFS-01", 7), ("H-NFS-02", 32), ("H-NFS-03", 17), ("H-NFS-04", 31),
    ("H-NFS-05", 53), ("H-NFS-06", 15), ("H-NFS-07", 67), ("H-NFS-08", 77),
    ("H-NFS-09", 13), ("H-NFS-10", 42), ("H-NFS-11", 2), ("H-NFS-12", 7),
    ("H-NFS-13", 4), ("H-NFS-14", 20), ("H-NFS-15", 31), ("H-NFS-16", 48),
    ("H-NFS-17", 7), ("H-NFS-18", 12), ("H-NFS-19", 29), ("H-NFS-20-1", 39),
    ("H-NFS-20-2", 51), ("H-NFS-21", 2), ("H-NFS-22-1", 37), ("H-NFS-22-2", 16),
    ("H-NFS-23", 5), ("H-NFS-24", 2), ("H-NFS-25", 42), ("H-NFS-26", 18),
    ("H-NFS-27", 2), ("H-NFS-28", 93), ("H-NFS-29", 100), ("H-NFS-30", 5),
    ("H-NFS-31", 54), ("H-NFS-32", 40)
]

# Aufgaben pro Handlungssituation
task_counts = [
    6, 16, 28, 37, 31, 14, 47, 36, 11, 25, 12, 18, 15, 18, 24, 26,
    24, 36, 20, 28, 29, 15, 5, 6, 17, 19, 11, 22, 9, 61, 55, 13, 54, 60
]

# Funktion zur Fluktuation eines Parameters innerhalb eines bestimmten Bereichs
def fluctuate_parameter(param, fluctuation_range=0.01):
    return param * (1 + np.random.normal(0, fluctuation_range))

# Anpassung der Bereitschaftssteigerung für jede Phase
for key in bereitschafts_steigerung_phase.keys():
    bereitschafts_steigerung_phase[key] = fluctuate_parameter(bereitschafts_steigerung_phase[key])

# Anpassung der PE-Auswirkungen
for key in pe_auswirkungen.keys():
    pe_auswirkungen[key] = fluctuate_parameter(pe_auswirkungen[key])

# Definition verschiedener Verteilungsfunktionen
def weibull_distribution(scale, shape, size):
    return np.random.weibull(shape, size) * scale

def normal_distribution(mean, std, size):
    return np.random.normal(mean, std, size)

def beta_distribution(alpha, beta, size):
    return np.random.beta(alpha, beta, size)

def poisson_distribution(lam, size):
    return np.random.poisson(lam, size)

# Berechnung der Kompetenzentwicklung mit der Weibull-Verteilung
def weibull_kompetenzentwicklung(scale, shape, current_level):
    improvement = np.random.weibull(shape) * scale
    new_competence_level = current_level + improvement
    return new_competence_level

# Überprüfung auf unerwartete Ereignisse
def check_for_unexpected_events(lam):
    return np.random.poisson(lam)

# Aktualisierung der Motivation mit Fluktuation
def update_motivation(current_motivation):
    fluctuation = np.random.normal(0, 0.1)
    new_motivation = max(0, min(10, current_motivation + fluctuation))
    return new_motivation

# Definition eines persönlichen Ereignisses und dessen Auswirkungen
def persoenliches_ereignis():
    ereignis_typ = np.random.choice(['PFE', 'PLE', 'PFV', 'PGV', 'PSE', 'PEE'],
                                    p=[0.125, 0.0833, 0.2083, 0.125, 0.4167, 0.0417])
    impacts = {
        'PFE': np.random.normal(-0.2, 0.1),
        'PLE': np.random.normal(-0.3, 0.2),
        'PFV': np.random.normal(0.2, 0.1),
        'PGV': np.random.normal(-0.4, 0.2),
        'PSE': np.random.normal(0.1, 0.05),
        'PEE': np.random.normal(0.3, 0.1)
    }
    return impacts[ereignis_typ]

# Klasse zur Darstellung eines Lernenden mit verschiedenen Attributen
class Lernender:
    def __init__(self, motivation, vorwissen, emotionales_wohlbefinden, soziale_interaktion, kognitive_faehigkeiten):
        self.motivation = motivation
        self.vorwissen = vorwissen
        self.emotionales_wohlbefinden = emotionales_wohlbefinden
        self.soziale_interaktion = soziale_interaktion
        self.kognitive_faehigkeiten = kognitive_faehigkeiten

    def update_motivation(self, delta):
        self.motivation = max(0, min(10, self.motivation + delta))

# Simulation der Motivation und Neugier eines Lernenden über mehrere Monate und Durchläufe
def simulate_motivation_neugier_modified(lernender, monate, durchlaeufe):
    np.random.seed(42)
    alle_neugier_verlaeufe = []
    alle_motivations_verlaeufe = []

    for _ in range(durchlaeufe):
        c = lernender.vorwissen
        motivation = lernender.motivation
        c_history = [c]
        m_history = [motivation]

        for _ in range(monate):
            c += np.random.normal(0, 0.5)
            c = max(0, min(10, c))
            delta_motivation = 0.1 * c
            lernender.update_motivation(delta_motivation)
            c_history.append(c)
            m_history.append(lernender.motivation)

        alle_neugier_verlaeufe.append(c_history)
        alle_motivations_verlaeufe.append(m_history)

    return alle_neugier_verlaeufe, alle_motivations_verlaeufe

# Anpassung der Bereitschaft je nach Phase
def anpassung_der_bereitschaft(aktuelles_quartal):
    phase = bereitschafts_steigerung_phase
    if aktuelles_quartal <= 4:
        return fluctuate_parameter(phase['Anpassung'])
    elif 5 <= aktuelles_quartal <= 6:
        return fluctuate_parameter(phase['Verfestigung'])
    elif 7 <= aktuelles_quartal <= 10:
        return fluctuate_parameter(phase['Wachstum'])
    else:
        return fluctuate_parameter(phase['Plateau'])

# Berechnung der Motivation je nach Quartal
def motivation(aktuelles_quartal):
    if aktuelles_quartal == 8:
        return fluctuate_parameter(-0.3)
    elif aktuelles_quartal == 12:
        return fluctuate_parameter(0.4)
    return fluctuate_parameter(0)

# Berechnung der Neugier je nach Quartal und Startkompetenz
def neugier(aktuelles_quartal, start_kompetenz):
    if aktuelles_quartal <= 6:
        return fluctuate_parameter(initial_neugier * 0.1)
    return fluctuate_parameter(-initial_neugier * 0.1)

# Berechnung der gesamten PE-Auswirkungen
def gesamtauswirkung_pe(pe_auswirkungen):
    auswirkungen = np.array(list(pe_auswirkungen.values()))
    zufallsfaktoren = np.random.uniform(0.8, 1.2, size=auswirkungen.shape)
    return np.sum(auswirkungen * zufallsfaktoren)

# Extreme finden
def identify_extrema_and_inflection_points(data):
    maxima, _ = find_peaks(data)
    minima, _ = find_peaks(-data)
    derivative = np.gradient(data)
    inflection_points, _ = find_peaks(np.abs(np.gradient(derivative)))
    return maxima, minima, inflection_points

# Glättung der Kurven mit Savitzky-Golay-Filter
def smooth_curve(data, window_length=21, polyorder=3):
    if len(data) < window_length:
        window_length = len(data) // 2 * 2 + 1  # Anpassen der Fensterlänge für sehr kleine Datensätze
    return savgol_filter(data, window_length, polyorder)

# Hilfsfunktion zur Summation von Listen von Listen
def flatten_and_sum(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return sum(flat_list)

# Glättung der Kurven und Beschränkung auf maximal 10
def smooth_curve(data, polyorder=3):
    n = len(data)
    window_length = min(21, n if n % 2 == 1 else n - 1)
    return savgol_filter(np.clip(data, None, 10), window_length, polyorder)


# =========================================
# Relevante Berechungen
# -----------------------------------------

# Aktuelles Datum und Uhrzeit erhalten
current_time = datetime.datetime.now()

# Formatieren des Datums und der Uhrzeit für den Titel
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Spaltennamen für DataFrames
quartale_columns = [f'Quartal_{i}' for i in range(0, quartale + 1)]
durchlauf_columns = [f'Durchlauf_{i}' for i in range(simulations_durchlaeufe)]

# Initialisierung der DataFrames zur Speicherung der Simulationsergebnisse und Bereitschaftssteigerungen
simulations_ergebnisse_pe = pd.DataFrame(index=range(0, quartale + 1), columns=durchlauf_columns)
bereitschaftssteigerungen = pd.DataFrame(index=range(0, simulations_durchlaeufe + 1), columns=quartale_columns)
kompetenzniveaus_df = pd.DataFrame(index=range(0, quartale + 1), columns=[f'Durchlauf_{i}' for i in range(simulations_durchlaeufe)])
neugier_entwicklung_df = pd.DataFrame(index=range(0, quartale + 1), columns=[f'Durchlauf_{i}' for i in range(simulations_durchlaeufe)])

# Initialisierung der Liste für die Aufzeichnung von PE-Auswirkungen
pe_auswirkungen_list = []

# Simulation der Kompetenzentwicklung für jeden Durchlauf
for durchlauf in range(simulations_durchlaeufe):
    kompetenzentwicklung = np.full(quartale + 1, start_kompetenz)
    neugierentwicklung = np.full(quartale + 1, initial_neugier)
    pe_auswirkungen_temp = []

    # Beginn der Schleife bei Quartal 0
    for quartal in range(0, quartale + 1):
        if quartal == 0:
            # Quartal 0 ist der Startpunkt, daher keine Veränderungen
            kompetenzniveaus_df.at[quartal, f'Durchlauf_{durchlauf}'] = start_kompetenz
            neugier_entwicklung_df.at[quartal, f'Durchlauf_{durchlauf}'] = initial_neugier
            simulations_ergebnisse_pe.at[quartal, f'Durchlauf_{durchlauf}'] = start_kompetenz
            pe_auswirkungen_temp.append(0)  # Keine PE-Auswirkungen im Startquartal
        else:
            # Berechnung der Steigerung der Bereitschaft, Motivation und Neugier sowie der gesamten PE-Auswirkungen
            steigerung = anpassung_der_bereitschaft(quartal)
            motivation_wert = motivation(quartal)
            neugier_wert = neugier(quartal, start_kompetenz)
            pe_auswirkung = gesamtauswirkung_pe(pe_auswirkungen)

            # Berechnung der neuen Bereitschaft und Anpassung der Kompetenzentwicklung
            bereitschaft = np.random.normal(steigerung + motivation_wert + neugier_wert + pe_auswirkung, bereitschafts_std)
            neue_kompetenz = np.clip(kompetenzentwicklung[quartal - 1] + bereitschaft, 1, 10)
            neue_neugier = max(0, min(10, neugierentwicklung[quartal - 1] + np.random.normal(0, 0.1)))

            # Speichern der neuen Werte
            kompetenzentwicklung[quartal] = neue_kompetenz
            neugierentwicklung[quartal] = neue_neugier
            kompetenzniveaus_df.at[quartal, f'Durchlauf_{durchlauf}'] = neue_kompetenz
            neugier_entwicklung_df.at[quartal, f'Durchlauf_{durchlauf}'] = neue_neugier
            bereitschaftssteigerungen.at[durchlauf, f'Quartal_{quartal}'] = bereitschaft
            pe_auswirkungen_temp.append(pe_auswirkung)

    pe_auswirkungen_list.append(pe_auswirkungen_temp)
    simulations_ergebnisse_pe.iloc[:, durchlauf] = kompetenzentwicklung

# Sicherstellen, dass alle Kompetenzniveaus auf maximal 10 beschränkt sind
simulations_ergebnisse_pe_clipped = simulations_ergebnisse_pe.clip(upper=10)

# Index zurücksetzen, falls der Startindex nicht 0 ist
if simulations_ergebnisse_pe_clipped.index[0] > 0:
    simulations_ergebnisse_pe_clipped.reset_index(drop=True, inplace=True)

# Wenn Quartal 0 inbegriffen ist, passen Sie die Spaltenberechnung entsprechend an
pe_auswirkungen_df = pd.DataFrame(pe_auswirkungen_list, columns=range(0, quartale + 1)).T

# Konvertierung der Datentypen falls notwendig
bereitschaftssteigerungen = bereitschaftssteigerungen.infer_objects(copy=False)
pe_auswirkungen_df = pe_auswirkungen_df.infer_objects(copy=False)

# Berechnung der Mittelwerte für Bereitschaft und PE-Auswirkungen
mittelwerte_bereitschaft = bereitschaftssteigerungen.mean(axis=0)
mittelwerte_pe = pe_auswirkungen_df.mean(axis=1)

# Berechnung der Median- und Mittelwerte sowie der Standardabweichung der Kompetenzentwicklung
mediane_kompetenz = simulations_ergebnisse_pe.median(axis=1)
mittelwerte_kompetenz = simulations_ergebnisse_pe.mean(axis=1)
stddev_kompetenz = simulations_ergebnisse_pe.std(axis=1)

# Berechnung der Unsicherheitsprodukte
delta_bereitschaft = bereitschafts_std
delta_kompetenz = stddev_kompetenz.mean()
unschaerfe_produkt = delta_bereitschaft * delta_kompetenz

# Berechnung der Median- und Mittelwerte sowie der Standardabweichung für die beschränkten Kompetenzwerte
mediane_kompetenz = simulations_ergebnisse_pe_clipped.median(axis=1)
mittelwerte_kompetenz = simulations_ergebnisse_pe_clipped.mean(axis=1)
stddev_kompetenz = simulations_ergebnisse_pe_clipped.std(axis=1).clip(upper=10)

# Berechnung der PE-Wirkungen für alle Durchläufe
pe_wirkungen = [gesamtauswirkung_pe(pe_auswirkungen) for _ in range(simulations_durchlaeufe)]

# Simulation der Änderungen von Neugier und Motivation
veranderungen_neugier, veranderungen_motivation = simulate_motivation_neugier_modified(Lernender(initial_neugier, start_kompetenz, 0, 0, 0), quartale, simulations_durchlaeufe)

# Berechnung der Bereitschaft für jedes Quartal
bereitschaft = [anpassung_der_bereitschaft(quartal) for quartal in range(1, quartale + 1)]

# Umwandlung der Kompetenzentwicklung in eine Liste
kompetenzentwicklung = simulations_ergebnisse_pe.mean(axis=1).tolist()

# Berechnung von Delta K und Delta E
delta_k = simulations_ergebnisse_pe.std(axis=1).tolist()  # Unsicherheit der Kompetenzentwicklung
delta_e = (simulations_ergebnisse_pe.mean(axis=1) - simulations_ergebnisse_pe.mean(axis=1).shift(1).fillna(0)).infer_objects().tolist()

# Runden der Werte auf 3 Dezimalstellen
delta_k_mean = round(np.mean(delta_k), 3)
delta_e_mean = round(np.mean(delta_e), 3)

# Berechnung des Bildungswirkfaktors und relevanter Werte
bildungswirkfaktoren = delta_bereitschaft * simulations_ergebnisse_pe.std(axis=1)

# Glättung der Bildungswirkfaktoren
bildungswirkfaktoren_smooth = smooth_curve(bildungswirkfaktoren)

# Berechnung der ersten Ableitung der geglätteten Bildungswirkfaktoren
steigungen_bildungswirkfaktor = np.gradient(bildungswirkfaktoren_smooth)

# Glättung der Steigungen
steigungen_bildungswirkfaktor_smooth = smooth_curve(steigungen_bildungswirkfaktor)

# Berechnung des Integrals des Bildungswirkfaktors
integral_bildungswirkfaktor = np.trapz(bildungswirkfaktoren, dx=1)

# Berechnung der Wendepunkte, Minima und Maxima für den Bildungswirkindikator (ι)
erste_ableitung_bildungswirkfaktor = steigungen_bildungswirkfaktor_smooth
zweite_ableitung_bildungswirkfaktor = np.gradient(steigungen_bildungswirkfaktor_smooth)

wendepunkte_bildungswirkfaktor = np.where(np.diff(np.sign(zweite_ableitung_bildungswirkfaktor)))[0]
maxima_bildungswirkfaktor, _ = find_peaks(bildungswirkfaktoren_smooth)
minima_bildungswirkfaktor, _ = find_peaks(-bildungswirkfaktoren_smooth)

# Berechnung des Bildungswirkindikators als die Ableitung des Bildungswirkfaktors
bildungswirkindikator = np.gradient(bildungswirkfaktoren)
integral_bildungswirkindikator = np.trapz(bildungswirkindikator, dx=1)

# Glättung der Kurven des Bildungswirkindikators
bildungswirkindikatoren_smooth = smooth_curve(bildungswirkindikator)
steigungen_bildungswirkindikator_smooth = smooth_curve(np.gradient(bildungswirkindikator))

# Berechnung der Wendepunkte, Minima und Maxima des Bildungswirkindikators
erste_ableitung_bildungswirkindikator = bildungswirkindikatoren_smooth
zweite_ableitung_bildungswirkindikator = np.gradient(bildungswirkindikatoren_smooth)

wendepunkte_bildungswirkindikator = np.where(np.diff(np.sign(zweite_ableitung_bildungswirkfaktor)))[0]

maxima_bildungswirkindikator, _ = find_peaks(bildungswirkindikatoren_smooth)
minima_bildungswirkindikator, _ = find_peaks(-bildungswirkindikatoren_smooth)

# Berechnung der Extrema und Wendepunkte für ν und ι
maxima_nu, minima_nu, inflection_points_nu = identify_extrema_and_inflection_points(bildungswirkfaktoren_smooth)
maxima_iota, minima_iota, inflection_points_iota = identify_extrema_and_inflection_points(steigungen_bildungswirkfaktor_smooth)

# Berechnung der Bildungswirkdynamik als zweite Ableitung der geglätteten Bildungswirkfaktoren
bildungswirkdynamik = np.gradient(np.gradient(bildungswirkfaktoren_smooth))

# Glättung der Bildungswirkdynamik
bildungswirkdynamik_smooth = smooth_curve(bildungswirkdynamik)

# Glättung der Ergebnisse durch rollierende Mittelwerte
smoothed_results = simulations_ergebnisse_pe_clipped.rolling(window=3, min_periods=1).mean()
mittelwerte = smoothed_results.mean(axis=1)
flaeche_unter_mittelwert = np.trapz(smooth_curve(mittelwerte), dx=1)
quartale_range = np.arange(0, quartale + 1)

# Berechnung der mittleren Steigungen der Kompetenzentwicklung
mittlere_steigungen = mittelwerte_kompetenz.diff().fillna(0).infer_objects().tolist()

# Bestimmung des besten und schlechtesten Ergebnisses sowie der Flächen unter den Kurven
bestes_ergebnis = simulations_ergebnisse_pe_clipped.max(axis=1)
schlechtestes_ergebnis = simulations_ergebnisse_pe_clipped.min(axis=1)
flaeche_unter_bestes = np.trapz(smooth_curve(bestes_ergebnis), dx=1)
flaeche_unter_schlechtestes = np.trapz(smooth_curve(schlechtestes_ergebnis), dx=1)

# Analyse der Endkompetenzen
end_kompetenzen = simulations_ergebnisse_pe.iloc[-1].dropna().apply(pd.to_numeric, errors='coerce')
data = end_kompetenzen.dropna()
data = data.apply(pd.to_numeric, errors='coerce').dropna()

# Erstellung der KDE und Normalverteilung für die Endkompetenzen
density_kde = gaussian_kde(data)
x_kde = np.linspace(min(data), max(data), 1000)
y_kde = density_kde(x_kde)

mean, std = norm.fit(data)
y_norm = norm.pdf(x_kde, mean, std)

# Behandeln von NaN-Werten in den Bereitschaftssteigerungen-Daten
# Ersetze NaN-Werte durch den Median oder entferne fehlende Daten
bereitschaftssteigerungen.fillna(bereitschaftssteigerungen.median(), inplace=True)

# Behandeln von NaN-Werten in den PE Auswirkungen-Daten
# Ersetze NaN-Werte durch den Median oder entferne fehlende Daten
pe_auswirkungen_df.fillna(pe_auswirkungen_df.median(), inplace=True)

# Berechnung der Korrelationsmatrix
df = pd.DataFrame(np.random.randn(100, 13), columns=[f'Durchlauf {i+1}' for i in range(13)])
korrelations_matrix_bereitschaft = np.corrcoef(bereitschaftssteigerungen.T)
korrelations_matrix_pe = np.corrcoef(pe_auswirkungen_df.T)

# Sicherstellen, dass die Dimensionen der Korrelationsmatrix korrekt sind
# simulations_durchlaeufe = korrelations_matrix_bereitschaft.shape[0]
simulations_durchlaeufe_pe = korrelations_matrix_pe.shape[0]

# Berechnung der minimalen und maximalen Werte für die Farbskala
zmin_bereitschaft = korrelations_matrix_bereitschaft.min().min()
zmax_bereitschaft = korrelations_matrix_bereitschaft.max().max()
zmin_pe = korrelations_matrix_pe.min().min()
zmax_pe = korrelations_matrix_pe.max().max()

# Berechnung der Korrelationskoeffizienten für jeden Durchlauf
korrelationskoeffizienten_durchlaeufe = [
    pearsonr(np.random.randn(100), np.random.randn(100))[0] for _ in range(simulations_durchlaeufe)
]

# Daten für das Streudiagramm
durchlauf_df = pd.DataFrame({
    'Durchlauf': range(1, simulations_durchlaeufe + 1),
    'Korrelationskoeffizient': korrelationskoeffizienten_durchlaeufe
})

# Berechnung der Korrelationskoeffizienten für Delta E und Delta K
korrelationskoeffizienten = [pearsonr(delta_e, delta_k)[0] for _ in range(simulations_durchlaeufe)]

# Zählen der positiven, negativen und nahe Null Korrelationskoeffizienten
positive_korrelationskoeffizienten = sum(1 for k in korrelationskoeffizienten if k > 0.1)
negative_korrelationskoeffizienten = sum(1 for k in korrelationskoeffizienten if k < -0.1)
nahe_null_korrelationskoeffizienten = sum(1 for k in korrelationskoeffizienten if -0.1 <= k <= 0.1)

# Daten für das Verhältnis
verhaeltnis_daten = {
    'Korrelationskoeffizient': ['Positiv', 'Negativ', 'Nahe Null'],
    'Anzahl': [positive_korrelationskoeffizienten, negative_korrelationskoeffizienten, nahe_null_korrelationskoeffizienten]
}

verhaeltnis_df = pd.DataFrame(verhaeltnis_daten)





# ====================================================
# ====================================================
# ====================================================



# Simulation der Unsicherheitswerte unter Berücksichtigung der Berechnungsformeln
np.random.seed(42)  # Für Reproduzierbarkeit

# Beispielwerte für die Parameter zur Berechnung
sigma_kompetenz = 0.8  # Beispielwert für σKompetenz (Standardabweichung der Kompetenz)
sigma_emotional = 0.5  # Beispielwert für σEmotional (Standardabweichung der emotionalen Reaktionen)
vorwissen_faktor = 5   # Subjektiver Wert für Vorwissen
emotionale_stabilitaet_faktor = 2  # Maß für die emotionale Stabilität
aufgabenkomplexitaet = 1.2         # Komplexitätsfaktor für die Aufgabenstellung
emotionale_herausforderung = 1.1   # Bewertungsmaß der emotionalen Anforderungen

# Berechnung der Kognitionsunsicherheit ΔK für jedes Element im Zeitplan (relative_schedule)
kognition_unsicherheit = [
    sigma_kompetenz * (1 / (vorwissen_faktor + 1)) * aufgabenkomplexitaet
    for _ in range(len(relative_schedule))
]

# Berechnung der Emotionalen Unsicherheit ΔE für jedes Element im Zeitplan (relative_schedule)
emotion_unsicherheit = [
    sigma_emotional * (1 / (emotionale_stabilitaet_faktor + 1)) * emotionale_herausforderung
    for _ in range(len(relative_schedule))
]

# Ausgabe der berechneten Unsicherheitswerte
# print(f"Kognitionsunsicherheit (ΔK): {kognition_unsicherheit}")
# print(f"Emotionale Unsicherheit (ΔE): {emotion_unsicherheit}")


# ====================================================
# ====================================================
# ====================================================


# =========================================
# Visualisierungen
# -----------------------------------------


# Visualisierung des Verhältnisses
fig_verhaeltnis = go.Figure(data=[
    go.Bar(name='Korrelationskoeffizienten', x=verhaeltnis_df['Korrelationskoeffizient'], y=verhaeltnis_df['Anzahl'], marker_color=[colors['positiveHighlight'], colors['negativeHighlight'], colors['accent']])
])

fig_verhaeltnis.update_layout(
    title='Verhältnis der Korrelationskoeffizienten in Bezug auf Null',
    xaxis=dict(
        title='Korrelationskoeffizient',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=False,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        title='Durchläufe',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    template='plotly_white',
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text'])
)



# Interpretation basierend auf der Verteilung der Korrelationskoeffizienten
interpretation_text = ""
if positive_korrelationskoeffizienten > negative_korrelationskoeffizienten and positive_korrelationskoeffizienten > nahe_null_korrelationskoeffizienten:
    interpretation_text = "Mehrheitlich positive Korrelationen: Verbesserungen in der Messgenauigkeit könnten auch die Unsicherheit in der Kompetenzentwicklung reduzieren."
elif negative_korrelationskoeffizienten > positive_korrelationskoeffizienten and negative_korrelationskoeffizienten > nahe_null_korrelationskoeffizienten:
    interpretation_text = "Mehrheitlich negative Korrelationen: Eine Balance zwischen Messgenauigkeit und Entwicklungsflexibilität ist notwendig."
elif nahe_null_korrelationskoeffizienten > positive_korrelationskoeffizienten and nahe_null_korrelationskoeffizienten > negative_korrelationskoeffizienten:
    interpretation_text = "Korrelationskoeffizienten nahe Null: Die Unsicherheiten in der Messung und Entwicklung können unabhängig voneinander optimiert werden."

# Textfeld zur Interpretation hinzufügen
fig_verhaeltnis.add_annotation(
    x=0.5, y=-0.2, xref='paper', yref='paper',
    text=interpretation_text,
    showarrow=False,
    font=dict(color=colors['text'])
)

fig_verhaeltnis.show()

# Visualisierung der einzelnen Durchläufe als Streudiagramm
fig_durchlaeufe = go.Figure(data=[
    go.Scatter(mode='markers', name='Durchläufe', x=list(range(1, simulations_durchlaeufe + 1)), y=[pearsonr(np.random.randn(100), np.random.randn(100))[0] for _ in range(simulations_durchlaeufe)], marker=dict(color=colors['primaryLine']))
])

fig_durchlaeufe.update_layout(
    title='Korrelationskoeffizienten der einzelnen Durchläufe',
    xaxis=dict(
        title='Durchlauf',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=False,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        title='Korrelationskoeffizient',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    template='plotly_white',
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text'])
)

fig_durchlaeufe.show()

# Bildungswirkgefüge | Unschärferelation (ΔE⋅ΔK=C)

labels = ['Kompetenzentwicklung ΔE', 'Kompetenzmessung ΔK']
values = [delta_bereitschaft, delta_kompetenz]

fig1 = go.Figure(data=[
    go.Bar(name='Unsicherheiten', x=labels, y=values, marker_color=[colors['brightArea'], colors['depthArea']])
])

fig1.update_layout(
    title='Kompetenzentwicklung | Unsicherheiten',
    xaxis=dict(
        title='Kategorie',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=False,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        title='Wert',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    template='plotly_white',
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text'])
)

categories = ['Produkt der Unsicherheiten', 'Dynamischer Unsicherheitswert (C)']
dynamic_C = calculate_dynamic_C(delta_e, delta_k)
values = [unschaerfe_produkt, dynamic_C]

fig2 = go.Figure(data=[
    go.Bar(name='Unschärfeprodukt', x=categories, y=values, marker_color=[colors['accent'], colors['negativeHighlight']])
])

fig2.update_layout(
    title='Kompetenzentwicklung | Unsicherheitsrelation',
    xaxis=dict(
        title='Kategorie',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=False,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        title='Wert',
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    template='plotly_white',
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text'])
)

erfuellt = unschaerfe_produkt >= dynamic_C
status_text = "Die Unsicherheitsrelation im Bildungswirkgefüge ist erfüllt." if erfuellt else "Die Unsicherheitsrelation im Bildungswirkgefüge ist nicht erfüllt."
status_color = colors['positiveHighlight'] if erfuellt else colors['negativeHighlight']

fig3 = go.Figure()

fig3.add_trace(go.Indicator(
    mode="gauge+number+delta",
    value=unschaerfe_produkt,
    delta={'reference': dynamic_C, 'increasing': {'color': colors['primaryLine']}},
    gauge={
        'axis': {'range': [None, max(unschaerfe_produkt, dynamic_C) * 1.2]},
        'steps': [
            {'range': [0, dynamic_C], 'color': colors['brightArea']},
            {'range': [dynamic_C, max(unschaerfe_produkt, dynamic_C) * 1.2], 'color': colors['depthArea']}
        ],
        'threshold': {
            'line': {'color': colors['negativeHighlight'], 'width': 4},
            'thickness': 0.75,
            'value': dynamic_C
        }
    },
    title={'text': "Bildungswirkgefüge | Unsicherheitsrelation (ΔE⋅ΔK=C)"}
))

fig3.update_layout(
    title=status_text,
    title_font=dict(color=status_color),
    template='plotly_white',
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text']),
    xaxis=dict(
        showgrid=False,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    )
)

fig1.show()
fig2.show()
fig3.show()

# -----------------------------------------
# Monte Carlo Simulation
# -----------------------------------------

fig_mc = go.Figure()

# Stellen Sie sicher, dass für jeden Durchlauf Daten für alle Quartale vorhanden sind
for i, column in enumerate(simulations_ergebnisse_pe_clipped.columns):
    smoothed_data = smooth_curve(simulations_ergebnisse_pe_clipped[column].values)
    smoothed_data_clipped = np.clip(smoothed_data, 0, 10)  # Begrenzen der interpolierten Werte auf 10
    fig_mc.add_trace(go.Scatter(
        x=simulations_ergebnisse_pe_clipped.index,  # Stellen Sie sicher, dass der Index von 1 bis 12 läuft
        y=smoothed_data_clipped,
        mode='lines',
        name=f'Durchlauf {i + 1}',
        line=dict(
            color=colors['primaryLine'],
            width=1
        )
    ))

fig_mc.update_xaxes(
    title="Zeit [Quartal]",
    title_font=dict(color=colors['text']),
    tickfont=dict(color=colors['text']),
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=3, label="1Q", step="month", stepmode="backward"),
            dict(count=12, label="1J", step="month", stepmode="backward"),
            dict(step="all", label="Alle")
        ])
    ),
    range=[0, 12],  # Stellen Sie sicher, dass die Achse von Quartal 1 bis 12 reicht
    showgrid=True,
    gridcolor='lightgray',
    dtick=1,  # Einstellung des Tick-Intervalls
    linecolor=colors['text'],
    tickcolor=colors['text']
)

fig_mc.update_layout(
    title="Kompetenzentwicklung | Monte Carlo-Simulation ({} Durchläufe)".format(simulations_durchlaeufe),
    title_font=dict(color=colors['text']),
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        linecolor=colors['text'],  # Setzt die Farbe der x-Achsenlinie
        tickcolor=colors['text'],  # Setzt die Farbe der Tick-Markierungen auf der x-Achse
        tickangle=0  # Optional, um den Winkel der Tick-Labels anzupassen
    ),
    yaxis=dict(
        title="Kompetenzniveau",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        range=[0, 10],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        linecolor=colors['text'],  # Setzt die Farbe der y-Achsenlinie
        tickcolor=colors['text']  # Setzt die Farbe der Tick-Markierungen auf der y-Achse
    ),
    legend_title="Legende",
    legend_title_font=dict(color=colors['text']),
    template="plotly_white",
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    hovermode="x unified"
)

fig_mc.show()

# -----------------------------------------
# Statistische Werte
# -----------------------------------------

fig_summary = go.Figure()

# Daten hinzufügen
# -----------------------------------------

# Streuungsbereich
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe_clipped.index.tolist() + simulations_ergebnisse_pe_clipped.index.tolist()[::-1],
    y=(np.clip(mittelwerte_kompetenz + stddev_kompetenz, None, 10)).tolist() + (np.clip(mittelwerte_kompetenz - stddev_kompetenz, None, 10)).tolist()[::-1],
    fill='toself',
    fillcolor=colors['brightArea'],
    line=dict(color=colors['depthArea']),
    name='Streuung',
    hoverinfo='text',
    hovertext=[
        f"Quartal {x}, Streuung oben: {y:.2f}" if i < len(simulations_ergebnisse_pe_clipped.index) else f"Quartal {x}, Streuung unten: {y:.2f}"
        for i, (x, y) in enumerate(zip(
            simulations_ergebnisse_pe_clipped.index.tolist() * 2,
            (np.clip(mittelwerte_kompetenz + stddev_kompetenz, None, 10)).tolist() + (np.clip(mittelwerte_kompetenz - stddev_kompetenz, None, 10)).tolist()[::-1]
        ))
    ]
))

# Mittelwert
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe_clipped.index,
    y=smooth_curve(mittelwerte_kompetenz),
    mode='lines',
    name='Mittelwert',
    line=dict(color=colors['background']),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Mittelwert %{y:.2f}<extra></extra>"
))

# Median
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe_clipped.index,
    y=smooth_curve(mediane_kompetenz),
    mode='lines',
    name='Median',
    line=dict(color=colors['secondaryLine'], dash='dash'),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Median %{y:.2f}<extra></extra>"
))

# Steigung
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe_clipped.index,
    y=smooth_curve(mittlere_steigungen),
    mode='lines',
    name='Steigung',
    line=dict(color=colors['accent']),
    yaxis='y2',
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Steigung %{y:.2f}<extra></extra>"
))

# Layout-Update
fig_summary.update_layout(
    title="Kompetenzentwicklung | Statistische Werte",
    title_font=dict(color=colors['text']),
    xaxis=dict(
        title="Quartal",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,  # x-Achsen-Gitter anzeigen
        gridcolor='lightgray',
        dtick=1,
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=3, label="1Q", step="month", stepmode="backward"),
                dict(count=12, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Kompetenzniveau",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        range=[0, 10],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1
    ),
    yaxis2=dict(
        title="Steigung Mittelwert",
        overlaying='y',
        side='right',
        range=[-0.5, 2],
        dtick=1,
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
    ),
    legend_title="Legende",
    legend_title_font=dict(color=colors['text']),
    template="plotly_white",
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    hovermode="x unified"
)

fig_summary.show()

# -----------------------------------------
# Kompetenzentwicklung | Kumulative Kompetenz
# -----------------------------------------

fig_kumulative_kompetenz = go.Figure()

fig_kumulative_kompetenz.add_trace(go.Scatter(
    x=quartale_range,
    y=smooth_curve(mittelwerte),
    fill='tozeroy',
    fillcolor=colors['background'],
    name='Kompetenz',
    line=dict(color=colors['background']),
    mode='lines'
))

fig_kumulative_kompetenz.update_layout(
    title=f"Kompetenzentwicklung | Kumulative Kompetenz: {flaeche_unter_mittelwert:.2f}",
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1Q", step="month", stepmode="backward"),
                dict(count=4, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Kompetenzniveau",
        range=[0, 10],
        dtick=1,
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
    ),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    template="plotly_white",
    hovermode="x unified",
    showlegend=True,
    legend_title=dict(text="Legende", font=dict(color=colors['text']))
)

fig_kumulative_kompetenz.show()

# -----------------------------------------
# Kompetenzentwicklung | Kumulativer Vergleich
# -----------------------------------------

fig_kumulativer_vergleich = go.Figure()

fig_kumulativer_vergleich.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe_clipped.index,
    y=smooth_curve(bestes_ergebnis),
    fill='tozeroy',
    name='Optimum',
    line=dict(color=colors['positiveHighlight']),
))

fig_kumulativer_vergleich.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe_clipped.index,
    y=smooth_curve(schlechtestes_ergebnis),
    fill='tozeroy',
    name='Minimum',
    line=dict(color=colors['negativeHighlight']),
))

fig_kumulativer_vergleich.update_layout(
    title=f"Kompetenzentwicklung | Kumulativer Vergleich: Beste ({flaeche_unter_bestes:.2f}) vs. Schlechteste ({flaeche_unter_schlechtestes:.2f})",
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1Q", step="month", stepmode="backward"),
                dict(count=4, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Kompetenzniveau",
        range=[0, 10],
        dtick=1,
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
    ),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    template="plotly_white",
    hovermode="x unified"
)

fig_kumulativer_vergleich.show()

# -----------------------------------------
# Kompetenzentwicklung | Histogramm, Dichte und Kernel-Dichte-Schätzung (KDE)
# -----------------------------------------

fig_histogram = go.Figure()

fig_histogram.add_trace(go.Histogram(
    x=data,
    name="Histogramm",
    marker_color=colors['accent'],
    opacity=0.3,
    histnorm='probability'
))

fig_histogram.add_trace(go.Scatter(
    x=x_kde,
    y=y_kde,
    mode='lines',
    line=dict(color=colors['primaryLine'], width=2),
    name='KDE'
))

fig_histogram.add_trace(go.Scatter(
    x=x_kde,
    y=y_norm,
    mode='lines',
    line=dict(color=colors['secondaryLine'], width=2),
    name='Dichte'
))

fig_histogram.update_layout(
    title="Kompetenzentwicklung | Histogramm, Dichte und Kernel-Dichte-Schätzung (KDE)",
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=False,
        gridcolor='lightgray',
        dtick=1,
        range=[0, 12],  # Den vollen Bereich der Quartale abdecken
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1Q", step="month", stepmode="backward"),
                dict(count=4, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Wert",
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1
    ),
    legend_title=dict(text="Legende", font=dict(color=colors['text'])),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    template="plotly_white",
    hovermode="x unified"
)

fig_histogram.show()

# -----------------------------------------
# Kompetenzentwicklung | Einflüsse persönlicher Ereignisse (PE)
# -----------------------------------------

data = pd.DataFrame(list(pe_auswirkungen.items()), columns=['Ereigniskategorie', 'Auswirkung'])
data = data.sort_values(by='Auswirkung', ascending=False)

data['Label'] = data.apply(lambda row: f"{row['Ereigniskategorie']}: {row['Auswirkung']:.2f}", axis=1)

fig_einfluss = px.bar(
    data,
    x='Ereigniskategorie',
    y='Auswirkung',
    title="Kompetenzentwicklung | Einflüsse persönlicher Ereignisse (PE)",
    labels={'Ereigniskategorie': "Kategorie", 'Einfluss': "Einfluss auf Kompetenzentwicklung"},
    color='Auswirkung',
    color_continuous_scale=[
        [0, colors['negativeHighlight']],
        [0.25, colors['accent']],
        [0.5, colors['secondaryLine']],
        [0.75, colors['primaryLine']],
        [1, colors['positiveHighlight']]
    ],
    text='Label'
)

fig_einfluss.update_layout(
    coloraxis_colorbar=dict(title="Stärke"),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text']),
    title_font=dict(color=colors['text']),
    xaxis=dict(
        title="Kategorie",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=False,  # x-Achsen-Gitter ausblenden
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        title="Wert",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,  # y-Achsen-Gitter anzeigen
        gridcolor='lightgray',
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    legend_title=dict(text="Legende", font=dict(color=colors['text']))
)

fig_einfluss.update_traces(texttemplate='%{text}', textposition='outside')

fig_einfluss.show()

# -----------------------------------------
# Kompetenzentwicklung | Korrelationsmatrix (Mittleres Kompetenzniveau und Bereitschaftssteigerung)
# -----------------------------------------

# Sicherstellen, dass die Anzahl der Durchläufe korrekt definiert ist
# simulations_durchlaeufe = bereitschaftssteigerungen.shape[1]

# Labels für die Durchläufe
labels = [f'Durchlauf {i+1}' for i in range(simulations_durchlaeufe)]
labels = [f'Durchlauf {i+1}' for i in range(korrelations_matrix_bereitschaft.shape[0])]
labels_pe = [f'Durchlauf {i+1}' for i in range(korrelations_matrix_pe.shape[0])]

# Berechnung der Korrelationsmatrix für Bereitschaftssteigerungen
korrelations_matrix_bereitschaft = np.corrcoef(bereitschaftssteigerungen.T)
korrelations_matrix_pe = np.corrcoef(pe_auswirkungen_df.T)

# Visualisierung der Korrelationsmatrix für Bereitschaftssteigerungen
fig_bereitschaft = px.imshow(
    korrelations_matrix_bereitschaft,
    text_auto=True,
    labels=dict(x="Durchläufe", y="Durchläufe", color="Korrelationskoeffizient"),
    x=labels,
    y=labels,
    title="Kompetenzentwicklung | Korrelationsmatrix (Mittleres Kompetenzniveau und Bereitschaftssteigerung)",
    color_continuous_scale=[(0.0, colors['primaryLine']), (1.0, colors['secondaryLine'])],
    zmin=zmin_bereitschaft,
    zmax=zmax_bereitschaft
)

fig_bereitschaft.update_traces(hoverinfo='text+z', hovertemplate="<b>%{x}, %{y}</b><br>Korrelationskoeffizient: %{z:.2f}<extra></extra>")
fig_bereitschaft.update_xaxes(side="bottom")
fig_bereitschaft.update_layout(
    coloraxis_colorbar=dict(title="ρ"),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text'])
)
fig_bereitschaft.show()

# Visualisierung der Korrelationsmatrix für PE-Auswirkungen
fig_pe = px.imshow(
    korrelations_matrix_pe,
    text_auto=True,
    labels=dict(x="Durchläufe", y="Durchläufe", color="Korrelationskoeffizient"),
    x=labels_pe,
    y=labels_pe,
    title="Kompetenzentwicklung | Korrelationsmatrix (Mittleres Kompetenzniveau und Auswirkungen Persönlicher Ereignisse (PE)",
    color_continuous_scale=[(0.0, colors['primaryLine']), (1.0, colors['secondaryLine'])],
    zmin=zmin_pe,
    zmax=zmax_pe
)

fig_pe.update_traces(hoverinfo='text+z', hovertemplate="<b>%{x}, %{y}</b><br>Korrelationskoeffizient: %{z:.2f}<extra></extra>")
fig_pe.update_xaxes(side="bottom")
fig_pe.update_layout(
    coloraxis_colorbar=dict(title="ρ"),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text'])
)
fig_pe.show()

# -----------------------------------------
# Kompetenzentwicklung | Entwicklung Kompetenzniveau
# -----------------------------------------

fig_kompetenzniveau = go.Figure()

fig_kompetenzniveau.add_trace(
    go.Scatter(
        x=kompetenzniveaus_df.index,
        y=kompetenzniveaus_df.mean(axis=1).clip(upper=10),
        mode='lines+markers',
        name='Kompetenzniveau',
        line=dict(color=colors['primaryLine'], width=2)
    )
)

# Festlegen des Bereichs basierend auf der Index-Länge
x_axis_range = [0, kompetenzniveaus_df.index.max()]  # Stellt sicher, dass wir bei 0 beginnen und beim letzten Quartal enden

fig_kompetenzniveau.update_layout(
    title="Kompetenzentwicklung | Entwicklung Kompetenzniveau",
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        range=x_axis_range,  # Setzen des expliziten Bereichs für die x-Achse
        rangeslider=dict(visible=True, range=x_axis_range),  # Schieberegler-Bereich entsprechend einstellen
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1Q", step="month", stepmode="backward"),
                dict(count=4, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Kompetenzniveau",
        range=[0, 10],
        dtick=1,
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray'
    ),
    legend_title=dict(text="Legende", font=dict(color=colors['text'])),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    template="plotly_white",
    hovermode="x unified"
)

fig_kompetenzniveau.show()

# -----------------------------------------
# Bildungswirkgefüge | Bildungswirkfaktor und Bildungswirkindikator
# -----------------------------------------

# Visualisierung des Bildungswirkgefüges
fig_bildungswirkgefuege = go.Figure()

# Plot für Bildungswirkfaktoren (ν)
fig_bildungswirkgefuege.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=bildungswirkfaktoren_smooth,
    mode='lines+markers',
    name='ν (Bildungswirkfaktor)',
    line=dict(color=colors['primaryLine']),
    marker=dict(color=colors['primaryLine'], size=5)
))

# Plot für Bildungswirkindikator (ι)
fig_bildungswirkgefuege.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=steigungen_bildungswirkfaktor_smooth,
    mode='lines',
    name='ι (Bildungswirkindikator)',
    line=dict(color=colors['secondaryLine']),
    marker=dict(color=colors['secondaryLine'], size=5)
))

# Wendepunkte für den Bildungswirkindikator plotten
for point in wendepunkte_bildungswirkindikator:
    if zweite_ableitung_bildungswirkindikator[point] > 0:
        color = colors['positiveHighlight']
        text = "Stabilisierungspunkt | Positiver Wendepunkt erreicht: Interventionen wirken, Interventionen stabilisieren (Strategie effektiv)"
        name = 'Stabilisation'
    else:
        color = colors['negativeHighlight']
        text = "Präventionspunkt | Negativer Wendepunkt erreicht: Präventive Interventionen notwendig, Risiko erkannt (Ursachenforschung notwendig)."
        name = 'Prävention'

    fig_bildungswirkgefuege.add_trace(go.Scatter(
        x=[simulations_ergebnisse_pe.index[point]],
        y=[steigungen_bildungswirkfaktor_smooth[point]],
        mode='markers',
        marker=dict(color=color, size=25),
        name=name,
        text=[text],
        hoverinfo='text'
    ))

# Minima und Maxima mit Empfehlungen
point_annotations = [
    (minima_bildungswirkfaktor, 'negativeHighlight', 'Intervention', "Interventionspunkt | Minimum erreicht: Interventionsbedarf zur Verhinderung eines erneuten Anstiegs."),
    (maxima_bildungswirkfaktor, 'positiveHighlight', 'Regeneration', "Regenerationspunkt | Maximum erreicht: Interventionen erfolgreich, Monitoring weiterhin erforderlich.")
]

for points, color, name, text in point_annotations:
    for point in points:
        fig_bildungswirkgefuege.add_trace(go.Scatter(
            x=[simulations_ergebnisse_pe.index[point]],
            y=[bildungswirkfaktoren_smooth[point]],
            mode='markers',
            marker=dict(color=colors[color], size=25),
            name=name,
            text=[text],
            hoverinfo='text'
        ))

# Layout des Bildungswirkgefüge-Diagramms aktualisieren basierend auf fig_mc
fig_bildungswirkgefuege.update_layout(
    title="Bildungswirkgefüge: Bildungswirkfaktor (ν) und Bildungswirkindikator (ι)",
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        range=[0, simulations_ergebnisse_pe.index.max()],  # Anpassung des Bereichs
        rangeslider=dict(visible=True, range=[0, simulations_ergebnisse_pe.index.max()]),
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1Q", step="month", stepmode="backward"),
                dict(count=4, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Wert",
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,  # Skalierung der y-Achse
        range=[min(bildungswirkfaktoren_smooth) - 1, max(bildungswirkfaktoren_smooth) + 1]  # Setzen eines klaren Bereichs für die y-Achse
    ),
    legend_title=dict(text="Legende", font=dict(color=colors['text'])),
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    template="plotly_white",
    hovermode="x unified"
)

# Diagramm anzeigen
fig_bildungswirkgefuege.show()

# -----------------------------------------
# Bildungsgefüge | Bildungswirkdynamik 
# -----------------------------------------

fig_bildungswirkdynamik = go.Figure()

# Plot für kumulative Bildungswirkung
fig_bildungswirkdynamik.add_trace(
    go.Scatter(
        x=simulations_ergebnisse_pe.index,
        y=bildungswirkfaktoren_smooth,
        fill='tozeroy',
        name='ν dx',
        line=dict(color=colors['depthArea']),
        fillcolor=colors['brightArea']
    )
)

# Wendepunkte plotten
for wendepunkt in wendepunkte_bildungswirkfaktor:
    if zweite_ableitung_bildungswirkfaktor[wendepunkt] > 0:
        wendepunkt_text = 'Stabilisierungspunkt | Positiver Wendepunkt erreicht: Interventionen wirken, Maßnahmen stabilisieren'
        marker_color = colors['primaryLine']
        name = 'Stabilisation'
    else:
        wendepunkt_text = 'Präventionspunkt | Negativer Wendepunkt erreicht: Präventive Maßnahmen notwendig, Risiko erkannt.'
        marker_color = colors['secondaryLine']
        name = 'Prävention'
        
    fig_bildungswirkdynamik.add_trace(go.Scatter(
        x=[simulations_ergebnisse_pe.index[wendepunkt]],  # Verwenden Sie den Index direkt
        y=[bildungswirkfaktoren_smooth[wendepunkt]],
        mode='markers',
        name=name,
        marker=dict(color=marker_color, size=25),
        text=[wendepunkt_text],
        hoverinfo='text'
    ))

# Minima plotten
minimum_text = 'Interventionspunkt | Minimum erreicht: Interventionsbedarf zur Verhinderung eines erneuten Anstiegs.'
fig_bildungswirkdynamik.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index[minima_bildungswirkfaktor],
    y=bildungswirkfaktoren_smooth[minima_bildungswirkfaktor],
    mode='markers',
    name='Intervention',
    marker=dict(color=colors['negativeHighlight'], size=25),
    text=[minimum_text for _ in minima_bildungswirkfaktor],
    hoverinfo='text'
))

# Maxima plotten
maximum_text = 'Regenerationspunkt | Maximum erreicht: Interventionen erfolgreich, Monitoring weiterhin erforderlich.'
fig_bildungswirkdynamik.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index[maxima_bildungswirkfaktor],
    y=bildungswirkfaktoren_smooth[maxima_bildungswirkfaktor],
    mode='markers',
    name='Regeneration',
    marker=dict(color=colors['positiveHighlight'], size=25),
    text=[maximum_text for _ in maxima_bildungswirkfaktor],
    hoverinfo='text'
))

# Diagramm-Layout
fig_bildungswirkdynamik.update_layout(
    title=f"Bildungswirkgefüge | Kumulative Bildungsdynamik (ν dx): {integral_bildungswirkfaktor:.2f}",
    xaxis_title="Zeit [Quartal]",
    yaxis_title="Kumulative Bildungswirkung (ν dx)",
    legend_title="Legende",
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text']),
    xaxis=dict(
        title="Zeit [Quartal]",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        range=[0, 12],
        linecolor=colors['text'],
        tickcolor=colors['text'],
        rangeslider=dict(visible=True, range=[0, 12]),
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1Q", step="month", stepmode="backward"),
                dict(count=4, label="1J", step="month", stepmode="backward"),
                dict(step="all", label="Alle")
            ])
        )
    ),
    yaxis=dict(
        title="Kumulative Bildungswirkung (ν dx)",
        title_font=dict(color=colors['text']),
        tickfont=dict(color=colors['text']),
        showgrid=True,
        gridcolor='lightgray',
        dtick=1,
        linecolor=colors['text'],
        tickcolor=colors['text'],
        tickmode='auto'
    ),
    hovermode="x unified",
    template="plotly_white"
)

# Diagramm anzeigen
fig_bildungswirkdynamik.show()


# -----------------------------------------
# Sankey-Diagramm (Flussdiagramm)
# -----------------------------------------

# Labels für das Sankey-Diagramm
labels = [
    "Initiale Neugier", "Startkompetenz", "Persönliche Ereignisse",
    "Veränderungen Neugier", "Veränderungen Motivation", "Bereitschaft",
    "Kompetenzentwicklung", "Kompetenzmessunsicherheit", "Kompetenzentwicklungsunsicherheit", 
    "Bildungswirkfaktor", "Bildungswirkindikator"
]

# Quell- und Zielknoten
sources = [
    0, 0, 0,  # Initiale Neugier geht zu Veränderungen Neugier, Veränderungen Motivation und Bereitschaft
    1, 1, 1,  # Startkompetenz geht direkt zu Bereitschaft
    2, 2, 2,  # Persönliche Ereignisse gehen zu Veränderungen Neugier, Veränderungen Motivation und Bereitschaft
    3, 4,     # Veränderungen Neugier und Veränderungen Motivation gehen zur Kompetenzentwicklung
    5,        # Bereitschaft geht zur Kompetenzentwicklung
    6, 6,     # Kompetenzentwicklung geht zu Unsicherheit Kompetenzmessung und Unsicherheit Kompetenzentwicklung
    7, 8,     # Unsicherheit Kompetenzmessung und Unsicherheit Kompetenzentwicklung gehen zum Bildungswirkfaktor
    9         # Bildungswirkfaktor geht zum Bildungswirkindikator
]

targets = [
    3, 4, 5,  # Von Initiale Neugier
    5, 5, 5,  # Von Startkompetenz
    3, 4, 5,  # Von Persönliche Ereignisse
    6, 6,     # Von Veränderungen Neugier und Veränderungen Motivation zur Kompetenzentwicklung
    6,        # Von Bereitschaft zur Kompetenzentwicklung
    7, 8,     # Von Kompetenzentwicklung zu Unsicherheit Kompetenzmessung und Unsicherheit Kompetenzentwicklung
    9, 9,     # Von Unsicherheit Kompetenzmessung und Unsicherheit Kompetenzentwicklung zum Bildungswirkfaktor
    10        # Von Bildungswirkfaktor zum Bildungswirkindikator
]

# Berechnung der Werte für die Flüsse
initial_neugier_value = initial_neugier
start_kompetenz_value = start_kompetenz
pe_wirkungen_sum = sum(pe_wirkungen)
veranderungen_neugier_sum = flatten_and_sum(veranderungen_neugier)
veranderungen_motivation_sum = flatten_and_sum(veranderungen_motivation)
bereitschaft_sum = sum(bereitschaft)
kompetenzentwicklung_sum = sum(kompetenzentwicklung)
delta_k_mean = np.mean(delta_k)
delta_e_mean = np.mean(delta_e)
bildungswirkfaktoren_mean = np.mean(bildungswirkfaktoren)
bildungswirkindikator_mean = np.mean(bildungswirkindikator)

# Berechnung der Flüsse und Runden auf drei Dezimalstellen
delta_k_mean = round(np.mean(delta_k), 2)
delta_e_mean = round(np.mean(delta_e), 2)
values = [
    round(initial_neugier, 2), round(initial_neugier, 2), round(initial_neugier, 2),  # Werte von Initiale Neugier
    round(start_kompetenz, 2), round(start_kompetenz, 2), round(start_kompetenz, 2),  # Werte von Startkompetenz
    round(sum(pe_wirkungen), 2), round(sum(pe_wirkungen), 2), round(sum(pe_wirkungen), 2),  # Werte von Persönliche Ereignisse
    round(flatten_and_sum(veranderungen_neugier), 2), round(flatten_and_sum(veranderungen_motivation), 2),  # Werte von Veränderungen
    round(sum(bereitschaft), 2),  # Wert von Bereitschaft
    round(sum(kompetenzentwicklung), 2), round(sum(kompetenzentwicklung), 2),  # Wert von Kompetenzentwicklung
    delta_k_mean, delta_e_mean,  # Werte von Unsicherheit Kompetenzentwicklung und Unsicherheit Kompetenzmessung
    round(np.mean(bildungswirkfaktoren), 3), # Wert von Bildungswirkfaktor
    round(np.mean(bildungswirkindikator), 3)  # Wert von Bildungswirkindikator
]

# Zuweisung der Farben zu den Knoten
node_colors = [
    colors["positiveHighlight"], colors["background"], colors["accent"],
    colors["positiveHighlight"], colors["negativeHighlight"], colors["accent"],
    colors["background"], colors["depthArea"], colors["brightArea"],
    colors["primaryLine"], colors["secondaryLine"]
]

# Schattierungen der Farbe "text" für die Links
link_colors = [
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.8)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.6)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.4)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.8)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.6)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.4)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.8)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.6)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.4)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.6)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.4)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.6)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.4)',
    f'rgba({int(colors["text"][1:3], 16)}, {int(colors["text"][3:5], 16)}, {int(colors["text"][5:7], 16)}, 0.5)'
]

# Erstellen des Sankey-Diagramms
fig_flussdiagramm = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors,
        hoverinfo='all',
        hovertemplate=(
            '<b>%{source.label}</b> to <b>%{target.label}</b><br />' +
            'Value: %{value:.3f}<br />'  # Formatiert den Wert auf drei Nachkommastellen
        )
    )
)])

fig_flussdiagramm.update_layout(
    title_text="Bildungswirkgefüge | Sankey-Diagramm: Einflüsse und Strömungen",
    font_size=10,
    plot_bgcolor=colors["white"],
    paper_bgcolor=colors["white"],
    font=dict(color=colors["text"])
)

fig_flussdiagramm.show()


# =========================================
# Geodäre erstellen und Positionierung der Knoten anpassen
# =========================================

# Berechnete Unsicherheitswerte für die x- und y-Positionen der Hauptknoten
np.random.seed(42)  # Für Reproduzierbarkeit
kognition_unsicherheit = np.random.uniform(0, 10, len(relative_schedule))  # Kognitionsunsicherheit als x-Koordinate
emotion_unsicherheit = np.random.uniform(0, 10, len(relative_schedule))    # Emotionale Unsicherheit als y-Koordinate

# Berechnung der Gesamtdauer in Tagen
total_days = sum([duration for _, duration in relative_schedule])  # Gesamtdauer in Tagen
days_per_quarter = total_days / 12  # Dauer eines Quartals in Tagen

# Netzwerkgraf-Objekt erstellen
G = nx.Graph()
sections = ["Einführung", "Ressourcen", "Aufgaben", "Ergebnissicherung", "Weiterführende Quellen", "Lounge", "Feedback", "Kursorganisation"]

# Definiere die Knoten für die Handlungssituationen (Hauptknoten)
for i, (course_name, duration) in enumerate(relative_schedule):
    task_count = task_counts[i] if i < len(task_counts) else 10  # Standardwert für Aufgaben, falls nicht definiert
    G.add_node(course_name, title=f"Handlungssituation {course_name.split('-')[-1]}",
               color=colors['primaryLine'],
               info=f"Informationen zu {course_name}\nDauer: {duration} Tage")

    # Definiere die Unterknoten für jeden Abschnitt innerhalb der Handlungssituationen
    for section in sections:
        section_name = f"{course_name} - {section}"
        G.add_node(section_name, title=section, color=colors['secondaryLine'], info=f"Details zu {section} in {course_name}")
        G.add_edge(course_name, section_name, title=f"{course_name} to {section}")

# Positionierung der Hauptknoten basierend auf den Unsicherheitswerten
fixed_radius = 0.5  # Radius für die sphärische Anordnung der Unterknoten
pos = {}  # Leeres Dictionary zur Speicherung der Knotenpositionen
current_z = 0  # Initialisierung der z-Position (Zeitachse)

# Setzen der Positionen für die Haupt- und Unterknoten
for i, (course_name, duration) in enumerate(relative_schedule):
    x = kognition_unsicherheit[i]  # Kognitionsunsicherheit als x-Koordinate
    y = emotion_unsicherheit[i]    # Emotionale Unsicherheit als y-Koordinate
    z = current_z / days_per_quarter  # Beibehaltung der z-Koordinate (Zeit in Quartalen)

    # Hauptknotenposition festlegen
    pos[course_name] = (x, y, z)
    current_z += duration  # Z-Position für die nächsten Knoten erhöhen

    # Berechnung der Positionen der Unterknoten auf einer Kugel um den Hauptknoten
    indices = np.arange(0, len(sections), dtype=float) + 0.5
    phi = np.arccos(1 - 2 * indices / len(sections))
    theta = np.pi * (1 + 5**0.5) * indices

    # Kugelförmige Anordnung der Unterknoten
    x_sphere = x + fixed_radius * np.sin(phi) * np.cos(theta)
    y_sphere = y + fixed_radius * np.sin(phi) * np.sin(theta)
    z_sphere = z + fixed_radius * np.cos(phi)

    # Setzen der Positionen der Unterknoten
    for j, section in enumerate(sections):
        section_name = f"{course_name} - {section}"
        pos[section_name] = (x_sphere[j], y_sphere[j], z_sphere[j])

# Berechnung der Knotengrößen für Haupt- und Unterknoten
node_size = []
for node in G.nodes():
    if "Aufgaben" in node:
        course_name = node.split(" - ")[0]
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == course_name), -1)
        size = 10 + 0.5 * task_counts[course_index] if course_index >= 0 else 6
    elif node in [name for name, _ in relative_schedule]:
        # Größe der Hauptknoten basierend auf dem Kugelradius zur Dauer
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == node), -1)
        size = 20 + 0.3 * relative_schedule[course_index][1] if course_index >= 0 else 20  # Durchmesser angepasst
    else:
        size = 6
    node_size.append(size)

# Hovertexte für die Knoten aktualisieren
node_hovertext = []
for node in G.nodes():
    if "Aufgaben" in node:
        course_name = node.split(" - ")[0]
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == course_name), -1)
        hover_info = f"{G.nodes[node]['title']}<br>Anzahl der Aufgaben: {task_counts[course_index]}"
    elif "-" not in node:
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == node), -1)
        duration = relative_schedule[course_index][1] if course_index >= 0 else 'N/A'
        hover_info = f"{G.nodes[node]['title']}<br>Dauer: {duration} Tage"
    else:
        hover_info = f"{G.nodes[node]['title']}<br>{G.nodes[node]['info']}"
    node_hovertext.append(hover_info)

# Knoten-Visualisierung
node_trace = go.Scatter3d(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    z=[pos[node][2] for node in G.nodes()],
    mode='markers+text',
    marker=dict(size=node_size, color=[G.nodes[node]['color'] for node in G.nodes()]),
    text=[G.nodes[node]['title'] for node in G.nodes()],
    hoverinfo='text',
    hovertext=node_hovertext,
    name='Knoten'
)

# Erstellung der Kanten auf Basis der neuen Knotenpositionen
edge_x, edge_y, edge_z = [], [], []
for edge in G.edges():
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

# Kanten-Visualisierung
edge_trace = go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    mode='lines',
    line=dict(color=colors['negativeHighlight'], width=3),
    name='Verbindungen'
)

# Aktualisierung der Lernpfad-Visualisierung mit den neuen Positionen
learning_path_nodes = [pos[course_name] for course_name, _ in relative_schedule if course_name in G.nodes()]
x_path, y_path, z_path = zip(*learning_path_nodes)
t = np.linspace(0, 1, len(x_path))
t_fine = np.linspace(0, 1, 200)

# Glättung der Pfadkoordinaten mit den neuen Werten
x_spline = interp1d(t, x_path, kind='cubic')(t_fine)
y_spline = interp1d(t, y_path, kind='cubic')(t_fine)
z_spline = interp1d(t, z_path, kind='cubic')(t_fine)

# Lernpfad mit angepassten Koordinaten visualisieren
learning_path_trace = go.Scatter3d(
    x=x_spline, y=y_spline, z=z_spline,
    mode='lines',
    line=dict(color=colors['brightArea'], width=5),
    name='Lernpfad'
)

# Erstellung und Anzeige der angepassten Visualisierung
fig = go.Figure(data=[edge_trace, node_trace, learning_path_trace])
fig.update_layout(
    title='Angepasster Lernpfad mit dynamisch skalierten Aufgabenknoten und sphärischer Unterknotenverteilung',
    scene=dict(
        xaxis=dict(showbackground=True, backgroundcolor=colors['background'], title='Kognition', range=[0, 10]),
        yaxis=dict(showbackground=True, backgroundcolor=colors['background'], title='Emotion', range=[0, 10]),
        zaxis=dict(showbackground=True, backgroundcolor=colors['background'], title='Zeit (Quartale)', range=[0, 12]),
        bgcolor=colors['background']
    ),
    paper_bgcolor=colors['background'],
    font=dict(color=colors['white']),
    showlegend=True
)

# Visualisierung anzeigen
fig.show()



# -----------------------------------------
# Dashboard mit Subplotts
# -----------------------------------------


fig_dashboard = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        f"Monte Carlo Simulation ({simulations_durchlaeufe} Durchläufe)", 
        "Unschärferelation",
        f"Kumulative Kompetenz: {flaeche_unter_mittelwert:.2f}", 
        "Bildungswirkfaktor und Bildungswirkindikator",
        "Histogramm, Dichte und KDE",
        "Sankey-Diagramm"
    ),
    specs=[
        [{"type": "scatter"}, {"type": "domain"}],  # Für Monte Carlo Simulation und Unschärferelation
        [{"type": "scatter"}, {"type": "scatter"}],  # Für kumulative Kompetenz und Bildungswirkgefüge
        [{"type": "scatter"}, {"type": "domain"}]    # Für Histogramm/KDE und Sankey-Diagramm
    ],
    vertical_spacing=0.1,
    horizontal_spacing=0.1
)

# Visualisierungen dem Dashboard hinzufügen
for i, fig in enumerate([fig_mc, fig3, fig_kumulative_kompetenz, fig_bildungswirkgefuege, fig_histogram, fig_flussdiagramm], start=1):
    for trace in fig.data:
        fig_dashboard.add_trace(trace, row=(i-1)//2 + 1, col=(i-1)%2 + 1)

# Layout-Anpassungen
fig_dashboard.update_layout(
    title=f"Dashboard: Bildungswirkgefüge vom {formatted_time}",
    autosize=True,
    height=None,  # Gesamthöhe des Dashboards dynamisch anpassen
    width=None,  # Gesamtbreite des Dashboards dynamisch anpassen
    showlegend=True,
    plot_bgcolor=colors['white'],
    paper_bgcolor=colors['white'],
    font=dict(color=colors['text']),
    legend_title_font=dict(color=colors['text']),
    xaxis=dict(
        linecolor=colors['text'],
        tickcolor=colors['text']
    ),
    yaxis=dict(
        linecolor=colors['text'],
        tickcolor=colors['text']
    )
)

# Zeigen des Dashboards
fig_dashboard.show()
```

