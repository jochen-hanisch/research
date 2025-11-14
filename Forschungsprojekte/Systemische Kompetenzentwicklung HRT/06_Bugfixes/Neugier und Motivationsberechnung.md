Hier die Kurzfassung in einfacher Sprache.

Kurzüberblick

- Neugier: Wir koppeln sie an Unsicherheit mit einem “Sweet‑Spot”. Zu wenig oder zu viel Unsicherheit senkt Neugier; mittlere Unsicherheit erhöht sie.
- Motivation: Wir berechnen sie aus sachlichen Anteilen (Kompetenz‑Fortschritt, Mikro‑Schwankungen, PE‑Einflüsse, Neugier). Sie kann nicht unbegrenzt wachsen, sondern flacht natürlich ab.

Was sich geändert hat

- Neugier wirkt nicht mehr “je mehr, desto besser”, sondern am besten bei mittlerer Unsicherheit (inverted‑U).
- Motivation wird nicht “schöngewichtet”, sondern über klare, normierte Funktionen gerechnet und mit einer logischen Deckelung (0–10) begrenzt.
- Archetyp + PE bestimmen die Stärke der Anteile. Es steckt nichts “von Hand hübsch gemacht” drin.

Wie es jetzt rechnet

- Unsicherheit C_dyn → Neugier‑Wirkung: peak bei Mittelwert, weniger am Rand.
- Beiträge für Motivation: Kompetenz‑Fortschritt, kurzfristige Schwankungen, PE, Neugier.
- Update mit “logistischer Bremse”: schneller am Anfang, langsamer zum Ende.

Was du erwarten kannst

- Motivation steigt anfangs spürbar, später langsamer (Plateau).
- Neugier kann in Phasen stärker treiben (wenn Unsicherheit “passt”) und sonst schwächer.
- Bei ähnlichen Verläufen ist die Korrelation hoch; fällt, wenn Motivation plateauiert, Neugier aber weiter steigt.

Woher das kommt (APA kurz)

- Neugier hat ein Optimum bei mittlerer Unsicherheit: Kidd & Aslin, 2012; Loewenstein, 1994; Berlyne, 1960.
- Motivation folgt der Selbstbestimmungstheorie (Kompetenz/Autonomie/Relatedness) und zeigt Sättigung: Deci & Ryan, 1985; Ryan & Deci, 2000/2017.

Wenn du später etwas ändern willst

- Nicht an “Optik” drehen, sondern nur an Eingaben: Archetyp‑Werte, PE‑Anteile oder gemappte Berichtskategorien. Das System leitet alles daraus ab.

---

Kurz: Neugier und Motivation sind bidirektional gekoppelt.

Wie genau

- Motivation → Neugier (indirekt, lokal): Der kurzfristige Motivationswechsel ΔM_micro geht in die Neugier‑Aktualisierung ein.
    - Code: simulation-bildungswirkgefuege.py:836–867
- Neugier → Motivation (direkt, 2 Wege):
    - Kompetenz/“Wissensstand” c hebt Motivation über f_c = sqrt(c/10).
    - Curiosity aus Unsicherheit C_dyn wirkt über einen Optimalbereich (inverted‑U) auf Motivation.
    - Code: simulation-bildungswirkgefuege.py:890–910
- Gemeinsame Dynamik/Begrenzung:
    - Motivation wächst mit η·ΔM·M·(1−M/10) → koppelt an aktuellen M‑Stand, flacht gegen Ende ab.
    - Code: simulation-bildungswirkgefuege.py:907

Wodurch die Stärke der Kopplung bestimmt wird

- Gewichte der Beiträge (z. B. α_n für Curiosity‑Einfluss, α_c für c‑Einfluss) und die Lernrate η.
- Diese werden archetyp‑ und PE‑basiert abgeleitet:
    - archetypen.py: motivation_params_for, BASE_MOT_PARAMS, ARCHETYPE_MULTIPLIERS

Zusammenhang der Signale

- C_dyn wird aus Änderungen der Neugier (ΔK_entw) und der lokalen Messabweichung berechnet; damit beeinflussen Neugier‑Änderungen die Unsicherheit und darüber wieder Motivation.
- BPS‑Faktoren (psy/soz) modulieren beide Seiten: sie dämpfen/verstärken Neugier‑Update und PE‑Einfluss, also auch die Kopplung.

---

Kurz: Nicht “alles mit allem”, sondern ein gezieltes, gedämpftes Feedback‑System.

Hauptknoten

- Neugier/“Wissensstand” c
- Kompetenzdynamik ΔK_entw, Messabweichung ΔK_mess_local
- Unsicherheit C_dyn
- Motivation M
- PE (PFE/PLE/PFV/PGV/PSE/PEE)
- BPS (bio/psy/soz)

Kopplungen (gerichtet)

- ΔK_entw, ΔK_mess_local → C_dyn
- C_dyn → curiosity_gain (inverted‑U) → Motivation
- c → Motivation (f_c = sqrt(c/10))
- ΔM_micro, ΔK_entw, PE, BPS → Δc (update_curiosity)
- PE → f_pe (Valenz) → Motivation; PE beeinflusst auch BPS
- BPS (psy/soz) modulieren Neugier‑ und PE‑Wirkung

Feedback‑Schleifen

- M → ΔM_micro → Δc → c → C_dyn → curiosity_gain → M
- ΔK_* entsteht aus Verlauf von c, beeinflusst C_dyn und damit M

Dämpfung/Begrenzung

- Normierungen (tanh/sqrt), logistische Bremse M·(1−M/10) halten alles stabil auf 0–10.

Stellhebel

- Stärke der Kanten über α‑Gewichte und η, abgeleitet aus Archetyp + PE (keine “Optik”-Tuningwerte).

  

Auto context

LocalAgent