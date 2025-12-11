---
author: Jochen Hanisch-Johannsen
title: Feedback – Eine systemische und zirkuläre Perspektive
created: 2024-12-06
updated: 2024-12-06
tags:
  - Feedback
  - Systemtheorie
  - Lernen
  - Reflexion
  - Kybernetik
project: Systemlernen
type:
  - Wissenschaftliche Notiz
publish: false
---

# Einleitung

Feedback ist ein zentrales Konzept in unterschiedlichsten wissenschaftlichen und praktischen Kontexten, von der Kybernetik über die Pädagogik bis hin zur Psychologie und Kommunikation. Ziel dieses Beitrags ist es, den Begriff Feedback systematisch herzuleiten, präzise zu definieren und seine Funktion im zirkulären Lernprozess theoretisch zu erklären. Dabei wird insbesondere auf die universelle Bedeutung von Feedback in lebenden, psychischen, sozialen und emergenten Systemen eingegangen.

# 1 Definition

Der Begriff Feedback bezieht sich auf einen neutralen Informationsimpuls, der Unterschiede zwischen einem Ist-Zustand und einem Soll-Zustand sichtbar macht. Es ist durch Neutralität, Kontextabhängigkeit und die Anregung von Reflexions- und Anpassungsprozessen gekennzeichnet. Feedback wird in biologischen, psychischen, sozialen und technischen Systemen verwendet und trägt wesentlich zur Selbstregulation, Anpassung und Weiterentwicklung dieser Systeme bei.

# 2 Herleitung

# 2.1 Physikalische Perspektive

Die physikalische Perspektive beschreibt Vorgänge ausschließlich über Zustände und deren Unterschiede. Diese Unterschiede erscheinen als Differenzen in Feldgrößen, Impulsen oder Zustandsvektoren und bleiben frei von Bewertung, Bedeutung oder innerer Verarbeitung. Die folgenden fünf Bereiche stellen physikalische Erscheinungsformen solcher Differenzen dar, ohne dass dabei eine Reaktion, Interpretation oder Integration beschrieben wird. Sie bilden die elementare Form dessen, was im Rahmen der Elementaroperationen als Feedback verstanden wird: die Realisierung eines Unterschieds.

## 2.1.1 Feldstärke und Potentialdifferenzen

Klassische Feldtheorien ordnen jedem Raum-Zeit-Punkt eine Feldstärke zu. Unterschiede zwischen zwei Punkten lassen sich als Feldstärkedifferenzen oder Potentialdifferenzen ausdrücken. Diese Unterschiede beschreiben zwei verschiedene Zustände eines Feldes, ohne darüber hinaus eine Folgedynamik zu enthalten.

In Maxwells „Treatise on Electricity and Magnetism“ (Maxwell, 1873) wird die räumliche Variation elektromagnetischer Felder mathematisch gefasst. Eine einfache Feldstärkedifferenz zwischen zwei Punkten lautet:

$$
\Delta \mathbf{E} = \mathbf{E}(\mathbf{x}_2) - \mathbf{E}(\mathbf{x}_1).
\tag{1}
$$

Auch in der Gravitationstheorie (Newton, 1687; Einstein, 1915) werden Potentialfunktionen eingeführt, deren Unterschiede rein strukturelle Differenzen zwischen zwei Punkten darstellen. Diese Differenzen markieren verschiedene Zustände eines Feldes, ohne sie zu bewerten oder als Ursache einer gerichteten Veränderung zu interpretieren.

## 2.1.2 Gradient und räumliche Ableitungen

Der Gradient beschreibt die lokale Änderung einer skalaren Größe pro Raumkoordinate:

$$
\nabla \phi =
\left(
\frac{\partial \phi}{\partial x},
\frac{\partial \phi}{\partial y},
\frac{\partial \phi}{\partial z}
\right).
\tag{2}
$$

Fourier (1822) und Fick (1855) formulieren Temperatur‑ bzw. Konzentrationsgradienten als präzise mathematische Darstellung räumlicher Unterschiede (Fourier, 1822; Fick, 1855). Der Gradient selbst beschreibt eine Struktur, in der Werte nicht gleich sind. Er markiert eine Differenz, ohne zu implizieren, wie ein System darauf reagiert.

## 2.1.3 Impulsübertragung und Stoßprozesse

In der klassischen Mechanik bezeichnet der Impuls $\mathbf{p} = m\mathbf{v}$ einen Bewegungszustand. Ein Stoßprozess wird formal durch die Differenz zwischen zwei Impulszuständen beschrieben:

$$
\Delta \mathbf{p} = \mathbf{p}_{\text{nach}} - \mathbf{p}_{\text{vor}}.
\tag{3}
$$

Diese Differenz bildet ausschließlich den Unterschied zwischen zwei Bewegungszuständen ab. Auch in quantenmechanischen Streuprozessen wird die Impulsänderung als reine Zustanddifferenz formuliert (Compton, 1923; Einstein, 1905), ohne dass diese Differenz mit einer Bewertung oder einem funktionalen Zweck verbunden wäre.

## 2.1.4 Interferenz und Superposition

In der klassischen Wellentheorie wird Interferenz über die Überlagerung von Wellen beschrieben (Huygens, 1690; Young, 1801). Die Beschreibung der Interferenz stützt sich auf eine Phasendifferenz:

$$
\Delta \phi = \phi_2 - \phi_1.
\tag{4}
$$

Diese Phasendifferenz beschreibt lediglich den Unterschied zweier Wellenausbreitungen. In der Quantenmechanik wird Interferenz als Differenz in Wahrscheinlichkeitsamplituden formalisiert (Dirac, 1930). Die Differenz selbst ist eine rein strukturelle Größe, ohne dass ihr eine interne Verarbeitung zugeschrieben wird.

## 2.1.5 Rückwirkung (Backaction) in Quantenprozessen

In der Quantenmechanik wird eine Messung definitionsgemäß als Zustandswechsel beschrieben. Der Übergang

$$
|\psi_1\rangle \longrightarrow |\psi_2\rangle
\tag{5}
$$

kann als Zustandsdifferenz

$$
\Delta |\psi\rangle = |\psi_2\rangle - |\psi_1\rangle
\tag{6}
$$

beschrieben werden. Heisenberg (1927), von Neumann (1932) sowie Wheeler und Zurek (1983) diskutieren diesen Zustandswechsel und seine mathematische Fassung im Rahmen der Theorie. Die Differenz selbst ist kein Ausdruck einer Bewertung oder einer funktionalen Reaktion, sondern die formale Darstellung zweier verschiedener Systemzustände.

---

Die fünf dargestellten Bereiche zeigen physikalische Realisierungen von Differenzstrukturen, die ohne Bedeutungszuschreibung oder Bewertung auftreten. Damit entsprechen sie der elementaren Form der Operation, die hier als Feedback bezeichnet wird: die Markierung eines Unterschieds zwischen zwei Zuständen.

## 2.2 Kybernetik, Regelungstechnik und Systemtheorie

Die Begriffsgeschichte von Feedback beginnt in der technischen Regelungstechnik, lange bevor Kybernetik und Systemtheorie den Begriff verallgemeinerten. Frühere selbstregulierende Vorrichtungen wie Schwimmerventil, Fliehkraftregler oder Temperaturregler realisierten bereits Rückkopplungsprinzipien, ohne dass ein einheitlicher Begriff dafür vorlag (Maxwell, 1868; Mayr, 1970). 

Der Ausdruck „feedback“ taucht zu Beginn des 20. Jahrhunderts zunächst im elektrotechnischen Kontext auf. Etymologische Analysen datieren die substantivische Verwendung im Elektronikbereich auf etwa 1920 und beschreiben damit die Rückführung eines Anteils des Ausgangssignals an den Eingang einer früheren Stufe (Online Etymology Dictionary, o. D.). 

Eine erste systematische Theorie von Rückkopplung in Verstärkerschaltungen formuliert Harold S. Black in einem Beitrag des Bell System Technical Journal. Negative Rückkopplung stabilisiert nach dieser Analyse die Verstärkung, reduziert Verzerrungen und macht Verstärkerkreise gegenüber Störungen robuster (Black, 1934). Rekonstruktionen der Geschichte der Regelungs- und Steuerungstechnik zwischen 1930 und 1955 zeigen, dass Feedback in dieser Phase zu einem Leitkonzept ingenieurwissenschaftlicher Praxis wird und die Ausbildung einer eigenen klassischen Regelungstheorie trägt (Bennett, 1993; Mayr, 1970). 

Norbert Wiener generalisiert diese technischen Einsichten in „Cybernetics: Or Control and Communication in the Animal and the Machine“ und beschreibt Feedback als grundlegenden Mechanismus der Steuerung in Maschinen und Organismen (Wiener, 1948). Die spätere Kybernetikliteratur stellt die Untersuchung zirkulärer Kausalverläufe in den Mittelpunkt und behandelt Rückkopplung als universelles Strukturprinzip dynamischer Systeme (Mayr, 1970). 

