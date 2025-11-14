---
title: "FU2a Prompt Sekundäranalyse"
fu: FU2a
version: tbd
last_updated: tbd
status: in_überarbeitung
procedure: "Probabilistisch‑Qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring"
sources_count: 85
sources_file: "FU2a Primäranalysen (85).md"
software: tbd
tags: [mayring, fu/FU2a, typ/prompt]
links:
  prompt: "FU2a Prompt Sekundäranalyse.md"
  primary: "FU2a Primäranalysen (85).md"
  analysis: "FU2a Qualitative Metaanalyse.md"
  codebook: "FU2a Codiersystem.md"
---

# Vorarbeiten

## Aufgabe:

Analysiere die bereitgestellte Datei systematisch und integriere alle enthaltenen Analysen zur Beantwortung der Forschungsunterfrage (FU2a).

Forschungsunterfrage (FU2a):

„Welchen Effekt erleben Lernende im digitalen Bildungsraum der Gesundheitsberufe bei der Nutzung eines Learning-Management-Systems (LMS)?“

## Methodik:

Führe eine probabilistisch‑qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring durch. Ziel ist es, die Lernendensicht auf Effekte der LMS‑Nutzung systematisch, probabilistisch gestützt und theoriebezogen zu erfassen (vgl. [[P-QIA Methode]]). Die Methodik umfasst folgende Schritte:

1. **Segmentierung und probabilistische Strukturierung (P‑QIA):**
   - Segmentiere die bereitgestellten Primäranalysen in Sinnabschnitte (1–3 Sätze).
   - Erzeuge GPT‑Embeddings für alle Segmente und führe ein k‑means‑Clustering mit FU‑spezifischem *k* durch (vgl. [[P-QIA Statistik]]).
   - Prüfe die Clusterqualität mithilfe des Silhouette‑Koeffizienten und fasse instabile Cluster ggf. zusammen.

2. **Kategorienbildung und Codierschema (Mayring + P‑QIA):**
   - Leite aus den stabilen Clustern die vier Dimensionen der Lernendensicht ab:
     - **Lernerleben:** Motivation, Autonomie, Usability, soziale Einbindung.
     - **Lernerfolg:** Kompetenzerwerb, Lernleistung, Anwendungstransfer.
     - **Nutzungsverhalten:** Nutzungsmuster, Wiederverwendung, Interaktion mit Inhalten.
     - **Perspektivische Bewertung:** Zufriedenheit, Lernpräferenzen, technologische Offenheit.
   - Erstelle ein Codierschema mit:
     - präzisen **Kategoriedefinitionen**,
     - **Ankerbeispielen** (konkrete Textstellen mit Pfadangabe, z. B. `FU2a Primäranalysen (85).md:Zeile`),
     - **Kodierregeln** (Zuordnungskriterien, Umgang mit Mehrdeutigkeiten, Regeln für Doppel‑/Mehrfachkodierungen).

3. **Kodierung und Synthese (Mayring + P‑QIA):**
   - Kodiere alle Segmente der Primäranalysen entlang des Codierschemas.
   - Synthese entlang der vier Dimensionen (Lernerleben, Lernerfolg, Nutzungsverhalten, Bewertung) unter Berücksichtigung der probabilistischen Clusterstruktur.
  
## Erwartete Leistung:

Erstelle eine umfassende, fundierte Darstellung des aktuellen Forschungsstands aus der Sicht Lernender. Beantworte FU2a, indem du Effekte des LMS beschreibst, Einflussgrößen identifizierst (z. B. Lernphase, Kontext, digitale Kompetenzen) und die Übertragbarkeit auf gesundheitsberufliche Bildung bewertest.

## Darstellung der Ergebnisse:

1. Anzahl der analysierten Studien/Notizen: n = …
2. Strukturierte Synthese: Ergebnisse zu Lernerleben, Lernerfolg, Nutzungsverhalten, perspektivischer Bewertung; Gemeinsamkeiten, Unterschiede, Tendenzen
3. Integration relevanter Begriffe und Theorien: z. B. Self-Determination Theory, Constructive Alignment, Cognitive Load
4. Tabellarische Darstellung des Codierschemas:

