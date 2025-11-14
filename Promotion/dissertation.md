---
author: "Jochen Hanisch-Johannsen"
title: "Wirkgefüge im digitalen Bildungsraum"
geometry: "left=2.5cm, right=2.5cm, top=2.5cm, bottom=1.0cm, includefoot, footskip=1.5cm"
papersize: a4
latex_engine: xelatex
bibliography: "Allgemein_beruflich/Research/Charité - Universitätsmedizin Berlin/Matadaten/Literaturverzeichnis.bib"
csl: "pandoc-templates/bibliography/apa.csl"
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

# Titelseite

<!-- Hier kannst du den bestehenden Titelseiten-Block aus
     `09 Backup/Versionen/v-0-0-3 Wirkgefüge im digitalen Bildungsraum.md`
     1:1 (inkl. LaTeX) einfügen. -->

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

<!-- Hier kannst du später die Abkürzungstabelle aus der bestehenden Version
     als LaTeX-Block einfügen. -->

\newpage

# Symbolverzeichnis

<!-- Platzhalter für das Symbolverzeichnis (ebenfalls als LaTeX-Tabelle möglich). -->

\newpage

# Formelverzeichnis

<!-- Optional: eigene Umgebung/Liste für Formeln, wenn du das weiter nutzen möchtest. -->

\newpage

# Einleitung und theoretischer Rahmen

<!-- Inhalte aus:
     04 Kapitelstruktur/04-01 Einleitung und theoretischer Rahmen/*.md
     und aus deiner Word-Datei hierher übertragen. -->

\newpage

# Theorieteil

<!-- Inhalte aus:
     04 Kapitelstruktur/04-02 Theorieteil/* -->

\newpage

# Forschungsgegenstand

<!-- Inhalte aus:
     04 Kapitelstruktur/04-03 Forschungsgegenstand/* -->

\newpage

# Methodologie

<!-- Inhalte aus:
     04 Kapitelstruktur/04-04 Methodologie/* -->

\newpage

# Ergebnisse

<!-- Inhalte aus:
     04 Kapitelstruktur/04-05 Ergebnisse/* -->

\newpage

# Diskussion

<!-- Inhalte aus:
     04 Kapitelstruktur/04-06 Diskussion/* -->

\newpage

# Conclusio

<!-- Inhalte aus:
     04 Kapitelstruktur/04-07 Conclusio/* -->

\newpage

# Literatur

<!-- Wenn du mit pandoc + CSL arbeitest, reicht normalerweise:

```{=latex}
\printbibliography
```

oder das Standard-Literaturverzeichnis von pandoc anhand deiner .bib-Datei. -->

