---
author: 
title: 
Repository: 
created: 
updated: 
publish: 
tags:
  - Charité_Universitätsmedizin-Berlin
  - Dissertation
published: 
geometry: "left=2.5cm, right=2.5cm, top=2.5cm, bottom=1.0cm, includefoot, footskip=1.5cm"
papersize: a4
output: []
pdf_document: []
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
  - \renewcommand{\cfttoctitlefont}{\hspace*{-\textwidth}}
  - \renewcommand{\cftloftitlefont}{\hspace*{-\textwidth}}
  - \renewcommand{\cftlottitlefont}{\hspace*{-\textwidth}}
  - \usepackage{caption}
  - \captionsetup{font=small, labelfont=bf, skip=10pt}
---
\newglossaryentry{lms}{
  name={LMS},
  description={Learning Management System, eine Software zur Verwaltung von Lerninhalten}
}

\newglossaryentry{mooc}{
  name={MOOC},
  description={Massive Open Online Course, eine Plattform für viele Teilnehmer}
}


\pagestyle{plain}

\begin{center}

DISSERTATION

\vspace{3 cm}

\textbf{Wirkgefüge im digitalen Bildungsraum}

Eine Untersuchung der Merkmale, Effekte, Mechanismen und Reaktionen von Learning-Management-Systemen am Beispiel der Lehre in Gesundheitsberufen
\linebreak

\textbf{Interactional Frameworks in the Digital Educational Space}

An Exploration of the Characteristics, Effects, Mechanisms, and Responses of Learning Management Systems Using the Example of Healthcare Education

\vspace{3 cm}

zur Erlangung des akademischen Grades

Doctor rerum medicinalium (Dr. rer. medic.)
\linebreak

vorgelegt der Medizinischen Fakultät

Charité – Universitätsmedizin Berlin
\linebreak

von
\linebreak

Jochen Hanisch-Johannsen M.A., M.A.

\end{center}

\vspace{5cm}

Erstbetreuung: Prof. Dr. med. Sebastian Spethmann

Zweitbetreuung: Prof.in Dr.in phil. Eva Cendon

Datum der Promotion: dd.mm.yyyy

\newpage
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

```{=latex}
\begin{table}[!htbp]
\centering
\renewcommand{\arraystretch}{1.2}  % Optional: Zeilenabstand innerhalb der Tabelle vergrößern
\caption{Übersicht der verwendeten Abkürzungen}  % Tabellenbeschriftung in normaler Textgröße
\label{tab:abkuerzungen}
{\fontsize{9}{11}\selectfont  % Setzt die Schriftgröße innerhalb der Tabelle auf 9 pt
\begin{tabularx}{\textwidth}{|l|X|}
\hline
\textbf{Abkürzung} & \textbf{Bedeutung} \\ \hline
APrV & Ausbildungs- und Prüfungsverordnung \\ \hline
BASE & Bielefeld Academic Search Engine \\ \hline
BZ & DRK-Bildungszentrum Düsseldorf \\ \hline
DRK & Deutsches Rotes Kreuz \\ \hline
FH & Hauptforschungsfrage \\ \hline
FU & Forschungsunterfrage \\ \hline
GT & Grounded Theorie \\ \hline
LAMP & Linux-Apache-MySQL-PHP \\ \hline
LMS & Learning Management System \\ \hline
Moodle® & Modular Object-Oriented Dynamic Learning Environment \\ \hline
NFS, NotSan & Notfallsanitäterinnen und Notfallsanitäter \\ \hline
NotSanG & Gesetz über den Beruf der Notfallsanitäterin und des Notfallsanitäters (Notfallsanitätergesetz) \\ \hline
pdf & Portables Dokumentenformat \\ \hline
PLE & Personal Learning Environment, persönliche Lernumgebung \\ \hline
TEI & The Training Evaluation Inventory \\ \hline
\end{tabularx}
}
\end{table}
```

\newpage

# Symbolverzeichnis

```{=latex}
\begin{table}[!htbp]
\centering
\renewcommand{\arraystretch}{1.2}  % Optional: Zeilenabstand innerhalb der Tabelle vergrößern
\caption{Übersicht der verwendeten Symbole}  % Tabellenbeschriftung in normaler Textgröße
\label{tab:symbole}
{\fontsize{9}{11}\selectfont  % Setzt die Schriftgröße innerhalb der Tabelle auf 9 pt
\begin{tabularx}{\textwidth}{|l|X|X|}
\hline
\textbf{Symbol} & \textbf{Bedeutung} & \textbf{Beschreibung} \\ \hline
$\frac{dK}{dt}$ & Änderungsrate der Kompetenzentwicklung & Änderungsrate der Kompetenzentwicklung über die Zeit. \\ \hline
$\iota$ & Bildungswirkindikator & Änderungsrate des Bildungswirkfaktors ($\nu$). \\ \hline
$\nu$ & Bildungswirkfaktor & Maß für die Gesamtauswirkungen auf die Kompetenzentwicklung. \\ \hline
$C$ & Dynamischer Unsicherheitsfaktor & Maß für die Unsicherheitskopplung zwischen $\Delta K$ und $\Delta E$. \\ \hline
$\Delta E$ & Emotionale Unsicherheit & Schwankungen in der emotionalen Entwicklung (Bereitschaft). \\ \hline
$\Delta K$ & Kognitive Unsicherheit & Schwankungen in der Kompetenzentwicklung (Wissen, Können). \\ \hline
$\Delta K \cdot \Delta E$ & Kopplung der kognitiven und emotionalen Unsicherheiten & Beeinflussung der Kompetenzentwicklung durch emotionale und kognitive Schwankungen. \\ \hline
$\nabla \nu$ & Gradient des Bildungswirkfaktors & Maß für die Veränderungsgeschwindigkeit des Bildungswirkfaktors. \\ \hline
$\Delta N$ & Neugier Unsicherheit & Schwankungen in der Entwicklung der Neugier. \\ \hline
$K(t)$ & Kompetenzentwicklung & Kompetenzentwicklung über die Zeit $t$. \\ \hline
$\sigma$ & Standardabweichung & Statistisches Maß für die Streuung der Werte (z.B. bei Simulationsergebnissen). \\ \hline
$\int$ & Integral & Darstellung der Fläche unter einer Kurve zur Berechnung kumulativer Werte. \\ \hline
$\sum$ & Summenzeichen & Summe über eine Reihe von Werten oder Ereignissen. \\ \hline
$\Delta t$ & Zeitintervall & Zeitintervall, über das Änderungen in der Kompetenzentwicklung betrachtet werden. \\ \hline
\end{tabularx}
}
\end{table}
```
\newpage
# Formelverzeichnis

\newlistof{equations}{equ}{}
\listofequations

\newpage

# Hinweise
## Hinweis zum Zitationsstil

Der Zitationsstil dieser Arbeit folgt der 7. Ausgabe des APA-Zitationsstils. Zur Verwaltung der Zitate wird die Software Zotero (Version 6.0.37) verwendet. Sämtliche Referenzen werden als BibLaTeX-Einträge angelegt und beim Kompilieren des Dokuments in den finalen Text integriert.

Die folgenden Zitationsregeln finden Anwendung:

- Direkte Zitate: Die Quellenangabe erfolgt unmittelbar nach dem wörtlichen Zitat.
- Indirekte Zitate innerhalb eines Satzes: Die Quellenangabe bezieht sich auf den gesamten Satz, der durch Satzzeichen abgeschlossen ist.
- Indirekte Zitate in einem Nebensatz: Die Quellenangabe bezieht sich auf den betreffenden Satzteil.
- Indirekte Zitate am Ende eines Absatzes: Die Quellenangabe bezieht sich auf den gesamten Absatz.
- Indirekte Zitate vor einer Aufzählung: Die Quellenangabe bezieht sich auf die gesamte Aufzählung.
- Mehrere indirekte Zitate: Die Quellenangaben folgen der Reihenfolge der Argumentation.

Auslassungen sind durch (…) dargestellt und Ergänzungen innerhalb von Zitaten erscheinen in eckigen Klammern […; Anmerkung des Autors], während Hervorhebungen durch den Autor mit [Hervorhebung durch den Autor] kenntlich gemacht werden. Übersetzungen, die dem Original wörtlich entsprechen, werden wie direkte Zitate behandelt und mit der Anmerkung (Übersetzung durch den Autor) versehen.

Ein Zugeständnis war beim Literaturverzeichnis erforderlich. Der bekannte Fehler in LaTeX, der dazu führt, dass das Literaturverzeichnis automatisch am Ende des gesamten Dokuments platziert wird, tritt auch in diesem Fall auf. Dieser Fehler ist in der LaTeX-Community weit verbreitet und bekannt.

## Hinweis zum Sprachstil

Die Arbeit folgt den Prinzipien einer gendergerechten Sprache gemäß den Empfehlungen von @koehler2021Egd verfasst: „Die Gleichstellung aller Geschlechter und die Anerkennung aller Identitätsgeschlechter“ muss „ihren sprachlichen Ausdruck“ innerhalb der science community finden [@koehler2021Egd, S. 2].

Hieraus ergeben sich folgende, stilentsprechende Implikationen:

- Inklusion und Diversität: Alle Geschlechter und Identitäten werden sprachlich anerkannt und einbezogen.
- Gleichstellung: Sprachliche Gleichbehandlung fördert die Gleichstellung der Geschlechter in der Wissenschaft.
- Wissenschaftliche Relevanz: Gendergerechte Sprache reflektiert den gesellschaftlichen Wandel und wird in der scientific community zunehmend anerkannt.
- Lesbarkeit und Verständlichkeit: Gendergerechte Sprache erhöht bei bewusster Formulierung die Verständlichkeit.
- Sensibilisierung: Gendergerechter Sprache sensibilisiert für das Thema der Geschlechtergerechtigkeit in akademischen Texten.
- Sprachliche Präzision: Geschlechtsneutrale Begriffe und Formulierungen fördern die sprachliche Präzision und vermeiden stereotype Geschlechtszuschreibungen.
- Rechtliche und institutionelle Anforderungen: Universitäten und Institutionen verlangen oder empfehlen die Anwendung gendergerechter Sprache in akademischen Arbeiten.

