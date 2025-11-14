---
title: "FU6 Prompt Sekundäranalyse"
fu: FU6
version: tbd
last_updated: tbd
status: in_überarbeitung
procedure: "Probabilistisch‑Qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring"
sources_count: 65
sources_file: "FU6 Primäranalysen (65).md"
software: tbd
tags: [mayring, fu/FU6, typ/prompt]
links:
  prompt: "FU6 Prompt Sekundäranalyse.md"
  primary: "FU6 Primäranalysen (65).md"
  analysis: "FU6 Qualitative Inhaltsanalyse.md"
  codebook: "FU6 Codiersystem.md"
---

Bitte diesen Prompt für diesen Chat nehmen, ich gebe eine Export-Datei aller Primäranalysen, die Du nach diesem Prompt bearbeitest:
# Vorarbeiten

**Aufgabe:**  
Analysiere die bereitgestellte Datei systematisch und integriere alle enthaltenen Analysen zur Beantwortung der Forschungsfrage (FU).

Forschungsfrage (FU6):

„Wie wird ein Learning-Management-System als Kompetenzerwerbssystem bei Akteuren im digitalen Bildungsraum der Gesundheitsberufe beurteilt?“


Methodik:

Führe eine probabilistisch‑qualitative Inhaltsanalyse (P‑QIA) auf Basis der qualitativen Inhaltsanalyse nach Mayring durch, um Aussagen zur Eignung des LMS als Kompetenzerwerbssystem zu strukturieren (vgl. [[P-QIA Methode]]). Die Methodik umfasst folgende Schritte:

1. **Segmentierung und probabilistische Strukturierung (P‑QIA):**
   - Segmentiere die Primäranalysen (FU6) in Sinnabschnitte (1–3 Sätze).
   - Erzeuge GPT‑Embeddings für alle Segmente und führe ein k‑means‑Clustering mit FU‑spezifischem *k* durch (vgl. [[P-QIA Statistik]]).
   - Prüfe die Clusterqualität mithilfe des Silhouette‑Koeffizienten und fasse instabile Cluster ggf. zusammen.

2. **Kategorienbildung und Codierschema (Mayring + P‑QIA):**
   - Leite aus den stabilen Clustern Kategorien zu:
     - **Kompetenzbezug** (Fach‑, Handlungs‑, Sozial‑, Selbstkompetenz),
     - **Kompetenzfördernden LMS‑Funktionen** (z. B. interaktive Lernmodule, kollaborative Werkzeuge, Feedback‑Mechanismen),
     - **Begrenzenden Faktoren** (z. B. fehlende Passung, technische/organisationale Hürden).
   - Erstelle ein Codierschema mit Definitionen, Ankerbeispielen (Pfad:Zeile) und Kodierregeln.

3. **Kodierung, Theoriearbeit und Synthese (Mayring + P‑QIA):**
   - Kodiere die Segmente entlang der Kategorien.
   - Verknüpfe die Ergebnisse mit Kompetenzmodellen und Theorien des selbstgesteuerten Lernens; leite daraus eine Bewertung der LMS‑Eignung als Kompetenzerwerbssystem ab.


Erwartete Leistung:

Erstelle eine fundierte Darstellung der Beurteilung eines LMS als Kompetenzerwerbssystem durch Akteure im Bildungsraum der Gesundheitsberufe. Zeige auf, wie die Funktionen des LMS die Entwicklung von beruflicher Handlungskompetenz, Fachkompetenz und Sozialkompetenz fördern können.

Darstellung der Ergebnisse:

 1. **Anzahl der analysierten Studien:**

- Gib die Gesamtzahl der analysierten und in die Synthese einbezogenen Studien an.

 2. **Strukturierte Synthese:**

- Beschreibe, wie das LMS als Kompetenzerwerbssystem wahrgenommen wird.
- Analysiere, welche Funktionen des LMS spezifisch zum Erwerb von Fach-, Sozial- und Handlungskompetenzen beitragen.
- Zeige die Wechselwirkungen zwischen theoretischen Konstrukten der Kompetenzforschung und der praktischen Anwendung des LMS auf.

 3. **Integration relevanter Begriffe und Theorien:**

- Erkläre zentrale Begriffe wie „Kompetenzerwerbssystem“, „berufliche Handlungskompetenz“ und „digitale Bildung“.
- Verknüpfe die Ergebnisse mit relevanten Theorien, z. B.:
    - **Kompetenzmodelle (z. B. Erpenbeck & von Rosenstiel):** Entwicklung und Förderung von Handlungskompetenzen.
    - **Theorien des selbstgesteuerten Lernens:** Unterstützung von Autonomie und Selbstkompetenz durch LMS-Funktionen.

 4. **Tabellarische Darstellung der Kompetenzerwerbsförderung:**

- Stelle die Funktionen des LMS und ihre Verbindung zu Kompetenzen in einer übersichtlichen Tabelle dar.

