\newpage

## Software und Quellcode (Reproduzierbarkeit) {#sec:A-15}

#todo revision: Anhang A-15 final prüfen (DOI/Version/Artefakte konsistent)

Dieser Anhang dokumentiert die in der Dissertation verwendeten Softwareartefakte als Reproduzierbarkeits- und Nachvollziehbarkeitsspur. Er beschreibt, welche Quellcodes eingesetzt wurden, welche Ergebnisartefakte erzeugt werden und welche Randbedingungen die Reproduzierbarkeit begrenzen. Die Software wird als Teil der methodischen Dokumentationslogik geführt und ergänzt die Textargumentation in Kapitel \hyperref[sec:Simulation-Kompetenzentwicklung]{4.4} sowie die methodenkritische Einordnung in Abschnitt \hyperref[sec:Methodenkritik-Absicherung]{4.5.2}. [@hanisch-johannsen_simulation_2025; @hanisch-johannsen_tei-bildungswirkgefuge_2025]

**Artefakte und Referenzen**

- **Simulation des Bildungswirkgefüges (Python):** Zenodo-Softwareartefakt zur simulationsgestützten Modellierung und Indikatorik (Bildungswirkfaktor $\nu(t)$, Bildungswirkindikator $\iota(t)$, Unsicherheitswert $C$). [@hanisch-johannsen_simulation_2025]
- **TEI-Bildungswirkgefüge (Python):** Zenodo-Softwareartefakt zur TEI-gestützten Anwendung/Integration im Kontext der Arbeit. [@hanisch-johannsen_tei-bildungswirkgefuge_2025]

**Quellenbasis Monte‑Carlo (PDF‑Seitenbezug)**

#todo revision: BibKeys der Monte‑Carlo‑Grundlagenliteratur in `Literaturverzeichnis.bib` prüfen und dann diese Seitenbezüge als Zitierungen (mit BibKey) in A‑15 und 4.4/4.5 einarbeiten

Die folgenden Seitenangaben beziehen sich auf die in den Zotero-Speichern hinterlegten PDFs und dienen als Prüfspur für die im Text verwendeten Monte‑Carlo‑Bezüge:

- Binder (2017): PDF S. 2–3 (Zufallszahlen/RNG; Stichprobenlogik), PDF S. 5–6 (Random Walk/Phasenraum), PDF S. 10 (Averaging über unabhängige Runs).
- Earl & Deem (o. J.): PDF S. 3–4 (random sampling; Metropolis‑Logik), PDF S. 8 (Lauflänge/Run‑Heuristik), PDF S. 10 (Varianz und Autokorrelation in Stichproben).
- Gleißner & Wolfrum (2019): PDF S. 7 (Varianz‑Kovarianz‑Ansatz und simulationsbasierte Risikoaggregation), PDF S. 29 (Random‑Walk‑Bezug in Modellierung von Risikofaktoren).
- Pudrovska & Anishkin (2015): PDF S. 1–4 (Einordnung der Monte‑Carlo‑Simulation; methodischer Zugriff), PDF S. 9 (Verteilungsannahmen), PDF S. 14–16 (Monte‑Carlo‑Simulationen und Ergebnisinterpretation).
- Rigopouli et al. (2025): PDF S. 1–3 (MCMC‑Rahmung im Bildungskontext), PDF S. 6 (Einordnung konventionelles Monte‑Carlo und Markov‑Chain‑Monte‑Carlo; Abhängigkeit der Ziehungen).
- Shonkwiler & Mendivil (2024): PDF S. 7 (Central‑Limit‑Theorem‑Bezug), PDF S. 18 (Beispielcode: Pseudorandom‑Samples; Stichprobenlogik).
- Voelkle & McKnight (2012): PDF S. 7–8 (Iterationszahl und Variabilität), PDF S. 7 (random sampling für Simulationsbedingungen).
- Theis & Kernbichler (2002): S. 2 (Definition Monte‑Carlo als Methodengruppe), S. 5–6 (Erwartungswert/Varianz/Standardabweichung), S. 7 (Samples/Laufzahl; Konvergenzbezug), S. 9 (Zufallszahlen/Zufallsgeneratoren), S. 20 (Iterationen/Simulationsablauf).
- Kany (2024): Buchseiten S. 49–50 (random draw; Monte‑Carlo‑Ablauf; Beispielcode/Standardabweichung).

**Funktionsüberblick: Was der Code macht**

#todo revision: Funktionsbeschreibung gegen die finalen Artefakte prüfen (A-15)

