---
author: Jochen Hanisch-Johannsen
title: Kompetenzmess-, Kompetenzentwicklungs-, emotionale, kognitive und Neugierunsicherheiten
Repository:
created: 2024-10-17
updated: 2024-10-17
publish: false
tags:
published:
project: Bildungsraum-Analyse
type:
  - Wissenschaftliche Notiz
---

# 1 Definition

Die verschiedenen Unsicherheiten im Bildungsprozess umfassen:

- **Kompetenzmessunsicherheit ($\Delta K_{mess}$)**: Diese beschreibt die epistemische Unschärfe bei der Messung des Kompetenzniveaus eines Lernenden aufgrund von äußeren Einflüssen wie Prüfungsangst oder Tagesform.
- **Kompetenzentwicklungsunsicherheit ($\Delta K_{entw}$)**: Diese erfasst die temporale Variabilität in der Kompetenzentwicklung eines Lernenden, die durch individuelle Schwankungen und externe Einflüsse über einen längeren Zeitraum beeinflusst wird.
- **Emotionale Unsicherheit ($\Delta E$)**: Sie bezieht sich auf die Schwankungen im affektiven Zustand des Lernenden, die den Lernprozess modulieren.
- **Kognitive Unsicherheit ($\Delta C_{kog}$)**: Diese beschreibt die semantische Unsicherheit in Bezug auf das Verständnis und die Anwendung von Wissen im Lernprozess.
- **Neugierunsicherheit ($\Delta N$)**: Sie beschreibt die explorative Unsicherheit über die intrinsische Motivation eines Lernenden, neue Inhalte zu erkunden und weiterführende Fragen zu stellen.

Die Symbolik spannt ein fünf-dimensionales Unsicherheitsfeld auf, dessen Dimensionen unterschiedlichen Beobachtungsebenen zugeordnet sind: externe Messung, interne Entwicklungsdynamik sowie affektive, semantische und explorative Kopplungen.

# 2 Herleitung

## 2.1 Perspektive 1: Kompetenzmess- und Kompetenzentwicklungsunsicherheit

### Kompetenzmessunsicherheit ($\Delta K_{mess}$)
- **Definition**: Unsicherheit, die durch Schwankungen und Fehler bei der Messung von Kompetenzen entsteht.
- **Merkmale**: Sie wird durch externe Faktoren wie Prüfungsbedingungen oder subjektive Einschätzungen beeinflusst.
- **Relevanz**: Diese Unsicherheit bestimmt die Genauigkeit der Erfassung des aktuellen Kompetenzniveaus.
- **Beispiel**: Ein Test misst möglicherweise nicht genau den Wissensstand eines Lernenden aufgrund von Stress.

### Kompetenzentwicklungsunsicherheit ($\Delta K_{entw}$)
- **Definition**: Unsicherheit, die durch unvorhersehbare Schwankungen in der Kompetenzentwicklung entsteht.
- **Merkmale**: Diese Unsicherheit bezieht sich auf die Veränderung von Kompetenzen im Laufe der Zeit und wird durch soziale, emotionale und externe Faktoren beeinflusst.
- **Relevanz**: Diese Unsicherheit bestimmt, wie vorhersehbar und stabil die Kompetenzentwicklung eines Lernenden ist.
- **Beispiel**: Ein Lernender zeigt über einen längeren Zeitraum ungleichmäßige Fortschritte.

## 2.2 Perspektive 2: Emotionale, kognitive und neugierbezogene Unsicherheiten

### Emotionale Unsicherheit ($\Delta E$)
- **Definition**: Unsicherheit, die durch emotionale Schwankungen im Lernprozess entsteht.
- **Merkmale**: Diese Unsicherheit umfasst Emotionen wie Angst, Frustration, Motivation oder Selbstvertrauen.
- **Relevanz**: Emotionale Unsicherheiten können die Lernbereitschaft, das Engagement und die Fähigkeit zur Problemlösung stark beeinflussen.
- **Beispiel**: Ein Lernender empfindet hohen Druck während einer Prüfung, was zu Fehlern führt.

### Kognitive Unsicherheit ($\Delta C_{kog}$)
- **Definition**: Unsicherheit, die im Lernprozess durch Schwierigkeiten im Verstehen und Anwenden von Wissen entsteht.
- **Merkmale**: Sie entsteht, wenn Lernende Schwierigkeiten haben, neue Konzepte zu verstehen oder bestehendes Wissen anzuwenden.
- **Relevanz**: Diese Unsicherheit kann die Leistung und den Lernerfolg beeinträchtigen.
- **Beispiel**: Ein Lernender versteht theoretische Konzepte, hat jedoch Schwierigkeiten, diese in der Praxis anzuwenden.