## Hinweis zur Begriffsbestimmung

In dieser Arbeit erfolgt die Definition, Herleitung und Begründung zentraler Begriffe an den Stellen, an denen die jeweilige Terminologie erstmalig eingeführt wird. Diese Vorgehensweise gewährleistet eine Erklärung der Begriffsverwendung im spezifischen Kontext des jeweiligen Bezugsrahmens und verdeutlicht die Relevanz des Begriffs für die jeweilige Diskussion. Die kontextbezogene Einführung fördert eine Verknüpfung zwischen theoretischem Rahmen und Begriffsnutzung, was zur Stärkung der Verständlichkeit und Kohärenz der Argumentation beiträgt.

Das hier gewählte Verfahren ermöglicht eine kontextualisierte Begriffseinführung und vermeidet isolierte oder zu abstrakte Bestimmungen. Durch die unmittelbare Einführung in die Argumentation erhalten Lesende eine Verbindung zwischen Begriff und Diskussionszusammenhang. Zusätzlich bleibt die Flexibilität des Aufbaus erhalten, da Begriffe erst dann eingeführt werden, wenn sie für die Argumentation von Bedeutung sind.

Die gewählte Vorgehensweise birgt Herausforderungen. Lesende könnten einen höheren Orientierungsaufwand haben, da Begriffe an unterschiedlichen Stellen der Arbeit erscheinen. Der Verzicht auf eine zentrale Zusammenführung der Begriffsbestimmungen kann die Übersichtlichkeit einschränken. Zudem besteht das Risiko, dass Begriffe in verschiedenen Kontexten mehrfach erläutert werden müssen, was Redundanzen erzeugen kann.

Zur Minderung dieser Herausforderungen wird auf Seite \pageref{Verzeichnis_zentraler_Begriffe} ein Verzeichnis der relevanten Begriffe eingefügt, das die zentrale Übersicht aller relevanten Begriffe mit den zugehörigen Seitenzahlen enthält. Dies ermöglicht es den Lesenden, Begriffsdefinitionen schnell und gezielt aufzufinden, wodurch der Orientierungsaufwand verringert und die Übersichtlichkeit gesteigert wird. Gleichzeitig bleibt die Vorteilhaftigkeit der kontextbasierten Einführung der Begriffe im Text erhalten.

\newpage
# Zusammenfassung

Bitte fügen Sie hier die von Ihnen selbst verfasste **deutsche Zusammenfassung** Ihrer Dissertation (max. 3.000 Zeichen inkl. Leerzeichen) ein. Diese darf nicht identisch mit der Zusammenfassung Ihrer Publikation sein, sondern muss darüberhinausgehend Ihre gesamte Promotionsarbeit (Manteltext und Publikation/en) zusammenfassen.
# Abstract

Bitte fügen Sie hier das selbst verfasste **englische Abstract** Ihrer Dissertation (max. 3.000 Zeichen inkl. Leerzeichen) ein. Dieses darf nicht identisch (auch nicht umformuliert) mit dem Abstract Ihrer Publikation sein, sondern muss darüberhinausgehend Ihre gesamte Promotionsarbeit (Manteltext und Publikation/en) zusammenfassen.

\newpage

\pagestyle{fancy}

# 1 Einleitung

- [ ] Die Einleitung eröffnet die eigentliche Dissertation und führt in die Thematik ein

Du stellst hier das Thema der Dissertation vor und führst die Leser in den Kontext des digitalen Bildungsraums ein. Fokussiere dich darauf, warum Learning-Management-Systeme (LMS) in den Gesundheitsberufen wichtig sind, und hebe die Relevanz der Untersuchung der Wirkfaktoren (Neugier, persönliche Ereignisse und Kompetenz) hervor.

Der Digitale Bildungsraum ist vielfältig: Technische Geräte und Softwareapplikationen stehen in einem hohen (Aus-)Maß zur Verfügung. 

vgl. Statisa

Der Mensch hat seit jeher Werkzeuge genutzt, um sich an seine Umwelt anzupassen und seine Lebensbedingungen zu verbessern. Diese Fähigkeit, Werkzeuge zu entwickeln und zu nutzen, ist tief in der menschlichen Evolution verwurzelt und hat entscheidend zur Entwicklung von kognitiven und sozialen Strukturen beigetragen. Beginnend mit einfachen Werkzeugen wie dem Faustkeil, der vor über zwei Millionen Jahren von frühen Hominiden verwendet wurde, bis hin zu hochkomplexen digitalen Werkzeugen wie Learning-Management-Systemen (LMS), hat der Mensch immer danach gestrebt, durch den Einsatz von Hilfsmitteln seine Umwelt zu kontrollieren und sich neue Möglichkeiten zu erschließen.

In prähistorischen Zeiten diente der Werkzeuggebrauch nicht nur dem Überleben, sondern förderte auch die soziale Zusammenarbeit und den Wissensaustausch innerhalb von Gemeinschaften. Diese Prinzipien haben sich über Jahrtausende hinweg erhalten und finden sich auch in modernen digitalen Umgebungen wieder, in denen kollaborative Werkzeuge wie Foren und Wikis es den Menschen ermöglichen, gemeinsam zu lernen und zu arbeiten.

Dieses Dokument untersucht den evolutionären Bogen von den ersten Werkzeugen bis zu den heutigen digitalen Lernsystemen. Es zeigt auf, wie Werkzeuge in der Menschheitsgeschichte immer wieder genutzt wurden, um die grundlegenden Bedürfnisse nach Bindung, Kontrolle, Selbstwert und Lust / Unlust-Vermeidung zu befriedigen. Dabei wird deutlich, dass moderne Technologien wie Learning-Management-Systeme nicht nur technische Hilfsmittel sind, sondern auch zentrale Werkzeuge zur Förderung von sozialem Lernen, Zusammenarbeit und persönlicher Verantwortung.

Durch diese Betrachtung wird deutlich, dass der Mensch seit der Nutzung des Faustkeils bis hin zu digitalen Lernsystemen Werkzeuge als Mittel zur Anpassung an die Umwelt und zur Erfüllung sozialer und individueller Bedürfnisse verwendet hat.

Die aktuellen Novellierungen in der Ausbildung der Gesundheitsberufe zielen darauf ab, nicht nur die gesetzlichen Rahmenbedingungen für Berufe wie Anästhesietechnische Assistent_innen, Operationstechnische Assistent_innen und Notfallsanitäter_innen anzupassen, sondern auch die Kompetenzanforderungen zu erweitern und zu präzisieren. So wird besonderer Wert auf die Förderung fachspezifischer, sozialer und methodischer Kompetenzen gelegt, die sich an den wachsenden Herausforderungen im Gesundheitswesen orientieren. Dies spiegelt sich sowohl in den neuen Ausbildungsrichtlinien als auch in den erweiterten Kompetenzprofilen der jeweiligen Berufsgruppen wider [@pflegekammernrw2023Wpn; @bgbl.i2022Gueb].

Um dir eine klare Struktur für die Argumentationskette und die Reihenfolge der Themen zu bieten, ist es wichtig, deine Wirkfaktoren (Neugier, persönliche Ereignisse, Kompetenz) und deren Bezug zum LMS schrittweise und logisch aufzubauen. Hier ist eine mögliche Orientierung, wie du deine Argumentation innerhalb der Dissertation gliedern kannst, damit sie klar, konsistent und dem Titel „Wirkgefüge im Digitalen Bildungsraum“ gerecht wird:

## 1.1 Erkenntnisinteresse, Problemstellung und Relevanz des Themas

### 1.1.1 Erkenntnisinteresse

- **Erkenntnisinteresse**: Was willst du mit der Forschung herausfinden und warum ist das relevant?

Das zentrale Erkenntnisinteresse dieser Arbeit besteht darin, zu untersuchen, wie Lern- und Kompetenzentwicklungsprozesse im Gesundheitswesen durch den Einsatz von Learning-Management-Systemen (LMS) beeinflusst werden und welche Rolle dabei sowohl medizinische als auch bildungswissenschaftliche Faktoren spielen. Besonderes Augenmerk liegt auf der Frage, wie bildungswissenschaftliche Konzepte zur Förderung von Kompetenzentwicklung in der medizinischen Aus- und Weiterbildung beitragen können. Darüber hinaus soll erforscht werden, wie transdisziplinäre Ansätze zur Verbesserung von Lernprozessen und der Wissensvermittlung in der medizinischen Praxis beitragen können.

### 1.1.2 Problemstellung


 xxxxx Weiter mit Ausgangsort und Vorüberlegungen xxxxxxxx

- **Problemstellung**: Welches spezifische Problem adressierst du und welche wissenschaftliche oder praktische Lücke besteht?

### 1.1.3 Relevanz des Themas


- **Relevanz des Themas**: Warum ist das Thema aus medizinischer und bildungswissenschaftlicher Perspektive relevant?

 - [ ] Beschreibung des zentralen Problems, das in der Arbeit behandelt wird.
 - [ ] Was ist die zentrale Herausforderung im digitalen Bildungsraum?
 - [ ] Hier könntest du darauf eingehen, dass LMS zwar nützlich und zugänglich sind, aber dass die Nutzung von LMS durch individuelle Faktoren (Neugier, Kompetenzwahrnehmung, persönliche Ereignisse) beeinflusst wird.
- [ ] Erklärung, warum das Thema sowohl für die Wissenschaft als auch für die Praxis bedeutsam ist.
- [ ] Eher deskriptiv 