Mit der Allgemeinen Systemtheorie von Ludwig von Bertalanffy verschiebt sich der Fokus von einzelnen Regelkreisen hin zu offenen, mit ihrer Umwelt im Austausch stehenden Systemen. Feedback unterstützt in dieser Perspektive die Aufrechterhaltung von Fern-Gleichgewicht, Selbstorganisation und Adaptivität, indem Rückwirkungen laufender Operationen auf Struktur und Parameter des Systems wirken (Bertalanffy, 1968). Rückkopplungsprozesse erhalten dadurch den Status eines generativen Mechanismus systemischer Ordnung in biologischen, psychischen und sozialen Systemen. 

Die sozialwissenschaftliche Spezifikation des Feedback-Begriffs knüpft an diese kybernetisch-systemtheoretischen Vorarbeiten an. In gruppendynamischen Laboratorien im Umfeld von Kurt Lewin wird Feedback während der 1940er Jahre als methodisch gestaltete Rückmeldung über Wahrnehmungen in Gruppen eingesetzt. Eine von Fengler rekonstruierte Entstehungsgeschichte, referiert bei Reich, datiert den Beginn eines eigenständigen sozialwissenschaftlichen Feedback-Konzepts auf das Jahr 1946 und verbindet damit Trainingsgruppen und Laboratorien, in denen Teilnehmerinnen und Teilnehmer die unmittelbare Rückmeldung über eigenes Verhalten systematisch auswerten (Fengler, 2004, zit. nach Reich, 2006).

## 2.3 Pädagogik und Psychologie

In der Pädagogik ist Feedback ein zentrales Element, um Lernprozesse zu unterstützen. Empirische Studien, insbesondere von **John Hattie**, zeigen, dass Feedback eine der höchsten Effektstärken im Lernen aufweist (*Hattie, 2009*). Hierbei ist die Qualität des Feedbacks entscheidend: Es sollte spezifisch, zeitnah und auf die Lücke zwischen Ist- und Soll-Zustand fokussiert sein.

In der Psychologie wurde Feedback durch **B. F. Skinner** im Kontext der operanten Konditionierung beschrieben (*Skinner, 1953*). Rückmeldungen dienen hier als Verstärker, die Verhalten formen und steuern können.

## 2.4 Kommunikation und technische Systeme

In der Kommunikationstheorie von **Claude Shannon** und **Warren Weaver** (*Shannon & Weaver, 1949*) spielt Feedback eine essenzielle Rolle, um die Wirksamkeit von Botschaften zu überprüfen und Kommunikationsprozesse anzupassen. In technischen Systemen wird Feedback verwendet, um Regelkreise und Automatisierungen zu steuern.


### Feedback

Feedback beschreibt den Vorgang, bei dem ein System die Wirkung eines eigenen Outputs als Input zurückführt. In mathematischer Sprache handelt es sich um eine rekursive Abhängigkeit $x_{t+1} = f(x_t)$, wobei $f$ eine Transformationsfunktion darstellt, die sich dynamisch anpasst. In sozialen und psychischen Systemen entspricht Feedback der Beobachtung von Konsequenzen, die aus dem eigenen Handeln resultieren.

Im Zusammenhang mit der Gleichung

$$ 
P(t) = P_{\text{real}}(t) + i \cdot \tan(\beta t) \cdot P_{\text{real}}(t) \tag{3}
$$

bedeutet Feedback, dass der imaginäre Anteil der [[Wirkungswahrscheinlichkeit]] keine eigenständige Größe ist, sondern eine systematische Funktion des reellen Anteils. Die Rückkopplung ist abhängig vom bereits vorhandenen Zustand. Damit lässt sich Feedback direkt über den Re-Entry-Faktor $\tan(\beta t)$ als Funktion der Zeit modellieren.

# 3 Folgerungen

Feedback ist ein universeller Mechanismus, der die Selbstregulation, Reflexion und Anpassung in lebenden, psychischen, sozialen und technischen Systemen ermöglicht. Seine Funktion im zirkulären Lernprozess ist zentral, um Unterschiede sichtbar zu machen und Anpassungen vorzunehmen.

# 4 Einordnung im Elementaroperations-Zyklus

