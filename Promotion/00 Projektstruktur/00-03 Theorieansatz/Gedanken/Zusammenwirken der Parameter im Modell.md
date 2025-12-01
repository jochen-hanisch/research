
# 1 Parameterübersicht

## 1.1 Kognitive Unsicherheit (`kognition_unsicherheit`)
- **Definition**: Schwankungen in den kognitiven Fähigkeiten.
- **Wertbereich**: 0 bis 10
- **Initialisierung**:
    ```python
    kognition_unsicherheit = np.random.uniform(0, 10, len(relative_schedule))
    ```
- **Einfluss**: Beeinflusst die Kompetenzentwicklung durch zufällige Fluktuationen in der Lernrate.

## 1.2 Emotionale Unsicherheit (`emotion_unsicherheit`)
- **Definition**: Schwankungen in der emotionalen Stabilität.
- **Wertbereich**: 0 bis 10
- **Initialisierung**:
    ```python
    emotion_unsicherheit = np.random.uniform(0, 10, len(relative_schedule))
    ```
- **Einfluss**: Beeinflusst die Motivation und führt zu Schwankungen in der Kompetenzentwicklung.

## 1.3 Startkompetenz (`start_kompetenz`)
- **Definition**: Ausgangsniveau der Kompetenz.
- **Wertbereich**: Festgelegter Startwert von 5
- **Initialisierung**:
    ```python
    start_kompetenz = 5
    ```
- **Einfluss**: Legt den Startwert der Kompetenz fest und dient als Basis für die Lernkurven.

## 1.4 Initiale Neugier (`initial_neugier`)
- **Definition**: Ausgangspunkt der Neugier.
- **Wertbereich**: 0 bis 10
- **Initialisierung**:
    ```python
    initial_neugier = 1.133
    ```
- **Einfluss**: Bestimmt den anfänglichen Lernimpuls und die Lernrate in den ersten Quartalen.

## 1.5 Persönliche Ereignisse (`pe_auswirkungen`)
- **Definition**: Positive oder negative Ereignisse, die die Kompetenzentwicklung beeinflussen.
- **Wertbereich**: Variabel je nach Typ
- **Initialisierung**:
    ```python
    pe_auswirkungen = {
        'PFE': 0.1,   # Persönlicher Fehlschlag extern
        'PLE': 0.08,  # Persönlicher Leistungseinbruch
        'PFV': 0.15,  # Persönlicher Fortschritt variabel
        'PGV': 0.1,   # Persönliches Großereignis variabel
        'PSE': 0.2,   # Persönlicher Stabilitätserfolg
        'PEE': 0.05   # Persönlicher Erfolg extern
    }
    ```
- **Einfluss**: Beeinflusst die Lernkurve durch sprunghafte Änderungen; positive Ereignisse fördern, negative Ereignisse hemmen die Kompetenzentwicklung.

## 1.6 Bereitschaftssteigerung (`bereitschafts_steigerung_phase`)
- **Definition**: Wachstumsrate der Bereitschaft in verschiedenen Phasen.
- **Wertbereich**: Variiert je nach Phase
- **Initialisierung**:
    ```python
    bereitschafts_steigerung_phase = {
        'Anpassung': fluctuate_parameter(-0.05, 0.01),
        'Verfestigung': fluctuate_parameter(0.05, 0.1),
        'Wachstum': fluctuate_parameter(0.1, 0.15),
        'Plateau': fluctuate_parameter(0.05, 0.1)
    }
    ```
- **Einfluss**: Moduliert die Lernbereitschaft in den verschiedenen Phasen der Simulation.

## 1.7 Dynamische Unsicherheitsrelation ($C$)
- **Definition**: Maß für die Korrelation zwischen Veränderungen in Motivation ($\Delta E$) und Kompetenzentwicklung ($\Delta K$).
- **Formel**:
    $$ 
    C = \left| r \right| \cdot \left( \sigma_{\Delta E} \cdot \sigma_{\Delta K} \right)
    $$
    ```python
    def calculate_dynamic_C(delta_e, delta_k):
        r, _ = pearsonr(delta_e, delta_k)
        return abs(r) * (np.std(delta_e) * np.std(delta_k))
    ```
- **Einfluss**: Je höher $C$, desto stärker die Unsicherheit im System.

## 1.8 Bildungswirkfaktor ($\nu$)
- **Definition**: Maß für die Gesamtauswirkungen auf das Kompetenzniveau.
- **Formel**:
    $$
    \nu = \Delta \text{Bereitschaft} \cdot \sigma(\text{simulations_ergebnisse_pe})
    $$
    ```python
    bildungswirkfaktoren = delta_bereitschaft * simulations_ergebnisse_pe.std(axis=1)
    ```