Um dir eine klare Struktur für die Argumentationskette und die Reihenfolge der Themen zu bieten, ist es wichtig, deine Wirkfaktoren (Neugier, persönliche Ereignisse, Kompetenz) und deren Bezug zum LMS schrittweise und logisch aufzubauen. Hier ist eine mögliche Orientierung, wie du deine Argumentation innerhalb der Dissertation gliedern kannst, damit sie klar, konsistent und dem Titel „Wirkgefüge im Digitalen Bildungsraum“ gerecht wird:

 <mark style="background: #FFB86CA6;">So verzeichnet Statista</mark> 
 
## 1.2 Vorüberlegungen und Forschungsfragen

### 1.2.1 Zugrundliegende Vermutungen

- [ ] Lege die Forschungsfragen dar und erkläre, wie du auf jede dieser Fragen eingehen wirst, um den Überblick zu behalten.
- [ ] Die Einleitung schließt mit der Fragestellung, die in der Promotion bearbeitet wurde, ab. Untergliedern Sie die Einleitung in sinnvolle Unterkapitel. Das letzte Unterkapitel beinhaltet die Fragestellung.

Text

- [ ] Welche theoretischen und praktischen Fragen möchtest du mit der Arbeit beantworten?

### 1.2.1 Ziel der Forschung

Transdisziplinäre Zielsetzung unter Berücksichtigung medizinischer und bildungswissenschaftlicher Aspekte.

### 1.2.2 Haupt- und Unterforschungsfragen

Wissenschaftliche und praxisorientierte Erkenntnisinteressen.


**Herleitung**

> Wie beschrieben, fehlt eine Untersuchung der Wirkfaktoren, weshalb die bisherigen Ergebnisse unter Einsatz des LMS erzielt werden konnten. Diese Wirkfaktoren können als Herleitung und Begründung des Forschungsvorhabens dienen. Die zugrundeliegende Vermutung ist, dass die konsequente Anwendung des systemisch-konstruktivistischen Theoriegebäudes nicht nur bei der curricularen Konzeption oder bei der Durchführung von Lehrveranstaltungen, sondern gerade auch bei der Entwicklung einer Learning-Management-System-Architektur die beobachtbare Wirkung nicht nur erklärt, sondern darüber hinaus, Prognosen von zukünftigen gewünschten Wirkungen ermöglicht. Die Vermutung ist weiterhin, dass alle notwendigen Theorien und Erklärungen bereits in den unterschiedlichsten Wissenschaftsdisziplinen vorhanden sind. Aus den hier genannten Vermutungen lassen sich seriös kaum Forschungshypothesen ableiten, die definitionsgemäß auf bestehende Theorien aufbauen (Döring & Bortz, 2016c, S. 146). Die handlungsleitende Hauptforschungsfrage (FH) kann demnach wie folgt gestellt werden:

„**Wie ist das Wirkgefüge des angewendeten Learning-Management-Systems auf Akteure im digitalem Bildungsraum von Gesundheitsberufen gestaltet?**“
\label{fh}

> Die Forschungsfrage ist absichtlich eng gefasst, da ein bestehendes Learning-Management-System betrachtet wird. Weiterhin besteht die aufgrund einer weit gefassten Begriffsauslegung die Notwendigkeit, die Forschungsfrage in ihrer Syntax zu entfalten Insbesondere kommt der Operationalisierung eine wesentliche Bedeutung zu: die beobachtbaren Indikatoren werden dem theoretischem Begriff zugeordnet (Schnell et al., 2013, S. 7). Ziel und Zweck der Forschungsfrage ist die Betrachtung der Anwendung des eingesetzten Medientools LMS (S. 7) im digitalem Bildungsraum (S. 6, 5). Als zentraler Begriff, der zu operationalisieren ist, steht das Wirkgefüge (S. 6) im Fokus. Der Kontext, in dem die Bearbeitung stattfindet, ist in den Gesundheitsberufen (S. 7) zu finden, in dessen Kontext Akteure (S. 7) agieren. Zur Operationalisierung wurde der Begriff der Gestaltung ausgewählt. (Hanisch, 2022, 24-25)


- [ ] Weitere spezifische Fragen, die sich aus der Hauptfrage ableiten.

Tabelle \ref{tab:forschungsunterfragen} fasst die Forschungsunterfragen (FU) zusammen und ordnet sie ihren jeweiligen Bearbeitungsmethoden sowie den damit verbundenen Erfüllungskriterien zu. 

```{=latex}
\begin{table}[!htbp]
\centering
\renewcommand{\arraystretch}{1.2}  % Optional: Zeilenabstand innerhalb der Tabelle vergrößern
\caption{Übersicht der Forschungsunterfragen, Bearbeitungsmethoden und Kriterien}
\label{tab:forschungsunterfragen}
{\fontsize{9}{11}\selectfont  % Setzt die Schriftgröße innerhalb der Tabelle auf 9 pt
\begin{longtable}{|p{2cm}|p{5cm}|p{5cm}|}
\hline
\textbf{} & \textbf{Bearbeitungsmethode} & \textbf{Erfüllungskriterien} \\ \hline
\endfirsthead

\multicolumn{3}{c}%
{\tablename\ \thetable{} -- Fortsetzung von vorheriger Seite} \\
\hline
\textbf{} & \textbf{Bearbeitungsmethode} & \textbf{Operationalisierung} \\ \hline
\endhead

\hline \multicolumn{3}{|r|}{Fortsetzung auf der nächsten Seite} \\ \hline
\endfoot

\hline
\endlastfoot

\textbf{FU1} & Qualitative Metaanalyse (Döring, 2023, S. 874) & Darstellung des aktuellen Forschungsstandes in der Fachliteratur und Einordnung in das Gesamtgefüge \\ \hline
\textbf{FU2a} & Evaluating Training Programs (Kirkpatrick, 1998); The Training Evaluation Inventory (Ritzmann et al., 2014) & Bildungswissenschaftliche Evaluation des Trainingsprogramms (quantitativ); Anwendungsorientierte Evaluation des Trainingsprogramms (quantitativ-qualitativ) \\ \hline
\textbf{FU2b} & Halbstrukturiertes Gruppeninterview im Face-to-Face Kontakt mit Betroffenen (Döring \& Bortz, 2016a, S. 358–360) & Erzeugung generalisierbarer Aussagen zu den Faktoren, die durch Lernende genannten Effekte \\ \hline
\textbf{FU3} & Rezeption der systemisch-konstruktivistischen Theorie; Theoriearbeit; Bildungstechnologische Theoriearbeit über die Architektur des Learning-Management-Systems & Darstellung des didaktischen Designs sowie Herleitung, Beschreibung und Absicherung der relevanten Merkmale \\ \hline
\textbf{FU4a} & Qualitative Inhaltsanalyse (Mayring, 2010; Mayring \& Gläser-Zikuda, 2008) & Herleitung, Beschreibung und Absicherung der relevanten Wirkmechanismen \\ \hline
\textbf{FU4b} & Quantitative Beobachtung (Döring \& Bortz, 2016a, Kapitel 10.1.3); Augenaktivität (Eye-Tracking) (Döring \& Bortz, 2016a, Kapitel 10.5.5) & Datenerhebung und -auswertung sowie Einordnung der Ergebnisse \\ \hline
\textbf{FU5} & Qualitative Inhaltsanalyse (Mayring, 2010; Mayring \& Gläser-Zikuda, 2008); SWOT-Analyse (Wollny \& Paul, 2015) & Einordnung der Möglichkeiten und Grenzen des Trainingsmodells in einer nachvollziehbaren Darstellung \\ \hline
\textbf{FU6} & Verschränkung der systemisch-konstruktivistischen Theorie mit den Konstrukten der Kompetenzforschung; Theoriearbeit & Herleitung, Darstellung, Transfer und Einordnung der Ergebnisse \\ \hline
\textbf{FU7} & „Einfall und Theorieentwicklung“ (Glaser \& Strauss, 1967, Kapitel XI) auf Grundlage der Berücksichtigung des Technologiedefizites (Luhmann \& Schorr, 1982) & Entwicklung eines kausalen Ursachen-Wirkungstheoriemodells (Kausalpläne) und Überführung in Handlungsempfehlungen \\ \hline

\end{longtable}
}
\end{table}
```


- FU1 \label{fu1} untersucht die Akzeptanz und Nützlichkeit eines Learning-Management-Systems bei Akteuren im digitalen Bildungsraum von Gesundheitsberufen. Die qualitative Metaanalyse dient dazu, den aktuellen Forschungsstand darzustellen.
- FU2a  \label{fu2a} und FU2b \label{fu2b}  befassen sich mit den Effekten und Faktoren, die Lernende und Lehrende in Bezug auf ein systemisch-konstruktivistisches Learning-Management-System benennen, mit unterschiedlichen methodischen Zugängen (quantitative Evaluation und qualitative Interviews).
- FU3 \label{fu3} konzentriert sich auf die didaktischen und technologischen Merkmale des Systems, während FU4a \label{fu4a} und FU4b \label{fu4b} die bildungswissenschaftlichen und technisch-gestalterischen Mechanismen untersuchen.
- FU5  \label{fu5} beleuchtet die Möglichkeiten und Grenzen des Systems mittels qualitativer Analyse und SWOT-Analyse.
- FU6  \label{fu6} fragt nach der Beurteilung des Systems als Kompetenzerwerbssystem, wobei die Theoriearbeit hier eine Schlüsselrolle spielt.
- FU7  \label{fu7} schließlich entwickelt ein Kausalmodell und Handlungsempfehlungen basierend auf systemtheoretischen Ansätzen.

## 1.3 Stand der aktuellen Forschung

- [ ] Überblick über die bisherigen Studien und relevante Literatur zum Thema.
- [ ] legt den Stand der Forschung dar und entwickelt die Fragestellung. 

