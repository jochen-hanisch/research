---
title: "FU7 Prompt Sekundäranalyse"
fu: FU7
version: tbd
last_updated: tbd
status: in_überarbeitung
procedure: "Probabilistisch‑Qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring"
sources_count: 8
sources_file: "FU7 Primäranalysen (8).md"
software: tbd
tags: [mayring, fu/FU7, typ/prompt]
links:
  prompt: "FU7 Prompt Sekundäranalyse.md"
  primary: "FU7 Primäranalysen (8).md"
  analysis: "FU7 Qualitative Inhaltsanalyse.md"
  codebook: "FU7 Codiersystem.md"
---

Bitte diesen Prompt für diesen Chat nehmen, ich gebe eine Export-Datei aller Primäranalysen, die Du nach diesem Prompt bearbeitest:
# Vorarbeiten

**Aufgabe:**  
Analysiere die bereitgestellte Datei systematisch und integriere alle enthaltenen Analysen zur Beantwortung der Forschungsfrage (FU).

**Forschungsfrage (FU7):**

„Welche Inputs und Strategien werden als Erweiterung von Kausalgesetzen bei der Anwendung eines Learning-Management-Systems durch Akteure im digitalen Bildungsraum von Gesundheitsberufen abgeleitet?“

Methodik:

Führe eine probabilistisch‑qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring durch, um Inputs und Strategien in einem kausalen Wirkmodell der LMS‑Nutzung zu rekonstruieren (vgl. [[P-QIA Methode]]). Die Methodik umfasst folgende Schritte:

1. **Segmentierung und probabilistische Strukturierung (P‑QIA):**
   - Segmentiere die Primäranalysen (FU7) in kurze Sinnabschnitte (1–2 Sätze).
   - Erzeuge GPT‑Embeddings für alle Segmente und führe ein k‑means‑Clustering mit FU‑spezifischem *k* durch (vgl. [[P-QIA Statistik]]).
   - Prüfe die Clusterqualität mithilfe des Silhouette‑Koeffizienten und fasse instabile Cluster ggf. zusammen.

2. **Kategorienbildung und Codierschema (Mayring + P‑QIA):**
   - Leite aus den stabilen Clustern Kategorien zu:
     - **Inputs** (z. B. Ressourcen, Rahmenbedingungen, technologische/didaktische/organisationale Inputs),
     - **Strategien** (z. B. didaktische, technologische, organisationale Strategien),
     - **Wirkungen** (z. B. Effekte auf Nutzung, Akzeptanz, Kompetenzerwerb).
   - Erstelle ein Codierschema mit Definitionen, Ankerbeispielen (Pfad:Zeile) und Kodierregeln zur Zuordnung von Segmenten zu Input, Strategie und Wirkung.

3. **Kodierung, Kausalmodellierung und Theoriebezug (Mayring + P‑QIA):**
   - Kodiere die Segmente entlang der drei Kategoriengruppen (Inputs, Strategien, Wirkungen).
   - Rekonstruiere auf dieser Basis Kausalpläne (Ursache‑Wirkungs‑Ketten) und verknüpfe sie mit theoretischen Konzepten (z. B. Technologiedefizit nach Luhmann & Schorr, systemtheoretische Perspektiven).

Erwartete Leistung:

Entwickle ein kausales Ursachen-Wirkungs-Theoriemodell (Kausalpläne), das Inputs, Strategien und Wirkungen im Zusammenhang mit der LMS-Anwendung darstellt. Formuliere auf dieser Basis fundierte Handlungsempfehlungen für den digitalen Bildungsraum der Gesundheitsberufe.


Darstellung der Ergebnisse:

 1. **Anzahl der analysierten Studien:**

- Gib die Gesamtzahl der analysierten und in die Theorieentwicklung einbezogenen Studien an.

 2. **Entwicklung des Kausalmodells:**

- Beschreibe Inputs (z. B. technologische, didaktische, soziale Faktoren) und Strategien (z. B. Anpassung an Bedürfnisse der Akteure, organisatorische Prozesse).
- Zeige, wie diese Inputs und Strategien in kausalen Beziehungen zu den Wirkungen des LMS stehen.
- Visualisiere diese Zusammenhänge in einem Kausalplan, der die Ursachen-Wirkungs-Beziehungen verdeutlicht.

 3. **Integration relevanter Begriffe und Theorien:**

- Erkläre Begriffe wie „Technologiedefizit“, „Inputs“, „Strategien“ und „Kausalgesetze“.
- Verknüpfe die Ergebnisse mit relevanten Theorien, z. B.:
    - **Technologiedefizit (Luhmann & Schorr, 1982):** Ergänzung technischer Systeme durch soziale und organisatorische Inputs.
    - **Systemtheorie:** Darstellung komplexer Wechselwirkungen in Bildungs- und Technologiesystemen.

 4. **Tabellarische Darstellung der Inputs, Strategien und Wirkungen:**

