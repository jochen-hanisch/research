# Einfluss des biopsychosozialen Modells auf die Simulation *Bildungswirkgefüge*

## Einleitung

Das biopsychosoziale Modell (Engel, 1977) beschreibt die Wechselwirkungen zwischen biologischen, psychologischen und sozialen Faktoren als Grundlage menschlichen Erlebens, Verhaltens und Lernens. In der Simulation *Bildungswirkgefüge* wurde dieses Modell als systemisch-dynamische Komponente integriert, um den Einfluss dieser drei Dimensionen auf Kompetenzentwicklung, Motivation und Neugier abzubilden.

## Integration in die Simulation

Jeder Archetyp in der Simulation besitzt nun ein eigenes **biopsychosoziales Profil (BPS)** mit den Dimensionen:

- **Bio:** physiologische und energetische Basis, Belastbarkeit, Stressregulation  
- **Psy:** emotionale Stabilität, Selbstwirksamkeit, kognitive Flexibilität  
- **Soz:** soziale Eingebundenheit, Beziehungsqualität, Unterstützungssysteme  

Diese drei Parameter werden als Startstatus in der Simulation definiert und wirken dynamisch auf die Lernprozesse ein. Der Archetyp repräsentiert damit nicht nur eine kognitive Struktur, sondern einen **biologisch-psychologisch-sozial verankerten Lernakteur**.

## Dynamische Wirkung in der Simulation

Das biopsychosoziale Modell beeinflusst mehrere zentrale Variablen:

1. **Motivation:**  
   Der BPS-Status moduliert die Veränderung der Motivation über Zeit.  
   - Ein hoher biologischer Wert erhöht die energetische Stabilität und Lernbereitschaft.  
   - Ein hoher psychologischer Wert stabilisiert Motivation auch bei negativen Ereignissen.  
   - Ein hoher sozialer Wert kompensiert Motivationsverluste durch soziale Rückkopplung.

2. **Neugier:**  
   Die Neugier wird durch den psychologischen und sozialen Status verstärkt.  
   - Psychologische Stabilität erhöht exploratives Verhalten.  
   - Soziale Sicherheit ermöglicht risikofreies Lernen und Fehlerakzeptanz.

3. **Verarbeitung persönlicher Ereignisse (PE):**  
   BPS-Parameter modulieren die Wirkung externer Ereignisse:
   - Ein niedriger biologischer oder psychologischer Status verstärkt negative PE-Effekte.  
   - Ein hoher sozialer Status dämpft negative Auswirkungen, da soziale Unterstützung als Puffer wirkt.  

4. **Systemische Selbstregulation:**  
   Über die Methode `update_bps()` wird jeder Lernende fortlaufend biopsychosozial angepasst.  
   - Positive PE-Einflüsse verbessern Bio-, Psy- und Soz-Werte leicht.  
   - Negative Ereignisse oder hohe Schwankungen in Motivation und Kompetenz führen zu Stress, der biologische und psychologische Werte senkt.  
   - Dadurch entsteht ein kybernetischer Regelkreis zwischen Ereignis, Motivation und biopsychosozialem Zustand.

## Mathematisch-funktionale Einbindung

Formal werden die BPS-Faktoren als **Multiplikatoren** in der Lernrate eingebunden:

$$
r(t) = k \cdot C \cdot M \cdot (\text{bio}_t \cdot 0.4 + \text{psy}_t \cdot 0.4 + \text{soz}_t \cdot 0.2)
$$

Dadurch werden alle Prozesse – von Neugier bis zur Kompetenzentwicklung – durch das biopsychosoziale Profil gewichtet. Das Modell simuliert so **funktionale Zustände von Gesundheit und Belastbarkeit**, anstatt starre Typen festzulegen.

## Export und Analyse

Die Simulation protokolliert und exportiert fortlaufend die drei Statusverläufe:
- `BPS_Bio`
- `BPS_Psy`
- `BPS_Soz`

Diese Zeitreihen zeigen, wie sich biologische, psychologische und soziale Anteile über Quartale entwickeln und wie sie in Beziehung zu Kompetenz, Motivation und Neugier stehen. Die Visualisierung `fig_bps_status` ermöglicht den direkten Vergleich der drei Verläufe im zeitlichen Verlauf.

## Theoretische Implikation

Durch die Integration des biopsychosozialen Modells wird das *Bildungswirkgefüge* zu einem **emergenten, selbstregulierenden Lernsystem**, das:
- die Vulnerabilität und Resilienz von Lernenden simuliert,  
- Übergänge zwischen Belastung und Erholung sichtbar macht,  
- und den Einfluss sozialer Eingebundenheit auf kognitive Leistungsfähigkeit quantifizierbar macht.

Das Modell operationalisiert damit erstmals das biopsychosoziale Paradigma in einer dynamischen Lernsimulation und ermöglicht, Bildung als **funktionales Gleichgewicht zwischen biologischer Regulation, psychischer Kohärenz und sozialer Resonanz** zu verstehen.

## Quellen
- Engel, G. L. (1977). *The need for a new medical model: A challenge for biomedicine.* Science, 196(4286), 129–136.  
- Antonovsky, A. (1979). *Health, Stress, and Coping: New Perspectives on Mental and Physical Well-Being.* Jossey-Bass.  
- Wade, D. T., & Halligan, P. W. (2017). *The biopsychosocial model of illness: a model whose time has come.* Clinical Rehabilitation, 31(8), 995–1004.