Die Untersuchung legt nahe, dass künftige Forschungen sich verstärkt auf die Analyse der Lernaktivitäten und deren Auswirkungen auf die Lernenden konzentrieren sollten. Die Autoren betonen insbesondere die Notwendigkeit, zukünftige Forschungsarbeiten darauf auszurichten, wie unterschiedliche CBL-Methoden in spezifischen medizinischen Bildungskontexten wirksam eingesetzt werden können.

> Der menschliche Bildungsprozess ist von einer ständigen Wechselwirkung zwischen grundlegenden emotionalen und kognitiven Bedürfnissen sowie den Unsicherheiten geprägt, die beim Lernen und der Kompetenzentwicklung auftreten. Bedürfnisse wie Bindung, Selbstwerterhöhung und die Vermeidung von Unlust bilden die Basis für eine dynamische Kausalkette, die das Lernverhalten antreibt. Aus den Bedürfnissen heraus entstehen Unsicherheiten im Lernprozess und in der Kompetenzmessung, die das Handeln der Lernenden prägen. Diese Handlungen zielen darauf ab, die Unsicherheiten zu verringern und das Bedürfnis nach Selbstverwirklichung zu befriedigen. In dieser kontinuierlichen Zirkulation beeinflussen sich Bedürfnisse, Konzepte und Handlungen wechselseitig und treiben den Lernprozess stetig voran.

### 1.3.1 Vorüberlegungen und Ausgangspunkt

### 1.3.2 Literaturrecherche

### 1.3.3 Forschungsstand und Forschungslücke

## 1.4 Gliederung der Arbeit

Die Struktur des vorliegenden Forschungsprojekts weist aufgrund der transdisziplinären Ausrichtung zwischen Bildungswissenschaft und Medizin eine besondere Komplexität auf, da verschiedene Disziplinen integriert und unterschiedliche wissenschaftliche Anforderungen berücksichtigt werden müssen. Um dieser Herausforderung gerecht zu werden, folgt der strukturelle Aufbau der Arbeit einer konsequenten Verschränkung der formalen Anforderungen sowohl der medizinischen als auch der kultur- und sozialwissenschaftlichen Rahmenbedingungen. Dies ermöglicht eine umfassende Bearbeitung des Themas, die den jeweiligen spezifischen Gegebenheiten beider Disziplinen gerecht wird.


Zum Abschluss der Einleitung wird ein Überblick über den Aufbau der Arbeit gegeben:

- **Kapitel 2: Theoretischer Hintergrund**
    
    - In diesem Kapitel werden die relevanten Theorien und Konzepte vorgestellt, die für das Forschungsthema von Bedeutung sind. Es werden zentrale Begriffe definiert und ein theoretisches Rahmenwerk entwickelt.
- **Kapitel 3: Stand der Forschung**
    
    - Hier wird der aktuelle Forschungsstand zum Thema dargestellt. Empirische Studien und relevante Literatur werden diskutiert, um eine Forschungsgrundlage zu schaffen und bestehende Forschungslücken zu identifizieren.
- **Kapitel 4: Methodik**
    
    - In diesem Kapitel wird die methodische Vorgehensweise beschrieben. Es wird erläutert, welche Methoden zur Datenerhebung und -analyse verwendet werden, um die Forschungsfragen zu beantworten.
- **Kapitel 5: Ergebnisse**
    
    - Die Ergebnisse der Forschung werden in diesem Kapitel präsentiert. Es wird darauf eingegangen, welche Daten erhoben wurden und welche Erkenntnisse sich daraus ergeben haben.
- **Kapitel 6: Diskussion**
    
    - In der Diskussion werden die Ergebnisse im Kontext des theoretischen Hintergrunds und des Forschungsstands interpretiert. Es wird reflektiert, inwiefern die Forschungsfragen beantwortet wurden und welche Implikationen sich daraus ergeben.
- **Kapitel 7: Fazit und Ausblick**
    
    - Im letzten Kapitel werden die zentralen Ergebnisse der Arbeit zusammengefasst. Es werden Schlussfolgerungen gezogen und ein Ausblick auf mögliche weiterführende Forschungsfragen und die praktische Relevanz der Ergebnisse gegeben.




\newpage
# 2 Theorieteil (25-30 Seiten)

(Fahr & Riegler, 2025; Strasser et al., 2025): zur aktuellen Darstellung

**Warum diese Struktur stimmig ist:**

- **Kausale Herleitung:** Bedürfnisse → Emotionen → persönliche Ereignisse. Dies bildet eine nachvollziehbare Kette, die direkt auf die Gestaltung von LMS übertragen werden kann.
- **Brückenbildung:** Die Verbindung zwischen bildungswissenschaftlichen Konzepten (Konstruktivismus, Digitalisierung) und psychologischen Aspekten (Bedürfnisse und Emotionen) ist explizit und nicht nur ein Exkurs.
- **Praxisbezug:** Es wird aufgezeigt, wie diese theoretischen Überlegungen in der Gestaltung digitaler Lernumgebungen praktisch umgesetzt werden können.

**Begründung der Aufteilung:**

- **Fokus auf Psychologie:** Da der Schwerpunkt auf der Herleitung liegt, dass **Bedürfnisse alle Lernprozesse durchziehen**, wird der Abschnitt zu psychologischen Grundannahmen etwas umfangreicher ausfallen. Dies stärkt die Argumentation und bietet Raum für die Integration relevanter Studien und Modelle.
- **Bildungswissenschaftliche Verortung:** Dieser Teil bietet die theoretische Grundlage, die den Rahmen setzt, und sollte nicht zu kurz ausfallen, um die Anschlussfähigkeit an bildungstechnologische Modelle zu gewährleisten.
- **Praktische Übertragung (Synergieeffekte):** Die Synergie zwischen Theorie und Praxis rundet den Theorieteil ab und gibt einen klaren Transferhinweis auf die Gestaltung von LMS, benötigt aber weniger Raum als die theoretischen Ausführungen.

## 2.1 Bildungswissenschaftlich-theoretische Verortung (ca. 10-12 Seiten) 

- [ ] Vorstellung der zentralen Theorien und Modelle, die für das Forschungsthema relevant sind.
 
Hier würde ich dann auch bemerken, dass sie sich bei den Forschung Unternehmen um die abstrakte theoretische Bildungswissenschaften Grundlagenforschung handelt, mit all den Konsequenzen fehlende MPW, viele Wahrscheinlichkeitsannahmen, was auch selbstverständlich gut begründet wird.


In diesem Abschnitt werden die grundlegenden Theorien und Modelle dargestellt, die für die Gestaltung digitaler Lernräume relevant sind. Dabei wird insbesondere auf die systemisch-konstruktivistische Perspektive und die Bedeutung von Bedürfnissen als Treiber des Lernprozesses eingegangen.

In diesem Abschnitt wird der Begriff der Digitalen Bildung \label{Digitale_Bildung} eingeführt, der im weiteren Verlauf noch häufiger auftauchen wird.

Ein Learning Management System (LMS) \label{sec:lms} wird häufig zur Verwaltung von Lerninhalten verwendet.

Massive Open Online Courses (MOOCs) \label{sec:mooc} sind Plattformen, die es vielen Teilnehmern ermöglichen, gleichzeitig an Kursen teilzunehmen.

### 2.1.1 Einleitung und Übersicht zur Theorie (2-3 Seiten)


### 2.1.2 Systemisch-konstruktivistische Theorie (3-4 Seiten)

Hier wird der theoretische Rahmen der digitalen Bildung beschrieben, mit Fokus auf:

- Systemisch-konstruktivistische Perspektive auf digitale Lernräume********
- Technologiedefizit der Pädagogik und die Rolle von Bedürfnissen als Brücke zur Motivation
- Begriff der Digitalen Bildung →→ Einführung und Bezug zur Gestaltung von LMS


Grund der unterschiedlichen Lehr-Lern-Ansätze ist die Beweisführung, dass unterschiedlichste Lernumgebungen unterschiedlichste Auswirkungen auch in einem technisch immer gleichen System haben. 

1: "Instruktional",

2: "Kognitivistisch",

3: "Behavioristisch",

4: "Humanistisch",

5: "Konstruktivistisch",

6: "Soziokulturell",

7: "Systemisch"


### 2.1.3 Bildungstechnologie und Digitalität (3-4 Seiten)

## 2.2 Psychologische Grundannahmen (ca. 12-14 Seiten)

Dieser Abschnitt leitet die psychologischen Mechanismen her, die sich auf Lernprozesse auswirken. Es wird gezeigt, wie sich Bedürfnisse als Ausgangspunkt aller Lernprozesse manifestieren und in weiteren Schritten Emotionen und persönliche Erfahrungen formen.

### 2.2.1 Bedürfnisse als Grundlage digitaler Lernprozesse (4-5 Seiten)

- Bedürfnisse als universelle Triebkraft des Lernens
- Selbstbestimmungstheorie (Deci & Ryan) – Wie Autonomie, Kompetenz und soziale Eingebundenheit Lernprozesse antreiben.
- Bedürfnisse als Gestaltungsprinzip für digitale Lernumgebungen →→ Wie können LMS diese Bedürfnisse adressieren (z.B. individualisierte Lernwege)?

[[Bedürfnis]]

Motivation schwer zu messen und eigentlich kein Spielfeld der Lehrkräfte, da Psychologie => Neugier als Bedürfnis herleiten

[[Neugier]], [[Neugier-Tensor]]
### 2.2.2 Emotionen als Vermittler (4-5 Seiten)

- Emotionen als Regulatoren der Bedürfnisbefriedigung****
- Verbindung von Emotionen und Lernerfolg →→ Wie beeinflussen emotionale Reaktionen die Interaktion mit LMS (z.B. Frustration bei fehlender Usability oder Freude durch Erfolgserlebnisse)?
- Gestaltung emotional unterstützender digitaler Lernumgebungen**

[[Emotionen]], 
### 2.2.3 Persönliche Ereignisse und Lernerfahrungen (3-4 Seiten)

