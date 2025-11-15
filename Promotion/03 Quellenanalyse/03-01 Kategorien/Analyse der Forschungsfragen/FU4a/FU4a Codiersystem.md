---
title: "Codiersystem FU4a"
fu: FU4a
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU4a Primäranalysen (220).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU4a, typ/codiersystem]
links:
  prompt: "FU4a Prompt Sekundäranalyse.md"
  primary: "FU4a Primäranalysen (220).md"
  analysis: "FU4a Qualitative Inhlatsanalyse.md"
  codebook: "FU4a Codiersystem.md"
---

# **Codiersystem FU4a**

## **Einleitung**

FU4a rekonstruiert Mechanismen (Selbstregulation, Reflexion, Ko-Produktion etc.) aus 220 Primäranalysen zu LMS-gestützter Qualitätsentwicklung. Die Kodierstruktur folgt der P‑QIA und fasst ausschließlich Kategorien, Definitionen, Kodierregeln und Ankerstellen zusammen.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU4a Primäranalysen (220) + FU4a Qualitative Inhaltsanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k‑means (k=12) → Silhouette 0.90.
- **Clusterprüfung:** `gpt-5-codex` Reasoner erzeugt Labels; Abgleich mit systemisch-konstruktivistischen Mechanismen (SRL, Reflexion, Ko-Produktion, LA, Simulation usw.).
- **Validierung:** 11/12 Cluster konsistent mit Metaanalyse, ein Cluster zusammengeführt.
- **Output:** Elf Kernkategorien mit Definition, Regel und Beispielsegment.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Selbstregulation & Selbststeuerung (SRL)|Mechanismen, die Planung, Monitoring, Zielsetzung oder Strategieregulation im LMS auslösen.|Kodieren, wenn SRL explizit oder implizit (Fortschrittsanzeigen, Ko-Regulation) benannt wird.|„Peer Observation wirkt als Mechanismus zur Förderung selbstregulierten Lernens.“|
|Reflexion & Portfolioarbeit|LMS-gestützte Reflexionsaufgaben, Simulation-Debriefings, Portfolioeinträge.|Segment verweist auf angeleitete Reflexion, Selbstbewertung oder strukturierte Debriefings.|„Portfolio-Einträge dienen der induzierten Reflexion.“|
|Ko-Produktion & kollaboratives Lernen|Partizipative Gestaltung, kollaborative Aufgaben, gemeinsame Wissenskonstruktion.|Kodieren, wenn Lehrende/Lernende gemeinsam Inhalte/Prozesse erzeugen.|„Kollaborative Aufgaben in Gruppen erzeugen geteilte Verantwortung.“|
|Feedback (Lehrende, Peer, automatisiert, LA)|Alle Feedbackschleifen, inkl. datenbasierter Rückmeldungen.|Segment thematisiert Wirkung oder Funktion von Feedback auf Lernqualität.|„Peer Feedback verbessert Selbstregulation.“|
|Learning Analytics & datenbasierte Reflexion|Einsatz von LA, Dashboards, Datenfeedback zur Qualitätsentwicklung.|Kodieren, wenn Daten genutzt werden, um Lernprozesse zu bewerten oder anzupassen.|„LA unterstützt als Mechanismus die Wirkgenese von Qualität.“|
|Simulation & szenariobasiertes Lernen|Digitale Simulationen, virtuelle Szenarien, AR/VR-gestützte Aufgaben.|Segment beschreibt Simulationen als Mechanismus zur Qualitätsentwicklung.|„Simulationen mit strukturiertem Debriefing fördern SRL und Reflexion.“|
|Community, soziale Interaktion & Identität|Mechanismen, die Zugehörigkeit, gemeinsame Identität oder Community-Building stärken.|Kodieren, wenn LMS sozialen Austausch, Community- oder Identitätsbildung unterstützt.|„Community-orientierte Foren erzeugen geteilte Verantwortung.“|
|Motivation & Engagement|Mechanismen, die Motivation, Engagement oder intrinsische Beteiligung auslösen.|Segment verweist auf motivationale Wirkungen (Gamification, sichtbarer Fortschritt).|„Gamifizierte LMS-Elemente steigern Engagement für Qualität.“|
|Kompetenzentwicklung & Professionalisierung|Langfristige Kompetenzaufbauprozesse (z. B. Coaching, professionelle Standards).|Kodieren, wenn LMS Mechanismen zur Professionalisierung oder Kompetenzentwicklung adressiert.|„Fortschrittsanzeigen, Tests und Portfolio fördern die Selbststeuerung.“|
|Qualitätsregulation & Governance|Mechanismen, die institutionelle Qualitätsentwicklung, Policies, Co-Regulation adressieren.|Segment thematisiert Governance, Steuerungsschleifen, Audit-Trails.|„Ko-Produktion ist zentrale Wirkfigur im Qualitätsmodell.“|
|Support & Infrastruktur|Unterstützende Strukturen (Coachings, technische Services, personelle Ressourcen).|Kodieren, wenn Supportmechanismen oder infrastrukturelle Voraussetzungen erwähnt werden.|„Coach-unterstützte Trainings steigern Completion und Lernleistung.“|
