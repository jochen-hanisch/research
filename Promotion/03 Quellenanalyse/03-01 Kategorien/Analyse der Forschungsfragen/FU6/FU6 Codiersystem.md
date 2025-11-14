---
title: "Codiersystem FU6"
fu: FU6
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU6 Primäranalysen (65).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU6, typ/codiersystem]
links:
  prompt: "FU6 Prompt Sekundäranalyse.md"
  primary: "FU6 Primäranalysen (65).md"
  analysis: "FU6 Qualitative Inhaltsanalyse.md"
  codebook: "FU6 Codiersystem.md"
---

# **Codiersystem FU6**

## **Einleitung**

FU6 untersucht LMS als Kompetenzerwerbssystem. Die P‑QIA verdichtet 65 Primäranalysen zu vier Kompetenzdimensionen (K/F/E/B) und ihren Unterkategorien.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU6 Primäranalysen (65) + FU6 Qualitative Inhaltsanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k‑means (k=12) → Silhouette 0.89.
- **Clusterprüfung:** `gpt-5-codex` Reasoner; Abgleich mit handlungstheoretischem Kompetenzmodell (Fach, Sozial, Selbst, Methoden) sowie LMS-spezifischen Designs.
- **Validierung:** 10/12 Cluster konsistent; zwei Cluster zusammengeführt.
- **Output:** Zehn Kategorien (Kompetenzarten, LMS-Elemente, Evaluation, Bedingungen) mit Definition, Regel und Beispiel.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Kompetenz: Fachkompetenz (K-FACH)|Domänenspezifisches Wissen/Fertilität (z. B. Weaning-Kompetenz, klinisches Denken).|Kodieren, wenn Lernende/Lehrende fachliche Urteile oder Wissenszuwächse beschreiben.|„MedMicroMaps verbessern infektionsmedizinisches Denken.“|
|Kompetenz: Handlungskompetenz (K-HAND)|Angewandte klinische Entscheidungen, situatives Handeln, Patientensicherheit.|Segment verweist auf Simulation, VR, praxisnahes Problemlösen.|„Simulationen verbessern die Reaktion in Notfallsituationen.“|
|Kompetenz: Sozialkompetenz (K-SOZ)|Teamarbeit, Kommunikation, interprofessionelle Kooperation.|Kodieren, wenn soziale Interaktion oder Koordination als Kompetenzgewinn genannt wird.|„Gruppenaufgaben fördern abgestimmtes Handeln im Team.“|
|Kompetenz: Selbst-/Lernkompetenz (K-SELBST)|Selbstregulation, Reflexion, Lernplanung, Selbstwirksamkeit.|Segment benennt Planungs-, Reflexions- oder Ko-Regulationsfähigkeiten.|„Portfolios regen Selbstevaluation und Selbststeuerung an.“|
|Kompetenz: Digitale Kompetenz (K-DIGI)|Sicherer Umgang mit digitalen Tools, Medien, Plattformen.|Kodieren, wenn digitale Lehr-/Lernkompetenz explizit genannt wird.|„Microteaching im digitalen Raum steigert berufspädagogische Digitalkompetenz.“|
|Kompetenzfördernde LMS-Elemente|Interaktive Module, Simulationen, kollaborative Werkzeuge, Feedback, ePortfolios, Learning Analytics.|Segment beschreibt ein LMS-Feature als Mechanismus für Kompetenzentwicklung.|„Interaktive Lernmodule und Fallvignetten fördern klinisches Denken.“|
|Evaluation & Nachweise|Prä/Post-Tests, OSCE, Portfolio-Bewertungen, LA-basierte Evidenz.|Kodieren, wenn Kompetenzzuwachs empirisch evaluiert wird.|„Signifikante Leistungszuwächse nach simulationsbasiertem Training.“|
|Bedingungen: Technische Infrastruktur|Stabilität, Performanz, Geräteverfügbarkeit als Voraussetzung.|Segment thematisiert Infrastruktur als Einflussfaktor.|„Interaktive Formate scheitern bei fehlender VR-Hardware.“|
|Bedingungen: Didaktisch-systemische Einbettung|Curriculare Verankerung, Support, Rollenmodelle.|Kodieren, wenn organisatorische Einbettung oder Coaching Voraussetzung ist.|„LMS wirkt nur, wenn digitale Lernaktivitäten curriculär verankert sind.“|
|Bedingungen: Motivation & Lernkultur|Einstellungen, Lernklima, Reflexions- oder Feedbackkultur.|Segment verweist auf motivationale oder kulturelle Faktoren, die Kompetenzerwerb moderieren.|„Community-Orientierung und Feedbackkultur verstärken Lernbereitschaft.“|