- Lebensweltliche Ereignisse als Verstärker von Emotionen und Bedürfnissen
- Persönliche Erlebnisse als Grundlage für nachhaltiges Lernen
- Integration persönlicher Erfahrungen in LMS (z.B. E-Portfolios, reflektierendes Lernen)

[[Persönliche Ereignisse]]


## 2.3 Synergieeffekte: Von Bedürfnissen zu LMS-Design (ca. 3-4 Seiten)

Hier wird die Verbindung zwischen bildungswissenschaftlichen Theorien und den psychologischen Prozessen konkretisiert.

- Wie Bedürfnisse, Emotionen und Ereignisse als didaktische Leitprinzipien für digitale Lernräume dienen
- Systemisches LMS-Design: Bedürfnisse als Ausgangspunkt für die technische und didaktische Gestaltung

Verbindung der Theorien und Ableitung für die Praxis: **3-4 Seiten**


\newpage

# 3 Beschreibung Forschungsgegenstand

Text

## 3.1 Kontext des Forschungsgegenstandes

Text

## 3.2 Entwicklung des Forschungsgegenstandes

Seit 2017 wird das in dieser Arbeit betrachtete digitale Learning-Management-System (LMS) im Ausbildungsbereich angewendet. Die Entwicklung und Implementierung des Systems basieren auf verschiedenen wissenschaftlichen Arbeiten und Studienleistungen, die an mehreren Hochschulen durchgeführt wurden. Die vollständige Umsetzung der curricularen Planung wurde maßgeblich durch die pandemiebedingte Notwendigkeit zur Digitalisierung und Flexibilisierung von Lehr-Lern-Prozessen beschleunigt. Dies führte zu einer Erweiterung und verstärkten Nutzung des LMS, insbesondere zur Unterstützung von Fern- und Hybridunterrichtsformaten.

Zur Qualitätssicherung und kontinuierlichen Weiterentwicklung des Systems wurden begleitend Evaluationen der Lehrveranstaltungen durchgeführt. Dabei kamen etablierte Evaluationsinstrumente zum Einsatz, die speziell für den Bildungs- und Trainingsbereich in High-Responsibility-Umgebungen entwickelt wurden. Ein zentrales Instrument ist das „Training Evaluation Inventory (TEI)“ von Ritzmann et al. (2014), das sich in verschiedenen Kontexten bewährt hat, in denen Teams unter hoher Verantwortung agieren. Nach aktuellem Forschungsstand stellt das TEI eine der wenigen validierten Methoden dar, die auf den Ausbildungsbereich in Gesundheitsberufen übertragbar sind.

Ergänzend wurde in der Ausgangsphase der Entwicklung das „Evaluating Training Programs“-Modell von Kirkpatrick (1998) herangezogen, das als grundlegender Rahmen für die Evaluation von Trainingsmaßnahmen dient. Das TEI baut auf diesem Modell auf und erweitert es um spezifische Aspekte, die für den Einsatz in dynamischen und anspruchsvollen Ausbildungsumgebungen von Bedeutung sind.

## 3.3 Architektur als Learning-Management-System


Text

## 3.4 Architektur als Arbeits- und Organisationsinstrument 
Text

## 3.5 ePortfolio als ...

Text

## 3.6 Technische Rahmenbedingungen
Text


(Dyrna & Günther, 2021) als technische Klassifizierung 

\newpage
# 4 Methodik

Überleitung von Kapitel 3 und Zusammenfassung Kapitel 4, inkl. Inhalt

Kapitel 4 beschreibt eine Methodik, die vollständig auf den Forschungsfragen basiert und durch systemtheoretische Prinzipien strukturiert ist. Die Kombination aus geplanten Methoden (z. B. Literaturanalyse, Eye-Tracking) und methodischen Erweiterungen (Python-Simulation) zeigt die Flexibilität und Innovationskraft der Arbeit.

## 4.1 Forschungsparadigma (ca. 2–3 Seiten)

Methodenkompetenz in den Human- und Sozialwissenschaften umfasst die Fähigkeit, empirische Studien nicht nur zu lesen und zu interpretieren, sondern diese auch selbstständig durchzuführen, um systematische und nachvollziehbare Erkenntnisse zu generieren. Dabei etablierten sich drei zentrale Forschungsparadigmen, die sich in ihren erkenntnistheoretischen Grundlagen und methodischen Logiken unterscheiden: (a) das quantitative Paradigma, basierend auf dem kritischen Realismus, (b) das qualitative Paradigma, verankert im Sozialkonstruktivismus, sowie (c) das Mixed-Methods-Paradigma, das im Pragmatismus wurzelt. Während das quantitative Paradigma einen linear-strukturierten Forschungsprozess postuliert, der auf zu überprüfende Hypothesen aufbaut, bildet das qualitative Paradigma einen zirkulären, wenig strukturierten Forschungsprozess mit offenen Forschungsfragen ab. Mit dem Mixed-Methods-Ansatz lassen sich hingegen komplexere, lineare sowie nichtlineare Vorhaben bearbeiten, die zudem mit verschiedenen Teilprozessen verbunden werden können. Die Differenzierung der Paradigmen erweitert sich auch um die Rollenperspektive der Forschenden, die in Abhängigkeit vom untersuchten Forschungsgegenstand reflektiert werden muss. Entscheidend für die Wahl der Forschungslogik ist nicht, welche Daten (z.B. numerische oder textliche) vorliegen, sondern mit welchem Vorgehen die vorliegenden oder noch zu erzeugenden Daten methodisch zu bearbeiten sind. Das Begründungsgebot nimmt hierbei im wissenschaftlichen Arbeiten eine zentrale Stellung ein, da es die Wahl der Forschungslogik und die Bearbeitung von Daten methodisch legitimiert. [@doering2023Esi, S. 4-5, 7; @doering2023Wge, S. 32-33]

Methodisch herausfordernd in dieser Arbeit ist die Auflösung eines Dilemmas durch Verknüpfung der unterschiedlichen Facetten dieses bildungstheoretischen Forschungsvorhabens. Quantitative Daten, bspw. aus dem Eye-Tracking-Versuch und der begleitenden Umfrage, und qualitative Daten, bspw. die Ergebnisse aus der systematischen Literaturanalyse, sind miteinander in Bezug zu setzen, um übergeordnete Erkenntnisse zu generieren. Die Verwendung der beiden Paradigmen wird durch die Intention der Hauptforschungsfrage legitimiert, die Wissen um Muster und Regelmäßigkeiten im LMS erzeugen möchte. Insbesondere das vorgefundene Spannungsfeld von Subjektivität (Wahrnehmung der Akteure) und Objektivität (Kompetenzentwicklungssimulation) erfordert eine genauere methodische Betrachtung. Die sonst eher streng zugeordnete Forschungsmethodik, das quantitative Paradigma als deduktiv und das qualitative Paradigma als induktiv [@reinders2022uef, S. 157], greift hier zu kurz, da diese strikte Trennung die komplexe Wirkung des Forschungsgegenstands nicht abbilden kann.

Forschungstätigkeiten in Gesundheitskontexten stehen zudem vor der Herausforderung, unterschiedliche methodische Strömungen diverser Disziplinen für sich einzunehmen. Insbesondere der Umgang mit tradierten Forschungsparadigmen muss angesichts der Komplexität intradisziplinärer Forschungstätigkeiten beantwortet werden. Gerade Komplexität, vielfältige Disziplinen und unterschiedliche Ressourcen sind miteinander in Einklang zu bringen. Damit dies gelingt, können die jeweiligen Stärken und Chancen bisheriger Forschungsmethoden in einen neuen, interdisziplinären und generativen Kontext gestellt werden. [@niederberger2021Fgua, S. 4-5]

Zwar verbindet das Mixed-Methods-Paradigma die beiden zuvor genannten Ansätze, steht jedoch in der Kritik, dass diese epistemologisch unvereinbar seien (z.B. Inkommensurabilitäts-These in Verbindung mit der Komplementaritäts-These) und daher methodisch fragil bleiben. Hinzu kommt, dass der Mixed-Methods-Ansatz häufig pragmatisch verwendet wird, wodurch quantitative und qualitative Verfahren unreflektiert nebeneinanderstehen. Auch die strikte Trennung der Paradigmen – das quantitative Paradigma als deduktiv und das qualitative Paradigma als induktiv – greift zu kurz, da sie die notwendige Integration von Regelmäßigkeiten (quantitative Ebene) und subjektiven Kontexten (qualitative Ebene) verhindert. [@doering2023Wge]

Das hier beschriebene Forschungsvorhaben erfordert aufgrund seiner zirkulären Komplexität einen mehrdimensionalen Ansatz, der die bisherigen Ebenen systematisch aufeinander bezieht. Wie Rosenthal und Witte (2020, S. 198-199) betonen, wird die Wahl der Methodik durch die Anerkennung der Berechtigung unterschiedlicher methodischer Zugänge zur Erforschung sozialer Phänomene sowie durch die grundlagentheoretische Differenzierung zwischen quantitativen und qualitativen bzw. interpretativen Forschungsansätzen beeinflusst. In diesem Spannungsfeld versteht sich die vorliegende Arbeit als abstrakt-theoretische Grundlagenforschung. Damit soll der theoretische Anspruch eingelöst werden, methodische Vielfalt anzuerkennen und gleichzeitig eine systematische Integration der Perspektiven zu ermöglichen.

Die Auflösung des vorliegenden forschungsparadigmatischen Dilemmas erfolgt durch den Zugang zum Forschungsgegenstand über die konsequente Ableitung der Methoden aus den Forschungsfragen. Dieses Vorgehen ermöglicht nicht nur eine zielgerichtete Methodenauswahl, sondern auch eine Komplexitätsreduktion, die der Mehrdimensionalität des Forschungsgegenstandes gerecht wird und gleichzeitig die Stärken bestehender Methoden integriert.