- **Einfluss**: Bestimmt die geglätteten Veränderungen des Bildungswirkfaktors und zeigt instabile Lernbedingungen an.

## 1.9 Bildungswirkindikator ($\iota$)
- **Definition**: Beschreibt die Veränderungsgeschwindigkeit des Bildungswirkfaktors.
- **Formel**:
    $$ 
    \iota = \nabla \nu
    $$
    ```python
    bildungswirkindikator = np.gradient(bildungswirkfaktoren)
    ```
- **Einfluss**: Wendepunkte im Bildungswirkindikator markieren Schlüsselstellen in der Lernentwicklung.

## 1.10 Lernpfadvisualisierung (`relative_schedule`)
- **Definition**: 3D-Visualisierung der Lernpfade mit den Parametern $kognition\_unsicherheit$, $emotion\_unsicherheit$, und Zeit ($z$).
- **Code für die Knotenpositionierung**:
    ```python
    pos[course_name] = (kognition_unsicherheit[i], emotion_unsicherheit[i], current_z / days_per_quarter)
    ```

## 1.11 Korrelationsmatrix (`korrelations_matrix_bereitschaft`)
- **Definition**: Misst die Korrelationen der Bereitschaftssteigerungen in verschiedenen Quartalen.
- **Einfluss**: Visualisiert die Beziehungen zwischen den Bereitschaftsveränderungen und den Lernphasen.

# 2 Zusammenhang der Parameter

## 2.1 Kognitive und Emotionale Unsicherheit (`kognition_unsicherheit` und `emotion_unsicherheit`)
- **Wechselwirkung**: Diese Parameter beeinflussen zusammen sowohl die Stabilität als auch die Dynamik der Kompetenzentwicklung.
- **Einfluss**:
    - $kognition\_unsicherheit$ wirkt hauptsächlich auf die kognitive Fluktuation in der Lernkurve.
    - $emotion\_unsicherheit$ steuert die Variabilität in der Motivation, was zu unvorhersehbaren Sprüngen in der Kompetenzentwicklung führen kann.
- **Implementierungsbeispiel**:
    ```python
    def update_motivation(current_motivation):
        fluctuation = np.random.normal(0, emotion_unsicherheit.mean() * 0.1)
        new_motivation = max(0, min(10, current_motivation + fluctuation))
        return new_motivation
    ```

## 2.2 Startkompetenz und Initiale Neugier (`start_kompetenz` und `initial_neugier`)
- **Wechselwirkung**: Bestimmen den Ausgangspunkt der Lernkurve.
- **Einfluss**:
    - $start\_kompetenz$ legt den Anfangswert der Kompetenz fest.
    - $initial\_neugier$ beeinflusst die Lernkurve in den ersten Quartalen und moduliert die Lernrate.
- **Mathematische Beziehung**:
    $$ 
    \Delta \text{Motivation} = 0.1 \cdot \text{Vorwissen}
    $$
    ```python
    lernender.update_motivation(delta_motivation)
    ```

## 2.3 Persönliche Ereignisse (`pe_auswirkungen`)
- **Wechselwirkung**: Verursachen sprunghafte Veränderungen in der Kompetenzentwicklung und Motivation.
- **Einfluss**:
    - Positive Ereignisse ($PSE$, $PEE$) fördern das Lernen und erhöhen die Motivation.
    - Negative Ereignisse ($PFE$, $PLE$) führen zu Rückschlägen in der Lernkurve.
- **Implementierungsbeispiel**:
    ```python
    def persoenliches_ereignis():
        ereignis_typ = np.random.choice(['PFE', 'PLE', 'PFV', 'PGV', 'PSE', 'PEE'], p=[0.125, 0.0833, 0.2083, 0.125, 0.4167, 0.0417])
        impacts = {
            'PFE': np.random.normal(-0.2, 0.1),
            'PLE': np.random.normal(-0.3, 0.2),
            'PFV': np.random.normal(0.2, 0.1),
            'PGV': np.random.normal(-0.4, 0.2),
            'PSE': np.random.normal(0.1, 0.05),
            'PEE': np.random.normal(0.3, 0.1)
        }
        return impacts[ereignis_typ]
    ```

# 3 Abhängigkeiten und Berechnungen

## 3.1 Berechnung von Kompetenz ($competence\_level$)
- **Formel**:
    $$ 
    \text{new\_competence\_level} = \text{current\_level} + \text{improvement}
    $$
    ```python
    new_competence_level = current_level + improvement
    ```

## 3.2 Berechnung der Bereitschaftssteigerung ($bereitschafts\_steigerung\_phase$)
- **Formel**:
    $$ 
    \Delta \text{Bereitschaft} = \text{Bereitschaft\_Steigerung}
    $$
    ```python
    bereitschafts_steigerung_phase = {
        'Anpassung': np.random.uniform(-0.05, 0),
        'Verfestigung': np.random.uniform(0.05, 0.1),
        'Wachstum': np.random.uniform(0.1, 0.15),
        'Plateau': np.random.uniform(0.05, 0.1)
    }
    ```