Feedback ist die auslösende Elementaroperation im Zyklus Feedback → Reflexion → Reentry. Es liefert den Differenzimpuls, der zur Reflexion führt (Inversion) und nachfolgend in der Reentry-Phase integriert wird. Damit ist Feedback nicht nur ein Regelungsmechanismus, sondern der operative Startpunkt für die kleinste nicht weiter teilbare Reflexionsschleife in allen Systemtypen (physikalisch, chemisch, biologisch, lebend, psychisch, sozial). Die spezifische Ausprägung der Reflexion im psychischen System (Günther: Reflexionsidentität, Selbstbruch) ist eine systemtypische Form, bleibt aber durch Feedback operativ angebunden.

# 5 Implikationen

Die Implikationen des Feedback-Konzepts sind vielfältig: 
- In der Bildung ermöglicht es zielgerichtete Lernprozesse und die Förderung von Selbstregulation.
- In der Technik sorgt es für stabile und adaptive Systeme.
- In der Kommunikation verbessert es die Effektivität zwischenmenschlicher und technischer Interaktionen.

# 6 Kritik

Trotz seiner universellen Bedeutung ist Feedback nicht immer effektiv. Es hängt stark von der Wahrnehmung, den Bedürfnissen und den Emotionen der empfänglichen Systeme ab. Unspezifisches oder übermäßig kritisches Feedback kann zu Widerständen und Fehlinterpretationen führen.

# 7 Zusammenfassung

Der Begriff **Feedback** beschreibt einen neutralen Informationsimpuls, der Unterschiede sichtbar macht, Reflexionsprozesse anstößt und systeminterne Anpassungen ermöglicht. Er wird in biologischen, psychischen, sozialen und technischen Systemen angewendet und ist entscheidend für die Selbstorganisation, Stabilität und Weiterentwicklung dieser Systeme.

# Quellen

- Bennett, S. (1993). A history of control engineering, 1930–1955. Peter Peregrinus.
- Bertalanffy, L. von. (1968). General system theory: Foundations, development, applications. George Braziller.
- Black, H. S. (1934). Stabilized feedback amplifiers. Bell System Technical Journal, 13(1), 1–18.
- Compton, A. H. (1923). A quantum theory of the scattering of X-rays by light elements. Physical Review, 21(5), 483–502.
- Dirac, P. A. M. (1930). The principles of quantum mechanics. Clarendon Press.
- Einstein, A. (1905). Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt. Annalen der Physik, 17, 132–148.
- Einstein, A. (1915). Die Feldgleichungen der Gravitation. Sitzungsberichte der Königlich-Preußischen Akademie der Wissenschaften zu Berlin, 1915, 844–847.
- Fick, A. (1855). Über Diffusion. Annalen der Physik und Chemie, 170(1), 59–86.
- Fengler, J. (2004). Feedback geben: Strategien und Übungen (3. Aufl.). Beltz.
- Fourier, J. (1822). Théorie analytique de la chaleur. Chez Firmin Didot Père et Fils.
- Hattie, J. (2009). Visible learning: A synthesis of over 800 meta-analyses relating to achievement. Routledge.
- Heisenberg, W. (1927). Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. Zeitschrift für Physik, 43, 172–198.
- Huygens, C. (1690). Traité de la lumière. Van der Aa.
- Maxwell, J. C. (1868). On governors. Proceedings of the Royal Society of London, 16, 270–283.
- Maxwell, J. C. (1873). A treatise on electricity and magnetism. Clarendon Press.
- Mayr, O. (1970). The origins of feedback control. MIT Press.
- Newton, I. (1687). Philosophiae naturalis principia mathematica. Jussu Societatis Regiae ac typis Josephi Streater.
- Online Etymology Dictionary. (o. D.). Feedback. Eintrag im Online Etymology Dictionary zum Stichwort „feedback“.
- Reich, K. (2006). Feedback. Methodenpool Universität zu Köln. Manuskript.
- Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.
- Skinner, B. F. (1953). Science and human behavior. Macmillan.
- von Neumann, J. (1932). Mathematische Grundlagen der Quantenmechanik. Springer.
- Wheeler, J. A., & Zurek, W. H. (Eds.). (1983). Quantum theory and measurement. Princeton University Press.
- Wiener, N. (1948). Cybernetics: Or control and communication in the animal and the machine. MIT Press.
- Young, T. (1801). On the theory of light and colours. Philosophical Transactions of the Royal Society of London, 92, 12–48.