|**Kategorie**|**Definition**|**Ankerbeispiele**|**Kodierregel**|
|---|---|---|---|
|Lernerleben|Subjektives Erleben bei LMS-Nutzung (Motivation, Autonomie, Usability, soziale Einbindung).|„Ich kann mein Lernen selbst steuern.“ / „Die Navigation ist verwirrend.“|Textstellen mit explizitem Erleben/Emotion/Bedienfeedback; Usability-Aussagen hier codieren, nicht bei Lernerfolg.|
|Lernerfolg|Nachweis/Erleben von Kompetenzzuwachs, Leistung, Transfer.|„Ich verstehe Fallbeispiele besser.“|Leistungs- oder Transferbezug hat Vorrang vor Zufriedenheit.|
|Nutzungsverhalten|Muster der Nutzung und Interaktion mit Inhalten/Features.|„Ich nutze Quizze mehrfach.“|Deskriptive Nutzungsbeschreibungen ohne Wertung.|
|Perspektivische Bewertung|Zufriedenheit, Präferenzen, Offenheit gegenüber Technologie.|„Insgesamt bin ich zufrieden.“|Summative Urteile; ohne Leistungs- oder Erlebensbezug.|

## Kritische Reflexion und Ausblick:

- Validiere die Aussagekraft und Reliabilität der Befunde.
- Diskutiere Kontextabhängigkeiten (Curriculum, Betreuung, medientechnische Ausstattung).
- Leite Handlungsempfehlungen für die LMS-Gestaltung aus Lernendensicht ab (z. B. Autonomie-Support, klare Navigationsstrukturen, formative Feedbackschleifen).
- Identifiziere Forschungslücken (z. B. Langzeit-Effekte, differenzielle Effekte nach Vorerfahrung).

## Zusatz:

- Gib die Anzahl der analysierten Notizen an.
- Format: Markdown
- Zitationsstil: APA 7 (in-text Klammerbelege, konsistent und überprüfbar).

# Metaprompt

**Ziel:**  
Führe eine strukturierte Metaanalyse unter Einbezug aller bereitgestellten Analysen durch. Die Analyse soll zentrale Erkenntnisse aggregieren und auf die folgende Forschungsunterfrage fokussieren:

**Forschungsunterfrage (FU2a):**  
_„Welchen Effekt erleben Lernende im digitalen Bildungsraum der Gesundheitsberufe bei der Nutzung eines Learning-Management-Systems (LMS)?“_

**Anweisungen für die Durchführung:**

1. **Themenkategorisierung:**  
   - Identifiziere wiederkehrende Aussagen und Schwerpunkte, insbesondere:
     - **Lernerleben:** Motivation, Autonomie, Usability, soziale Einbindung.
     - **Lernerfolg:** Kompetenzerwerb, Lernleistung, Anwendungstransfer.
     - **Nutzungsverhalten:** Nutzungsmuster, Wiederverwendung, Interaktion mit Inhalten.
     - **Perspektivische Bewertung:** Zufriedenheit, Lernpräferenzen, technologische Offenheit.

2. **Synthese der Ergebnisse:**  
   - Aggregiere die Befunde aus Einzelanalysen bezogen auf die Lernendensicht.
   - Vergleiche unterschiedliche Studiendesigns, Stichproben und theoretische Bezüge (z. B. Self-Determination Theory, Constructive Alignment).
   - Herausarbeitung von Gemeinsamkeiten, Unterschieden, Tendenzen.

3. **Diskussion und Bewertung:**  
   - Beurteile, wie valide, reliabel und differenziert die Effekte auf Lernende dargestellt sind.
   - Identifiziere Einflussgrößen wie Lernphase, Kontext, digitale Kompetenzen.
   - Erörtere Übertragbarkeit der Befunde auf gesundheitsberufliche Bildungskontexte.

4. **Theoretischer und praktischer Beitrag:**  
   - Leite handlungsleitende Schlussfolgerungen für didaktische Gestaltung ab.
   - Gib Empfehlungen zur lernförderlichen LMS-Nutzung aus Sicht der Lernenden.
   - Identifiziere Forschungslücken und Bedarfe für vertiefende Studien.

**Output-Struktur:**  
1. **Einleitung**  
   - Ziel und Relevanz der Metaanalyse  
   - Beschreibung der genutzten Datenbasis

2. **Themenkategorisierung**  
   - Gruppierung der Erkenntnisse entlang der vier Hauptbereiche (Lernerleben, Lernerfolg, Nutzungsverhalten, Bewertung)

3. **Synthese und Diskussion**  
   - Zusammenfassung zentraler Muster  
   - Reflexion theoretischer und empirischer Bezüge

4. **Praktische Empfehlungen**  
   - Hinweise für Gestaltung und Verbesserung von LMS-Angeboten für Lernende  
   - Beispiele für gute Praxis

5. **Schlussfolgerung**  
   - Bewertung der Erkenntnislage in Bezug auf FU2a  
   - Weiterführende Fragen und Perspektiven

**Zusatz:**  
Bitte gib die Anzahl der analysierten Notizen an.

**Format:** Markdown

Links: [[FU2a Prompt Sekundäranalyse]] · [[FU2a Primäranalysen (85)]] · [[FU2a Qualitative Metaanalyse]] · [[FU2a Codiersystem]]