### Neugierunsicherheit ($\Delta N$)
- **Definition**: Unsicherheit, die durch Schwankungen in der Neugier und Lernbereitschaft des Lernenden entsteht.
- **Merkmale**: Sie wird beeinflusst durch die Herausforderungen und die intrinsische Motivation, neue Informationen zu entdecken.
- **Relevanz**: Diese Unsicherheit beeinflusst die explorative Motivation und die Bereitschaft des Lernenden, sich aktiv mit dem Stoff auseinanderzusetzen.
- **Beispiel**: Ein Lernender, der anfangs neugierig ist, verliert das Interesse, wenn der Stoff zu komplex oder unattraktiv wird.

## 2.3 Mathematische Formeln

Die verschiedenen Unsicherheiten können durch folgende mathematische Relationen beschrieben werden:

- **Unsicherheitsrelation der Kompetenzmessung und -entwicklung**:
  
  $$
  \Delta K_{mess} \cdot \Delta K_{entw} \geq C(\gamma)
  $$

  Diese Formel stellt sicher, dass die kombinierte Unsicherheit aus der Messung und Entwicklung der Kompetenz eine Mindestschwelle nicht unterschreiten kann.

- **Dreidimensionale Unsicherheitsrelation (Kognition, Emotion, Neugier)**:

  $$
  \Delta C_{kog} \cdot \Delta E \cdot \Delta N \geq C(\gamma)
  $$

  Diese dreidimensionale Relation beschreibt, dass die Unsicherheiten in den Bereichen Kognition, Emotion und Neugier nicht unabhängig voneinander sind und stets ein Mindestmaß an Unsicherheit bestehen bleibt.

- **Kombinierte Stabilitätsbedingung**:

  $$
  \left(\Delta K_{mess} \cdot \Delta K_{entw}\right) \times \left(\Delta C_{kog} \cdot \Delta E \cdot \Delta N\right) \geq \left[C(\gamma)\right]^2
  $$

  Die Stabilität des Bildungsprozesses hängt davon ab, dass äußere Beobachtungsrelationen und innere Autopoiesis gleichzeitig innerhalb ihrer Kopplungsgrenzen gehalten werden.

## 2.4 Versionierung als Operation

Versionierung lässt sich als diskrete Operation begreifen, die jeden Zustand des Lernsystems in eine beobachtbare Version überführt. Dadurch entsteht ein struktureller Balanceakt:

- **Reduktion temporaler Unsicherheit**: Jeder Commit markiert einen Stabilitätspunkt und reduziert kurzfristig $\Delta K_{entw}$, weil der Entwicklungsverlauf fixiert wird.
- **Zunahme epistemischer Unsicherheit**: Dieselbe Versionierung erzeugt neue Differenzen für die Beobachtung und erhöht $\Delta K_{mess}$, da jedes neue Artefakt erneut validiert werden muss.
- **Rückkopplung auf Neugier**: Die Veränderung der Mess- und Entwicklungsunsicherheiten moduliert $\Delta N$, indem neue explorative Horizonte geöffnet oder geschlossen werden.

Formal lässt sich der Balanceeffekt skizzieren als:

$$
\Delta K_{entw}(t+1) \downarrow \quad \Rightarrow \quad \Delta K_{mess}(t+1) \uparrow \quad \Rightarrow \quad \Delta N(t+1) \text{ moduliert}
$$

Damit wird sichtbar, dass jede Versionierung Ordnung (Fixpunkte) und Varianz (neue Differenzen) gleichermaßen erzeugt – genau der autopoietische Kern von Kompetenzentwicklung innerhalb der Grenze $C(\gamma)$.

## 2.5 Beispiele

- **Beispiel 1: Kompetenzmessung ($\Delta K_{mess}$)**: Bei einer Prüfung wird der Wissensstand eines Lernenden falsch eingeschätzt, weil externe Faktoren wie Müdigkeit oder Stress die Ergebnisse verfälschen.
- **Beispiel 2: Kompetenzentwicklung ($\Delta K_{entw}$)**: Über einen Zeitraum von mehreren Monaten zeigt ein Lernender inkonsistente Fortschritte, was auf emotionale und soziale Einflüsse zurückzuführen ist.
- **Beispiel 3: Emotionale Unsicherheit ($\Delta E$)**: Ein Lernender verliert in einer Prüfungssituation durch hohe emotionale Unsicherheit das Selbstvertrauen und zeigt dadurch schlechtere Leistungen.
- **Beispiel 4: Kognitive Unsicherheit ($\Delta C_{kog}$)**: Ein Lernender versteht theoretisch ein mathematisches Konzept, kann es jedoch nicht in einer praktischen Anwendung umsetzen.
- **Beispiel 5: Neugierunsicherheit ($\Delta N$)**: Ein Lernender, der anfangs sehr neugierig ist, verliert das Interesse, wenn die Inhalte zu komplex oder zu wenig relevant erscheinen.

