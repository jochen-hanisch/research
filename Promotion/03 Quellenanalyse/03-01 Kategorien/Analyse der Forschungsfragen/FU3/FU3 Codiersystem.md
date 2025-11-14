---
title: "Codiersystem FU3"
fu: FU3
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU3 Primäranalysen (116).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU3, typ/codiersystem]
links:
  prompt: "FU3 Prompt Sekundäranalyse.md"
  primary: "FU3 Primäranalysen (116).md"
  analysis: "FU3 Qualitative Inhaltsanalyse.md"
  codebook: "FU3 Codiersystem.md"
---

# **Codiersystem FU3**

## **Einleitung**

FU3 adressiert die Konzeption und Merkmale eines LMS für Akteur*innen im digitalen Bildungsraum der Gesundheitsberufe. Die Kategorien wurden mittels P‑QIA aus 116 Primäranalysen und der FU3-Inhaltsanalyse abgeleitet.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU3 Primäranalysen (116) + FU3 Qualitative Inhaltsanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k‑means (k=15) → Silhouette 0.87.
- **Clusterprüfung:** `gpt-5-codex` Reasoner erzeugt Labels/Definitionen; Abgleich mit Didaktik-/Systemliteratur (COI, Constructive Alignment, UX, Systemarchitektur).
- **Validierung:** 13/15 Cluster stabil; zwei Cluster (niedrige Distanz) verworfen.
- **Output:** Dreizehn Kategorien mit Definition, Kodierregel und Beispielsegment.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Didaktisches Design – Lernaktivitäten & Aufgaben|Strukturierte Lernpfade, Aufgabenketten, problem- und fallbasierte Szenarien im LMS.|Kodieren, wenn Lehrende Lernaktivitäten oder Task-Designs beschreiben.|„Strukturierte Lernpfade, kollaborative Aufgaben, praxisnahe Szenarien.“|
|Didaktisches Design – Feedback & Prüfungsdesign|Online-Feedback, formative/summative Assessments, Rubrics, ePortfolios.|Segment benennt Feedbackmechanismen oder Prüfungsstrukturen.|„Quiz mit unmittelbarem Feedback zur Lernfortschrittskontrolle.“|
|Didaktisches Design – Motivation & Unterstützung (ARCS)|Motivationale Scaffolds, ARCS-Elemente, Multimedia-Unterstützung.|Kodieren, wenn Motivation, ARCS oder kognitive Unterstützungen thematisiert werden.|„Adaptives, ARCS-gestütztes Kursdesign steigert Motivation.“|
|Didaktisches Design – Kollaborative Lernarrangements|Förderung sozialer Interaktion, Peer-Feedback, Gruppenarbeit.|Segment beschreibt kollaborative oder konstruktivistische Settings.|„Kollaboratives Lernen über Lehrlabor³-Strukturen.“|
|Systemfunktionalität – Kommunikation & Kollaborationstools|Foren, Chats, Videokonferenzen, gemeinsame Dokumente.|Kodieren, wenn spezifische Kommunikations-/Kollaborationstools diskutiert werden.|„COI-basierte Flipped-Classrooms betonen Diskussionsforen.“|
|Systemfunktionalität – Adaptivität & Personalisierung|Learning Analytics, adaptive Pfade, Rule Engines.|Segment verweist auf datenbasierte Adaption oder Personalisierung.|„Learning Analytics-Dashboards steuern Lernpfade.“|
|Systemfunktionalität – Integration externer Tools|Einbindung von ePortfolios, Simulationen, Cloud-Services.|Kodieren, wenn Schnittstellen oder Tool-Kopplungen beschrieben werden.|„Kopplung von LMS mit ePortfolio-Systemen erhöht Sichtbarkeit von Artefakten.“|
|Nutzerzentrierung – Barrierefreiheit & Zugänglichkeit|WCAG, Usability, Mobile Fit, UI/UX.|Segment benennt Barrierefreiheit, UI oder Device-Kompatibilität.|„Responsives Design erleichtert mobile Nutzung.“|
|Nutzerzentrierung – Selbstregulation & Dashboarding|Unterstützung für Selbstmonitoring, Fortschrittsanzeigen.|Kodieren, wenn Dashboards, Analytics für Lernende oder Selbstregulation genannt werden.|„Fortschrittsanzeigen helfen bei der Lernplanung.“|
|Systemarchitektur – Sicherheit & Datenschutz|Policies, Rollenmodelle, Zugriffskontrolle, Compliance.|Segment thematisiert Sicherheit, DSGVO, Governance.|„Gesicherte Rollen und Rechte sind Voraussetzung für klinische Datenintegration.“|
|Systemarchitektur – Interoperabilität & Standards|APIs, LTI, IMS, technologische Kopplung.|Kodieren, wenn Standards oder Schnittstellen erwähnt werden.|„LTI-Standards ermöglichen Einbindung externer Simulationen.“|
|Systemarchitektur – Skalierbarkeit & Performance|Leistungsfähigkeit bei großen Nutzerzahlen, Ausfallsicherheit.|Segment beschreibt Infrastruktur, Cloud, Lastverteilung.|„Cloudbasierte Bereitstellung garantiert Skalierbarkeit im Klinikverbund.“|
|Systemintegration – Organisationales Embedding|Einbettung ins Curriculum, Supportstrukturen, Governance.|Kodieren, wenn LMS in Programme, Rollen oder Institutionen eingebettet wird.|„Curriculare Verankerung und Supportteams sichern Nachhaltigkeit.“|
