### Kurzanleitung zur Anpassung von Parametern

#### 1. **Startwert der Kompetenz**
   - **Parameter:** `start_kompetenz`
   - **Beschreibung:** Definiert den Anfangswert der Kompetenz zu Beginn der Simulation.
   - **Anpassung:** Ändere den Wert, um mit einer höheren oder niedrigeren Anfangskompetenz zu starten.
   - **Beispiel:**
     ```python
     start_kompetenz = 1.5  # Erhöht den Startwert der Kompetenz
     ```

#### 2. **Anzahl der Quartale**
   - **Parameter:** `quartale`
   - **Beschreibung:** Gibt die Dauer der Simulation in Quartalen an.
   - **Anpassung:** Ändere die Zahl, um die Simulationsdauer zu verlängern oder zu verkürzen.
   - **Beispiel:**
     ```python
     quartale = 16  # Verlängert die Simulation auf 4 Jahre
     ```

#### 3. **Standardabweichung der Bereitschaft**
   - **Parameter:** `bereitschafts_std`
   - **Beschreibung:** Steuert die Volatilität der Kompetenzsteigerung innerhalb jedes Quartals.
   - **Anpassung:** Erhöhe oder verringere den Wert, um größere oder kleinere Schwankungen zu simulieren.
   - **Beispiel:**
     ```python
     bereitschafts_std = 0.2  # Erhöht die Variabilität der Kompetenzsteigerungen
     ```

#### 4. **Phasen der Bereitschaftssteigerung**
   - **Parameter:** `bereitschafts_steigerung_phase`
   - **Beschreibung:** Definiert die Änderungsrate der Kompetenz für verschiedene Phasen der Simulation.
   - **Anpassung:** Modifiziere die Werte für jede Phase, um unterschiedliche Wachstumsdynamiken zu simulieren.
   - **Beispiel:**
     ```python
     bereitschafts_steigerung_phase = {
         'Anpassung': -0.05,
         'Verfestigung': 0.15,
         'Wachstum': 0.45,
         'Plateau': 0.65
     }  # Ändert die Steigerungsraten in allen Phasen
     ```

#### 5. **Funktionen zur Steigerung und Motivation**
   - **Parameter:** Funktionen `anpassung_der_bereitschaft` und `motivation`
   - **Beschreibung:** Diese Funktionen definieren, wie sich die Kompetenz über die Zeit ändert.
   - **Anpassung:** Passe die Bedingungen oder Rückgabewerte an, um die Simulation an spezifische Szenarien anzupassen.
   - **Beispiel:**
     ```python
     def motivation(aktuelles_quartal):
         if aktuelles_quartal == 7:
             return -0.3  # Ändert den Zeitpunkt des Motivationsknicks
         elif aktuelles_quartal == 11:
             return 0.5  # Ändert den Zeitpunkt und die Intensität der Motivationssteigerung
         else:
             return 0
     ```

#### 6. **Visualisierung anpassen**
   - **Beschreibung:** Änderungen in der Art, wie Ergebnisse dargestellt werden.
   - **Anpassung:** Ändere Farben, Transparenz oder andere visuelle Elemente in den `plt`-Funktionen.
   - **Beispiel:**
     ```python
     plt.plot(smoothed_results, color='green', alpha=0.1)  # Ändert die Farbe der Kurven
     ```

Diese Anleitung gibt dir einen Überblick, wie du die verschiedenen Parameter und Funktionen in deinem Simulationsskript anpassen kannst, um unterschiedliche Szenarien und Auswirkungen zu simulieren. Experimentiere mit diesen Einstellungen, um ein tieferes Verständnis für die Dynamik der Kompetenzentwicklung zu erlangen.