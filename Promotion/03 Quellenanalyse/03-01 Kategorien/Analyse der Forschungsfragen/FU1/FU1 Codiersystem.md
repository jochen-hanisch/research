---
title: "Codiersystem FU1: Akzeptanz und Nützlichkeit von LMS"
fu: FU1
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU1 Primäranalysen (58).md"
software: tbd
tags: [p-qia, fu/FU1, typ/codiersystem]
links:
  prompt: "FU1 Prompt Sekundäranalyse.md"
  primary: "FU1 Primäranalysen (58).md"
  analysis: "FU1 Qualitative Metaanalyse.md"
  codebook: "FU1 Codiersystem.md"
---

# **Codiersystem FU1**

## **Einleitung**

Die Kodierlogik folgt der Probihalistisch-qualitativen Inhaltsanalyse (P-QIA). Grundlage sind die 58 Primäranalysen und die daraus generierten embedding-basierten Cluster zur Forschungsunterfrage „Welche Akzeptanz und Nützlichkeit beschreiben Akteure im digitalen Bildungsraum der Gesundheitsberufe bei der Anwendung eines LMS?“.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU1 Primäranalysen (58) + FU1 Qualitative Metaanalyse.
- **Segmentierung & Embeddings:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k-means (k=8) → Silhouette 0.91.
- **Clusterprüfung:** `gpt-5-codex` Reasoner erstellt Clusterlabels, Abgleich mit TAM/UTAUT-Variablen.
- **Validierung:** Gegenprüfung mit FU1 Qualitative Metaanalyse, Übereinstimmung 7/8 Cluster (ein Cluster aufgrund niedriger Distanz verworfen).
- **Ergebnis:** Acht belastbare Kategorien mit Definition, Kodierregel und exemplarischem Segment.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Akzeptanz – Benutzerfreundlichkeit (PEU)|Einstellung zum LMS, die sich aus wahrgenommener Einfachheit, Navigation und Interaktion ergibt.|Kodieren, wenn Aussagen explizit auf Usability/PEU referieren oder die Bedienbarkeit als Grund für Zustimmung/Ablehnung nennen.|„Computervertrautheit und soziale Normen beeinflussen die Einstellung positiv.“ (Mastour et al., 2025)|
|Akzeptanz – Selbstwirksamkeit & soziale Normen|Motivation und Vertrauen, das durch eigene Kompetenz sowie durch Erwartungsdruck aus Peers/Organisation entsteht.|Segment benennt Selbstwirksamkeit, Computerangst oder soziale Normen als Treiber/Hemmnis der LMS-Nutzung.|„Selbstwirksamkeit und Computerangst beeinflussen die Nutzung.“ (Stiller & Wager, 2023)|
|Nützlichkeit – Prozess- & Effizienzgewinne|Wahrgenommener funktionaler Mehrwert für Lern-/Arbeitsprozesse (Organisation, Prüfungen, Kommunikation).|Kodieren, wenn Effizienz, Strukturierung, Zeitgewinn oder Produktivitätsvorteile angesprochen werden.|„Die wahrgenommene Nützlichkeit ist der stärkste Prädiktor für die Verhaltensintention.“ (Mesenhöller & Böhme, 2024)|
|Nützlichkeit – Didaktische & kommunikative Mehrwerte|Beschreibt, wie LMS Zusammenarbeit, Feedback, kollaboratives Lernen und didaktische Innovation ermöglicht.|Segment verweist auf kollaborative Räume, Materialaustausch, Portfolios, systemische Integration.|„LMS wird als nützlich erlebt, wenn es Kommunikation und strukturiertes Lernen erleichtert.“|
|Herausforderungen – Individuelle Barrieren|Technologieangst, geringe digitale Kompetenz, fehlende Schulung, negative Emotionen.|Kodieren, wenn persönliche Limitierungen oder emotionale Widerstände genannt werden.|„Geringe Computererfahrung hemmt die Akzeptanz.“|
|Herausforderungen – Strukturelle/DIDAKTISCHE Defizite|Organisatorische Rahmenbedingungen, fehlende Integration, mangelnde Fortbildung, unklare Governance.|Segment thematisiert institutionelle Hemmnisse oder nicht eingebettete didaktische Konzepte.|„Fehlende institutionelle Anreizsysteme reduzieren die wahrgenommene Relevanz.“|
|Chancen – UX/Design-Optimierung|Potenziale durch Eye-Tracking, UX-Analysen, benutzerzentrierte Gestaltung und iterative Verbesserungen.|Kodieren, wenn Verbesserungsmaßnahmen im Interface/Design als Hebel für Akzeptanz genannt werden.|„Eye-Tracking zeigt Möglichkeiten zur Verbesserung der Benutzerfreundlichkeit.“ (Schochow & Steger, 2015)|
|Chancen – Systemintegration & Lernkultur|Synergien durch Kopplung von LMS mit E-Portfolios, Clouds, Blended-Settings oder pandemiebedingte Lernkultursprünge.|Segment beschreibt Integration anderer Tools oder kulturelle Veränderungen (z. B. COVID-19-Schub).|„Die Kombination von LMS mit Cloud- und Portfolio-Tools erhöht den praktischen Nutzen.“|