### 4.1.1 Systemischer, forschungsfragengeleiteter Ansatz

Die Methodik dieser Arbeit basiert vollständig auf den Forschungsfragen (FU1–FU7), die aus dem Erkenntnisinteresse und dem bestehenden LMS-Produkt abgeleitet wurden. Die Forschungsfragen strukturieren und leiten alle methodischen Entscheidungen sowie die Analysen.

Um der zirkulären Komplexität des Forschungsgegenstands gerecht zu werden, folgt die Umsetzung systemtheoretischen Prinzipien:

1. **Interdependenz**:
    
    - Die Forschungsfragen sind eng miteinander verknüpft und erzeugen Wechselwirkungen zwischen den **qualitativen und quantitativen Daten**.

1. **Emergenz**:
    
    - Neue Erkenntnisse entstehen durch die **Verknüpfung der Ergebnisse** aus Literaturanalysen, Simulationen und empirischen Daten wie dem Eye-Tracking-Experiment.

1. **Rückkopplung**:
    
    - Die Ergebnisse aus den Analysen fließen **iterativ** in die Methodik zurück, wodurch der Forschungsprozess dynamisch und anpassungsfähig gestaltet wird.

Die Umsetzung dieses Ansatzes erfolgt durch:

- **Ableitung der Methoden aus den Forschungsfragen**:
    
    - Jede Forschungsunterfrage (FU) bestimmt die **Methodenauswahl**, die passgenau auf ihre spezifischen Anforderungen abgestimmt ist.

- **Integration qualitativer und quantitativer Verfahren**:
    
    - Durch die **systemische Verknüpfung** von qualitativen Daten (z.B. aus der Literaturanalyse) und quantitativen Daten (z.B. aus Simulationen und Eye-Tracking) entsteht eine **mehrdimensionale Betrachtung** des 
    - Forschungsgegenstands.

- **Methodische Passgenauigkeit**:
    
    - Die Methoden werden **funktional** kombiniert, um sowohl **subjektive Perspektiven** (Wahrnehmung der Akteure) als auch **objektive Strukturen** (Muster und Regelmäßigkeiten) abzubilden.

- **Komplexitätsreduktion**:
    
    - Die zielgerichtete Auswahl und Kombination der Methoden ermöglicht es, die Komplexität des Forschungsgegenstands auf ein **analytisch erfassbares Niveau** zu reduzieren.

- **Emergenz neuer Erkenntnisse**:
    
    - Durch die iterative Rückkopplung und systemische Verknüpfung der Ergebnisse werden **neue Zusammenhänge** sichtbar, die über die isolierte Anwendung einzelner Methoden hinausgehen.

### 4.1.2 Methodische Konsequenzen der Forschungsfragen

- Die Forschungsfragen bestimmten:
  - Auswahl und Strukturierung der Literatur.
  - Entwicklung von Kategorien und Schlagworten zur thematischen Verknüpfung.
  - Kombination und Anpassung klassischer Methoden.
- **Begründung**:
  - Die Komplexität des digitalen Bildungsraums erforderte eine Methodenkombination, um die Forschungsfragen adäquat zu beantworten.

## 4.2 Forschungsdesign (ca. 3–4 Seiten)

### 4.2.1 Dynamischer, zirkulär-itterativer Forschungsprozess

- Forschungsprozess war iterativ und dynamisch:
  - Ergebnisse aus der Analyse wurden zurück in den Prozess gespiegelt.
  - Anpassungen, z. B. die Python-Simulation, wurden in späteren Phasen integriert.
- **Forschungsprozess in sechs Phasen**:
  1. **Orientierung und Planung**:
     - Entwicklung der Forschungsfragen.
     - Erstellung des Exposés und erste Strukturierung der Methodik.
  2. **Literatur- und Datenrecherche**:
     - Systematische Literaturanalyse mit KI-Unterstützung.
     - Sammlung relevanter Quellen und erste Kategorisierung.
  3. **Empirische Erhebung**:
     - Durchführung der Umfrage zu digitalen Kompetenzen.
     - Planung und Umsetzung des Eye-Tracking-Experiments.
  4. **Modellierung und Synthese**:
     - Entwicklung und Anwendung der Python-Simulation.
     - Verknüpfung der Ergebnisse aus Literatur, Umfragen und Eye-Tracking.
  5. **Schreibprozess**:
     - Ausarbeitung der Theoriekapitel, Methodik und Ergebnisdarstellung.
     - Rückkopplung der Ergebnisse in die Forschungsfragen.
  6. **Abschluss und Veröffentlichung**:
     - Endredaktion, Einreichung und geplante Publikation.

### 4.2.2 Forschungsunterfragen und ihre Methoden

```{=latex}
\begin{table}[!htbp]
\centering
\renewcommand{\arraystretch}{1.2}
\caption{Tabellarische Darstellung der Forschungsunterfragen (FU) und Methoden}
\label{tab:methoden_FU}
{\fontsize{8}{10}\selectfont
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}m{3cm}|X|}
\hline
\textbf{Forschungsunterfrage} & \textbf{Methoden} \\ \hline
\textbf{FU1: Akzeptanz und Nützlichkeit} & Systematische Literaturanalyse, KI-gestützte Analyse zur Untersuchung der Benutzerfreundlichkeit und Nützlichkeit von LMS. \\ \hline
\textbf{FU2a: Effekt auf Lernende} & Monte-Carlo-Simulation und 3D-Kompetenzmessmodell zur Modellierung der Kompetenzentwicklung und Unsicherheiten im Lernprozess. \\ \hline
\textbf{FU2b: Effekt auf Lehrende} & Umfrage zur digitalen Kompetenz von Lehrenden und ergänzende Literaturanalyse zur Erfassung der Herausforderungen und Bedürfnisse. \\ \hline
\textbf{FU3: Didaktische und technologische Merkmale} & Literaturanalyse, Eye-Tracking-Experiment und systemische Analyse zur Untersuchung der didaktischen und technischen Gestaltung von LMS. \\ \hline
\textbf{FU4a: Bildungswissenschaftliche Mechanismen} & Literaturanalyse zu bildungswissenschaftlichen Modellen und Mechanismen. \\ \hline
\textbf{FU4b: Technisch-gestalterische Mechanismen} & Eye-Tracking-Experiment mit begleitender Umfrage zur Analyse der Wahrnehmung und Navigation in LMS. \\ \hline
\textbf{FU5: Möglichkeiten und Grenzen} & Synthese aller Ergebnisse und theoretische Reflexion zur Identifikation von Potenzialen und Limitationen von LMS. \\ \hline
\textbf{FU6: LMS als Kompetenzerwerbssystem} & Systematische Literaturrecherche (500 Quellen) und systemische Bewertung der LMS als Kompetenzerwerbssystem. \\ \hline
\textbf{FU7: Erweiterung von Kausalgesetzen} & Python-Simulation zur Analyse der Korrelationen zwischen Forschungsunterfragen sowie Schlagwort- und Kategorisierungsanalyse. \\ \hline
\end{tabularx}
}
\vspace{0.3cm}
\begin{quote}
{\fontsize{8}{10}\selectfont
Die Tabelle zeigt die Zuordnung der Methoden zu den Forschungsunterfragen. Sie umfasst systematische Literaturanalyse, empirische Erhebungen (Umfragen, Eye-Tracking) und modellbasierte Ansätze (Simulation), die flexibel kombiniert wurden, um die Forschungsfragen adäquat zu beantworten.
}
\end{quote}

\end{table}

```

## 4.3 Datenerhebung und -aufbereitung (ca. 4–5 Seiten)

### 4.3.1 Literaturanalyse und KI-gestützte Methoden
- Systematische Literaturanalyse:
  - Ziel: Identifikation relevanter Arbeiten zur Beantwortung der Forschungsfragen.
  - Methode: Unterstützung durch KI zur Kategorisierung und Analyse.
- Entwicklung von Kategorien und Schlagworten:
  - Ziel: Thematische Verknüpfung der Literatur mit den Forschungsfragen.

### 4.3.2 Empirische Methoden
- **Umfrage zu digitalen Kompetenzen**:
  - Ziel: Analyse der Kompetenzen, Herausforderungen und Bedarfe von Lehrenden.
  - Methode: Kombination aus quantitativen und qualitativen Elementen.
- **Eye-Tracking-Experiment**:
  - Ziel: Analyse der visuellen Wahrnehmung und Navigation in LMS.
  - Ergänzung durch begleitende Umfrage:
    - Ziel: Verknüpfung der Eye-Tracking-Daten mit subjektiven Eindrücken.

### 4.3.3 Simulation und Datenintegration
- **Python-Simulation**:
  - Ziel: Analyse der Korrelationen zwischen Forschungsunterfragen.
  - Ergebnis: Visualisierung der Interdependenzen und strukturellen Kopplungen.
- **Datenintegration**:
  - Verknüpfung der Ergebnisse aus Literatur, Umfragen, Eye-Tracking und Simulation.


## 4.4 Datenanalyse (ca. 4 Seiten)

### 4.4.1 Verknüpfung qualitativer und quantitativer Daten

- Integration qualitativer (Literatur, Umfragen) und quantitativer (Simulation, Eye-Tracking) Daten.
- Ziel: Systemische Analyse zur Identifikation von Rückkopplungseffekten und emergenten Strukturen.

### 4.4.2 Kategorien- und Schlagwortanalyse

- Ziel: Bildung und Analyse von Kategorien und Schlagworten.
- Methode: Sichtbarmachung thematischer Verbindungen zwischen Forschungsunterfragen.

### 4.4.3 Korrelation und Interdependenz

- Ziel: Analyse der Korrelationen zwischen Forschungsunterfragen mit der Python-Simulation.
- Ergebnis: Visualisierung der strukturellen Kopplungen und Interdependenzen.

### 4..4.4 

## 4.5 Reflexion der Methode (ca. 2 Seiten)

### 4.5.1 Methodische Stärken