# 3 Folgerungen

- **Aspekt 1: Dynamische Unsicherheiten**: Sowohl die Mess- als auch die Entwicklungsunsicherheit sind dynamisch und werden stark von äußeren und inneren Faktoren beeinflusst.
- **Aspekt 2: Interdependenz**: Die Unsicherheiten in den Bereichen Kognition, Emotion und Neugier beeinflussen einander wechselseitig. Eine Reduktion der Unsicherheit in einem Bereich kann eine Zunahme der Unsicherheiten in den anderen Bereichen nach sich ziehen.
- **Aspekt 3: Praktische Anwendung**: Um Unsicherheiten im Lernprozess zu reduzieren, müssen gezielte Interventionen auf verschiedenen Ebenen (emotionale Unterstützung, kognitive Förderung, Stimulation der Neugier) erfolgen.

ΔK war in meinem Modell dreifach besetzt – Messung, Entwicklung und Kognition – und erzeugte eine konzeptionelle Überlagerung. Die drei Dimensionen adressieren jedoch verschiedene Beobachtungsebenen: die externe Messung ($\Delta K_{mess}$), die interne Entwicklungsdynamik ($\Delta K_{entw}$) und die inhaltlich-semantische Unsicherheit ($\Delta C_{kog}$). Ergänzend bilden die affektive Varianz ($\Delta E$) und die explorative Neugierunsicherheit ($\Delta N$) das innere Kopplungsfeld. Versionierung wirkt direkt auf $\Delta K_{entw}$, indem sie temporäre Stabilitätspunkte im Lernverlauf erzeugt, während sie gleichzeitig neue Messunsicherheiten ($\Delta K_{mess}$) hervorbringt und über Rückkopplungen $\Delta N$ moduliert. Damit wird sichtbar, dass jede Versionierung zugleich Ordnung und Varianz generiert – genau der autopoietische Kern von Kompetenzentwicklung, begrenzt durch den Kopplungsfaktor $C(\gamma)$.

# 4 Implikationen

- **Implikation 1**: Lehrkräfte sollten bei der Kompetenzmessung stets externe Einflüsse und emotionale Faktoren berücksichtigen, um zu verhindern, dass Messfehler den Lernfortschritt verfälschen.
- **Implikation 2**: In der Kompetenzentwicklung müssen langfristige individuelle Schwankungen in der Lernleistung berücksichtigt werden, um realistische Entwicklungsprognosen zu stellen.
- **Implikation 3**: Die Förderung von Neugier und emotionaler Stabilität ist entscheidend, um Unsicherheiten in der Kognition und im Lernprozess zu verringern.

# 5 Zusammenfassung

Die **Kompetenzmessunsicherheit ($\Delta K_{mess}$)** und die **Kompetenzentwicklungsunsicherheit ($\Delta K_{entw}$)** bilden den äußeren Kopplungsraum zwischen Beobachtung und Dynamik, während **kognitive ($\Delta C_{kog}$)**, **emotionale ($\Delta E$)** und **neugierbezogene Unsicherheiten ($\Delta N$)** die innere Autopoiesis strukturieren. Die Relationen $\Delta K_{mess} \cdot \Delta K_{entw} \geq C(\gamma)$ und $\Delta C_{kog} \cdot \Delta E \cdot \Delta N \geq C(\gamma)$ sichern gemeinsam, dass der Bildungsprozess nur stabil bleibt, wenn beide Unsicherheitsräume innerhalb ihrer Kopplungsgrenzen balanciert werden. Versionierung fungiert als operativer Hebel, der temporale Stabilität und neue Beobachtungsdifferenzen gleichzeitig erzeugt und so den autopoietischen Charakter von Kompetenzentwicklung sichtbar macht.

# Quelle(n)

- Beispielquelle: Luhmann, N. (1997). *Soziale Systeme: Grundriss einer allgemeinen Theorie*. Suhrkamp Verlag.
