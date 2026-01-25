---
author: Jochen Hanisch-Johannsen
title: Projektbeschreibung Kompetenzentwicklung
Repository: https://github.com/jochen-hanisch/research/tree/main/Forschungsprojekte/Systemische%20Kompetenzentwicklung
created: 2026-01-25
updated: 2026-01-25
publish: true
published: 2026-01-25
tags:
---
created: 25.01.2026 | updated: 25.01.2026 | published: 25.1.2026 | [Austausch](https://github.com/jochen-hanisch/research/discussions) | [[Hinweise]]

# Projektbeschreibung: Systemische Kompetenzentwicklung

## Ausgangslage und Problemstellung

Kompetenzentwicklung in der Notfallsanitäterausbildung findet unter Bedingungen statt, die für **High Responsibility Teams (HRT)** typisch sind: Handlungen sind teils irreversibel, können Dritte gefährden, betreffen Leben und lassen sich im Einsatz nicht beliebig unterbrechen. In diesem Kontext reicht eine rein lineare oder rein wissensbasierte Betrachtung von Lernen nicht aus. Benötigt wird ein Modell, das **Kompetenz als dynamische, unsichere und von Kontextfaktoren beeinflusste Entwicklung** beschreibbar macht.

Als Arbeitsdefinition wird Kompetenz im HRT-Kontext verstanden als: *„die individuelle Bereitschaft, Operationen auf ausbildungsrechtlichen Grundlagen zu planen, deren Wirkung zu angemessenem und brauchbarem Handeln führt, um Transformationsbarrieren vom unerwünschten zum erwünschten Zustand zu überwinden.“* (Hanisch, 2023, S. 81)

## Zielsetzung

Ziel des Projekts ist die Entwicklung einer **Simulierten Kompetenzentwicklungsreferenz (Systemische Kompetenzentwicklung)**: einer Referenzkurve bzw. Referenzbandbreite, die eine **idealtypische Kompetenzentwicklung** von Auszubildenden (Notfallsanitäter) über die dreijährige Ausbildungsdauer abbildet – einschließlich Unsicherheiten, individueller Unterschiede und störender bzw. verstärkender Ereignisse.

Die Kompetenzentwicklung soll

- als **Orientierungs- und Vergleichsmaßstab** für Entwicklungsverläufe dienen (z.B. typische, günstige und ungünstige Verläufe),
- **kritische Phasen** und potenzielle Interventionspunkte sichtbar machen,
- und die Modellierung des **Bildungswirkgefüges** (Einfluss- und Wechselwirkungsstruktur zentraler Faktoren) unterstützen.

## Leitfragen

- Wie lässt sich Kompetenzentwicklung im HRT-Kontext als **zeitlicher Verlauf** auf einer Nominalskala (0–10) modellieren?
- Welche **Unsicherheiten und Streuungen** sind erwartbar und wie wirken sie auf die Interpretation von Entwicklungsständen?
- Welche Rolle spielen **Motivation, Neugier, individuelle Dispositionen** sowie **persönliche Ereignisse** im Verlauf?
- Welche **typischen Entwicklungsphasen** (z.B. Stagnation, Plateau, Motivationsknick, Prüfungsvorbereitungs-Effekt) lassen sich abbilden und analysieren?

## Methodischer Ansatz

Das Projekt nutzt eine Monte-Carlo-Simulation zur Erzeugung vieler plausibler Entwicklungsverläufe. Dadurch wird keine einzelne „wahre“ Kurve behauptet, sondern eine **Verteilung möglicher Verläufe** modelliert (Mittelwerte, Streuungen, Quantile, Best-/Worst-Cases).

### Zeitmodell und Darstellung

- Simulation in **monatlichen Intervallen** mit **quartalsweiser Aggregation** (4 Quartale pro Ausbildungsjahr).
- Gesamtdauer: **36 Monate / 12 Quartale**.
- Achsenkonvention: x = *Quartal*, y = *Niveau* (0–10).

### Variablen und Verteilungen (Auszug)

Die Modellparameter werden über geeignete Wahrscheinlichkeitsverteilungen abgebildet:
- **Weibull-Verteilung**: allgemeine Kompetenzentwicklung über die Zeit (flexible Lernkurvenformen).
- **Normalverteilung**: z.B. individuelle Lern-/Aufnahmefähigkeit, Selbstreflexion, Stressbewältigung, Anpassungsfähigkeit, Problemlösen/Entscheiden, Kooperation/Konfliktlösung, Anwendung standardisierter Verfahren.
- **Beta-Verteilung**: z.B. Motivation/Engagement, Kommunikations-/Teamfähigkeit, Empathie, Berücksichtigung persönlicher/situativer Umstände.
- **Poisson-Verteilung**: seltene **persönliche Ereignisse (PE)** während der Ausbildung mit positiven/negativen Effekten (z.B. familiäre, gesundheitliche, finanzielle, soziale Ereignisse).

### Wechselwirkungen (Beispiele)

Wechselwirkungen zwischen Variablen werden als Hypothesen modelliert, z.B.:
- höhere Lern-/Aufnahmefähigkeit → schnellere Aneignung standardisierter Verfahren,
- Stressstabilität → stabilere patientenorientierte Entscheidungen,
- Motivation → stärkere Anpassungsbereitschaft und Lernaktivität,
- Teamkommunikation → bessere Kooperation und Konfliktlösung.

## Empirisch informierte Beobachtungen als Modellannahmen

Aus Beobachtungen zur Notfallsanitäterausbildung werden dynamische Muster als Parameter-/Phasenlogik integriert:
- **Initiale Verzögerung**: Didaktik wird erst nach ca. **5–6 Quartalen** bewusst verstanden; bis dahin teils Stagnation/leichter Rückgang.
- **Verfestigung** nach ca. **6 Quartalen**.
- **Plateau** nach ca. **10 Quartalen**.
- **Motivationsknick** beim Übergang vom **2. zum 3. Ausbildungsjahr**.
- **Anstieg** in den letzten **ca. 2 Monaten** / den letzten Quartalen durch intensive Prüfungsvorbereitung.

## Auswertung und erwartete Ergebnisse

Aus den Simulationen werden u.a. abgeleitet:
- Referenzkurve/-band (Systemische Kompetenzentwicklung) inkl. Streuung (z.B. Median, Mittelwert, Standardabweichung, Quantile),
- Mustererkennung (z.B. Phasenwechsel, Wendepunkte, Knicke),
- Sensitivität/Robustheit gegenüber Parameteränderungen,
- Korrelations- und Wirkgefügeanalysen (Einflussstrukturen).

## Nutzen und Anwendungsfelder

- **Didaktische Planung**: Identifikation typischer kritischer Phasen und erwartbarer Dynamiken.
- **Diagnostik/Monitoring**: Einordnung individueller Verläufe relativ zur Systemische Kompetenzentwicklung (ohne vorschnelle Defizitdiagnosen).
- **Interventionsdesign**: Ableitung von Zeitfenstern mit besonders hohem Wirkpotenzial (z.B. vor/ nach Motivationsknick).
- **Forschung**: Explizite, testbare Hypothesen über Wirkzusammenhänge und Unsicherheiten.

## Abgrenzung

Die Systemische Kompetenzentwicklung ist eine **simulationsbasierte Referenz**, kein deterministischer Leistungsmaßstab. Sie liefert eine strukturierte, nachvollziehbare Modellierung von Entwicklung **unter Unsicherheit** und basiert auf Annahmen, die iterativ an Daten, Expertise und Plausibilitätsprüfungen rückgekoppelt werden.

## Nächste Schritte (Arbeitslogik)

1. Parameterkonsolidierung und Plausibilitätsprüfung.
2. Kalibrierung mit verfügbaren empirischen Hinweisen (wo möglich).
3. Ableitung und Dokumentation einer Systemische Kompetenzentwicklung-Referenzbandbreite (inkl. High-/Low-/Realperformer).
4. Iteration des Wirkgefüges und Ableitung von Interventionsempfehlungen.

## Praktische Nutzung (WebUI / Replikation)

- Die WebUI startet Simulationen und legt pro Run einen Ordner unter `Kompetenzentwicklung/web_runs/<Run-ID>/` an (CSV, HTML, Report, Log).
- Für die automatische GPT-Interpretation muss `OPENAI_API_KEY` gesetzt sein (empfohlen: macOS-Keychain pro Benutzer; keine Keys in Dateien speichern).
- Bei mehreren Rechnern/Benutzern mit gemeinsamem iCloud-Projektordner gilt: **Code & Daten** können geteilt werden, **Python-Pakete** müssen pro Rechner installiert sein (Homebrew-Python).
