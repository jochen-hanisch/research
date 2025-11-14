# Vorarbeiten

Aufgabe:  
Analysiere die bereitgestellte Datei systematisch und integriere alle enthaltenen Analysen zur Beantwortung der Forschungsfrage (FU).

Forschungsunterfrage (FU1):

„Welche Akzeptanz und Nützlichkeit (Bedeutung) beschreiben Akteure im digitalen Bildungsraum der Gesundheitsberufe bei der Anwendung eines Learning-Management-Systems (LMS)?“

Methodik:

Führe eine probabilistisch‑qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring durch. Ziel ist es, zentrale Aussagen und Themen aus den enthaltenen Analysen systematisch zu extrahieren, probabilistisch zu strukturieren und theoretisch zu interpretieren. Die Methodik umfasst folgende Schritte (vgl. [[P-QIA Methode]]):

1. **Segmentierung und probabilistische Strukturierung (P‑QIA):**
    - Segmentiere die bereitgestellten Primäranalysen in Sinnabschnitte (1–3 Sätze).
    - Erzeuge GPT‑Embeddings für alle Segmente und führe ein k‑means‑Clustering mit FU‑spezifischem *k* durch (vgl. [[P-QIA Statistik]]).
    - Prüfe die Clusterqualität mithilfe des Silhouette‑Koeffizienten und fasse instabile Cluster ggf. zusammen.
2. **Kategorienbildung und Codierschema (Mayring + P‑QIA):**
    - Leite aus den stabilen Clustern Kategorien für **Akzeptanz** und **Nützlichkeit** ab:
      - **Akzeptanz:** Einstellungen, emotionale Reaktionen und Nutzungsmuster der Akteure.
      - **Nützlichkeit:** Wahrgenommener Nutzen des LMS für Lernprozesse, Kommunikation und Organisation im Bildungsraum der Gesundheitsberufe.
    - Erstelle ein Codierschema mit:
      - **Kategoriedefinitionen** (präzise Abgrenzung der Dimensionen „Akzeptanz“ und „Nützlichkeit“),
      - **Ankerbeispielen** (konkrete Textstellen mit Pfadangabe, z. B. `FU1 Primäranalysen (58).md:Zeile`),
      - **Kodierregeln** (Kriterien für die Zuordnung von Textstellen, inkl. Umgang mit Mehrdeutigkeiten und Mehrfachkodierungen).
3. **Kodierung und Synthese (Mayring + P‑QIA):**  
    - Kodierung der bereitgestellten Segmente anhand des Codierschemas.
    - Verbindung und Gegenüberstellung der Kategorien, um Wechselwirkungen zwischen Akzeptanz und Nützlichkeit des LMS herauszuarbeiten (z. B. Rolle von Benutzerfreundlichkeit, wahrgenommener Nützlichkeit, Selbstwirksamkeit, Rahmenbedingungen).

Erwartete Leistung:

Erstelle eine fundierte und umfassende Darstellung des aktuellen Forschungsstandes auf Basis aller enthaltenen Analysen. Beantworte die Forschungsfrage, indem du:

- die probabilistisch gewonnenen Cluster und Kategorien transparent darstellst,
- die Ergebnisse theoriegeleitet (z. B. TAM, UTAUT, Motivationstheorien) einordnest,
- die Interdependenzen zwischen Akzeptanz und Nützlichkeit im digitalen Bildungsraum der Gesundheitsberufe herausarbeitest.

Darstellung der Ergebnisse:

1. **Anzahl der analysierten Studien:**  
    Gib die Gesamtzahl der ausgewerteten und in die Synthese einfließenden Analysen an.
2. **Strukturierte Synthese:**
    - Beschreibe die Ergebnisse der Analysen in Bezug auf die Kategorien „Akzeptanz“ und „Nützlichkeit“.
    - Stelle die Wechselwirkungen und deren Bedeutung für den Bildungsraum der Gesundheitsberufe ausführlich dar.
3. **Integration relevanter Begriffe und Theorien:**
    - Erläutere die Begriffe „Akzeptanz“ und „Nützlichkeit“ im Kontext digitaler Bildung.
    - Verknüpfe die Ergebnisse mit Theorien wie dem Technology Acceptance Model (TAM) oder Motivationstheorien, um die wissenschaftliche Fundierung zu stärken.
4. **Tabellarische Darstellung des Codierschemas:**
    - Zeige die Kategorien, Definitionen, Ankerbeispiele und Kodierregeln in tabellarischer Form.

| **Kategorie**    | **Definition**                                                                                           | **Ankerbeispiele**                                    | **Kodierregel**                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------- |
| **Akzeptanz**    | Einstellungen und emotionale Reaktionen gegenüber dem LMS.                                               | „Ich mag das LMS, weil es einfach zu bedienen ist.“   | Textstellen mit klar positiver oder negativer Bewertung. |
| **Nützlichkeit** | Wahrgenommener Nutzen des LMS für Lern- und Organisationsprozesse im Bildungsraum der Gesundheitsberufe. | „Das LMS hilft mir, meine Lernmaterialien zu ordnen.“ | Fokus auf praktische Vorteile oder Effizienzgewinne.     |

