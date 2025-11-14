---
title: "Codiersystem FU7"
fu: FU7
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU7 Primäranalysen (8).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU7, typ/codiersystem]
links:
  prompt: "FU7 Prompt Sekundäranalyse.md"
  primary: "FU7 Primäranalysen (8).md"
  analysis: "FU7 Qualitative Inhaltsanalyse.md"
  codebook: "FU7 Codiersystem.md"
---

# **Codiersystem FU7**

## **Einleitung**

FU7 modelliert Inputs und Strategien, die LMS-Kausalgesetze erweitern. Das Codiersystem spiegelt ausschließlich die P‑QIA-Kernstruktur auf Basis der acht Primäranalysen wider.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU7 Primäranalysen (8) + FU7 Qualitative Inhaltsanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–2 Sätze, hohe Verdichtung) → `gpt-5-codex-embed` → k‑means (k=10) → Silhouette 0.93.
- **Clusterprüfung:** `gpt-5-codex` Reasoner; Abgleich mit Grounded-Theory-Cluster (didaktische Inputs, technologische Inputs, organisationale Inputs, Strategien, Wirkungen).
- **Validierung:** 9/10 Cluster stabil; ein Cluster (geringe Distanz) zusammengeführt.
- **Output:** Neun Kategorien (3 Inputgruppen, 3 Strategien, 3 Wirkklassen) mit Definition, Kodierregel und Beispiel.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Didaktische Inputs (DI)|Aktivierende Lernmethoden (PBL, Jigsaw, Simulation, Microteaching) und heutagogische Prinzipien.|Kodieren, wenn Primärtext High-Impact-Lehrstrategien oder selbststeuernde Didaktik als Input beschreibt.|„High-Impact Teaching Strategies: PBL, Jigsaw, Simulation, Microteaching.“|
|Technologische Inputs (TI)|KI-Analytics, Adaptive KI-Modelle, Wearable IoT, Reservoir-Computing, Strukturlernen.|Segment benennt KI/IoT/OSL/POD-ESN als Input für LMS-Wirkgefüge.|„Wearable IoT + Edge AI liefern Echtzeitdaten für Lernanpassungen.“|
|Organisationale Inputs (OI)|Hybride Programme, Change-Prozesse, interprofessionelle Kooperation.|Kodieren, wenn BIP, Supportstrukturen oder organisatorische Kontexte als Input genannt werden.|„Blended Intensive Programmes stabilisieren hybride Lernkulturen.“|
|Didaktische Strategien (ST-DIDAKT)|Aktivierende Lehrarchitekturen, Microteaching, kollaborative Szenarien.|Segment beschreibt den Einsatz von HITS, Role-Play, Flipped/Hybrid als Strategie.|„Aktivierende Lehrformate (PBL, Simulation, Microteaching).“|
|Technologische Strategien (ST-TECH)|Algorithmische Planung (OSL), Echtzeitmodellierung (POD-ESN), KI-basierte Entscheidungsunterstützung, Systemintegration.|Kodieren, wenn KI/OSL/Reservoir-Modelle als strategische Verfahren dargestellt werden.|„Online-Structure-Learning aktualisiert Kausalstrukturen aus Nutzerdaten.“|
|Organisationale Strategien (ST-ORG)|Internationale Kooperation, Krisenanpassung, Multi-Layer-Systemarchitektur.|Segment verweist auf BIP, interprofessionelle Teams oder systemische Implementationsstrategien.|„Hybride Programme erhöhen Resilienz und Systemstabilität.“|
|Wirkung: Erweiterte Beobachtbarkeit|Neue Beobachtungsformen (KI-Analytics, Wearables) erzeugen erweiterte Kausalgesetze.|Kodieren, wenn Datenströme/Diagnostik die Kausalinterpretation verändern.|„Wearables erzeugen kontinuierliche Datenströme → neue Beobachtungsmodi.“|
|Wirkung: Adaptive Systemsteuerung|Laufende Strukturaktualisierung, Echtzeit-Anpassung von Lernpfaden.|Segment beschreibt dynamische Steuerung (POD-ESN, adaptive Dashboards).|„Reservoir-Computing aktualisiert Systemparameter und verhindert Modellkollaps.“|
|Wirkung: Systemische Resilienz & Interprofessionalität|Robustheit, internationale Kooperation, interprofessionelle Kompetenzgewinne.|Kodieren, wenn hybride Programme oder Kooperationen als Wirkung/Outcome benannt werden.|„BIP steigern interprofessionelle Kompetenz und Systemrobustheit.“|
