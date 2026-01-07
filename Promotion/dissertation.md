---
geometry: "left=2.5cm, right=2.5cm, top=2.5cm, bottom=1.0cm, includefoot, footskip=1.5cm"
papersize: a4
latex_engine: xelatex
lang: de-DE
csquotes: true
bibliography: "08 Metaquellen/Matadaten/Literaturverzeichnis.bib"
csl: "08 Metaquellen/Matadaten/apa-no-initials.csl"
table-placement: [htbp]
header-includes:
  - \usepackage{fontspec}
  - \usepackage{newunicodechar}
  - \newunicodechar{�}{?}
  - \newunicodechar{→}{$\rightarrow$}
  - \usepackage{unicode-math}
  - \setmainfont{STIX Two Text}
  - \setsansfont{STIX Two Text}
  - \setmathfont{STIX Two Math}
  - \usepackage{microtype}
  - \UseMicrotypeSet[protrusion]{basicmath}
  - \usepackage{setspace}
  - \onehalfspacing
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \setlength{\headheight}{14pt}
  - \fancyhead[L]{\nouppercase{\leftmark}}
  - \fancyhead[R]{\nouppercase{\rightmark}}
  - \fancyfoot[C]{\thepage}
  - \renewcommand{\sectionmark}[1]{\markboth{#1}{}}
  - \renewcommand{\subsectionmark}[1]{\markright{#1}}
  - \usepackage{titlesec}
  - \titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
  - \usepackage{hyperref}
  - \usepackage{csquotes}
  - \addto\captionsngerman{\renewcommand{\contentsname}{Inhaltsverzeichnis}}
  - \addto\captionsngerman{\renewcommand{\listtablename}{Tabellenverzeichnis}}
  - \addto\captionsngerman{\renewcommand{\listfigurename}{Abbildungsverzeichnis}}
  - \addto\captionsngerman{\renewcommand{\figurename}{Abbildung}}
  - \addto\captionsngerman{\renewcommand{\tablename}{Tabelle}}
  - \usepackage{graphicx}
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{placeins}
  - \usepackage{longtable}
  - \usepackage{tocloft}
  - \usepackage{tabularx}
  - \usepackage{pdflscape}
  - \usepackage{imakeidx}
  - \makeindex
  - \usepackage{glossaries}
  - \makeglossaries
  - \usepackage{tikz}
  - \usetikzlibrary{positioning}
  - \usetikzlibrary{positioning}
  - \usetikzlibrary{arrows.meta}
  - \usetikzlibrary{shapes.geometric}
  - \usetikzlibrary{fit}
  - \usepackage[singlelinecheck=false]{caption}
  - \captionsetup[figure]{font=small, labelfont=bf, skip=4pt, justification=justified, format=plain}
  - \captionsetup[table]{font=small, labelfont=bf, skip=10pt, justification=justified, format=plain}
  - \providecommand*{\figureautorefname}{Abbildung}
  - \providecommand*{\tableautorefname}{Tabelle}
  - \providecommand*{\equationautorefname}{Gleichung}
  - \newcommand{\figsubcaption}[1]{{\begingroup\small\setstretch{1.0}#1\endgroup}}
  - \newcommand{\tabsubcaption}[1]{{\begingroup\small\setstretch{1.0}#1\endgroup}}
  - \usepackage{draftwatermark}
  - \SetWatermarkText{Arbeitsversion}
---

\pagestyle{plain}

```{=latex}
\begin{titlepage}
\thispagestyle{empty}
\begin{center}

{\Large DISSERTATION}\\[2.5cm]

{\bfseries\LARGE Wirkgefüge im digitalen Bildungsraum}\\[0.6cm]

{\large Eine Untersuchung der Merkmale, Effekte, Mechanismen und Reaktionen von Learning-Management-Systemen am Beispiel der Lehre in Gesundheitsberufen}\\[1.2cm]

{\bfseries\large Interactional Frameworks in the Digital Educational Space}\\[0.6cm]

{\large An Exploration of the Characteristics, Effects, Mechanisms, and Responses of Learning Management Systems Using the Example of Healthcare Education}\\[1.2cm]

{\large zur Erlangung des akademischen Grades}\\[0.5cm]
{\large Doctor rerum medicinalium (Dr. rer. medic.)}\\[1.2cm]

{\large vorgelegt der Medizinischen Fakultät}\\[0.2cm]
{\large Charité – Universitätsmedizin Berlin}\\[2.0cm]

{\large von}\\[0.2cm]
{\large Jochen Hanisch-Johannsen M.A., M.A.}\\[1.8cm]

\vfill

{\large Erstbetreuung: Prof. Dr. med. Sebastian Spethmann}\\[0.2cm]
{\large Zweitbetreuung: Prof.in Dr.in phil. Eva Cendon}\\[0.6cm]
{\large Datum der Promotion: dd.mm.yyyy}\\

\end{center}
\end{titlepage}
```

# Inhaltsverzeichnis
\renewcommand{\contentsname}{}
\tableofcontents

\newpage

# Tabellenverzeichnis

\renewcommand{\listtablename}{}
\listoftables

\newpage

# Abbildungsverzeichnis

\renewcommand{\listfigurename}{}
\listoffigures

\newpage

# Abkürzungsverzeichnis {#sec:abkuerzungsverzeichnis}

| Abkürzung       | Bedeutung                                                               |
| --------------- | ----------------------------------------------------------------------- |
| AOI             | Area of Interest                                                        |
| CES             | Collaborative Learning Ecosystem                                         |
| CoP             | Community of Practice                                                    |
| ET              | Eye-Tracking                                                            |
| E-Portfolio     | Digitales Portfolio                                                     |
| FU              | Forschungsunterfrage (FU1–FU7)                                          |
| KI              | Künstliche Intelligenz                                                  |
| KH              | Kernhypothese                                                           |
| LMS             | Learning-Management-System                                              |
| LXP             | Learning Experience Platform                                            |
| mdaCV           | Mehrdimensional-analytische Clustervalidierung                          |
| MOOC            | Massive Open Online Course                                              |
| HRT             | High Responsibility Teams                                               |
| NH              | Nebenhypothese                                                          |
| NotSan-APrV     | Ausbildungs- und Prüfungsverordnung für Notfallsanitäter:innen          |
| NotSanG         | Notfallsanitätergesetz                                                  |
| NotSan / NFS    | Notfallsanitäter:in                                                     |
| PE              | Persönliche Ereignisse                                                  |
| PEE             | Persönlicher Erfolg extern                                              |
| PFE             | Persönlicher Fehlschlag extern                                          |
| PFV             | Persönlicher Fortschritt variabel                                       |
| PGV             | Persönliches Großerlebnis variabel                                      |
| PLE             | Persönlicher Leistungseinbruch                                          |
| PSE             | Persönlicher Stabilitätserfolg                                          |
| EpiGesAusbSichV | Verordnung zur Sicherung der Ausbildungen in den Gesundheitsfachberufen |
| TEI             | Training Evaluation Inventory                                           |
| P-QIA           | Probabilistisch-Qualitative Inhaltsanalyse                              |
| SC              | Silhouette-Score                                                        |

Ausführliche Begriffsdefinitionen finden sich im \hyperref[sec:A-1]{Verzeichnis zentraler Begriffe} im Anhang.

\newpage

# Symbolverzeichnis {#sec:symbolverzeichnis}

| Symbol | Beschreibung |
| --- | --- |
| $\beta$ | Standardisierter Regressionskoeffizient. |
| $\Delta$ | Effekt- bzw. Varianzanteil eines Modellfaktors. |
| $\Delta E$ | Emotionale Unsicherheit innerhalb der Kompetenzentwicklung. |
| $\Delta K$ | Kognitive Unsicherheit innerhalb der Kompetenzentwicklung. |
| $\epsilon$ | Epistemische Verlustfunktion zur Bewertung der Integrität der mdaCV (Gl.~\eqref{eq:verlust}). |
| $\iota$ | Bildungswirkindikator; Steigung des Bildungswirkfaktors. |
| $k$ | Anzahl der Cluster im k-Means-Algorithmus. |
| $\nu$ | Bildungswirkfaktor als aggregiertes Maß der Kompetenzwirkung. |
| $C$ | Dynamischer Unsicherheitswert zur Koppelungsprüfung zwischen $\Delta E$ und $\Delta K$ (Gl.~\eqref{eq:bildungswirk_c}). |
| $r$ | Korrelationskoeffizient (hier: Korrelation zwischen $\Delta E$ und $\Delta K$). |
| $\sigma$ | Standardabweichung (hier: Streuung von $\Delta E$ bzw. $\Delta K$). |
| $S$ | Silhouette-Score als Maß der Clusterdifferenzierung. |
| $t$ | Zeitvariable der Dynamikmodelle. |

\newpage

# Formelverzeichnis {#sec:formelverzeichnis}

| Gleichung | Beschreibung |
| --- | --- |
| \eqref{eq:verlust} | Epistemische Verlustfunktion zur Bewertung der Integrität der mehrdimensional-analytischen Clustervalidierung (mdaCV). |
| \eqref{eq:kmeans} | Zielfunktion des k‑Means-Algorithmus zur Minimierung der quadrierten Abstände der Datenpunkte zu ihren jeweiligen Clusterzentren. |
| \eqref{eq:bildungswirkfaktor} | Bildungswirkfaktor $\nu(t)$ als zeitabhängiges Aggregatmaß aus emotionaler und kognitiver Unsicherheit ($\Delta E(t)\cdot\Delta K(t)$). |
| \eqref{eq:bildungswirkindikator} | Bildungswirkindikator $\iota(t)$ als zeitliche Änderungsrate des Bildungswirkfaktors ($d\nu(t)/dt$). |
| \eqref{eq:bildungswirk_c} | Dynamischer Unsicherheitswert $C$ zur Koppelungsprüfung zwischen $\Delta E$ und $\Delta K$ (Korrelationsstärke und Streuung). |

\newpage

# Hinweise

Diese Hinweise gewährleisten durch einheitliche und transparente Vorgaben die wissenschaftliche Nachvollziehbarkeit und vermitteln Lesenden ein Verständnis der angewandten Prinzipien. Der gewählte APA-Zitationsstil (7. Ausgabe) ermöglicht eine standardisierte Referenzierung und trägt zur internationalen Anschlussfähigkeit der Arbeit bei. Die Prinzipien der gendergerechten Sprache spiegeln den gesellschaftlichen Wandel wider und fördern die Inklusion in der akademischen Kommunikation. Die kontextbezogene Begriffsdefinition verortet zentrale Konzepte präzise innerhalb des spezifischen Diskussionsrahmens und minimiert Missverständnisse.

Damit wird eine Grundlage für die Struktur und Verständlichkeit der Arbeit geschaffen. Die Darstellung der Zitations- und Sprachstandards sowie der Begriffsverwendung stärkt die methodische Stringenz, die inhaltliche Kohärenz und die wissenschaftliche Qualität.

## Hinweis zum Zitationsstil

Der Zitationsstil dieser Arbeit basiert auf der 7. Ausgabe der @american_psychological_association_style_2024. Zur Verwaltung der Zitate wird die Software Zotero (Version 7.0.29) verwendet, alle Referenzen sind als BibLaTex-Zitierschlüssel angelegt und in der PDF-Fassung von Referenzen zu Text umgewandelt worden.

Innerhalb der Zitationen werden diese Regeln angewendet:

- Direkte Zitate: Die Quellenangabe erfolgt unmittelbar nach dem wörtlichen Zitat.
- Indirekte Zitate innerhalb eines Satzes: Die Quellenangabe bezieht sich auf den gesamten Satz, der durch Satzzeichen abgeschlossen ist.
- Indirekte Zitate in einem Nebensatz: Die Quellenangabe bezieht sich auf den betreffenden Satzteil.
- Indirekte Zitate am Ende eines Absatzes: Die Quellenangabe bezieht sich auf den gesamten Absatz.
- Indirekte Zitate vor einer Aufzählung: Die Quellenangabe bezieht sich auf die gesamte Aufzählung.
- Mehrere indirekte Zitate: Die Quellenangaben beziehen sich auf die Reihenfolge der Argumentation.

Auslassungen sind durch „(…)“ dargestellt und Ergänzungen innerhalb von Zitaten erscheinen in eckigen Klammern „[…; Anmerkung des Autors]“, während Hervorhebungen durch den Autor mit „[Hervorhebung durch den Autor]“ kenntlich gemacht werden. Übersetzungen, die dem Original wörtlich entsprechen, werden wie direkte Zitate behandelt und mit der Anmerkung „(Übersetzung durch den Autor)“ versehen.

Sofern in den Abbildungsunterschriften nichts anderes angegeben ist, stammen alle Abbildungen aus eigener Darstellung und basieren auf den in dieser Arbeit erhobenen, ausgewerteten oder rekonstruierten Daten.

## Hinweis zum Sprachstil

Die Arbeit folgt den Prinzipien einer gendergerechten Sprache. Orientierung bietet der Vorschlag von @koehler_empfehlung_2021, dass „die Gleichstellung aller Geschlechter und die Anerkennung aller Identitätsgeschlechter“ [@koehler_empfehlung_2021, Seite 2] ihren sprachlichen Ausdruck innerhalb der scientific community finden muss.

Hieraus ergeben sich folgende, stilentsprechende Implikationen:

- Inklusion und Diversität: Alle Geschlechter und Identitäten werden sprachlich anerkannt und einbezogen.
- Gleichstellung: Sprachliche Gleichbehandlung fördert die Gleichstellung der Geschlechter in der Wissenschaft.
- Wissenschaftliche Relevanz: Gendergerechte Sprache reflektiert den gesellschaftlichen Wandel und wird in der scientific community zunehmend anerkannt.
- Lesbarkeit und Verständlichkeit: Gendergerechte Sprache erhöht bei bewusster Formulierung die Verständlichkeit.
- Sensibilisierung: Gendergerechte Sprache sensibilisiert für das Thema der Geschlechtergerechtigkeit in akademischen Texten.
- Sprachliche Präzision: Geschlechtsneutrale Begriffe und Formulierungen fördern die sprachliche Präzision und vermeiden stereotype Geschlechtszuschreibungen.
- Rechtliche und institutionelle Anforderungen: Universitäten und Institutionen verlangen oder empfehlen die Anwendung gendergerechter Sprache in akademischen Arbeiten.

Der angewendete Sprachstil möchte die genannten Barrieren überwinden und damit einen Beitrag zur Lebendwirklichkeit aller Personen leisten, was sich zudem in der Verwendung des Asterisks beim Gendern ausdrückt. Hierdurch können typografische Verzerrungen im Vorfeld auf ein Minimum reduziert und eine weite Beteiligung aller erreicht werden [@koehler_empfehlung_2021, Kapitel 7 und 8].

**Schreibweisen für Literatur- und Abbildungsverweise**

Im Fließtext werden die Begriffe "Kapitel", "Tabelle", "Abbildung" und "Seite" in der Regel ausgeschrieben (z.B. "wie in Kapitel 2.2 dargestellt", "siehe Tabelle 4"). Klammerangaben und technische Verweise werden mit diesen standardisierten Abkürzungen referenziert:

- S.   = Seite (z.B. "[@doring_forschungsmethoden_2023, Seite 4–5]")
- Kap. = Kapitel (z.B. "[@doring_forschungsmethoden_2023, Kapitel 2.2]")
- Abb. = Abbildung (z.B. "siehe Abbildung 3")
- Tab. = Tabelle (z.B. "vgl. Tab.~\\ref{tab:methoden_FU}")

Die Abkürzung "z.B." ("zum Beispiel") wird vor allem in Klammern und Fußnoten genutzt; im Fließtext wird nach Möglichkeit die ausgeschriebene Form "zum Beispiel" verwendet; nur in Ausnahmefällen wird "bspw." genutzt.

## Hinweis zur Begriffsbestimmung {#sec:begriffsbestimmung}

In dieser Arbeit erfolgen die Definition, Herleitung und Begründung zentraler Begriffe an den Stellen, an denen die jeweilige Terminologie erstmalig eingeführt wird. Diese Vorgehensweise gewährleistet eine Erklärung der Begriffsverwendung im spezifischen Kontext des jeweiligen Bezugsrahmens und verdeutlicht die Relevanz des Begriffs für die jeweilige Diskussion.
Die kontextbezogene Einführung fördert eine Verknüpfung zwischen theoretischem Rahmen und Begriffsnutzung, was zur Stärkung der Verständlichkeit und Kohärenz der Argumentation beiträgt. Eine weitergehende Unterscheidung unterschiedlicher Definitionstypen (z.B. Nominal‑ vs. Realdefinition) sowie deren formale Analyse wird, in Anlehnung an die einschlägige Methodikliteratur, nicht vertieft, da sie für die empirische Forschungspraxis nachrangig ist. [@doring_forschungsmethoden_2023, Seite 226-227]

Das hier gewählte Verfahren ermöglicht eine kontextualisierte Begriffseinführung und vermeidet isolierte oder zu abstrakte Bestimmungen [@doring_forschungsmethoden_2023, Seite 227]. Durch die unmittelbare Einführung in die Argumentation erhalten Lesende eine Verbindung zwischen Begriff und Diskussionszusammenhang. Zusätzlich bleibt die Flexibilität des Aufbaus erhalten, da Begriffe erst dann eingeführt werden, wenn sie für die Argumentation von Bedeutung sind. 

Diese Vorgehensweise birgt gleichzeitig Herausforderungen. Lesende könnten einen höheren Orientierungsaufwand haben, da Begriffe an unterschiedlichen Stellen der Arbeit erscheinen und der Verzicht auf eine zentrale Zusammenführung der Begriffsbestimmungen die Übersichtlichkeit einschränken kann. Zudem besteht das Risiko, dass Begriffe in verschiedenen Kontexten mehrfach erläutert werden müssen, was zu Redundanzen führen kann. Zur Minderung dieser Herausforderungen wird ein Verzeichnis zentraler Begriffe eingefügt, das die zentrale Übersicht aller relevanten Begriffe mit den zugehörigen Seitenzahlen enthält (vgl. \hyperref[sec:A-1]{Abschnitt A.1}). Dies ermöglicht es den Lesenden, Begriffsdefinitionen schnell und gezielt aufzufinden, wodurch der Orientierungsaufwand verringert und die Übersichtlichkeit gesteigert wird. Gleichzeitig bleibt die Vorteilhaftigkeit der kontextbasierten Einführung der Begriffe im Text erhalten.

## Hinweis zum Einsatz generativer KI-Systeme {#sec:hinweis-ki}

In dieser Arbeit wurden generative KI-Systeme (Large-Language-Modelle; im Workflow u.a. als „GPT“ bezeichnet) als kognitive Assistenz in Recherche-, Auswertungs- und Schreibprozessen eingesetzt. Der Einsatz erfolgte methodengeleitet, forschungsfragenorientiert und mit dem Ziel, große Materialmengen (Literaturkorpus, Protokolle, Artefakte) konsistent zu strukturieren, nicht jedoch, um menschliche Urteils- und Verantwortungsfunktionen zu ersetzen. Der KI-Einsatz ist in der Methodologie transparent hergeleitet und als Teil der Reproduzierbarkeitslogik dokumentiert (Abschnitte \hyperref[sec:Systematische-Literaturrecherche]{4.2.1}, \hyperref[sec:Sekundaranalysen]{4.3.3}, \hyperref[sec:SWOT-KI-Methodik]{4.5.1} und \hyperref[sec:Methodenkritik-Absicherung]{4.5.2}).

Konkret wurde KI vor allem für

1. strukturierte Zusammenfassungen und Extraktion von Kernaussagen aus Quellen,
2. die promptbasierte, kategoriengeleitete Vorstrukturierung von Primär- und Sekundäranalysen,
3. die Konsistenzunterstützung bei qualitativen Codierungen (z.B. beschreibende Auswertung von Eye‑Tracking‑Artefakten) sowie
4. textliche Formulierungs- und Redaktionsunterstützung genutzt.

Alle KI-Outputs wurden als vorläufige Verdichtungen behandelt, im Lektüre- und Analyseprozess kontrolliert, bei Bedarf korrigiert und mit eigenen Einschätzungen sowie den Primärquellen abgeglichen. Damit folgt der Workflow der in der Literatur beschriebenen Leitlinie, KI als Verstärkung in Recherche und Wissensorganisation zu nutzen, bei fortbestehender menschlicher Validierungsverantwortung [@hebbel-seeger_wissenschaftliches_2025, Seite 434-436; @storey_ai_2023, Seite 4].

Die Arbeit berücksichtigt zugleich die in der Forschungsliteratur diskutierten Risiken generativer KI, insbesondere Halluzinationen und Referenzfehler, Verzerrungen, Integritäts- und Zuschreibungsfragen sowie die Gefahr epistemischer Verflachung [@van_niekerk_addressing_2025, Seite 2; @biswas_chatgpt_2023, Seite 1; @parker_negotiating_2024, Seite 2; @giannakos_promise_2024, Seite 22; @hebbel-seeger_wissenschaftliches_2025, Seite 438-440].

Aus diesen Gründen sind

- standardisierte, versionierte Prompts,
- Protokollierung von Prompt-Ständen/Revisionen und
- eine menschliche Endredaktion als verbindliche Absicherungsmaßnahmen integriert.

Die Detektion KI-generierter Textanteile wird als ergänzende Kontrollspur eingesetzt und zusammen mit Prompt-/Versionsprotokollen sowie Quellenabgleichen interpretiert. Detektionsverfahren werden damit nicht als alleinige Begründungsbasis verwendet, sondern als kontextabhängige Zusatzprüfung im Rahmen der dokumentierten Validierungs- und Reproduzierbarkeitslogik [@hebbel-seeger_wissenschaftliches_2025, Seite 438-440]. Ergänzend dazu ist der gesamte Entstehungsprozess des Dissertationstextes vollständig versioniert dokumentiert. Die Texterstellung, Überarbeitungen und strukturellen Anpassungen erfolgten in Markdown-Dateien, die fortlaufend über ein Git-basiertes Versionskontrollsystem archiviert wurden. Dadurch sind sämtliche Entwicklungsstände, Revisionen und inhaltlichen Entscheidungen der Arbeit zeitlich nachvollziehbar und prinzipiell rekonstruierbar, was die Transparenz und Nachvollziehbarkeit der Textgenese zusätzlich absichert.

\newpage
