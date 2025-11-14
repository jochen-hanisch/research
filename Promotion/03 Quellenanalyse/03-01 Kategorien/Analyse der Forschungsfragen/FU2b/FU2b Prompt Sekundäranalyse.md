
---
title: "FU2b Prompt Sekundäranalyse"
fu: FU2b
version: tbd
last_updated: tbd
status: in_überarbeitung
procedure: "Probabilistisch‑Qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring"
sources_count: 27
sources_file: "FU2b Primäranalysen (27).md"
software: tbd
tags: [mayring, fu/FU2b, typ/prompt]
links:
  prompt: "FU2b Prompt Sekundäranalyse.md"
  primary: "FU2b Primäranalysen (27).md"
  analysis: "FU2b Qualitative Metaanalyse.md"
  codebook: "FU2b Codiersystem.md"
---

# Vorarbeiten

**Aufgabe:**  
Analysiere die bereitgestellte Datei systematisch und integriere alle enthaltenen Analysen zur Beantwortung der Forschungsfrage (FU).

Forschungsunterfrage (FU2b):

„Welche Effekt-Faktoren erläutern Lehrende im digitalen Bildungsraum der Gesundheitsberufe bei der Anwendung eines Learning-Management-Systems (LMS)?“

Methodik:

Führe eine probabilistisch‑qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring durch, um Effekt‑Faktoren aus Lehrendensicht systematisch und probabilistisch gestützt zu erfassen (vgl. [[P-QIA Methode]]). Die Methodik umfasst folgende Schritte:

1. **Segmentierung und probabilistische Strukturierung (P‑QIA):**
   - Segmentiere die bereitgestellten Primäranalysen in Sinnabschnitte (1–3 Sätze).
   - Erzeuge GPT‑Embeddings für alle Segmente und führe ein k‑means‑Clustering mit FU‑spezifischem *k* durch (vgl. [[P-QIA Statistik]]).
   - Prüfe die Clusterqualität mithilfe des Silhouette‑Koeffizienten und fasse instabile Cluster ggf. zusammen.

2. **Kategorienbildung und Codierschema (Mayring + P‑QIA):**
   - Leite aus den stabilen Clustern Kategorien zu:
     - **Faktoren:** Merkmale des LMS, die von Lehrenden als wirksam beschrieben werden (z. B. Interaktivität, Adaptivität, Flexibilität).
     - **Effekten:** beobachtete Wirkungen auf Lernprozesse, soziale Interaktionen oder organisatorische Unterstützung.
     - **Interaktionen:** Wechselwirkungen zwischen LMS‑Funktionen und wahrgenommener Wirksamkeit in verschiedenen Kontexten.
   - Erstelle ein Codierschema mit:
     - klaren **Kategoriedefinitionen**,
     - **Ankerbeispielen** mit Pfadangabe (z. B. `FU2b Primäranalysen (27).md:Zeile`),
     - **Kodierregeln** zur Zuordnung von Textstellen, inkl. Regeln für Mehrfachkodierungen.

3. **Kodierung und Synthese (Mayring + P‑QIA):**
   - Kodiere die Segmente entlang des Codierschemas.
   - Synthese der Ergebnisse entlang der Dimensionen Faktoren, Effekte und Interaktionen; Ableitung eines zusammenhängenden Bildes der Effekt‑Faktoren aus Lehrendensicht.
    

**Codierschema:**

- **Definition der Kategorien:** Präzise Beschreibung der Dimensionen „Faktoren“ und „Effekte“.
- **Ankerbeispiele:** Textstellen, die die jeweilige Kategorie typisieren.
- **Kodierregeln:** Kriterien für die Zuordnung von Textstellen zu den Dimensionen, um Transparenz und Reliabilität sicherzustellen.

Erwartete Leistung:

Generiere generalisierbare Aussagen zu den Faktoren, die Lehrende als Grundlage für die beschriebenen Effekte im digitalen Bildungsraum der Gesundheitsberufe identifizieren. Ordne die Ergebnisse in den Kontext systemisch-konstruktivistischer Didaktik ein.


Darstellung der Ergebnisse:

 1. **Anzahl der analysierten Studien:**

Gib die Gesamtzahl der ausgewerteten und in die Synthese eingebundenen Studien an.

 2. **Strukturierte Synthese:**

- Beschreibe ausführlich die von Lehrenden genannten Effekt-Faktoren und ihre wahrgenommenen Wirkungen.
- Analysiere die Wechselwirkungen zwischen den LMS-Funktionen und der Wirksamkeit für den Bildungsprozess.

 3. **Integration relevanter Begriffe und Theorien:**

- Erkläre zentrale Begriffe wie „Effekt-Faktoren“ und „Lernprozesse“ im Kontext systemisch-konstruktivistischer Didaktik.
- Verknüpfe die Ergebnisse mit relevanten Theorien, z. B.:
    - **Theorie der sozialen Interaktion**: Bedeutung kollaborativer Funktionen im LMS.
    - **Systemisch-konstruktivistischer Ansatz**: Förderung von Eigenverantwortung und reflexivem Lernen.

 4. **Tabellarische Darstellung des Codierschemas:**