# 4 Visualisierung der Parameterbeziehungen

- Die Hauptknoten ($course\_name$) werden durch die Kombination von $kognition\_unsicherheit$ und $emotion\_unsicherheit$ auf der $x$- und $y$-Achse dargestellt.
- Die $z$-Position der Knoten wird durch die Zeit ($\frac{current_z}{days\_per\_quarter}$) gesteuert.
- Persönliche Ereignisse verursachen Abweichungen entlang des $z$-Pfads.

# 5 Wechselwirkungen und Effekte im Simulationsmodell

## 5.1 Einfluss der Unsicherheitsparameter auf das Lernverhalten
- Die Parameter $kognition\_unsicherheit$ und $emotion\_unsicherheit$ steuern die Variabilität im Lernverhalten und damit die Dynamik der Lernkurve.
    1. **Kognitive Unsicherheit** ($kognition\_unsicherheit$): Schwankungen im Kompetenzniveau.
    2. **Emotionale Unsicherheit** ($emotion\_unsicherheit$): Verursacht instabile Motivation.
    
- **Berechnung der Knotenposition**:
    ```python
    x = kognition_unsicherheit[i]
    y = emotion_unsicherheit[i]
    z = current_z / days_per_quarter
    pos[course_name] = (x, y, z)
    ```

## 5.2 Bereitschaftssteigerung und Phasenübergänge
- Die **Bereitschaftssteigerung** bestimmt, wie stark die Lernbereitschaft in den verschiedenen Phasen der Simulation schwankt.
- Jede Phase hat eine eigene Steigerungsrate:
    $$ 
    \Delta \text{Bereitschaft} = \text{Bereitschafts\_Steigerung\_Wachstum}
    $$

## 5.3 Integration persönlicher Ereignisse in die Simulation
- Persönliche Ereignisse ($pe\_auswirkungen$) erzeugen sprunghafte Veränderungen in der Lernkurve:
    $$ 
    \text{PE} = \{ PFE: 0.1, PLE: 0.08, PFV: 0.15, PGV: 0.1, PSE: 0.2, PEE: 0.05 \}
    $$
- **Einfluss auf das Kompetenzniveau**: Sprünge im Kompetenzniveau, die sich von der normalen Entwicklungskurve abheben.

# 6 Dynamische Anpassung der Variabilität ($C$)

- Die Funktion `calculate_dynamic_C` berechnet den dynamischen Unsicherheitswert $C$, basierend auf der Korrelation zwischen den Veränderungen in der Motivation ($\Delta E$) und der Kompetenzentwicklung ($\Delta K$).
- **Formel**:
    $$ 
    C = |r| \cdot (\sigma_{\Delta E} \cdot \sigma_{\Delta K})
    $$
    ```python
    def calculate_dynamic_C(delta_e, delta_k):
        r, _ = pearsonr(delta_e, delta_k)
        return abs(r) * (np.std(delta_e) * np.std(delta_k))
    ```

# 7 Der Bildungswirkfaktor ($\nu$) und Bildungswirkindikator ($\iota$)

## 7.1 Berechnung des Bildungswirkfaktors ($\nu$)
- Der **Bildungswirkfaktor** ist ein Maß für die Gesamtauswirkung aller Einflüsse auf das Kompetenzniveau.
- **Formel**:
    $$ 
    \nu = \Delta \text{Bereitschaft} \cdot \sigma(\text{PE})
    $$
    ```python
    bildungswirkfaktoren = delta_bereitschaft * simulations_ergebnisse_pe.std(axis=1)
    ```

## 7.2 Berechnung des Bildungswirkindikators ($\iota$)
- Der **Bildungswirkindikator** ist die Ableitung des Bildungswirkfaktors und beschreibt die Veränderungsgeschwindigkeit.
- **Formel**:
    $$ 
    \iota = \nabla \nu
    $$
    ```python
    bildungswirkindikator = np.gradient(bildungswirkfaktoren)
    ```

# 8 Sankey-Diagramm: Einflussströme im Bildungswirkgefüge

- Das Sankey-Diagramm zeigt die Flüsse zwischen den einzelnen Einflussfaktoren:
    - $Initiale\_Neugier \rightarrow \Delta \text{Neugier}$
    - $Startkompetenz \rightarrow \Delta \text{Bereitschaft}$
    - $Persönliche\_Ereignisse \rightarrow \Delta \text{Motivation}$
- **Werte**:
    - Jeder Pfeil im Sankey-Diagramm repräsentiert die Stärke des Einflusses auf die Zielgröße.