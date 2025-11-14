---
geometry: "left=2.5cm, right=2.5cm, top=2.5cm, bottom=1.0cm, includefoot, footskip=1.5cm"
papersize: a4
latex_engine: xelatex
bibliography: "08 Metaquellen/Matadaten/Literaturverzeichnis.bib"
csl: "08 Metaquellen/Matadaten/apa-no-initials.csl"
header-includes:
  - \usepackage{fontspec}
  - \setmainfont{Arial}
  - \usepackage[ngerman]{babel}
  - \usepackage{setspace}
  - \onehalfspacing
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyhead[L]{\leftmark}
  - \fancyfoot[C]{\thepage}
  - \renewcommand{\sectionmark}[1]{\markboth{#1}{}}
  - \renewcommand{\subsectionmark}[1]{\markright{#1}}
  - \usepackage{titlesec}
  - \titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
  - \usepackage{hyperref}
  - \addto\captionsngerman{\renewcommand{\contentsname}{Inhaltsverzeichnis}}
  - \addto\captionsngerman{\renewcommand{\listtablename}{Tabellenverzeichnis}}
  - \addto\captionsngerman{\renewcommand{\listfigurename}{Abbildungsverzeichnis}}
  - \usepackage{graphicx}
  - \usepackage{float}
  - \usepackage{longtable}
  - \usepackage{tocloft}
  - \usepackage{tabularx}
  - \usepackage{imakeidx}
  - \makeindex
  - \usepackage{glossaries}
  - \makeglossaries
  - \usepackage{tikz}
  - \usetikzlibrary{positioning}
  - \usetikzlibrary{arrows.meta}
  - \usepackage{caption}
  - \captionsetup{font=small, labelfont=bf, skip=10pt}
---

\pagestyle{plain}

```{=latex}
\begin{titlepage}
\begin{center}

{\Large DISSERTATION}\\[3cm]

{\bfseries\LARGE Wirkgefüge im digitalen Bildungsraum}\\[0.8cm]

{\large Eine Untersuchung der Merkmale, Effekte, Mechanismen und Reaktionen von Learning-Management-Systemen am Beispiel der Lehre in Gesundheitsberufen}\\[1.5cm]

{\bfseries\large Interactional Frameworks in the Digital Educational Space}\\[0.8cm]

{\large An Exploration of the Characteristics, Effects, Mechanisms, and Responses of Learning Management Systems Using the Example of Healthcare Education}\\[3cm]

{\large zur Erlangung des akademischen Grades}\\[0.5cm]
{\large Doctor rerum medicinalium (Dr. rer. medic.)}\\[1.5cm]

{\large vorgelegt der Medizinischen Fakultät}\\[0.2cm]
{\large Charité – Universitätsmedizin Berlin}\\[1.5cm]

{\large von}\\[0.2cm]
{\large Jochen Hanisch-Johannsen M.A., M.A.}\\[2cm]

{\large Erstbetreuung: Prof. Dr. med. Sebastian Spethmann}\\[0.2cm]
{\large Zweitbetreuung: Prof.in Dr.in phil. Eva Cendon}\\[0.8cm]
{\large Datum der Promotion: dd.mm.yyyy}\\

\end{center}
\end{titlepage}
```

# Inhaltsverzeichnis

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

# Abkürzungsverzeichnis

\begin{longtable}{p{3cm}p{10cm}}
\textbf{Abkürzung} & \textbf{Bedeutung} \\
\hline
LMS & Learning-Management-System; zentrale Plattform zur Bereitstellung und Organisation der Lehrangebote. \\
FU & Forschungsunterfrage (FU1–FU7) als operationalisierte Teilfragestellungen. \\
mdaCV & Mehrdimensional-analytische Clustervalidierung zur Prüfung der literaturbasierten Clusterstruktur. \\
P-QIA & Probabilistisch-Qualitative Inhaltsanalyse – hybride Methode zur Quellenkodierung. \\
KI & Künstliche Intelligenz; insbesondere generative Verfahren zur Dokumentenanalyse. \\
LLM & Large Language Model; Sprachmodell zur semantischen Einordnung großer Textkorpora. \\
SC & Silhouette-Score; Maß für die Trennschärfe von Clustern (Kapitel 4.3.3). \\
E-Portfolio & Digitales Portfolio zur Dokumentation und Reflexion von Lernleistungen. \\
MOOC & Massive Open Online Course; frei zugängliches Online-Lernformat. \\
LXP & Learning Experience Platform; nutzungszentrierte Erweiterung eines LMS. \\
\end{longtable}

\newpage

# Symbolverzeichnis

\begin{longtable}{p{3cm}p{10cm}}
\textbf{Symbol} & \textbf{Beschreibung} \\
\hline
$\varepsilon$ & Epistemische Verlustfunktion zur Bewertung der Integrität der mdaCV (Gl.~\eqref{eq:verlust}). \\
$S$ & Silhouette-Score als Maß der Clusterdifferenzierung. \\
$k$ & Anzahl der Cluster im k-Means-Algorithmus. \\
$\nu$ & Bildungswirkfaktor als aggregiertes Maß der Kompetenzwirkung. \\
$\iota$ & Bildungswirkindikator; Steigung des Bildungswirkfaktors. \\
$\Delta K$ & Kognitive Unsicherheit innerhalb der Kompetenzentwicklung. \\
$\Delta E$ & Emotionale Unsicherheit innerhalb der Kompetenzentwicklung. \\
$t$ & Zeitvariable der Dynamikmodelle. \\
\end{longtable}

\newpage

# Formelverzeichnis

Die nachfolgende Tabelle listet alle im Manuskript aufgeführten Gleichungen mit der jeweils zugehörigen inhaltlichen Beschreibung.

\begin{longtable}{p{4cm}p{10cm}}
\caption{Formelverzeichnis}\label{tab:formelverzeichnis}\\
\textbf{Gleichung} & \textbf{Beschreibung} \\
\hline
\eqref{eq:verlust} & Epistemische Verlustfunktion zur Bewertung der Integrität der mehrdimensional-analytischen Clustervalidierung (mdaCV). \\
\end{longtable}

\newpage

# Hinweise

Diese Hinweise gewährleisten durch einheitliche und transparente Vorgaben die wissenschaftliche Nachvollziehbarkeit und vermitteln Lesenden ein Verständnis der angewandten Prinzipien. Der gewählte APA-Zitationsstil (7. Ausgabe) ermöglicht eine standardisierte Referenzierung und trägt zur internationalen Anschlussfähigkeit der Arbeit bei. Die Prinzipien der gendergerechten Sprache spiegeln den gesellschaftlichen Wandel wider und fördern die Inklusion in der akademischen Kommunikation. Die kontextbezogene Begriffsdefinition verortet zentrale Konzepte präzise innerhalb des spezifischen Diskussionsrahmens und minimiert Missverständnisse.

Damit wird eine Grundlage für die Struktur und Verständlichkeit der Arbeit geschaffen. Die Darstellung der Zitations- und Sprachstandards sowie der Begriffsverwendung stärkt die methodische Stringenz, die inhaltliche Kohärenz und die wissenschaftliche Qualität.

## Hinweis zum Zitationsstil

Der Zitationsstil dieser Arbeit basiert auf der 7. Ausgabe des APA-Zitationsstils. Zur Verwaltung der Zitate wird die Software Zotero (Version 7.0.8) verwendet, alle Referenzen sind als Zitationen angelegt und in der vorliegenden Fassung von Feldern zu Text umgewandelt worden, um die Verweise eindeutig zu gestalten.

Innerhalb der Zitationen werden diese Regeln angewendet:

- Direkte Zitate: Die Quellenangabe erfolgt unmittelbar nach dem wörtlichen Zitat.
- Indirekte Zitate innerhalb eines Satzes: Die Quellenangabe bezieht sich auf den gesamten Satz, der durch Satzzeichen abgeschlossen ist.
- Indirekte Zitate in einem Nebensatz: Die Quellenangabe bezieht sich auf den betreffenden Satzteil.
- Indirekte Zitate am Ende eines Absatzes: Die Quellenangabe bezieht sich auf den gesamten Absatz.
- Indirekte Zitate vor einer Aufzählung: Die Quellenangabe bezieht sich auf die gesamte Aufzählung.
- Mehrere indirekte Zitate: Die Quellenangaben beziehen sich auf die Reihenfolge der Argumentation.

Auslassungen sind durch „(…)“ dargestellt und Ergänzungen innerhalb von Zitaten erscheinen in eckigen Klammern „[…; Anmerkung des Autors]“, während Hervorhebungen durch den Autor mit „[Hervorhebung durch den Autor]“ kenntlich gemacht werden. Übersetzungen, die dem Original wörtlich entsprechen, werden wie direkte Zitate behandelt und mit der Anmerkung „(Übersetzung durch den Autor)“ versehen.

## Hinweis zum Sprachstil

Die Arbeit folgt den Prinzipien einer gendergerechten Sprache. Orientierung bietet der Vorschlag von Koehler und Wahl, dass „die Gleichstellung aller Geschlechter und die Anerkennung aller Identitätsgeschlechter“ ihren sprachlichen Ausdruck innerhalb der scientific community finden muss [@koehler_empfehlung_2021, S. 2].

Hieraus ergeben sich folgende, stilentsprechende Implikationen:

- Inklusion und Diversität: Alle Geschlechter und Identitäten werden sprachlich anerkannt und einbezogen.
- Gleichstellung: Sprachliche Gleichbehandlung fördert die Gleichstellung der Geschlechter in der Wissenschaft.
- Wissenschaftliche Relevanz: Gendergerechte Sprache reflektiert den gesellschaftlichen Wandel und wird in der scientific community zunehmend anerkannt.
- Lesbarkeit und Verständlichkeit: Gendergerechte Sprache erhöht bei bewusster Formulierung die Verständlichkeit.
- Sensibilisierung: Gendergerechte Sprache sensibilisiert für das Thema der Geschlechtergerechtigkeit in akademischen Texten.
- Sprachliche Präzision: Geschlechtsneutrale Begriffe und Formulierungen fördern die sprachliche Präzision und vermeiden stereotype Geschlechtszuschreibungen.
- Rechtliche und institutionelle Anforderungen: Universitäten und Institutionen verlangen oder empfehlen die Anwendung gendergerechter Sprache in akademischen Arbeiten.

Der angewendete Sprachstil möchte die genannten Barrieren überwinden und damit einen Beitrag zur Lebendwirklichkeit aller Personen leisten, was sich zudem in der Verwendung des Asterisks beim Gendern ausdrückt. Hierdurch können typografische Verzerrungen im Vorfeld auf ein Minimum reduziert und eine weite Beteiligung aller erreicht werden [@koehler_empfehlung_2021, Kapitel 7; @koehler_empfehlung_2021, Kapitel 8].

## Hinweis zur Begriffsbestimmung

In dieser Arbeit erfolgen die Definition, Herleitung und Begründung zentraler Begriffe an den Stellen, an denen die jeweilige Terminologie erstmalig eingeführt wird. Diese Vorgehensweise gewährleistet eine Erklärung der Begriffsverwendung im spezifischen Kontext des jeweiligen Bezugsrahmens und verdeutlicht die Relevanz des Begriffs für die jeweilige Diskussion. Die kontextbezogene Einführung fördert eine Verknüpfung zwischen theoretischem Rahmen und Begriffsnutzung, was zur Stärkung der Verständlichkeit und Kohärenz der Argumentation beiträgt.

Das hier gewählte Verfahren ermöglicht eine kontextualisierte Begriffseinführung und vermeidet isolierte oder zu abstrakte Bestimmungen. Durch die unmittelbare Einführung in die Argumentation erhalten Lesende eine Verbindung zwischen Begriff und Diskussionszusammenhang. Zusätzlich bleibt die Flexibilität des Aufbaus erhalten, da Begriffe erst dann eingeführt werden, wenn sie für die Argumentation von Bedeutung sind.

Diese Vorgehensweise birgt gleichzeitig Herausforderungen. Lesende könnten einen höheren Orientierungsaufwand haben, da Begriffe an unterschiedlichen Stellen der Arbeit erscheinen und der Verzicht auf eine zentrale Zusammenführung der Begriffsbestimmungen die Übersichtlichkeit einschränken kann. Zudem besteht das Risiko, dass Begriffe in verschiedenen Kontexten mehrfach erläutert werden müssen, was zu Redundanzen führen kann. Zur Minderung dieser Herausforderungen wird ein Verzeichnis zentraler Begriffe (S. VI) eingefügt, das die zentrale Übersicht aller relevanten Begriffe mit den zugehörigen Seitenzahlen enthält. Dies ermöglicht es den Lesenden, Begriffsdefinitionen schnell und gezielt aufzufinden, wodurch der Orientierungsaufwand verringert und die Übersichtlichkeit gesteigert wird. Gleichzeitig bleibt die Vorteilhaftigkeit der kontextbasierten Einführung der Begriffe im Text erhalten.

\newpage