- Zeige die Kategorien, Definitionen, Ankerbeispiele und Kodierregeln in einer Tabelle.

|**Kategorie**|**Definition**|**Ankerbeispiele**|**Kodierregel**|
|---|---|---|---|
|**Faktoren**|Merkmale des LMS, die von Lehrenden als zentral für die Effektivität beschrieben werden.|„Die Möglichkeit, Inhalte individuell anzupassen, erleichtert die Lehre.“|Fokus auf konkrete LMS-Funktionen.|
|**Effekte**|Beobachtete Veränderungen in Lernprozessen, sozialen Interaktionen oder organisatorischer Effizienz.|„Die Studierenden arbeiten aktiver und mit höherer Eigenverantwortung.“|Textstellen mit klaren Aussagen zu beobachtbaren Ergebnissen.|

 5. **Kritische Reflexion und Ausblick:**

- Reflektiere die Ergebnisse hinsichtlich ihrer Aussagekraft und Relevanz für die Gestaltung und Implementierung von LMS in der Gesundheitsbildung.
- Diskutiere mögliche Limitationen der Metaanalyse und zeige Handlungsempfehlungen für die Praxis auf.

Zusatz:

Betone besonders die Interaktion zwischen den von Lehrenden beschriebenen LMS-Faktoren und deren Auswirkungen auf die Lernprozesse, um die ganzheitliche Bedeutung des Ansatzes zu verdeutlichen.

# Metaprompt

**Ziel:**  
Führe eine strukturierte Metaanalyse durch, die zentrale Erkenntnisse aus den bereitgestellten Analysen extrahiert, synthetisiert und auf die folgende Forschungsunterfrage abstimmt:

**Forschungsunterfrage (FU2b):**  
_„Welche Faktoren beeinflussen die Anwendung und Wirkung von Learning-Management-Systemen (LMS) auf Seiten der Lehrenden im digitalen Bildungsraum der Gesundheitsberufe?“_

**Anweisungen für die Durchführung:**

1. **Themenkategorisierung:**  
   - Kategorisiere die Aussagen entlang folgender Schwerpunkte:
     - **Professionelle Haltung und Motivation** (z. B. Offenheit, Selbstwirksamkeit, Erfahrung)
     - **Technisch-didaktische Kompetenzen** (z. B. Medienkompetenz, LMS-spezifisches Know-how)
     - **Rollenverständnis** (z. B. Shift vom Lehrenden zum Lernbegleitenden)
     - **Unterstützungsstrukturen** (z. B. Fortbildung, Support, kollegiale Netzwerke)

2. **Synthese der Ergebnisse:**  
   - Fasse die zentralen Erkenntnisse zur Lehrendenperspektive zusammen.
   - Untersuche die verwendeten theoretischen Konzepte (z. B. TPACK, SAMR-Modell, Adult Learning Theory).
   - Identifiziere Unterschiede zwischen verschiedenen Berufsgruppen oder Erfahrungsniveaus.

3. **Diskussion und Bewertung:**  
   - Reflektiere Barrieren und förderliche Bedingungen aus Sicht der Lehrenden.
   - Beurteile die Aussagekraft der Analysen hinsichtlich Methodik, Kontext und Relevanz.
   - Ziehe Rückschlüsse auf die Voraussetzungen für erfolgreiche LMS-Implementierung durch Lehrende.

4. **Theoretischer und praktischer Beitrag:**  
   - Leite Empfehlungen für Qualifizierungsmaßnahmen und Unterstützungskonzepte ab.
   - Zeige exemplarische Lösungsansätze für häufige Herausforderungen.
   - Benenne Desiderate und offene Forschungsfragen zur Lehrendenrolle.

**Output-Struktur:**  
1. **Einleitung**  
   - Ziel und Relevanz der Metaanalyse  
   - Überblick über die ausgewertete Datenbasis

2. **Themenkategorisierung**  
   - Gruppierung nach Haltung, Kompetenzen, Rollenverständnis, Unterstützung

3. **Synthese und Diskussion**  
   - Darstellung zentraler Muster und Einflussfaktoren  
   - Einordnung in theoretische Modelle

4. **Praktische Empfehlungen**  
   - Gestaltung von Qualifizierungsstrategien für Lehrende  
   - Gelingensbedingungen und Good-Practice-Beispiele

5. **Schlussfolgerung**  
   - Bewertung der Erkenntnisse im Kontext der FU2b  
   - Implikationen für Bildungspraxis und Forschung

**Zusatz:**  
Bitte nenne die Anzahl der analysierten Notizen.

**Format:** Markdown

Links: [[FU2b Prompt Sekundäranalyse]] · [[FU2b Primäranalysen (27)]] · [[FU2b Qualitative Metaanalyse]] · [[FU2b Codiersystem]]
