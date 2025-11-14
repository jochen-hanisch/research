**Wesentliche Änderungen & Wirkung**

- simulation-bildungswirkgefuege.py (lines 1759-1865): Unsicherheits‑Plots in render_competence_and_uncertainty() gekapselt; Funktion liefert nun fig3 (Gauge) plus Balkendiagramme zurück, damit das Dashboard saubere Referenzen hat und die Reihenfolge der Visualisierungen CI-konform bleibt.
    
- simulation-bildungswirkgefuege.py (lines 1863-1940): render_neugier_und_motivation() sowie render_bps_status() erzeugen ihre Figuren als globale Hand‑ups; BPS‑Statusfunktion erkennt leere Daten und gibt None zurück → Dashboard kann robust entscheiden, was eingeblendet wird.
    
- simulation-bildungswirkgefuege.py (lines 1968-2183): Neue Hilfsfunktionen für BPS‑Phaseportrait und Kopplungen (render_bps_phaseportrait, render_correlation_and_dynamics) statt Inline‑Code. Zusätzlich wird künftig sowohl die normierte als auch die Rohdifferenz Neugier–Motivation geplottet, plus Rolling Pearson und BPS‑Korrelationen – bessere Nachvollziehbarkeit der Kopplung.
    
- simulation-bildungswirkgefuege.py (lines 301-318): Strukturierte Startausgabe (inkl. BPS-Profil) erfolgt erst, nachdem Archetypdaten geladen sind, damit alle Werte in einem konsistenten Block erscheinen.
    
- archetypen.py (lines 1-219) + simulation-bildungswirkgefuege.py:167, 299–306: Neues Mapping map_report_pe_to_internal erlaubt Berichtskategorien (familiär, finanziell, usw.) direkt zu internen PE-Treibern zu machen. Die Simulation nutzt wahlweise PE_report aus dem Archetyp und rechnet alles literaturkonform auf PFE/PLE/PFV/PGV/PSE/PEE um – keine Hardcodings mehr.
    
- simulation-bildungswirkgefuege.py (lines 374-404): Paradigma-spezifische Phasenanteile (instruktional … systemisch). Dadurch steuert der Ansatz, wann Adaptions-, Verfestigungs- und Wachstumsphasen anstehen – näher an den realen Lehr-Lern-Theorien als die alten Fixwerte.
    

**Wirkungen**

- Visualisierungen laufen in definierter Reihenfolge; jede Figur hat einen klaren Render-Hook – zuverlässige Dashboard-Erstellung und CI-Konformität.
- Kopplungsplots zeigen jetzt beide Differenzen (roh + normiert) → Interpretation der Kurven fällt leichter.
- PE-Inputs lassen sich direkt aus den sechs Berichtskategorien übernehmen; keine manuellen Umcodierungen.
- Phasenlogik folgt der Theorie des gewählten Paradigmas, was den zeitlichen Verlauf von Motivation/Neugier realistischer macht.
