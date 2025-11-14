---
title: "Codiersystem FU4b"
fu: FU4b
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU4b Primäranalysen (93).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU4b, typ/codiersystem]
links:
  prompt: "FU4b Prompt Sekundäranalyse.md"
  primary: "FU4b Primäranalysen (93).md"
  analysis: "FU4b Qualitative Inhaltsanalyse.md"
  codebook: "FU4b Codiersystem.md"
---

# **Codiersystem FU4b**

## **Einleitung**

FU4b fokussiert technisch-gestalterische Mechanismen im LMS. Die P‑QIA kondensiert 93 Primäranalysen in zehn Kernkategorien – jeweils mit Definition, Kodierregel und Ankerstelle.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU4b Primäranalysen (93) + FU4b Qualitative Inhaltsanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k‑means (k=12) → Silhouette 0.92.
- **Clusterprüfung:** `gpt-5-codex` Reasoner; Abgleich mit Usability-, Cognitive-Load- und Systemarchitektur-Konzepten.
- **Validierung:** 10/12 Cluster stabil; zwei sehr kleine Cluster integriert.
- **Output:** Zehn Kategorien mit Definition, Kodierregel und Beispielsegment.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Benutzer*innenfreundlichkeit – Navigationsklarheit|Verständliche Struktur, Orientierung, Informationsarchitektur.|Kodieren, wenn Aussagen explizit Orientierung, Menüführung oder Suchaufwand adressieren.|„Die Teilnehmer*innen finden relevante Inhalte schneller.“|
|Benutzer*innenfreundlichkeit – Konsistenz & Interface-Logik|Wiedererkennbare Layouts, konsistente Symbole und Interaktionen.|Segment benennt konsistente/inkonsistente Gestaltung als Wirkfaktor.|„Unterschiedliche Kursseiten verwirren die Nutzer*innen.“|
|Benutzer*innenfreundlichkeit – Wahrnehmbare Bedienbarkeit|Sichtbarkeit von Funktionen, Fehlertoleranz, Barrierefreiheit.|Kodieren, wenn Nutzbarkeit oder Zugänglichkeit (inkl. mobile Nutzung) diskutiert wird.|„Es ist nicht sichtbar, wo Aufgaben abgegeben werden.“|
|Funktionale Gestaltung – Interaktivität & Aufgabenformate|Drag-and-drop, Szenarien, VR/AR, kollaborative Boards.|Segment beschreibt technische Interaktivität als Lernmechanismus.|„Interaktive Multimedia-Module strukturieren Lernhandlungen.“|
|Funktionale Gestaltung – Feedback- & Assessment-Funktionen|Automatisiertes Feedback, Tests, Kompetenzchecks, Analytics-basierte Rückmeldungen.|Kodieren, wenn Funktionen zur Bewertung oder Rückmeldung thematisiert werden.|„Dashboards visualisieren Lernfortschritt und identifizieren Risiken.“|
|Systemarchitektur – Leistung & Skalierbarkeit|Stabilität, Performance, Verhalten bei hoher Last.|Segment verweist auf technische Robustheit oder Engpässe.|„Bei hoher Last bricht die Seite ab.“|
|Systemarchitektur – Interoperabilität & Integration|Schnittstellen, LTI, mobile Devices, Kopplung externer Tools.|Kodieren, wenn Integrationsfragen als Wirkungstreiber beschrieben werden.|„LTI-Schnittstellen binden Simulationen nahtlos ein.“|
|Technologie–Didaktik – Visuelle Segmentierung & Blickführung|Layoutentscheidungen, die Aufmerksamkeit und Lernpfade steuern.|Segment beschreibt UI-Elemente als didaktische Führung.|„Visuelle Segmentierung erleichtert den Lernpfad.“|
|Technologie–Didaktik – Adaptive/Personalisierte Unterstützung|Adaptive Pfade, kognitive Entlastung, scaffolding-orientierte Prompts.|Kodieren, wenn Technik explizit zur Reduktion extrinsischer Load oder zur Personalisierung dient.|„Adaptive Dashboards fokussieren Aufmerksamkeit auf kritische Kennzahlen.“|
|Technologie–Didaktik – Selbstorganisation & Datenfeedback|Mechanismen, die Selbststeuerung, Monitoring, Learning Analytics-basierte Reflexion ermöglichen.|Segment verweist auf Datenfeedback, das Lernhandlungen strukturiert.|„Learning Analytics unterstützt ko-regulative Mechanismen.“|
