Um drei Referenzperformer als Highperformer, Lowperformer und Realperformer zu simulieren, können wir das existierende Simulationsmodell anpassen, um diese unterschiedlichen Leistungsniveaus abzubilden. Dabei setzen wir spezifische Werte für die Startkompetenz, die Varianz und die Wachstumsraten, um die gewünschten Profile zu erzeugen. Hier sind die Anpassungen für jeden Performer:

## **Tabelle der Parameter für drei Referenzperformer**

| Performer | Startkompetenz | Standardabweichung | Anpassung | Verfestigung | Wachstum | Plateau |
| -- | -- | -- | -- | -- | -- | -- |
| Highperformer | 1.5 | 0.05 | 0.0 | 0.3 | 0.6 | 0.8 |
| Lowperformer | 1.0 | 0.2 | -0.2 | 0.0 | 0.3 | 0.4 |
| Realperformer | 1.25 | 0.1 | -0.1 | 0.2 | 0.5 | 0.7 |



### **Erläuterung der Parameter**
- Startkompetenz: Initialwert der Kompetenz zu Beginn der Simulation. Höhere Werte bedeuten eine stärkere Ausgangsposition.
- Standardabweichung: Beeinflusst die Variabilität der Kompetenzentwicklung. Eine geringere Standardabweichung führt zu stabileren Entwicklungen.
- Anpassung / Verfestigung / Wachstum / Plateau: Diese Werte definieren die Steigerungsrate der Kompetenz in den verschiedenen Phasen der Karriereentwicklung.
Diese Anpassungen ermöglichen eine differenzierte Betrachtung der Leistungsunterschiede zwischen den Performern. Je nachdem, wie aggressiv oder konservativ die Steigerungsraten und die Standardabweichungen gesetzt werden, können die Performer effektiv simuliert werden.


## **Tabelle der Parameter für drei zusätzliche Akteure**

| Performer | Startkompetenz | Standardabweichung | Anpassung | Verfestigung | Wachstum | Plateau |
| -- | -- | -- | -- | -- | -- | -- |
| Glückspilz | 1.25 | 0.1 | 0.0 | 0.3 | 0.7 | 0.9 |
| Pechvogel | 1.25 | 0.15 | -0.2 | 0.0 | 0.2 | 0.3 |
| Durchschnitt | 1.25 | 0.1 | -0.05 | 0.2 | 0.5 | 0.6 |



### **Erläuterung der Parameter**
- Startkompetenz: Alle beginnen mit demselben Kompetenzwert, was eine gleichmäßige Basis für den Vergleich bietet.
- Standardabweichung: Der Glückspilz hat eine moderate Variabilität mit gelegentlichen positiven Ausschlägen, der Pechvogel eine etwas höhere Variabilität mit der Tendenz zu negativen Ergebnissen. Der Durchschnittsakteur hat eine stabile Entwicklung.
- Anpassung / Verfestigung / Wachstum / Plateau: Diese Werte sind bei Glückspilz und Durchschnitt höher, was eine erfolgreichere Karriereentwicklung suggeriert. Der Pechvogel erlebt dagegen eine schlechtere Entwicklungsphase.