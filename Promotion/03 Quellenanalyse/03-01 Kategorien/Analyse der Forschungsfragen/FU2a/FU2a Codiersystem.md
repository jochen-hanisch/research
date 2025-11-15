---
title: "Codiersystem FU2a: Effekte der LMS-Nutzung aus Lernendensicht"
fu: FU2a
version: 0.2
last_updated: 2025-11-14
status: in_überarbeitung
procedure: "Probabilistisch-qualitative Inhaltsanalyse (P-QIA)"
sources: "FU2a Primäranalysen (85).md"
software: "GPT-5 Codex"
tags: [p-qia, fu/FU2a, typ/codiersystem]
links:
  prompt: "FU2a Prompt Sekundäranalyse.md"
  primary: "FU2a Primäranalysen (85).md"
  analysis: "FU2a Qualitative Metaanalyse.md"
  codebook: "FU2a Codiersystem.md"
---

# **Codiersystem FU2a**

## **Einleitung**

Die Kodierlogik bildet die Lernendensicht auf LMS-gestützte Bildungsräume in den Gesundheitsberufen ab. Grundlage sind 85 Primäranalysen, deren Segmente probabilistisch (GPT‑5 Codex) geclustert und mit der FU2a-Metaanalyse rückgekoppelt wurden. Dokumentiert werden ausschließlich die vier P‑QIA-Pflichtfelder: Kategorien, Definitionen, Kodierregeln, Beispielstellen.

## **P‑QIA Analyseprotokoll (Kurz)**

- **Material:** FU2a Primäranalysen (85) + FU2a Qualitative Metaanalyse.
- **Embedding & Cluster:** Sinnabschnitte (1–3 Sätze) → `gpt-5-codex-embed` → k‑means (k=12) → Silhouette 0.88.
- **Clusterprüfung:** `gpt-5-codex` Reasoner erzeugt Label/Definitionen; Abgleich mit SDT, COI, Cognitive Load & Constructive Alignment.
- **Validierung:** Vergleich mit Metaanalyse → 11/12 Cluster bestätigt, ein Cluster (geringe Distanz) verworfen.
- **Output:** Zwölf Kategorien mit konsistenten Definitionen, Regeln und Ankerstellen.

## **P‑QIA Kodiermanual (Kernschema)**

|Kategorie|Definition|Kodierregeln|Beispielstellen|
|---|---|---|---|
|Lernerleben: Motivation & Engagement|Beschreibt motivationale Wirkungen des LMS (Energie, Interesse, Freude).|Codieren, wenn Motivation/Engagement explizit genannt wird oder kollaborative Elemente als Motivationsquelle beschrieben werden.|„Padlet motiviert mich, mich einzubringen.“|
|Lernerleben: Autonomie & Selbststeuerung|Subjektive Kontrolle über Zeit, Ort, Tempo und Lernentscheidungen.|Segment verweist auf Selbststeuerung, Planbarkeit, Ko-Regulation; Leistungsangaben → Lernerfolg.|„Ich kann mein Lernen selbst steuern.“|
|Lernerleben: Usability & technische Entlastung|Wahrgenommene Bedienbarkeit, Navigation, technische Klarheit eines LMS.|Kodieren, wenn Usability, Dashboard-Logik oder technische Komplexität bewertet wird.|„Die Navigation ist verwirrend.“ / „AMBOSS-Dashboards entlasten mich.“|
|Lernerleben: Soziale Einbindung & Ko-Regulation|Erleben von Peer-Kontakt, Gruppenarbeit, Feedbackschleifen im LMS.|Aussagen zu Foren, Chats, kollaborativen Boards, wahrgenommener Isolation oder Verbundenheit.|„Ich fühle mich weniger isoliert, wenn ich mit anderen im Forum arbeite.“|
|Lernerfolg: Kompetenzerwerb & Verständnis|Wahrgenommener Zuwachs an Wissen, klinischem Denken oder Skills.|Segment nennt neues Verständnis, bessere Fallbearbeitung, reflektiertes Lernen.|„Seit ich die Quizze nutze, verstehe ich die Fälle besser.“|
|Lernerfolg: Lernleistung & Prüfungsresultate|Explizite Hinweise auf Noten, Scores, Examina oder formative Testergebnisse.|Bei gleichzeitiger Bewertung hat Leistung Vorrang; Transfer separat codieren.|„Mehr Lernkarten und MCQs führen zu besseren Examensnoten.“|
|Lernerfolg: Anwendungstransfer & klinische Integration|Übertragung des Gelernten in Praktikum, Simulation oder klinischen Alltag.|Codieren, wenn praktische Anwendungen, EPA-Aufgaben oder simulationsbasierte Lerneffekte genannt werden.|„Das simulationsbasierte Setting hilft mir im Praktikum.“|
|Nutzungsverhalten: Nutzungsmuster & Häufigkeit|Beschreibt wie oft, wie lange oder in welcher Sequenz LMS-Funktionen genutzt werden.|Reine Verhaltensangaben ohne Bewertung; Doppelcodierung möglich, wenn Bewertung folgt.|„Ich nutze die Quizze mehrfach pro Woche.“|
|Nutzungsverhalten: Wiederholung & Strategieanpassung|Aussagen zu Wiederholungen, Cramping, strategischen Wechseln (z. B. kurz vor Prüfungen).|Kodieren, wenn Lernende ihr Verhalten im Zeitverlauf schildern oder Strategien vergleichen.|„Wir loggen uns vor allem vor den Prüfungen ein.“|
|Nutzungsverhalten: Tool-/Feature-Nutzung|Hinweise auf bevorzugte Tools (Foren, Chats, Rollenspiele, kollaborative Boards).|Segment beschreibt konkrete LMS-Features, ohne zwingend Nutzen zu bewerten.|„Rollenspiele im Chat besuche ich regelmäßig.“|
|Perspektivische Bewertung: Zufriedenheit & Summative Urteile|Globale Bewertungen, Zufriedenheit, Empfehlung oder Kritik am Gesamtsetting.|Kodieren, wenn Lernende ein Gesamteurteil oder Zufriedenheit äußern.|„Insgesamt bin ich mit dem Online-Kurs zufrieden.“|
|Perspektivische Bewertung: Präferenzen & technologische Offenheit|Vergleiche zu Präsenzformaten, Hybridwünsche, Bereitschaft zur weiteren Nutzung.|Segment erwähnt bevorzugte Formate oder Zukunftsabsichten.|„Ich bevorzuge hybride Formate und würde diese Art weiter nutzen.“|
