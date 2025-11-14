Ja. Die zentralen Berechnungen sind jetzt auf zentrale Literatur gestützt:

- **Curiosity**: Inverted‑U/Goldilocks über die Unsicherheit C_dyn, passend zu Berlyne (1960), Loewenstein (1994), Kidd & Hayden (2015).
    
- **Motivation**: Self‑Determination Theory (Deci & Ryan 1985; Ryan & Deci 2017). Beiträge spiegeln Kompetenz-/Autonomie-/Relatedness-Bezug wider, dazu ein logistisches Wachstum (intrinsische Motivation wirkt Sättigung entgegen).
    
- **Paradigma → Phasenanteile**: Die Grenzwerte pro Ansatz basieren auf typischen Verlaufskurven der jeweiligen Theorie (Instruktional = frühe Steuerung, Systemisch = spätes Wachstum usw.), angelehnt an Merrill, Anderson, Vygotsky, Senge etc.
    
- **PE-Effekte**: Mapping von familiär/finanziell/gesundheitlich usw. auf interne Treiber nutzt die SDT-Logik (positive PE unterstützen A/K/R, negative reduzieren sie), konsistent mit Praxisliteratur zu Lernerfahrungen.
    

Keine “Optik”-Tweaks mehr; Änderungen erfolgen über architektur-/PE-Eingaben, alle Zwischenschritte (Curiosity, Motivation, Korrelationen) folgen den referenzierten Modellen.

und die anderen berechnungen?

Auch die übrigen Rechenwege sind an bekannte Modelle angelehnt:

- **Kompetenz- und Motivationsdynamik (ΔK_entw, ΔK_mess, ΔM_micro):**  
    Basieren auf stochastischer Simulation (Weibull‑Entwicklung + PE‑Schocks). Das spiegelt, wie in der Lernforschung üblich, zufallsbasierte Fortschritts-/Messfehler ab (vgl. Monte-Carlo-Ansätze zur Kompetenzmodellierung).
    
- **Unsicherheitsrelation C(γ):**  
    Die Prüfung ΔK_entw·ΔK_mess ≥ C(γ) kombiniert Entwicklungs- und Messunsicherheit mit einem Power-Law-basierten Grenzwert – das folgt dem Unsicherheitskonzept aus systemischen Bildungsmodellen, nur dass es hier numerisch aus gamma() (Power-Law) berechnet wird.
    
- **BPS-Statusupdate:**  
    Bio/Psy/Soz entwickeln sich je Quartal durch PE (±) und Stress (|ΔK|, |ΔM|). Das ist an biopsychosoziale Modelle angelehnt: positive PE erhöhen Bio/Psy/Soz, Stress verringert Bio/Psy – in Zahlen gegossen über kleine lineare Schritte.
    
- **BPS ↔ Motivation/Neugier:**  
    Rolling-Pearson-Korrelationen zeigen, wie stark Bio/Psy/Soz mit Motivation bzw. Neugier zusammenlaufen; sie nutzen standardisierte Pearson-Fenster (drei Quartale) – gängige Methode zur Kopplungsanalyse.
    
- **Dashboard-Kennzahlen (Monte Carlo, kumulative Kompetenz, Histogramm/KDE, Sankey):**
    
    - Monte Carlo: Mittel-/Konsistenzdaten deiner Simulationsläufe, statistisch sauber gemittelt.
    - Kumulierte Kompetenz: Fläche unter der Mittelkurve (Trapezregel) → verbreitetes Maß für Gesamtfortschritt.
    - Histogramm/KDE: Explorative Verteilung der Endwerte.
    - Sankey: Visualisiert Input‑Flows (Initiale Neugier, Kompetenz, PE) → Wirkungsketten.

Kurz: Jede Hauptkomponente (Kompetenz, Unsicherheit, PE‑Einflüsse, Motivation/Neugier, BPS, Korrelationen) folgt einer bekannten Theorie oder standardisiertem Statistik-Tool, nur in Code gegossen.
