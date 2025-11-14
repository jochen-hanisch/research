Genau — in der Didaktik‐/Lernforschung ist das Paradigma (Instruktional, Kognitivistisch, Behavioristisch usw.) eng mit typischen gekoppelt. Beispielsweise starten behavioristische Settings mit schneller “Anpassung” (klar strukturierte Reize), kognitivistische entwickeln längere “Verfestigung”, systemische verschieben “Wachstum” nach hinten (Reflexions‑/Transferphasen) usw. Das deckt sich mit Literatur wie Merrill, Anderson, Kolodner oder den klassischen Phasenmodellen in den jeweiligen Theorien.

Für den Code empfiehlt sich darum ein Ansatz‑basiertes Mapping der Grenzanteile – also nicht bloß fixe 0.25/0.50/0.75, sondern z. B.:

|Ansatz (ansatz_wahl)|Empfohlene Phasenanteile (Anpassung, Verfestigung, Wachstum)|Literaturhinweis|
|---|---|---|
|Instruktional|0.20 / 0.45 / 0.70|Merrill (2002) “First Principles” – klare Anfangsführung|
|Kognitivistisch|0.25 / 0.55 / 0.80|Anderson (ACT*), Ausubel: längere Verfestigung|
|Behavioristisch|0.15 / 0.40 / 0.65|Skinner, Gagné: frühe Automatisierung|
|Humanistisch|0.30 / 0.55 / 0.85|Rogers/Knowles: Phase der Selbstreflexion und späteres Wachstum|
|Konstruktivistisch|0.25 / 0.50 / 0.80|Jonassen: Exploration + iteratives Verfestigen|
|Soziokulturell|0.30 / 0.60 / 0.85|Vygotsky/Lave: lange gemeinschaftliche Konsolidierung|
|Systemisch|0.35 / 0.65 / 0.90|Argyris/Senge: späte Manifestation, viel Verknüpfung|

Technisch: Lege ein Dictionary PHASEN_AUFTEILUNG an, lese es über ansatz_wahl aus, fallback auf Standard. So bleiben die Phasen literaturtreu und du kannst sie bei Bedarf weiter feinjustieren (z. B. Archetyp-Modifikationen).