- Zeige die Inputs, Strategien und ihre kausalen Wirkungen in einer übersichtlichen Tabelle.

|**Input**|**Strategie**|**Wirkung**|**Kausale Beziehung**|
|---|---|---|---|
|Technologische Funktionen|Anpassung der LMS-Funktionen an spezifische Bildungsbedürfnisse|Effektiver Kompetenzerwerb|Technologie als Grundlage, ergänzt durch didaktische Anpassung.|
|Didaktische Inputs|Entwicklung kollaborativer und interaktiver Lerninhalte|Stärkung der sozialen Interaktion|Soziale Strategien fördern die Nutzung und Akzeptanz des LMS.|
|Organisatorische Prozesse|Unterstützung durch Schulungen und begleitende Maßnahmen|Höhere Akzeptanz und Motivation|Schulung gleicht technologische Schwächen aus.|

 5. **Kritische Reflexion und Ausblick:**

- Reflektiere die Aussagekraft und die Limitationen des entwickelten Kausalmodells.
- Zeige, wie die Handlungsempfehlungen zur Verbesserung der LMS-Nutzung beitragen können und welche weiteren Forschungsschritte notwendig sind.


Zusatz:

Betone, wie die Kausalpläne nicht nur technische, sondern auch soziale und organisatorische Inputs als integralen Bestandteil berücksichtigen, um die Wirksamkeit des LMS im Bildungsraum der Gesundheitsberufe zu maximieren.

# Metaprompt

**Ziel:**  
Führe eine strukturierte Metaanalyse durch, die zentrale Erkenntnisse aus den bereitgestellten Analysen aggregiert und auf die folgende Forschungsunterfrage abstimmt:

**Forschungsunterfrage (FU7):**  
_„Welche Inputs (z. B. Ressourcen, Rahmenbedingungen) und Strategien (z. B. didaktische, technologische, organisationale) werden im digitalen Bildungsraum der Gesundheitsberufe bei der Nutzung eines Learning-Management-Systems (LMS) beschrieben?“_

**Anweisungen für die Durchführung:**

1. **Themenkategorisierung:**  
   - Ordne die analysierten Inhalte folgenden Themenfeldern zu:
     - **Didaktische Strategien:** z. B. Blended Learning, flipped classroom, adaptives Lernen.
     - **Technologische Strategien:** z. B. Tool-Integration, Interoperabilität, Skalierbarkeit.
     - **Organisationale Strategien:** z. B. Schulungsprogramme, Change Management, Supportstrukturen.
     - **Inputs:** Ressourcen (zeitlich, personell, finanziell), technische Ausstattung, institutionelle Vorgaben.
     - **Rahmenbedingungen:** rechtliche, ethische, kulturelle und infrastrukturelle Voraussetzungen.

2. **Synthese der Ergebnisse:**  
   - Fasse wiederkehrende Muster und erfolgskritische Faktoren für die erfolgreiche LMS-Nutzung zusammen.
   - Hebe innovative oder besonders wirkungsvolle Strategien hervor.
   - Identifiziere Wechselwirkungen zwischen Inputfaktoren und Implementierungsstrategien.

3. **Diskussion und Bewertung:**  
   - Diskutiere die Bedeutung der genannten Inputs und Strategien im Kontext der Gesundheitsberufe.
   - Reflektiere kritische Punkte, z. B. Abhängigkeit von Ressourcen oder mangelnde Strategieumsetzung.
   - Bewerte den Innovationsgrad und die Skalierbarkeit der beschriebenen Modelle.

4. **Theoretischer und praktischer Beitrag:**  
   - Formuliere konkrete Handlungsempfehlungen für Bildungsinstitutionen im Gesundheitswesen.
   - Identifiziere Gelingensbedingungen für nachhaltige LMS-Integration.
   - Benenne Forschungslücken und Perspektiven zur strategischen Weiterentwicklung.

**Output-Struktur:**  
1. **Einleitung**  
   - Ziel und Kontext der Metaanalyse  
   - Überblick über das untersuchte Material

2. **Themenkategorisierung**  
   - Systematische Darstellung nach Inputs und Strategien

3. **Synthese und Diskussion**  
   - Zentrale Befunde und deren Bedeutung für die LMS-Nutzung  
   - Kritische Reflexion und Kontextualisierung

4. **Praktische Empfehlungen**  
   - Strategien für die erfolgreiche LMS-Implementierung  
   - Empfehlungen für Inputmanagement und Rahmenbedingungen

5. **Schlussfolgerung**  
   - Zusammenfassung zentraler Erkenntnisse und Ausblick

**Zusatz:**  
Bitte gib die Anzahl der analysierten Notizen an.

**Format:** Markdown

Links: [[FU7 Prompt Sekundäranalyse]] · [[FU7 Primäranalysen (8)]] · [[FU7 Qualitative Inhaltsanalyse]] · [[FU7 Codiersystem]]