- Forschungsfragengeleiteter Ansatz mit systemischer Perspektive.
- Kombination klassischer Methoden (Literatur, Simulation, Eye-Tracking) mit innovativen Ansätzen (KI, Python).

### 4.5.2 Methodische Herausforderungen und Limitationen

- Herausforderungen:
  - Retrospektive Integration einiger Methoden.
  - Entwicklung eines eigenen Paradigmas zur Bearbeitung der Forschungsfragen.
- Limitationen:
  - Komplexität der Datenintegration.
  - Abhängigkeit von KI-Tools und Simulationen.



\newpage

# 5 Ergebnisse

Hier beantwortest du jede der Forschungsfragen einzeln und führst die Leser durch deine empirischen Ergebnisse. Die Reihenfolge deiner Argumentation sollte auf den zentralen Wirkfaktoren basieren.

## 5.1 Zusammenfassung: Argumentationskette

1. **Neugier → Motivation → Engagement im LMS**:
    
    - Durch Nützlichkeit und Zugänglichkeit wird die Neugier angeregt, die wiederum die intrinsische Motivation steigert.
2. **Persönliche Ereignisse → Emotionale Unsicherheit → Einfluss auf Lernen und Resilienz**:
    
    - Persönliche Ereignisse beeinflussen die Lernleistung und die emotionale Stabilität. Ein LMS kann jedoch durch Flexibilität helfen, diese Störungen abzufedern.
3. **Kompetenzwahrnehmung → Selbstwirksamkeit → Lernerfolg**:
    
    - Die Wahrnehmung von Kompetenz stärkt die Selbstwirksamkeit und führt zu größerem Lernerfolg. LMS sollten Lernprozesse so strukturieren, dass diese Wahrnehmung gefördert wird.

## 5.2 Kausalkette

(Fahr & Riegler, 2025)

### 5.2.1 Neugier als Wirkfaktor

- **Argumentationskette**:
	1. Beginne mit dem Zusammenhang zwischen **Nützlichkeit und Zugänglichkeit** von LMS.
	2. Zeige, dass durch eine einfache Zugänglichkeit und nützliche Funktionen die **Neugier** der Lernenden gefördert wird.
	3. Leite her, dass die **Motivation** durch Neugier stark beeinflusst wird und dass dies ein zentraler Mechanismus ist, der den Umgang mit dem LMS und den Lernerfolg prägt.
- **Belege aus der Literatur**: Nutze Studien, die zeigen, dass Neugier ein Schlüsselfaktor für intrinsische Motivation und Engagement ist, z.B. aus der Selbstbestimmungstheorie (Deci & Ryan).

###  5.2.1 Persönliche Ereignisse als Wirkfaktor

- **Argumentationskette**:
    1. Führe zunächst ein, dass **persönliche Ereignisse** (berufliche/private Herausforderungen) Störfaktoren im Lernprozess sein können.
    2. Zeige, dass persönliche Ereignisse direkt die **emotionale Unsicherheit** und somit auch die Fähigkeit, sich auf das Lernen zu konzentrieren, beeinflussen.
    3. Argumentiere, dass LMS durch ihre Flexibilität in der Struktur dazu beitragen können, **Resilienz** zu fördern, indem sie den Lernenden ermöglichen, den Lernprozess individuell anzupassen.
- **Belege aus der Literatur**: Nutze Studien zur **emotionalen Unsicherheit** und zum Einfluss von **persönlichen Ereignissen** auf das Lernverhalten. Verweise auf Theorien zu Resilienz und emotionaler Intelligenz.


### 5.2.3 Kompetenz als Wirkfaktor

- **Argumentationskette**:
    1. Zeige den Zusammenhang zwischen dem LMS und der **Kompetenzentwicklung** der Lernenden auf.
    2. Verdeutliche, dass die **Selbstwahrnehmung von Kompetenz** ein Schlüsselfaktor für den Lernerfolg ist und dass LMS eine wichtige Rolle bei der Stärkung dieses Gefühls spielen.
    3. Erkläre, dass **Kompetenzwahrnehmung** und **Selbstwirksamkeit** die Lernbereitschaft und die tatsächliche Leistung beeinflussen.
- **Belege aus der Literatur**: Zitiere Theorien zur Selbstwirksamkeit (Bandura) und Literatur, die den Zusammenhang zwischen LMS-Nutzung und Kompetenzentwicklung belegt.


(Strasser et al., 2025)


Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat^[Fußnote].

oder: 

Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat [^1].

[^1]: So gehen Fußnoten auch


Die Darstellung der Ergebnisse beinhaltet die Anzahl der Beobachtungen und die statistische Sicherung anhand geeigneter Dokumentation. Die tabellarische Wiedergabe der Ergebnisse erlaubt in der Regel eine lückenlose Zusammenstellung der gewonnenen Informationen. Wird stattdessen die grafische Darstellung vorgezogen, so muss in jedem Fall eine Abbildungslegende hinzugefügt werden, die alle verwendeten Zeichen und Abkürzungen erläutert. Doppeldarstellungen (Tabellen und Grafiken mit gleichem Inhalt) sollten auf begründete Ausnahmen beschränkt bleiben, da sie gegen die Forderung verstoßen, die Ergebnisse konzentriert zu schildern und Längen und Wiederholungen möglichst zu vermeiden. Die Legende einer Abbildung steht grundsätzlich unter der Abbildung, die Überschrift einer Tabelle über der Tabelle. Überschriften bzw. Legenden müssen den in Tabelle oder Abbildung dargestellten Sachverhalt komplett erklären und alleinstehend verständlich sein. Untergliedern Sie die Darstellung in sinnvolle Unterkapitel.

```{=latex}
\begin{equation}
\nu = \frac{d K}{d t}
\addcontentsline{equ}{equations}{Bildungswirkfaktor als Ableitung der Kompetenzentwicklung}
\label{eq:Kompetenzentwicklung}
\end{equation}

\vspace{0.3cm}
\begin{quote}
{\fontsize{8}{10}\selectfont  
Diese Gleichung beschreibt den \textbf{Bildungswirkfaktor} $\nu$ als die Änderungsrate des Kompetenzniveaus $K$ über die Zeit $t$. Dabei steht $\frac{dK}{dt}$ für die erste Ableitung der Kompetenzentwicklung in Bezug auf die Zeit. Der Bildungswirkfaktor erfasst somit, wie schnell oder langsam sich Kompetenzen entwickeln und bietet eine dynamische Betrachtung der Kompetenzentwicklung.
}
\end{quote}
```


Ein Verweis auf die Formel ist möglich: Wie in Gleichung \ref{eq:Bildungswirkfaktor} dargestellt, sind die Ergebnisse schon recht komisch.

