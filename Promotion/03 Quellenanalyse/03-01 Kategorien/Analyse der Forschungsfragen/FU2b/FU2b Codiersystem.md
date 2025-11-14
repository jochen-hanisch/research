---
title: "Codiersystem FU2b"
fu: FU2b
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU2b Primäranalysen (27).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU2b, typ/codiersystem]
links:
  prompt: "FU2b Prompt Sekundäranalyse.md"
  primary: "FU2b Primäranalysen (27).md"
  analysis: "FU2b Qualitative Metaanalyse.md"
  codebook: "FU2b Codiersystem.md"
---

# **Codiersystem FU2b**

## **Einleitung**

FU2b beschreibt die Lehrendensicht auf LMS im digitalen Bildungsraum der Gesundheitsberufe. Die Kodierlogik folgt der P‑QIA und basiert auf 27 Primäranalysen plus der FU2b-Metaanalyse.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU2b Primäranalysen (27) + FU2b Qualitative Metaanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k‑means (k=14) → Silhouette 0.89.
- **Clusterprüfung:** `gpt-5-codex` Reasoner generiert Labels/Definitionen; Abgleich mit TPACK, Pygmalion-Effekten, Technostress-Modellen, systemisch-konstruktivistischem Rahmen.
- **Validierung:** 13/14 Cluster deckungsgleich mit Metaanalyse; ein Cluster (geringe Distanz) verworfen.
- **Output:** 13 Kategorien mit Definition, Kodierregel und exemplarischer Stelle.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Didaktisches Design / LMS-Szenarien|Strukturmerkmale der von Lehrenden konfigurierten LMS-Räume (Aufgabenketten, PBL, Simulation, Flipped Classroom).|Kodieren, wenn Lehrende erläutern, _wie_ sie das Design einsetzen, um Effekte zu erzielen.|„Blended Learning mit Supervision führt zu besseren praktischen Ergebnissen.“|
|Feedback- & Kooperationsarchitekturen|Organisierte Formen von Peer-/Tutor*innen-Feedback, kollaborativem Schreiben, Storytelling, Gruppenarbeit.|Segment beschreibt Feedbackschleifen oder Kooperation als Wirkmechanismus.|„Kollaboratives Schreiben steigert Interdependenz.“|
|Learning Analytics & Datenpraxis|Nutzung von Dashboards, Logdaten, Risikoidentifikation oder adaptiven Lernpfaden durch Lehrende.|Kodieren, wenn Daten ausgewertet oder für Entscheidungen genutzt werden.|„Learning Analytics unterstützt die Identifikation gefährdeter Studierender.“|
|Technische Infrastruktur & Systemqualität|Aussagen zu Stabilität, Zugriff, Bandbreite, Tool-Kopplung und Systemservice.|Segment bezieht sich auf technische Rahmenbedingungen und deren Einfluss.|„Unzureichende Infrastruktur verursacht Belastung.“|
|Effekte – Lernprozesse & Kompetenzentwicklung|Wahrgenommene Auswirkungen auf Wissen, Skills, Selbstregulation der Lernenden.|Kodieren, wenn Lehrende Kompetenz- oder Lernerfolgsänderungen beschreiben.|„Microlearning erhöht VC-Kompetenzen signifikant.“|
|Effekte – Soziale Interaktion / Teamkognition|Kooperation, Peer-Abhängigkeiten, Teamlernen als Ergebnis des LMS-Settings.|Segment berichtet, dass soziale Dynamiken Leistungs- oder Engagementeffekte erzeugen.|„Peer-Feedback korreliert mit höherer Leistung.“|
|Effekte – Motivation & Selbstwirksamkeit der Lernenden|Auswirkungen der Lehrendenmaßnahmen auf Engagement, Aktivität oder Selbstvertrauen der Lernenden.|Kodieren, wenn Motivation/Selbstwirksamkeit explizit genannt wird.|„E-Portfolios fördern Reflexion und Eigenverantwortung.“|
|Effekte – Beanspruchung & Technostress|Lehrenden werden psychosoziale Belastungen, Overload oder Stress zugeschrieben.|Segment benennt Technostress, Burnout, Überforderung.|„Techno-overload führt zu Burnout-Risiko.“|
|Lehrendenfaktoren – Haltung & Motivation|Eigene Einstellungen, Erwartungen, Selbstwirksamkeit, Offenheit der Lehrenden.|Kodieren, wenn Lehrende ihre Motivation oder Ressentiments beschreiben.|„Erwartungen der Studierenden beeinflussen Emotionen der Lehrenden.“|
|Lehrendenfaktoren – Technisch-didaktische Kompetenz (TPACK)|Fähigkeit, Technologie, Didaktik und Fachlichkeit zu verbinden.|Segment verweist auf Fortbildung, Sicherheit im Medienmix oder TPACK-Rahmen.|„Fortbildungen mit TPACK-Bezug führen zu höherer Kompetenz und Qualität.“|
|Rollenverständnis / Rollenwandel|Selbstbeschreibung als Lernbegleitung, Feedbackdesigner*in, Dateninterpret*in statt Instrukteur*in.|Kodieren, wenn Lehrende ihre Rolle/Identität im digitalen Setting reflektieren.|„Lehrende gestalten kooperative Lernprozesse statt Inhalte zu vermitteln.“|
|Kontext: Unterstützungsstrukturen & Fortbildung|Organisatorische Hilfen, Coaching, kollegiale Netzwerke, IT-Support.|Segment benennt Supportangebote und deren Einfluss.|„Coach-unterstützte Trainings steigern Completion und Lernleistung.“|
|Kontext: Arbeitsbedingungen & Kultur|Workload, Zeitfenster, institutionelle Policies, Führungskultur.|Kodieren, wenn Arbeitsorganisation oder Kultur als Ermöglichung/Barriere genannt wird.|„Erhöhte Anforderungen durch Online-Lernen führen zu Erschöpfung.“|