5. **Kritische Reflexion und Ausblick:**
    - Beurteile die Ergebnisse hinsichtlich ihrer Aussagekraft und Relevanz für die Implementierung von LMS in der Gesundheitsbildung.
    - Diskutiere potenzielle Limitationen und zeige Handlungsempfehlungen für die Praxis auf.

Zusatz:

Hebe besonders die Schnittstellen zwischen wahrgenommener Nützlichkeit und Akzeptanz hervor, um die Bedeutung des LMS für Akteure im digitalen Bildungsraum umfassend darzustellen.

# Metaprompt

**Ziel:**  
Führe eine strukturierte Metaanalyse unter Einbezug aller bereitgestellten Analysen durch. Die Analyse soll zentrale Erkenntnisse aggregieren und auf die folgende Forschungsunterfrage fokussieren:

**Forschungsunterfrage:**  
_„Welche der Akzeptanz und Nützlichkeit (Bedeutung) beschreiben Akteure im digitalen Bildungsraum von Gesundheitsberufen bei Anwendung eines Learning-Management-Systems (LMS)?“_

**Anweisungen für die Durchführung:**

1. **Themenkategorisierung:**  
   - Identifiziere wiederkehrende Themen und inhaltliche Foki innerhalb der Analysen, insbesondere:
     - **Akzeptanzfaktoren:** Technologische, soziale und organisationale Einflussgrößen.
     - **Nützlichkeit:** Beiträge zur Lehr-/Lerneffektivität, zur Praxisrelevanz und zur didaktischen Gestaltung.
     - **Herausforderungen:** Barrieren und Widerstände bei Einführung und Nutzung.
     - **Chancen:** Potenziale für Integration, Akzeptanzförderung und Systementwicklung.

2. **Synthese der Ergebnisse:**  
   - Fasse zentrale Aussagen, empirische Befunde und Argumentationsmuster zusammen.
   - Unterscheide Gemeinsamkeiten und Unterschiede zwischen den Einzelanalysen.
   - Identifiziere verwendete theoretische Modelle (z. B. Technology Acceptance Model, UTAUT etc.) und methodische Zugänge.

3. **Diskussion und Bewertung:**  
   - Bewerte die Übertragbarkeit der Analyseergebnisse auf den digitalen Bildungsraum in Gesundheitsberufen.
   - Diskutiere Zusammenhänge zwischen Akzeptanzfaktoren und erlebter bzw. beschriebener Nützlichkeit.
   - Beurteile die Relevanz und Aktualität der ausgewerteten Literaturquellen.

4. **Theoretischer und praktischer Beitrag:**  
   - Leite Empfehlungen für die Gestaltung und Implementierung eines LMS in gesundheitsberuflichen Bildungskontexten ab.
   - Identifiziere mögliche Forschungsdesiderate und offene Fragestellungen für zukünftige Studien.

**Output-Struktur:**  
1. **Einleitung**  
   - Zielsetzung und Bedeutung der Metaanalyse  
   - Beschreibung der Datenbasis (z. B. Anzahl der analysierten Notizen, Herkunft, Art)

2. **Themenkategorisierung**  
   - Gruppierung der Einträge entlang der vier Kernkategorien (Akzeptanz, Nützlichkeit, Herausforderungen, Chancen)

3. **Synthese und Diskussion**  
   - Zusammenführung der Ergebnisse  
   - Kritische Reflexion methodischer oder konzeptioneller Muster

4. **Praktische Empfehlungen**  
   - Handlungsvorschläge für Praktiker*innen, Lehrende, Systemverantwortliche  
   - Ggf. Best Practices

5. **Schlussfolgerung**  
   - Gesamteinschätzung im Hinblick auf die Forschungsfrage  
   - Weiterführende Forschungsimpulse

**Zusatz:**  
Bitte gib die Anzahl der analysierten Notizen an.

**Format:** Markdown
---
title: "FU1 Prompt Sekundäranalyse"
fu: FU1
version: tbd
last_updated: tbd
status: in_überarbeitung
procedure: "Qualitative Inhaltsanalyse (Mayring) – Promptrahmen"
sources_count: 58
sources_file: "FU1 Primäranalysen (58).md"
software: tbd
tags: [mayring, fu/FU1, typ/prompt]
links:
  prompt: "FU1 Prompt Sekundäranalyse.md"
  primary: "FU1 Primäranalysen (58).md"
  analysis: "FU1 Qualitative Metaanalyse.md"
  codebook: "FU1 Codiersystem.md"
---

Links: [[FU1 Prompt Sekundäranalyse]] · [[FU1 Primäranalysen (58)]] · [[FU1 Qualitative Metaanalyse]] · [[FU1 Codiersystem]]