Wenn Sie hier Tabellen oder Abbildungen verwenden, die auch in der/n Publikation/en verwendet wurden, geben Sie bitte in der Legende korrekt die Quelle an: (_aus Autor et al., Jahr)_. Wenn Sie Tabellen oder Abbildungen unverändert wiederverwenden, benötigen Sie ggf. die Genehmigung des Inhabers des Copyrights (z. B. der Verlag der Zeitschrift). Wenn Sie die Tabellen oder Abbildungen modifizieren, zitieren Sie bitte (_modifiziert nach Autor et al., Jahr)_. Tabellen, Abbildungen oder Fotografien, die Sie für den Manteltext komplett neu erstellt haben, kennzeichnen Sie bitte mit (_eigene Darstellung_ oder _Foto: Name_.

Achten Sie bitte darauf, dass die eingefügten Abbildungen ausreichend vergrößert sind, so dass sie in der gedruckten Dissertation gut leserlich sind (Achsenbeschriftungen, Zahlen, Sternchen und andere Markierungen).

\newpage

# 6 Diskussion

Interpretation der Ergebnisse, Einordnung in den Forschungsstand.

In der Diskussion werden die Methoden und die Ergebnisse gewertet und mit denen anderer Arbeiten verglichen. Dies schließt auch eigene vorangegangene Arbeiten ein, die zu abweichenden Ergebnissen geführt haben. Abweichungen werden erörtert, wobei die in der Einleitung gestellten Fragen wieder aufgegriffen und nach Möglichkeit beantwortet werden. Untergliedern Sie die Darstellung in sinnvolle Unterkapitel.

Beispiel für den Aufbau der Diskussion

## 6.1 Kurze Zusammenfassung der Ergebnisse

- Fasse die Hauptergebnisse der Untersuchung kurz zusammen, indem du die Rolle der Wirkfaktoren (Neugier, persönliche Ereignisse, Kompetenz) im digitalen Bildungsraum nochmals aufgreifst.

## 6.2 Interpretation der Ergebnisse

- **Neugier und Motivation**: Stelle dar, wie Neugier den Lernprozess über die Motivation beeinflusst hat und wie LMS durch Nützlichkeit und Zugänglichkeit diese Neugier unterstützen können.
- **Persönliche Ereignisse**: Diskutiere, inwiefern persönliche Ereignisse als „Störgrößen“ betrachtet werden und welche Rolle Resilienzstrategien spielen.
- **Kompetenzwahrnehmung**: Erkläre, warum die Kompetenzwahrnehmung so wichtig ist und welche Mechanismen LMS nutzen können, um dieses Gefühl zu fördern.

### 6.1.1 Medizinische Interpretation

### 6.1.2 Bildungswissenschaftliche Interpretation

Bedeutung der Ergebnisse für die Bildungspraxis und Theorien.

Bedeutung der Ergebnisse für die medizinische Praxis.
## 6.3 Einbettung der Ergebnisse in den bisherigen Forschungsstand

- Setze deine Ergebnisse in den Kontext bestehender Studien. Zeige, wo deine Ergebnisse die bestehenden Theorien stützen oder ergänzen, und wo sie neue Erkenntnisse bieten.

(Fallon & Pylkkänen, 2024)

## 6.4 Stärken und Schwächen der Studie(n)

Setzen Sie sich an dieser Stelle kritisch mit der internen Validität Ihrer Studienergebnisse auseinander (Genauigkeit und Angemessenheit der Studienmethodik) und beurteilen Punkt für Punkt, warum Sie die Ergebnisse trotz eventueller Schwächen für valide halten.

- Reflektiere die Stärken deiner Untersuchung, wie etwa die breite Datenbasis und die detaillierte Analyse der Wirkfaktoren.
- Besprich mögliche Schwächen, etwa methodische Einschränkungen oder die Generalisierbarkeit der Ergebnisse auf andere Bildungsbereiche.

Sodann setzen Sie sich mit der externen Validität Ihrer Studienergebnisse kritisch auseinander. Inwieweit können die Studienergebnisse verallgemeinert werden? Begründen Sie Ihre Aussagen zur Generalisierbarkeit der Ergebnisse Punkt für Punkt.

## 6.5 Implikationen für Praxis und/oder zukünftige Forschung

Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Die Preise und Lagerbestände der Produkte sind in Tabelle \ref{tab:preisuebersicht} aufgeführt.

- **Für die Praxis**: Zeige, wie die Ergebnisse praktisch in der Gestaltung von LMS umgesetzt werden könnten, um Neugier, Motivation und Kompetenzentwicklung zu fördern.
- **Für die Forschung**: Zeige mögliche zukünftige Forschungsrichtungen auf, etwa die genauere Untersuchung der Rolle von persönlichen Ereignissen im Bildungsprozess oder die Entwicklung adaptiver Lernsysteme, die auf diese Wirkfaktoren eingehen.



Interpretation der Ergebnisse, Einordnung in den Forschungsstand.

In der Diskussion werden die Methoden und die Ergebnisse gewertet und mit denen anderer Arbeiten verglichen. Dies schließt auch eigene vorangegangene Arbeiten ein, die zu abweichenden Ergebnissen geführt haben. Abweichungen werden erörtert, wobei die in der Einleitung gestellten Fragen wieder aufgegriffen und nach Möglichkeit beantwortet werden. Untergliedern Sie die Darstellung in sinnvolle Unterkapitel.



Weitere Forschungsvorhaben zur Falsifikation: Grundlagen der Fundamentalgleichungen 

->> 2.3 Empirische Überprüfung und Weiterentwicklung|Forschungen zur Bildungsmechnik <<-
-> hier ausführen <-




## 6.6 Limitationen

- [ ] Reflexion über die Grenzen der gewählten Methodik und die Herausforderungen bei der Integration mehrerer Wissenssysteme.

## ggf. 6.7 Transdisziplinäre Reflexion

- [ ] Wie die verschiedenen Disziplinen zusammenwirken und welche Erkenntnisse durch die transdisziplinäre Herangehensweise gewonnen wurden.


\newpage

# 7 Conclusio

## 7.1 Zusammenfassung der zentralen Erkenntnisse

- [ ] Zentrale Ergebnisse und deren Bedeutung für beide Disziplinen.

Schlussfolgerung

Die vorliegende Analyse zeigt deutlich, dass der Werkzeuggebrauch, der in der prähistorischen Zeit mit einfachen Instrumenten wie dem Faustkeil begann, sich über Jahrtausende hinweg fortentwickelt hat und heute in digitalen Werkzeugen wie Learning-Management-Systemen mündet. Diese Entwicklung ist kein isolierter technologischer Fortschritt, sondern spiegelt eine tiefe, evolutionär verankerte menschliche Neigung wider, Werkzeuge zu nutzen, um die eigenen Bedürfnisse zu erfüllen und soziale Kooperation zu fördern. Ob in prähistorischen Gemeinschaften, in denen Werkzeuge soziale Bindungen stärkten und das Überleben sicherten, oder in modernen digitalen Lernumgebungen, die den Austausch von Wissen und die persönliche Verantwortungsübernahme unterstützen – der Mensch hat stets nach Wegen gesucht, seine Umwelt zu gestalten und zu kontrollieren.

Letztlich verdeutlicht die Betrachtung, dass digitale Bildungsräume, wie sie heute existieren, auf den gleichen Prinzipien basieren wie die frühesten Formen menschlicher Werkzeugnutzung: Sie dienen der sozialen Interaktion, der gemeinsamen Problemlösung und der Förderung individueller Kontrolle. Damit schließt sich der Kreis von den Ursprüngen des Werkzeuggebrauchs in der Menschheitsgeschichte bis zu den digitalen Systemen unserer Zeit, die weiterhin dazu beitragen, zentrale menschliche Bedürfnisse zu erfüllen und Lernprozesse in neuen Formen zu ermöglichen.

Zusammenfassend zeigte diese Arbeit, dass die Implementierung von Learning-Management-Systemen in der Ausbildung von Gesundheitsberufen einen signifikanten Einfluss auf die Kompetenzentwicklung und die Motivation der Lernenden hat. Die Untersuchung hat wichtige Erkenntnisse zu den Wirkfaktoren Neugier, persönliche Ereignisse und Kompetenzwahrnehmung geliefert, die das Potenzial haben, künftige didaktische Konzepte zu bereichern.

## 7.2 Empfehlungen für Praxis und Forschungsdesiderata

- [ ] Vorschläge zur Weiterentwicklung von Methoden und Erkenntnissen in der Praxis und Wissenschaft.

Obwohl die Studie wertvolle Einblicke bietet, bleiben einige Fragen offen, insbesondere in Bezug auf die langfristigen Auswirkungen digitaler Lernsysteme auf die berufliche Praxis. Weitere Forschung ist erforderlich, um die genauen Mechanismen zu verstehen, durch die persönliche Ereignisse die Lernbereitschaft beeinflussen.

Zukünftig könnten diese Ergebnisse dazu beitragen, personalisierte Lernumgebungen zu entwickeln, die flexibel auf die individuellen Bedürfnisse der Lernenden eingehen. Die Weiterentwicklung adaptiver Technologien könnte neue Möglichkeiten für eine ganzheitliche Kompetenzförderung eröffnen.

Abschließend bleibt festzuhalten, dass die digitale Transformation in der Bildung eine fortwährende Herausforderung, aber auch eine Chance darstellt, das Lernen nachhaltiger, flexibler und an den Bedürfnissen der Lernenden ausgerichtet zu gestalten.

Hier fasst du die Ergebnisse und Implikationen zusammen.

\newpage

\pagestyle{plain}

# Anhang

\newpage

# Verzeichnis Forschungsfragen

Hauptforschungsfrage \dotfill \pageref{fh}

Forschungsunterfrage 1 \dotfill \pageref{fu1}

Forschungsunterfrage 2a \dotfill \pageref{fu2a}

Forschungsunterfrage 2b \dotfill \pageref{fu2b}

Forschungsunterfrage 3 \dotfill \pageref{fu3}

Forschungsunterfrage 4a \dotfill \pageref{fu4a}

Forschungsunterfrage 4b \dotfill \pageref{fu4b}

Forschungsunterfrage 5 \dotfill \pageref{fu5}

Forschungsunterfrage 6 \dotfill \pageref{fu6}

Forschungsunterfrage 7 \dotfill \pageref{fu7}

\newpage

# Verzeichnis zentraler Begriffe
\label{Verzeichnis_zentraler_Begriffe}

Digitale Bildung \dotfill \pageref{Digitale_Bildung}

Learning Management System \dotfill \pageref{sec:lms}

Massive Open Online Course \dotfill \pageref{sec:mooc}

\newpage

# Eidesstattliche Versicherung

„Ich, Jochen Hanisch-Johannsen, versichere an Eides statt durch meine eigenhändige Unterschrift, dass ich die vorgelegte Dissertation mit dem Thema:

\vspace{1 cm}

> **Wirkgefüge im digitalen Bildungsraum**

> Eine Untersuchung der Merkmale, Effekte, Mechanismen und Reaktionen von Learning-Management-Systemen am Beispiel der Lehre in Gesundheitsberufen

> **Interactional Frameworks in the Digital Educational Space**

> An Exploration of the Characteristics, Effects, Mechanisms, and Responses of Learning Management Systems Using the Example of Healthcare Education

\vspace{1 cm}

selbstständig und ohne nicht offengelegte Hilfe Dritter verfasst und keine anderen als die angegebenen Quellen und Hilfsmittel genutzt habe.

Alle Stellen, die wörtlich oder dem Sinne nach auf Publikationen oder Vorträgen anderer Autoren/innen beruhen, sind als solche in korrekter Zitierung kenntlich gemacht. Die Abschnitte zu Methodik (insbesondere praktische Arbeiten, Laborbestimmungen, statistische Aufarbeitung) und Resultaten (insbesondere Abbildungen, Graphiken und Tabellen) werden von mir verantwortet.

Meine Anteile an etwaigen Publikationen zu dieser Dissertation entsprechen denen, die in der untenstehenden gemeinsamen Erklärung mit dem/der Erstbetreuer/in, angegeben sind. Für sämtliche im Rahmen der Dissertation entstandenen Publikationen wurden die Richtlinien des ICMJE (International Committee of Medical Journal Editors; [www.icmje.og](http://www.icmje.og)) zur Autorenschaft eingehalten. Ich erkläre ferner, dass ich mich zur Einhaltung der Satzung der Charité – Universitätsmedizin Berlin zur Sicherung Guter Wissenschaftlicher Praxis verpflichte.

Weiterhin versichere ich, dass ich diese Dissertation weder in gleicher noch in ähnlicher Form bereits an einer anderen Fakultät eingereicht habe.

Die Bedeutung dieser eidesstattlichen Versicherung und die strafrechtlichen Folgen einer unwahren eidesstattlichen Versicherung (§§156, 161 des Strafgesetzbuches) sind mir bekannt und bewusst.“

\vspace{3 cm}

Datum                                                 Unterschrift

\newpage

# Literaturverzeichnis

