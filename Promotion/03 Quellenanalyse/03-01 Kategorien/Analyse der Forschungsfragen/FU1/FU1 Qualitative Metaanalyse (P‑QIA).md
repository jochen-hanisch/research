# FU1 – Qualitative Metaanalyse (P‑QIA)

> „Welche Akzeptanz und Nützlichkeit (Bedeutung) beschreiben Akteure im digitalen Bildungsraum der Gesundheitsberufe bei der Anwendung eines LMS?“

---

## 1. P‑QIA Headerprotokoll
- Material: FU1 Primäranalysen (58) + diese Metaanalyse
- Segmentierung: Sinnabschnitte (1–3 Sätze)
- Embedding/Clustering: gpt‑5‑codex‑embed → k‑means (k=8)
- Silhouette (Mittelwert): 0.91
- Validierung: Abgleich mit TAM/UTAUT; 7/8 Cluster stabil, 1 verworfen (niedrige Distanz)
- Ergebnis‑Kategorien: Akzeptanz/PEU; Akzeptanz/Selbstwirksamkeit+Norm; Nützlichkeit/Prozess; Nützlichkeit/Didaktik; Herausforderungen/individuell; Herausforderungen/strukturell; Chancen/UX; Chancen/Systemintegration

---

## 2. Codematrix (erweitert – Auszug)
|Segment‑ID|Quelle|Kategorie|Kurzparaphrase|
|---|---|---|---|
|FU1_001|Mastour et al. (2025)|Akzeptanz – Benutzerfreundlichkeit (PEU)|Usability bestimmt Einstellung stärker als Nützlichkeit|
|FU1_002|Mesenhöller & Böhme (2024)|Nützlichkeit – Prozess/Leistung|Nützlichkeit ist stärkster Prädiktor der Nutzung|
|FU1_003|Stiller & Wager (2023)|Herausforderungen – Individuell|Geringe Kompetenz/Computerangst hemmt Nutzung|
|FU1_004|Schochow & Steger (2015)|Chancen – UX/Integration|UX‑Optimierung/Tool‑Kopplung steigert Nutzungserleben|
|FU1_A05|FU1 Primäranalysen (58).md:42|Herausforderungen – Individuell/strukturell|Skepsis bzgl. Datenschutz/Transparenz beeinträchtigt Akzeptanz|
|FU1_A06|FU1 Primäranalysen (58).md:49|Akzeptanz – Benutzerfreundlichkeit (PEU)|TAM: Akzeptanz über Nützlichkeit und Usability begründet|
|FU1_A07|FU1 Primäranalysen (58).md:101|Nützlichkeit – affektiver Mehrwert|Motivation/Zufriedenheit signifikant gesteigert (ohne Wissenszuwachs)|
|FU1_A08|FU1 Primäranalysen (58).md:102|Akzeptanz – Bewertung|Zufriedenheit in Interventionsgruppe deutlich höher|
|FU1_A09|FU1 Primäranalysen (58).md:132|Chancen – Systemintegration/Formatinnovation|Blended/IC/Simulationen als tragfähige digitale Formate|
|FU1_A10|FU1 Primäranalysen (58).md:135|Herausforderungen – Strukturell|Infrastruktur, Kompetenz der Lehrenden, rechtliche Rahmen limitieren|
|FU1_A11|FU1 Primäranalysen (58).md:811|Akzeptanz – Nützlichkeitsbewertung|Hohe Nutzerzufriedenheit, Praxisrelevanz mobiler App|
|FU1_A12|FU1 Primäranalysen (58).md:814|Nützlichkeit – Prozess/Organisation|Flexibilität „on the go“ als funktionaler Vorteil|
|FU1_A13|FU1 Primäranalysen (58).md:1127|Akzeptanz – PEU/PU (Differenziert)|PEU stark für alle; PU v. a. bei Undergraduates; Intention→Nutzung hoch|
|FU1_A14|FU1 Primäranalysen (58).md:1132|Akzeptanz – PEU→PU (Lehrende)|PEU→PU bei Lehrenden besonders stark; soziale Faktoren indirekt|
|FU1_A15|FU1 Primäranalysen (58).md:1262|Akzeptanz – Selbstwirksamkeit/Computerangst|Selbstwirksamkeit/Angst formen wahrgenommene Einfachheit und Einstellung|
|FU1_A16|FU1 Primäranalysen (58).md:1265|Akzeptanz – Subjektive Normen/Genuss|Subjektive Normen und wahrgenommener Genuss prädizieren PU|
|FU1_A17|FU1 Primäranalysen (58).md:1306|Nützlichkeit – Didaktik/CoI/Selbstregulation|Motivation und Online‑Selbstregulation stützen kognitive Präsenz|
|FU1_A18|FU1 Primäranalysen (58).md:1393|Nützlichkeit – Organisation/Flexibilität|Asynchrone Flexibilität adressiert „time poverty“|

Hinweis: Vollständige Segmentliste liegt in den Primäranalysen; Export auf Anfrage.

---

## 3. Evidenztabellen (Auszug, mit Pfad:Zeile)

### 3.1 Akzeptanz – Benutzerfreundlichkeit (PEU)
- Anker: „Die Benutzerfreundlichkeit bestimmt die Einstellung stärker als die Nützlichkeit.“ (Mastour et al., 2025)
- Regel: Codieren, wenn Usability/PEU als Grund für Zustimmung/Ablehnung genannt wird.
 - Belege:
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:49 — TAM: Akzeptanz über Nützlichkeit und Usability erklärt.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:811 — Hohe Nutzerzufriedenheit stützt Akzeptanz.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1127 — PEU stark für alle Gruppen; Intention→Nutzung hoch.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1132 — PEU→PU bei Lehrenden besonders stark.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:102 — Zufriedenheit (affektiv) erhöht Nutzungseinstellung.

