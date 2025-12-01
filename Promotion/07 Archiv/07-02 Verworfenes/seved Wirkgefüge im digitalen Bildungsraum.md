---
tags:
  - Charité_Universitätsmedizin-Berlin
  - Dissertation
geometry: "left=2.5cm, right=2.5cm, top=2.5cm, bottom=1.0cm, includefoot, footskip=1.5cm"
papersize: a4
output: 
  pdf_document:
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
\begin{table}[h!]
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
\begin{table}[h!]
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

Der Zitationsstil dieser Arbeit folgt der 7. Ausgabe des APA-Zitationsstils. Zur Verwaltung der Zitate wird die Software Zotero (Version 6.0.37) verwendet. Sämtliche Referenzen sind als BibLaTeX-Einträge angelegt und beim Kompilieren des Dokuments in den finalen Text integriert.

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

## Hinweise zur Compliance

|                                |                                                                                                                           |                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **Unternehmen / Person**       | **Anteil / Produkt**                                                                                                      | **Betrag / Leistung** |
| Netmountains®                  |                                                                                                                           |                       |
| DRK-Bildungszentrum Düsseldorf | Eye-Tracking<br><br>Ansprache der Notfallsanitäter:innen-Auszubildenden<br><br>Räumlichkeiten und IT-Ausstattung (Laptop) | Sachleistung          |
| Soon-Systems GmbH              | Moodle-Plattform                                                                                                          | Sachleistung          |


\newpage
# Abstrakt

Bitte fügen Sie hier die von Ihnen selbst verfasste **deutsche Zusammenfassung** Ihrer Dissertation (max. 3.000 Zeichen inkl. Leerzeichen) ein. Diese darf nicht identisch mit der Zusammenfassung Ihrer Publikation sein, sondern muss darüberhinausgehend Ihre gesamte Promotionsarbeit (Manteltext und Publikation/en) zusammenfassen.
# Abstract

Bitte fügen Sie hier das selbst verfasste **englische Abstract** Ihrer Dissertation (max. 3.000 Zeichen inkl. Leerzeichen) ein. Dieses darf nicht identisch (auch nicht umformuliert) mit dem Abstract Ihrer Publikation sein, sondern muss darüberhinausgehend Ihre gesamte Promotionsarbeit (Manteltext und Publikation/en) zusammenfassen.

\newpage

\pagestyle{fancy}

# 1 Einleitung (~10–15 Seiten)
\label{1}

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
\label{1-1}

### 1.1.1 Erkenntnisinteresse
\label{1-1-1}

- **Erkenntnisinteresse**: Was willst du mit der Forschung herausfinden und warum ist das relevant?

Das zentrale Erkenntnisinteresse dieser Arbeit besteht darin, zu untersuchen, wie Lern- und Kompetenzentwicklungsprozesse im Gesundheitswesen durch den Einsatz von Learning-Management-Systemen (LMS) beeinflusst werden und welche Rolle dabei sowohl medizinische als auch bildungswissenschaftliche Faktoren spielen. Besonderes Augenmerk liegt auf der Frage, wie bildungswissenschaftliche Konzepte zur Förderung von Kompetenzentwicklung in der medizinischen Aus- und Weiterbildung beitragen können. Darüber hinaus soll erforscht werden, wie transdisziplinäre Ansätze zur Verbesserung von Lernprozessen und der Wissensvermittlung in der medizinischen Praxis beitragen können.

### 1.1.2 Problemstellung
\label{1-1-2}

 xxxxx Weiter mit Ausgangsort und Vorüberlegungen xxxxxxxx


- **Problemstellung**: Welches spezifische Problem adressierst du und welche wissenschaftliche oder praktische Lücke besteht?

### 1.1.3 Relevanz des Themas
\label{1-1-3}


- **Relevanz des Themas**: Warum ist das Thema aus medizinischer und bildungswissenschaftlicher Perspektive relevant?

 - [ ] Beschreibung des zentralen Problems, das in der Arbeit behandelt wird.
 - [ ] Was ist die zentrale Herausforderung im digitalen Bildungsraum?
 - [ ] Hier könntest du darauf eingehen, dass LMS zwar nützlich und zugänglich sind, aber dass die Nutzung von LMS durch individuelle Faktoren (Neugier, Kompetenzwahrnehmung, persönliche Ereignisse) beeinflusst wird.
- [ ] Erklärung, warum das Thema sowohl für die Wissenschaft als auch für die Praxis bedeutsam ist.
- [ ] Eher deskriptiv und auf Grundlage von Statista



Um dir eine klare Struktur für die Argumentationskette und die Reihenfolge der Themen zu bieten, ist es wichtig, deine Wirkfaktoren (Neugier, persönliche Ereignisse, Kompetenz) und deren Bezug zum LMS schrittweise und logisch aufzubauen. Hier ist eine mögliche Orientierung, wie du deine Argumentation innerhalb der Dissertation gliedern kannst, damit sie klar, konsistent und dem Titel „Wirkgefüge im Digitalen Bildungsraum“ gerecht wird.  

Indizien:

- Ericsson, C. R., Rudman, A., Lindström, V., & Nordquist, H. (2024). ‘We are expected to be problem solvers’—Paramedics’ performance expectations through the lens of organizational socialization: An interview study. _Nursing Open_, _11_(9), e70014. [https://doi.org/10.1002/nop2.70014](https://doi.org/10.1002/nop2.70014)

Absolut, Ihre Erkenntnisse liefern nicht nur eine gefühlte, sondern eine empirisch gestützte und theoretisch fundierte Relevanz, die sich hervorragend in Ihr Kapitel „1.3 Relevanz des Themas“ integrieren lässt. Ihre Analyse bietet eine starke Grundlage, um die Notwendigkeit Ihrer Arbeit überzeugend darzustellen, ohne dabei überzogene Behauptungen aufzustellen.

  

Strategische Darstellung der Relevanz

1. Positionierung der Kontrollillusion

• Sie können die Kontrollillusion sachlich und differenziert einführen:

• „Im Bildungssystem lässt sich eine deutliche Orientierung an technikzentrierten Ansätzen erkennen, die den Eindruck erwecken, dass technische Infrastruktur alleine ausreicht, um die Herausforderungen der Digitalisierung zu bewältigen. Die vorliegende Analyse zeigt jedoch, dass diese Perspektive in eine Kontrollillusion führt, da grundlegende systemische Verknüpfungen fehlen.“

• Das Wort „Technikhörigkeit“ könnten Sie ersetzen durch einen präziseren Begriff wie technikzentrierte Orientierung, um sachlich zu bleiben.

2. Relevanz über gemessene Daten begründen

• Betonen Sie, dass die Relevanz Ihrer Arbeit nicht auf einer subjektiven Wahrnehmung, sondern auf einer fundierten Analyse basiert:

• „Die Ergebnisse einer Umfrage unter Lehrenden deuten darauf hin, dass zentrale Bedürfnisse im Bildungssystem – wie soziale Bindung, Kontrolle und Selbstwirksamkeit – unzureichend berücksichtigt werden. Gleichzeitig wird Technik als Symbol für Modernität positiv wahrgenommen, ohne dass sie systemisch in den Bildungsprozess eingebettet ist.“

3. Verknüpfung zur Forschungsfrage

• Leiten Sie elegant zur Zielsetzung Ihrer Arbeit über:

• „Diese Diskrepanz zwischen technischer Ausstattung und den tatsächlichen Bedürfnissen von Akteuren im Bildungssystem unterstreicht die Notwendigkeit, das Wirkgefüge im digitalen Bildungsraum systematisch zu untersuchen und neue Ansätze zu entwickeln, die Technik, Didaktik und menschliche Bedürfnisse in Einklang bringen.“

  

Argumentative Stärke ohne Übertreibung

  

Ihre Ergebnisse sind bereits stark genug, um die Relevanz Ihrer Arbeit zu verdeutlichen, ohne provokante oder ironische Formulierungen einzusetzen. Ein solcher Einstieg könnte folgende Struktur haben:

1. Kontext: Einführung in die Bedeutung der Digitalisierung im Bildungssystem und die verbreitete technikzentrierte Ausrichtung.

2. Problem: Präsentation der Kontrollillusion und die fehlenden systemischen Verknüpfungen.

3. Relevanz: Argument, dass diese Dysfunktion die Effektivität digitaler Bildungsräume beeinträchtigt und daher eine systemtheoretische Untersuchung notwendig ist.

4. Zielsetzung: Vorstellung, wie Ihre Arbeit einen neuen Ansatz entwickelt, um die systemische Dimension des Wirkgefüges zu erfassen.

  

Beispielhafte Formulierung des Kapitels 1.3

  

„Relevanz des Themas“

*„Die Digitalisierung des Bildungssystems wird häufig mit technikzentrierten Lösungen assoziiert. Investitionen in technische Infrastruktur und digitale Geräte suggerieren, dass diese alleine ausreichen, um Lehr- und Lernprozesse zu modernisieren. Eine tiefere Analyse zeigt jedoch, dass diese Perspektive in eine Kontrollillusion führt: Während die technische Ausstattung als Symbol für Fortschritt und Modernität wahrgenommen wird, bleiben grundlegende menschliche Bedürfnisse – wie Bindung, Kontrolle, Selbstwert und soziale Interaktion – unberücksichtigt.

  

Die vorliegende Untersuchung liefert Indizien dafür, dass die digitale Transformation des Bildungssystems in ihrer aktuellen Form technikhörig ist und die systemischen Verknüpfungen zwischen Technik, Didaktik und den Bedürfnissen der Akteure vernachlässigt. Dieser Zustand beeinträchtigt die Effektivität des digitalen Bildungsraums und unterstreicht die Notwendigkeit einer systemtheoretischen Analyse, die Technik als Teil eines umfassenden Wirkgefüges begreift.“*

  

Warum dieser Ansatz effektiv ist

1. Sachlich und überzeugend:

• Ihre Argumentation bleibt wissenschaftlich und fundiert, ohne polemisch zu wirken.

2. Datenbasiert:

• Die Korrelationen und Ergebnisse aus der Umfrage geben Ihrer These eine empirische Grundlage.

3. Relevanz wird messbar:

• Sie zeigen nicht nur, dass das Thema relevant ist, sondern auch warum – und zwar auf Basis klarer Schwächen im aktuellen System.

  

Mit dieser Herangehensweise erreichen Sie, dass Ihre Arbeit von Anfang an nicht nur als theoretisch fundiert, sondern auch als praktisch und systemisch notwendig wahrgenommen wird. Sie schaffen die perfekte Grundlage, um Leser:innen und Gutachter:innen gleichermaßen zu überzeugen.

## 1.2 Ziel und Forschungsfragen
\label{1-2}


Text

### 1.2.1 Ziel der Forschung
\label{1-2-1}

- [ ] Welche theoretischen und praktischen Fragen möchtest du mit der Arbeit beantworten?

Transdisziplinäre Zielsetzung unter Berücksichtigung medizinischer und bildungswissenschaftlicher Aspekte.

### 1.2.2 Zugrundeliegende Vermutungen und Forschungsfragen

Wissenschaftliche und praxisorientierte Erkenntnisinteressen.

- [ ] Lege die Forschungsfragen dar und erkläre, wie du auf jede dieser Fragen eingehen wirst, um den Überblick zu behalten.
- [ ] Die Einleitung schließt mit der Fragestellung, die in der Promotion bearbeitet wurde, ab. Untergliedern Sie die Einleitung in sinnvolle Unterkapitel. Das letzte Unterkapitel beinhaltet die Fragestellung.
- [ ] @kerres2020Bdw


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

Der Schlüssel liegt darin, deine Vorgehensweise klar zu **kommunizieren**. Du kannst erklären, dass die Analyse des Forschungsstands bereits Teil deiner Methodik ist, aber im Kapitel 1 vorgezogen wird, um den Kontext der Arbeit zu schaffen. Hier ist, wie das funktionieren könnte:

  

**In Kapitel 1 (Einleitung):**

• Mache explizit, dass du bereits in diesem Kapitel auf Grundlage einer vorbereitenden Analyse arbeitest, die methodisch fundiert ist.

• Beispiel:

„Der in diesem Kapitel dargestellte Forschungsstand basiert auf einer systematischen Literaturanalyse, die im Rahmen der hier entwickelten Methodik durchgeführt wurde. Die genaue Beschreibung dieser Methodik erfolgt in Kapitel 4, wo auch die weiterführende Analyse beschrieben wird.“

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
# 2 Theorieteil (10–15 Seiten)

## 2.1 Bildungswissenschaltlich-theoretische Verortung

- [ ] Vorstellung der zentralen Theorien und Modelle, die für das Forschungsthema relevant sind.
Hier würde ich dann auch bemerken, dass sie sich bei den Forschung Unternehmen um die abstrakte theoretische Bildungswissenschaften Grundlagenforschung handelt, mit all den Konsequenzen fehlende MPW, viele Wahrscheinlichkeitsannahmen, was auch selbstverständlich gut begründet wird.

In diesem Abschnitt wird der Begriff der Digitalen Bildung \label{Digitale_Bildung} eingeführt, der im weiteren Verlauf noch häufiger auftauchen wird.

Ein Learning Management System (LMS) \label{sec:lms} wird häufig zur Verwaltung von Lerninhalten verwendet.

Massive Open Online Courses (MOOCs) \label{sec:mooc} sind Plattformen, die es vielen Teilnehmern ermöglichen, gleichzeitig an Kursen teilzunehmen.


Grund der unterschiedlichen Lehr-Lern-Ansätze ist die Beweisführung, dass unterschiedlichste Lernumgebungen unterschiedlichste Auswirkungen auch in einem technisch immer gleichen System haben. 

1: "Instruktional",

2: "Kognitivistisch",

3: "Behavioristisch",

4: "Humanistisch",

5: "Konstruktivistisch",

6: "Soziokulturell",

7: "Systemisch"


## 2.2 Systemtheoretische Grundlagen

Hier alle systematischen Überlegungen zusammenführen, Grundlage ist das Templet für die Begriffe

Brinkmann, D. (2022). Freizeitpädagogik in der entwickelten Erlebnisgesellschaft. _MedienPädagogik: Zeitschrift für Theorie und Praxis der Medienbildung_, _50_, 233–251. [https://doi.org/10.21240/mpaed/50/2022.12.10.X](https://doi.org/10.21240/mpaed/50/2022.12.10.X)
> Emergente Systeme einbeziehen

### 2.2.x Systemtheoretisches Lernmodell

Das systemtheoretische Lernmodell 



## 2.3 Exkurs: Bildungstechnologie und das Technologiedefizit der Pädagogik

\newpage

# 3 Beschreibung Forschungsgegenstand (~10 Seiten)


Text

## 3.1 Kontext des Forschungsgegenstandes

Text

## 3.2 Entwicklung des Forschungsgegenstandes

Text

## 3.3 Architektur eines Learning-Management-System

Text

## 3.4 Learning Management System Architektur als Arbeits- und Organisationsinstrument

Text

## 3.5 Ergänzung durch ePortfolio

Text

## 3.6 Technische Rahmenbedingungen

Text

\newpage

# Kapitel 4: Methodik

## 4.1 Forschungsparadigma (ca. 2–3 Seiten)

### 4.1.1 Forschungsfragengeleiteter systemischer Ansatz
- Die Methodik basiert vollständig auf den Forschungsfragen (FU1–FU7), die aus dem Erkenntnisinteresse und dem bestehenden LMS-Produkt hergeleitet wurden.
- Forschungsfragen strukturieren und leiten alle methodischen Entscheidungen und Analysen.
- **Systemtheoretische Prinzipien**:
  - **Interdependenz**: Wechselwirkungen zwischen den Forschungsfragen und deren Daten.
  - **Emergenz**: Neue Erkenntnisse entstehen aus der Verknüpfung von Literatur, Simulation und empirischen Daten.
  - **Rückkopplung**: Ergebnisse aus Analysen fließen iterativ in die Methodik zurück.
- Klassische Methoden (Literaturanalyse, Simulation, Eye-Tracking) wurden angepasst und systemisch integriert.

### 4.1.2 Methodische Konsequenzen der Forschungsfragen
- Die Forschungsfragen bestimmten:
  - Auswahl und Strukturierung der Literatur.
  - Entwicklung von Kategorien und Schlagworten zur thematischen Verknüpfung.
  - Kombination und Anpassung klassischer Methoden.
- **Begründung**:
  - Die Komplexität des digitalen Bildungsraums erforderte eine Methodenkombination, um die Forschungsfragen adäquat zu beantworten.

## 4.2 Forschungsdesign (ca. 3–4 Seiten)

### 4.2.1 Iterativer und dynamischer Forschungsprozess
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
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\caption{Tabellarische Darstellung der Forschungsunterfragen (FU) und Methoden}
\label{tab:methoden_FU}
{\fontsize{8}{10}\selectfont
\begin{tabularx}{\textwidth}{|p{2.5cm}|X|}
\hline
\textbf{Forschungsunterfrage (FU)} & \textbf{Methoden} \\ \hline
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
\vspace{0.2cm}
\begin{quote}
{\fontsize{8}{10}\selectfont
Die Tabelle zeigt die Zuordnung der Methoden zu den Forschungsunterfragen (FU). Sie umfasst systematische Literaturanalyse, empirische Erhebungen (Umfragen, Eye-Tracking) und modellbasierte Ansätze (Simulation), die flexibel kombiniert wurden, um die Forschungsfragen adäquat zu beantworten.
}
\end{quote}

\end{table}

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

## 4.6 Zusammenfassung von Kapitel 4 (ca. 1 Seite)
Kapitel 4 beschreibt eine Methodik, die vollständig auf den Forschungsfragen basiert und durch systemtheoretische Prinzipien strukturiert ist. Die Kombination aus geplanten Methoden (z. B. Literaturanalyse, Eye-Tracking) und methodischen Erweiterungen (Python-Simulation) zeigt die Flexibilität und Innovationskraft der Arbeit.


\newpage

# 5 Ergebnisse (~20–22 Seiten)

Hier beantwortest du jede der Forschungsfragen einzeln und führst die Leser durch deine empirischen Ergebnisse. Die Reihenfolge deiner Argumentation sollte auf den zentralen Wirkfaktoren basieren.


## 5.1 Zusammenfassung: Argumentationskette

1. **Neugier → Motivation → Engagement im LMS**:
    
    - Durch Nützlichkeit und Zugänglichkeit wird die Neugier angeregt, die wiederum die intrinsische Motivation steigert.
2. **Persönliche Ereignisse → Emotionale Unsicherheit → Einfluss auf Lernen und Resilienz**:
    
    - Persönliche Ereignisse beeinflussen die Lernleistung und die emotionale Stabilität. Ein LMS kann jedoch durch Flexibilität helfen, diese Störungen abzufedern.
3. **Kompetenzwahrnehmung → Selbstwirksamkeit → Lernerfolg**:
    
    - Die Wahrnehmung von Kompetenz stärkt die Selbstwirksamkeit und führt zu größerem Lernerfolg. LMS sollten Lernprozesse so strukturieren, dass diese Wahrnehmung gefördert wird.

## 5.2 Kausalkette

**Indizien**

für [[Lernen als universelles Prinzip]]

- Daas, H., Arregui, M., Tarrida, L. G., Glanville, R., & Ali, K. (2024). Qatar dental student perceptions of Sirona prep-check software for learning crown preparations. _BMC Medical Education_, _24_(1), 1409. [https://doi.org/10.1186/s12909-024-06412-z](https://doi.org/10.1186/s12909-024-06412-z)
- Nicol, D. J., & Macfarlane‐Dick, D. (2006). Formative assessment and self‐regulated learning: A model and seven principles of good feedback practice. _Studies in Higher Education_, _31_(2), 199–218. [https://doi.org/10.1080/03075070600572090](https://doi.org/10.1080/03075070600572090)
- 
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

```{=latex}
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}  % Optional: Zeilenabstand innerhalb der Tabelle vergrößern
\caption{Übersicht der Berufszufriedenheit}  % Titel der Tabelle oberhalb
\label{tab:uebersicht-berufszufriedenheit}
{\fontsize{9}{11}\selectfont  % Setzt die Schriftgröße innerhalb der Tabelle auf 9 pt
\begin{tabular}{|l|c|l|c|}
\hline
\textbf{Name} & \textbf{Alter} & \textbf{Beruf} & \textbf{Zufriedenheit (1-5)} \\ \hline
Anna         & 28             & Ingenieurin   & 4 \\ \hline
Max          & 34             & Lehrer        & 3 \\ \hline
Sophie       & 45             & Ärztin        & 5 \\ \hline
Michael      & 31             & Softwareentwickler & 4 \\ \hline
Julia        & 38             & Architektin   & 2 \\ \hline
\end{tabular}
}

\vspace{0.2cm}  % Abstand zur Erläuterung
\begin{quote}
{\fontsize{8}{10}\selectfont  % Setzt die Schriftgröße der Erläuterung auf 8 pt
Die Tabelle \ref{tab:uebersicht-berufszufriedenheit} zeigt die Zufriedenheit in verschiedenen Berufen auf einer Skala von 1 (sehr unzufrieden) bis 5 (sehr zufrieden). Sophie, die als Ärztin tätig ist, erreicht die höchste Zufriedenheit (5), während Julia, die als Architektin arbeitet, die niedrigste Zufriedenheit (2) aufweist. Technische Berufe wie Ingenieurin und Softwareentwickler zeigen eine gute Zufriedenheit (beide 4), während der Lehrer Max eine mittlere Zufriedenheit (3) erreicht. Diese Daten könnten auf eine höhere Zufriedenheit in Gesundheits- und Technikberufen hinweisen.
}
\end{quote}
\end{table}
```

### 3.2.3 Kompetenz als Wirkfaktor

- **Argumentationskette**:
    1. Zeige den Zusammenhang zwischen dem LMS und der **Kompetenzentwicklung** der Lernenden auf.
    2. Verdeutliche, dass die **Selbstwahrnehmung von Kompetenz** ein Schlüsselfaktor für den Lernerfolg ist und dass LMS eine wichtige Rolle bei der Stärkung dieses Gefühls spielen.
    3. Erkläre, dass **Kompetenzwahrnehmung** und **Selbstwirksamkeit** die Lernbereitschaft und die tatsächliche Leistung beeinflussen.
- **Belege aus der Literatur**: Zitiere Theorien zur Selbstwirksamkeit (Bandura) und Literatur, die den Zusammenhang zwischen LMS-Nutzung und Kompetenzentwicklung belegt.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat^[Fußnote].

oder: 

Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat [^1].

[^1]: So gehen Fußnoten auch


m veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat.

```{=latex}
\begin{table}[h!]
\centering
\renewcommand{\arraystretch}{1.2}  % Optional: Zeilenabstand innerhalb der Tabelle vergrößern
\caption{Übersicht der Berufe}  % Tabellenbeschriftung in normaler Textgröße
\label{tab:uebersicht-berufe}
{\fontsize{9}{11}\selectfont  % Setzt die Schriftgröße innerhalb der Tabelle auf 9 pt
\begin{tabular}{|l|c|l|}
\hline
\textbf{Name} & \textbf{Alter} & \textbf{Beruf} \\ \hline
Anna         & 28             & Ingenieurin    \\ \hline
Max          & 34             & Lehrer         \\ \hline
Sophie       & 45             & Ärztin         \\ \hline
Michael      & 31             & Softwareentwickler \\ \hline
\end{tabular}
}

\vspace{0.2cm}  % Abstand zur Erläuterung
\begin{quote}
{\fontsize{8}{10}\selectfont  % Setzt die Schriftgröße der Erläuterung auf 8 pt
Die Tabelle \ref{tab:uebersicht-berufe} zeigt eine Übersicht verschiedener Personen, deren Alter und Beruf. Die ausgewählten Berufe spiegeln eine Bandbreite von technischen, pädagogischen und medizinischen Berufen wider. Besonders fällt auf, dass die Altersverteilung relativ gleichmäßig zwischen 28 und 45 Jahren liegt, was auf eine berufliche Etablierung hinweist. Dies kann zur Interpretation der Berufswege beitragen, insbesondere im Hinblick auf den Einfluss des Alters auf die Berufswahl und -zufriedenheit.
}
\end{quote}
\end{table}
```

Wie in Tabelle \ref{tab:uebersicht-berufe} gezeigt, handelt es sich um eine Übersicht der Berufe. 



```{=latex}
\begin{table}[h!]
\centering
\renewcommand{\arraystretch}{1.2}  % Optional: Zeilenabstand innerhalb der Tabelle vergrößern
\caption{Preisübersicht der Produkte}  % Tabellenbeschriftung in normaler Textgröße
\label{tab:preisuebersicht}
{\fontsize{9}{11}\selectfont  % Setzt die Schriftgröße innerhalb der Tabelle auf 9 pt
\begin{tabular}{|l|r|c|}
\hline
\textbf{Produkt} & \textbf{Preis (\$)} & \textbf{Lagerbestand} \\ \hline
Laptop           & 1200.50             & 25                   \\ \hline
Smartphone       & 899.99              & 34                   \\ \hline
Tablet           & 499.99              & 12                   \\ \hline
Desktop-PC       & 750.00              & 7                    \\ \hline
\end{tabular}
}

\vspace{0.2cm}  % Abstand zur Erläuterung
\begin{quote}
{\fontsize{8}{10}\selectfont  % Setzt die Schriftgröße der Erläuterung auf 8 pt
Die Tabelle \ref{tab:preisuebersicht} gibt eine Übersicht über die Preise verschiedener Produkte und deren Lagerbestand. Laptops sind mit einem Preis von 1200,50 \$ das teuerste Produkt, gefolgt von Smartphones mit 899,99 \$ und Desktop-PCs mit 750,00 \$. Tablets stellen das günstigste Produkt in dieser Auswahl dar, mit einem Preis von 499,99 \$. Der Lagerbestand variiert je nach Produkt, wobei Smartphones den höchsten Bestand (34 Stück) und Desktop-PCs den niedrigsten (7 Stück) haben. Diese Unterschiede können auf verschiedene Markttrends und Nachfrageverhalten hinweisen.
}
\end{quote}
\end{table}
```


Die Darstellung der Ergebnisse beinhaltet die Anzahl der Beobachtungen und die statistische Sicherung anhand geeigneter Dokumentation. Die tabellarische Wiedergabe der Ergebnisse erlaubt in der Regel eine lückenlose Zusammenstellung der gewonnenen Informationen. Wird stattdessen die grafische Darstellung vorgezogen, so muss in jedem Fall eine Abbildungslegende hinzugefügt werden, die alle verwendeten Zeichen und Abkürzungen erläutert. Doppeldarstellungen (Tabellen und Grafiken mit gleichem Inhalt) sollten auf begründete Ausnahmen beschränkt bleiben, da sie gegen die Forderung verstoßen, die Ergebnisse konzentriert zu schildern und Längen und Wiederholungen möglichst zu vermeiden. Die Legende einer Abbildung steht grundsätzlich unter der Abbildung, die Überschrift einer Tabelle über der Tabelle. Überschriften bzw. Legenden müssen den in Tabelle oder Abbildung dargestellten Sachverhalt komplett erklären und alleinstehend verständlich sein. Untergliedern Sie die Darstellung in sinnvolle Unterkapitel.

\begin{equation}
\nu = \frac{d K}{d t}
\addcontentsline{equ}{equations}{Bildungswirkfaktor als Ableitung der Kompetenzentwicklung}
\label{eq:Kompetenzentwicklung}
\end{equation}

\begin{equation}
\nu = \frac{\Delta K}{\Delta t}
\addcontentsline{equ}{equations}{Veränderung der Kompetenzentwicklung pro Zeiteinheit}
\label{eq:Bildungswirkfaktor}
\end{equation}

\begin{equation}
\nu = \Delta K \cdot \Delta E
\addcontentsline{equ}{equations}{Kopplung der kognitiven und emotionalen Unsicherheiten}
\label{eq:Unsicherheiten}
\end{equation}

\begin{equation}
\Delta E \cdot \Delta K \geq C
\addcontentsline{equ}{equations}{Unschärferelation der Unsicherheitskopplung}
\label{eq:Unsicherheitskopplung}
\end{equation}

\begin{equation}
\int_{a}^{b} f(x) \,dx
\addcontentsline{equ}{equations}{Integral zur Berechnung kumulativer Werte}
\label{eq:Kumulative Werte}
\end{equation}

\begin{equation}
\sum_{i=1}^{N} x_i
\addcontentsline{equ}{equations}{Summenzeichen zur Berechnung der Summe über Ereignisse oder Werte}
\end{equation}

Ein Verweis auf die Formel ist möglich: Wie in Gleichung \ref{eq:Bildungswirkfaktor} dargestellt, sind die Ergebnisse schon recht komisch.

Wenn Sie hier Tabellen oder Abbildungen verwenden, die auch in der/n Publikation/en verwendet wurden, geben Sie bitte in der Legende korrekt die Quelle an: (_aus Autor et al., Jahr)_. Wenn Sie Tabellen oder Abbildungen unverändert wiederverwenden, benötigen Sie ggf. die Genehmigung des Inhabers des Copyrights (z. B. der Verlag der Zeitschrift). Wenn Sie die Tabellen oder Abbildungen modifizieren, zitieren Sie bitte (_modifiziert nach Autor et al., Jahr)_. Tabellen, Abbildungen oder Fotografien, die Sie für den Manteltext komplett neu erstellt haben, kennzeichnen Sie bitte mit (_eigene Darstellung_ oder _Foto: Name_.

Achten Sie bitte darauf, dass die eingefügten Abbildungen ausreichend vergrößert sind, so dass sie in der gedruckten Dissertation gut leserlich sind (Achsenbeschriftungen, Zahlen, Sternchen und andere Markierungen).

\newpage


## 5.2 Systemtheoretische Erklärungen 

Regmi, A., Mao, X., Qi, Q., Tang, W., & Yang, K. (2024). Students’ perception and self-efficacy in blended learning of medical nutrition course: A mixed-method research. _BMC Medical Education_, _24_(1), 1411. [https://doi.org/10.1186/s12909-024-06339-5](https://doi.org/10.1186/s12909-024-06339-5)




# 6 Diskussion (~10–12 Seiten)

Interpretation der Ergebnisse, Einordnung in den Forschungsstand.

In der Diskussion werden die Methoden und die Ergebnisse gewertet und mit denen anderer Arbeiten verglichen. Dies schließt auch eigene vorangegangene Arbeiten ein, die zu abweichenden Ergebnissen geführt haben. Abweichungen werden erörtert, wobei die in der Einleitung gestellten Fragen wieder aufgegriffen und nach Möglichkeit beantwortet werden. Untergliedern Sie die Darstellung in sinnvolle Unterkapitel.

Beispiel für den Aufbau der Diskussion

## 6.1 Zusammenfassung der Ergebnisse

- Fasse die Hauptergebnisse der Untersuchung kurz zusammen, indem du die Rolle der Wirkfaktoren (Neugier, persönliche Ereignisse, Kompetenz) im digitalen Bildungsraum nochmals aufgreifst.

## 6.2 Interpretation der Ergebnisse

- **Neugier und Motivation**: Stelle dar, wie Neugier den Lernprozess über die Motivation beeinflusst hat und wie LMS durch Nützlichkeit und Zugänglichkeit diese Neugier unterstützen können.
- **Persönliche Ereignisse**: Diskutiere, inwiefern persönliche Ereignisse als „Störgrößen“ betrachtet werden und welche Rolle Resilienzstrategien spielen.
- **Kompetenzwahrnehmung**: Erkläre, warum die Kompetenzwahrnehmung so wichtig ist und welche Mechanismen LMS nutzen können, um dieses Gefühl zu fördern.

### 6.1.2 Bildungswissenschaftliche Bedeutung

Bedeutung der Ergebnisse für die Bildungspraxis und Theorien.

Bedeutung der Ergebnisse für die medizinische Praxis.

### 6.1.1 Übertragung auf medizinische Ausbildung
Text


### 6.1.3 Transdisziplinäre Reflexion

- [ ] Wie die verschiedenen Disziplinen zusammenwirken und welche Erkenntnisse durch die transdisziplinäre Herangehensweise gewonnen wurden.

### 6.1.4 Einbettung der Ergebnisse in den bisherigen Forschungsstand

- Setze deine Ergebnisse in den Kontext bestehender Studien. Zeige, wo deine Ergebnisse die bestehenden Theorien stützen oder ergänzen, und wo sie neue Erkenntnisse bieten.

## 6.3 Methodenkritik und Limitationen

- [ ] Reflexion über die Grenzen der gewählten Methodik und die Herausforderungen bei der Integration mehrerer Wissenssysteme.
- [ ] Setzen Sie sich an dieser Stelle kritisch mit der internen Validität Ihrer Studienergebnisse auseinander (Genauigkeit und Angemessenheit der Studienmethodik) und beurteilen Punkt für Punkt, warum Sie die Ergebnisse trotz eventueller Schwächen für valide halten.

- Reflektiere die Stärken deiner Untersuchung, wie etwa die breite Datenbasis und die detaillierte Analyse der Wirkfaktoren.
- Besprich mögliche Schwächen, etwa methodische Einschränkungen oder die Generalisierbarkeit der Ergebnisse auf andere Bildungsbereiche.

Sodann setzen Sie sich mit der externen Validität Ihrer Studienergebnisse kritisch auseinander. Inwieweit können die Studienergebnisse verallgemeinert werden? Begründen Sie Ihre Aussagen zur Generalisierbarkeit der Ergebnisse Punkt für Punkt.

## 6.4 Implikationen für Praxis und/oder zukünftige Forschung

Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Die Preise und Lagerbestände der Produkte sind in Tabelle \ref{tab:preisuebersicht} aufgeführt.

- **Für die Praxis**: Zeige, wie die Ergebnisse praktisch in der Gestaltung von LMS umgesetzt werden könnten, um Neugier, Motivation und Kompetenzentwicklung zu fördern.
- **Für die Forschung**: Zeige mögliche zukünftige Forschungsrichtungen auf, etwa die genauere Untersuchung der Rolle von persönlichen Ereignissen im Bildungsprozess oder die Entwicklung adaptiver Lernsysteme, die auf diese Wirkfaktoren eingehen.



Interpretation der Ergebnisse, Einordnung in den Forschungsstand.

In der Diskussion werden die Methoden und die Ergebnisse gewertet und mit denen anderer Arbeiten verglichen. Dies schließt auch eigene vorangegangene Arbeiten ein, die zu abweichenden Ergebnissen geführt haben. Abweichungen werden erörtert, wobei die in der Einleitung gestellten Fragen wieder aufgegriffen und nach Möglichkeit beantwortet werden. Untergliedern Sie die Darstellung in sinnvolle Unterkapitel.


Weitere Forschungsvorhaben zur Falsifikation: Grundlagen der Fundamentalgleichungen 

->> 2.3 Empirische Überprüfung und Weiterentwicklung|Forschungen zur Bildungsmechnik <<-
-> hier ausführen <-


\newpage

# 7 Conclusio (~ Seiten)

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

## Prompt zum Training der Literaturanalyse

Dieser Anhang dokumentiert den Prompt, der zur Schulung eines Chat-GPT-Modells entwickelt wurde. Ziel war es, das Modell darauf vorzubereiten, wissenschaftliche Artikel, Forschungsarbeiten oder Konferenzbeiträge im Bereich der digitalen Bildungssysteme effektiv zu analysieren. Die Aufgabe bestand darin, die Entwicklung, Nutzung und Bewertung dieser Bildungssysteme zu untersuchen und die relevanten Methoden, Theorien, Ergebnisse und Diskussionen präzise zusammenzufassen.

Der Prompt gab Anweisungen, um sicherzustellen, dass das Modell systematisch und fundiert vorgeht. Der Analyseprozess umfasste Schritte wie die Identifikation zentraler Fragestellungen, die Ermittlung von Methoden und Datenquellen sowie die Extraktion der wesentlichen Aussagen. Zudem wurden Anweisungen gegeben, um Argumentationslinien und logische Strukturen im Text nachzuvollziehen.

>  Du bist ein wissenschaftlicher Mitarbeiter an einem renommierten kultur- und sozialwissenschaftlichen Institut für Bildung mit jahrzehntelanger Erfahrung in der Analyse wissenschaftlicher Quellen.
> 
> Deine Aufgabe ist es, wissenschaftliche Artikel, Forschungsarbeiten oder Konferenzbeiträge zu analysieren, die sich mit digitalen Bildungssystemen, deren Entwicklung, Nutzung oder Bewertung befassen. Die Texte sollen Informationen zu Methoden, Theorien, Ergebnissen und Diskussionen enthalten.
> 
> Deine Schritte:
> 
> 1. **Analyse**:
>     
>     - Identifikation der Hauptthemen und -ziele: Erfasse die zentralen Fragestellungen und Ziele der Forschung.
>     - Ermittlung der verwendeten Methoden und Datenquellen: Beschreibe die methodischen Ansätze und Datenquellen.
>     - Erklärung der zentralen Forschungsergebnisse: Stelle die wichtigsten Ergebnisse und ihre Implikationen für das Feld der digitalen Bildung dar.
> 2. **Zusammenfassung**:
>     
>     - Fasse die Kernpunkte prägnant zusammen, einschließlich Problemstellung, Methodik, Hauptergebnissen und Schlussfolgerungen.
> 3. **Kernaussagen**:
>     
>     - Extrahiere zentrale Aussagen und Befunde aus dem Text und gebe die Fundstellen (Seitenangabe) an.
> 4. **Argumentationslinien**:
>     
>     - Beschreibe die logische Struktur und die Verbindungen zwischen den Aussagen, inklusive Fundstellen (Seitenangabe).
> 5. **Verschlagwortung**:
>     
>     - Weise relevante Schlagwörter basierend auf Inhalten und Ergebnissen zu, z.B. „Lernsystemarchitektur“, „Bildungstheorien“, „Lehr- und Lerneffektivität“, „Kollaboratives Lernen“, „Bewertungsmethoden“, „Technologieintegration“, „Datenschutz und IT-Sicherheit“, „Systemanpassung“, „Krisenreaktion im Bildungsbereich“, „Forschungsansätze“. Begründe jedes Schlagwort.
> 6. **Kategorisierung**:
>     
>     - Ordne spezifische Begriffe im Kontext des Exposés zu, z.B. Argumentation, Kerngedanke, Weiterführung, Schlussfolgerung.
> 7. **Relevanzbewertung**:
>     
>     - Bewerte die Quelle nach ihrer Relevanz für die Forschungsfragen auf einer Skala von 1 bis 5 (1 = irrelevant, 5 = hoch relevant).
> 8. **Zuordnung zu Forschungsfragen**:
>     
>     - Ordne die Quelle der passenden Forschungsfrage zu und erläutere die Zuordnung.
> 
> Ziel ist es, die Quellen effizient zu analysieren, präzise zusammenzufassen und systematisch zu verschlagworten, um die Organisation und das Verständnis der Forschungsliteratur zu unterstützen."

Der vorangestellte Prompt wird an dieser Stelle in verkürzter Fassung wiedergegeben. Die vorgenommenen Veränderungen am ursprünglichen Prompt waren notwendig, um ihn für den begrenzten Rahmen des Anhangs anzupassen.

1. **Sprachliche Straffung**: Der Prompt wurde sprachlich vereinfacht und gestrafft, um Redundanzen zu vermeiden und die Anweisungen präziser und kürzer zu formulieren. Beispielsweise wurden detaillierte Erklärungen zu einzelnen Schritten gekürzt, ohne die inhaltliche Aussage zu verändern.
    
2. **Klarheit in den Anweisungen**: Die Anweisungen wurden so formuliert, dass sie auf den Punkt gebracht und flüssig zu lesen sind. Komplexere Sätze wurden vereinfacht, um den Prozess für das Modell nachvollziehbar zu machen.
    
3. **Kompakte Gliederung**: Einige Unterpunkte, die ähnliche Inhalte behandelten, wurden zusammengeführt. Beispielsweise wurden die „Hauptthemen und Ziele der Forschung“ und „Erklärung der Forschungsergebnisse“ kompakter zusammengefasst, um Wiederholungen zu vermeiden.
    
4. **Zusammenführung von Schlagwörtern**: Die Anzahl der genannten Schlagwörter und deren Begründungen wurde reduziert, indem ähnliche Konzepte zusammengefasst und deren Relevanz im Allgemeinen beschrieben wurde. Dies erleichtert es, den Fokus auf die wichtigsten Begriffe zu legen, die für das Modell relevant sind.
    
5. **Klarere Struktur**: Die einzelnen Schritte wurden in einer logischeren Reihenfolge angeordnet, um den Analyseprozess besser darzustellen. Beispielsweise wurde die Verschlagwortung nach der Zusammenfassung und Extraktion von Aussagen platziert, um einen natürlichen Fluss im Ablauf zu gewährleisten.
    
6. **Verkürzte Beispiele**: Die ausführlichen Beispiele für Kategorien und Forschungsfragen wurden auf wesentliche Elemente reduziert, um die Anweisungen konkreter zu gestalten und den Prompt kürzer zu halten.
    
7. **Präzise Zielsetzung**: Der Abschnitt zur Zielsetzung des Prompts wurde gekürzt, um die Kernbotschaft klar und prägnant darzustellen: die systematische Organisation und das Verständnis der Forschungsliteratur zu fördern.

Durch diesen strukturierten Ansatz lernte das Modell (GPT-4o), nicht nur die Inhalte der Quellen präzise zusammenzufassen, sondern auch deren Relevanz für die digitale Bildungsforschung zu bewerten und systematisch zu verschlagworten. Dadurch war eine präzise Einordnung der Artikel in den Forschungsrahmen, die Identifikation von Forschungslücken sowie die Ableitung neuer Forschungsperspektiven und die Beantwortung der Forschungsunterfragen möglich. Insgesamt wurden die zur Verfügung stehenden Ressourcen effizienter eingesetzt, was im Forschungsverlauf zu einer inhaltlichen Sättigung führte.

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

Das Literaturverzeichnis enthält die im vorherigen Text zitierte Literatur (und nur diese) inklusive der eigenen Publikation(en), zusammengestellt nach internationalen Vorschriften. Geben Sie bitte – ungeachtet der verwendeten Zitiermethodik – alle Autor*innen an.

Sie dürfen und sollen Literatur bei der Erstellung Ihrer wissenschaftlichen Arbeiten verwenden. Entscheidend hierbei ist, dass Sie transparent darlegen, welcher Quellen Sie sich bedient haben. Hierzu dienen das Zitat bzw. die Quellenangabe. Die Pflicht hierzu besteht auch, wenn es sich bei der Quelle um von Ihnen verfasste, veröffentlichte Texte handelt. Die Quellenangabe erfolgt in Kurzform im Text (in-text-reference) und ausführlich im Literaturverzeichnis (reference list). Die Quellenangabe im Text muss die Lesenden sicher durch das Literaturverzeichnis „führen“ und umgekehrt! Bitte informieren Sie sich auf den Webseiten der Geschäftsstelle Gute Wissenschaftliche Praxis unter „Ausarbeitung der Promotion“.]

Folgende Formen des Zitats sind verwendbar:

Indirektes Zitat (Paraphrasieren): Die Ausführungen eines anderen Autors werden sinngemäß übernommen, aber in eigenen Worten ausgedrückt und häufig zusammengefasst. Der ursprüngliche Sinn und Grundgedanke muss erhalten bleiben, wird häufig aber „kondensiert“. Durch Setzen der Quellangabe muss ersichtlich sein, wo das Zitat endet und ggf. die eigene Argumentation beginnt.

Direktes Zitat: Der Originaltext wird wörtlich – und buchstabengenau – vom Autor/der Autorin übernommen. Diese Form des Zitats ist durch Anführungszeichen kenntlich zu machen. Die Quellenangabe muss direkt vor oder nach dem Zitat erfolgen. Rechtschreibfehler o.ä. werden übernommen und mit [sic!] (=lat. „so lautet die Quelle“) kenntlich gemacht. Auslassungen werden mit (…) aufgezeigt. Ergänzungen erfolgen in eckigen Klammern […; Anmerkung des Autors] und Hervorhebungen werden durch [Hervorhebung durch den Autor] kenntlich gemacht. Wortgleiche Übersetzungen werden wie ein direktes Zitat behandelt und mit der Ergänzung (Übersetzung durch den Autor) ergänzt.

Es existieren diverse weitere Zitierstile, z.B. der APA-Style, der häufig in der Psychologie und den Sozialwissenschaften angewendet wird (Link: http://www.apastyle.org/). Alle Stile sind anwendbar, solange Ihre Arbeit Gleichmäßigkeit aufweist! Wenn Sie Ihre Literatur in einem Literaturdatenbanksystem (an der Charité endnote) verwalten, können Sie diverse Stile voreinstellen.]

Wenn Sie ein Literaturdatenbanksystem wie endnote, zotero o.ä. verwenden, überprüfen Sie abschließend, dass alle Quellen im Literaturverzeichnis korrekt dargestellt werden. Insbesondere Autoren oder Herausgeber wie World Health Organisation, Fachgesellschaften oder Bundesministerien müssen überprüft ggf. händisch korrigiert werden.