Die Simulation implementiert ein quartalsbasiertes Dynamikmodell der Kompetenzentwicklung, das mehrere Einflusskomponenten (u.a. Neugier/Motivation, persönliche Ereignisse, Paradigmen-Parameter) als gekoppelten Update-Schritt führt. Die Auswertung erzeugt Monte‑Carlo‑Verteilungsfamilien von Verläufen sowie abgeleitete Kennwerte und Indikatoren (u.a. $\Delta E$, $\Delta K$, $\nu(t)$, $\iota(t)$, $C$) zur Interpretation von Dynamikformen, Kippstellen und Zeitfenstern. Die Artefakte umfassen Visualisierungen und tabellarische Exporte, die als Modellspur in die Argumentation rückgebunden werden. [@hanisch-johannsen_simulation_2025; @theis_grundlagen_2002, S. 2 und 7; @uskov_teaching_2024, S. 49–50]

Die TEI-gestützte Anwendung erweitert diese Logik um einen Import-/Mapping-Schritt: Aus TEI-Daten (Excel/CSV) werden heuristische Profil- und Parameterannahmen abgeleitet, die anschließend in die Simulation bzw. in die Auswertungsketten eingespeist werden. Auch hier werden Auswertungen, Visualisierungen und Exporte erzeugt; die Verwendung bleibt an die im Haupttext ausgewiesene methodische Rolle gebunden. [@hanisch-johannsen_tei-bildungswirkgefuge_2025; @theis_grundlagen_2002, S. 2 und 9; @uskov_teaching_2024, S. 49]

**Reproduktionshinweise**

Die folgenden Hinweise sind als Minimalprotokoll gedacht. Sie beschreiben, welche Schritte typischerweise erforderlich sind, um die in der Dissertation beschriebenen Ergebnisartefakte (z.B. Abbildungen, Kennwerte, Tabellen) auszuführen bzw. erneut zu erzeugen. [@hanisch-johannsen_simulation_2025; @hanisch-johannsen_tei-bildungswirkgefuge_2025]

- **Umgebung:** Python 3.x, Standardbibliothek plus die im jeweiligen Zenodo-Artefakt dokumentierten Abhängigkeiten. [@hanisch-johannsen_simulation_2025; @hanisch-johannsen_tei-bildungswirkgefuge_2025]
- **Ausführung:** Start über den in den Artefakten dokumentierten Einstiegspunkt (z.B. `python simulation-bildungswirkgefuege.py`). [@hanisch-johannsen_simulation_2025]
- **Determinismus:** Bei Monte‑Carlo‑Anteilen wird ein Seed/Random-State dokumentiert, da Lauf-zu-Lauf-Varianz in Verläufen sichtbar werden kann und als Teil der Modellspur transparent zu führen ist. [@theis_grundlagen_2002, S. 9; @uskov_teaching_2024, S. 49; @rakhlin_stability_nodate, Seite 1-2]
- **Outputs:** Ergebnisartefakte sind grafische Verläufe (Monte‑Carlo‑Familien, $\nu(t)$/$\iota(t)$) sowie Kennwert-/Tabellenausgaben, die als Modellspur interpretiert werden. [@hanisch-johannsen_simulation_2025; @theis_grundlagen_2002, S. 7; @uskov_teaching_2024, S. 50]

**Reproduzierbarkeitsgrenzen (methodische Einordnung)**

Die Nachvollziehbarkeit ist an mehrere Bedingungen gekoppelt, die im Sinne einer methodischen Transparenz als Begrenzungen dokumentiert werden. [@low_data_2023]

- **Parametrisierung und Annahmen:** Die Simulation operiert mit modellinternen Koppelungs- und Verteilungsannahmen. Abweichende Parametrierungen erzeugen veränderte Dynamikformen; daraus folgt eine Sensitivität der Ergebnisse gegenüber Setzungen. [@hanisch-johannsen_simulation_2025]
- **Abhängigkeiten/Versionen:** Python- und Paketversionen beeinflussen Laufverhalten und Plot-Outputs; die Reproduzierbarkeit profitiert von klar dokumentierten Versionsständen. [@low_data_2023]
- **Zugriff/Verfügbarkeit:** Die Softwareartefakte sind über Zenodo referenzierbar, der Zugriff kann als geschlossen geführt sein. Damit wird die Zitierfähigkeit gesichert, die unmittelbare Replikation durch Dritte hängt vom gewährten Zugriff ab. [@hanisch-johannsen_simulation_2025; @hanisch-johannsen_tei-bildungswirkgefuge_2025]
- **Interpretationsrahmen:** Die erzeugten Verläufe sind Modellspuren. Ihre Einordnung bleibt an die in Kapitel \hyperref[sec:Simulation-Kompetenzentwicklung]{4.4} formulierte Rolle als formalisierte Verdichtung und an die methodenkritische Begrenzung in Abschnitt \hyperref[sec:Methodenkritik-Absicherung]{4.5.2} gebunden. [@hanisch-johannsen_simulation_2025]