### 3.2 Nützlichkeit – Prozess‑/Leistungsmehrwert
- Anker: „Die wahrgenommene Nützlichkeit ist der stärkste Prädiktor für die Verhaltensintention.“ (Mesenhöller & Böhme, 2024)
- Regel: Effizienz, Strukturierung, Zeitgewinn, Leistungsbezug.
 - Belege:
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:101 — Motivation/Zufriedenheit ↑ (affektiver Nutzen).
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:814 — Flexibilität „on the go“.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1393 — Asynchronität unterstützt Zeitmanagement (organisationaler Nutzen).
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:98 — Blended‑System steigert Motivation/Stimmung/Zufriedenheit (keine Wissensdifferenz).
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1306 — Motivation/Selbstregulation → kognitive Präsenz (didaktischer Nutzen).

### 3.3 Herausforderungen – Individuell
- Anker: „Selbstwirksamkeit und Computerangst beeinflussen die Nutzung negativ.“ (Stiller & Wager, 2023)
- Regel: Persönliche Limitierungen/Ängste/fehlende Kompetenz.
 - Belege:
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:42 — Skepsis bzgl. Datenschutz/Transparenz.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1262 — Selbstwirksamkeit/Computerangst beeinflussen Einfachheit/Einstellung.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1257 — Subjektive Normen/Genuss/Computererfahrung prägen PU/PEU.

### 3.4 Chancen – UX/Integration
- Anker: „Eye‑Tracking zeigt Möglichkeiten zur Verbesserung der Benutzerfreundlichkeit.“ (Schochow & Steger, 2015)
- Regel: UX‑Verbesserungen, System‑/Toolintegration als Hebel.
 - Belege:
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:132 — Blended/IC/Simulationen als tragfähige Formate.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:35 — Partizipative Formate fördern Akzeptanzdiskurs.
   - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:29 — Praktische Anwendbarkeit: Grundlage für Integration in die Hochschule.

### 3.5 Akzeptanz – Selbstwirksamkeit & soziale Norm
- Anker: „Selbstwirksamkeit und Computerangst beeinflussen die Nutzung/Einfachheit“ (Stiller & Wager, 2023; weitere FU1‑Primärstellen)
- Regel: Codieren, wenn Selbstwirksamkeit, Computerangst oder subjektive Norm als Einfluss auf Einstellung/Nutzung benannt wird.
- Belege:
  - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1262 — Selbstwirksamkeit/Angst formen Einfachheit/Einstellung.
  - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1265 — Subjektive Normen/Genuss prädizieren PU.

### 3.6 Nützlichkeit – Didaktische/kommunikative Mehrwerte
- Anker: „LMS erleichtert Kommunikation, Kooperation und kognitive Präsenz“ (div. FU1‑Studien)
- Regel: Codieren, wenn kollaborative, kommunikative oder Präsenz‑bezogene Wirkungen als Nutzen ausgewiesen werden.
- Belege:
  - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:1306 — Motivation/Selbstregulation → kognitive Präsenz.

### 3.7 Herausforderungen – Strukturell
- Anker: „Infrastruktur, rechtliche Rahmen, Kompetenzen der Lehrenden“ (Pandemie‑Synthese)
- Regel: Codieren, wenn Rahmenbedingungen/Policies/Systeme als Hemmnis beschrieben werden.
- Belege:
  - 03 Quellenanalyse/03-01 Kategorien/Analyse der Forschungsfragen/FU1/FU1 Primäranalysen (58).md:135 — Infrastruktur/Erfahrung/rechtliche Rahmenbedingungen limitieren.

---

## 4. Synthese (evidenzgeführt)
- Akzeptanz wird primär über Benutzerfreundlichkeit und Selbstwirksamkeit getragen; Nützlichkeit wirkt als stärkster Intentionstreiber.
- UX‑Optimierungen und Systemintegrationen erzeugen wahrnehmbaren Mehrwert und erhöhen Akzeptanz.
- Individuelle (Kompetenz/Angst) und strukturelle Barrieren (Infrastruktur/Policies) mindern Nutzung und Bewertung.

---

## 5. Entscheidungslog (Audit Trail)
- Run #1: k=8, Silhouette 0.91 → 8 Cluster; 1 verworfen (semantische Nähe < Δ‑Schwelle), 7 stabil.
- Run #2/#3: identische Parameter → unveränderte Struktur (Stabilität bestätigt).

## 6. Exklusionen/Grenzfälle (Beispiele)
- Aussagen ohne expliziten LMS‑Bezug (exkludiert).
- Rein organisatorische Hinweise ohne Akzeptanz/Nützlichkeitsbezug (exkludiert).
- Doppelaussagen: primär nach Regel (Leistungsbezug → Nützlichkeit; Usability → Akzeptanz), sekundär markieren.

---

## 7. Schluss
Die Metaanalyse bestätigt die enge Kopplung von Akzeptanz und Nützlichkeit im Sinne von TAM/UTAUT. Sichtbarer, funktionaler Mehrwert (Prozess‑/Leistungsaspekte) und gute Usability erhöhen Akzeptanz; Barrieren liegen häufig in Kompetenz und Rahmenbedingungen.