|**Funktion des LMS**|**Definition**|**Beispiele**|**Geförderte Kompetenz**|
|---|---|---|---|
|**Interaktive Lernmodule**|Inhalte, die aktives Mitdenken und Problemlösen erfordern.|Szenarienbasierte Aufgaben, Quizfragen|Fachkompetenz, Problemlösungskompetenz.|
|**Kollaborative Werkzeuge**|Funktionen zur Zusammenarbeit und Kommunikation.|Diskussionsforen, Gruppenprojekte|Sozialkompetenz, Teamfähigkeit.|
|**Feedback-Mechanismen**|Automatisierte oder personalisierte Rückmeldungen zu Leistungen und Lernfortschritten.|Lernfortschrittsberichte, Quiz-Feedback|Selbstkompetenz, Reflexionsfähigkeit.|

 5. **Kritische Reflexion und Ausblick:**

- Reflektiere die Aussagekraft der Analysen und die Identifikation der förderlichen Funktionen des LMS.
- Diskutiere Limitationen der Untersuchung und zeige Perspektiven für die Weiterentwicklung des LMS als Kompetenzerwerbssystem im Gesundheitsbereich auf.


Zusatz:

Hebe hervor, wie ein LMS zur Förderung spezifischer Kompetenzen beiträgt und welche Voraussetzungen erfüllt sein müssen, damit es als effektives Kompetenzerwerbssystem dienen kann.

# Metaprompt

**Ziel:**  
Führe eine strukturierte Metaanalyse durch, die zentrale Erkenntnisse aus den bereitgestellten Analysen aggregiert und auf die folgende Forschungsunterfrage abstimmt:

**Forschungsunterfrage (FU6):**  
_„Wie wird ein Learning-Management-System (LMS) im digitalen Bildungsraum der Gesundheitsberufe im Hinblick auf seine Eignung als System zum Kompetenzerwerb bewertet?“_

**Anweisungen für die Durchführung:**

1. **Themenkategorisierung:**  
   - Ordne Inhalte den folgenden Kategorien zu:
     - **Kompetenzbegriff:** Welche Kompetenzmodelle werden herangezogen (z. B. Fach-, Handlungs-, Sozialkompetenz)?
     - **Kompetenzfördernde Elemente:** Welche LMS-Funktionalitäten (z. B. Feedback, Simulation, Individualisierung) werden als förderlich beschrieben?
     - **Evaluation und Nachweise:** Welche Kriterien und Methoden zur Kompetenzüberprüfung werden genannt?
     - **Begrenzende Faktoren:** Wo liegen aus Sicht der Quellen Grenzen der Kompetenzentwicklung via LMS?

2. **Synthese der Ergebnisse:**  
   - Fasse zentrale Aussagen zusammen, die das LMS als lernwirksames System für Kompetenzentwicklung charakterisieren.
   - Analysiere Gemeinsamkeiten und Unterschiede hinsichtlich Kompetenzverständnis und eingesetzter Didaktik.
   - Berücksichtige Wirkbedingungen (z. B. Lernkultur, technische Infrastruktur, Zielgruppen).

3. **Diskussion und Bewertung:**  
   - Diskutiere, inwieweit die analysierten LMS-Modelle als systematisch auf Kompetenzerwerb ausgerichtet gelten können.
   - Reflektiere kritisch, ob der Kompetenzerwerb auch über Prüfungsleistungen hinaus beschrieben wird (implizites Lernen, Transferfähigkeit etc.).
   - Bewerte Evidenzlage und methodische Güte der Aussagen.

4. **Theoretischer und praktischer Beitrag:**  
   - Leite Kriterien ab, unter welchen Bedingungen LMS als wirksames Kompetenzsystem gelten kann.
   - Formuliere Gestaltungsprinzipien für kompetenzorientiertes digitales Lernen.
   - Identifiziere konzeptionelle Leerstellen und benenne Perspektiven für Weiterentwicklung.

**Output-Struktur:**  
1. **Einleitung**  
   - Ziel und Kontext der Metaanalyse  
   - Überblick über das Datenmaterial

2. **Themenkategorisierung**  
   - Strukturierung der Aussagen nach Kompetenzbezug

3. **Synthese und Diskussion**  
   - Bewertung der Eignung des LMS als Kompetenzsystem  
   - Einordnung theoretischer und praktischer Implikationen

4. **Praktische Empfehlungen**  
   - Empfehlungen für Design, Implementierung und Evaluation kompetenzorientierter LMS  
   - Hinweise zur Nachweisführung von Kompetenzentwicklung

5. **Schlussfolgerung**  
   - Zentrale Erkenntnisse und Forschungsbedarfe

**Zusatz:**  
Bitte gib die Anzahl der analysierten Notizen an.

**Format:** Markdown

Links: [[FU6 Prompt Sekundäranalyse]] · [[FU6 Primäranalysen (65)]] · [[FU6 Qualitative Inhaltsanalyse]] · [[FU6 Codiersystem]]
