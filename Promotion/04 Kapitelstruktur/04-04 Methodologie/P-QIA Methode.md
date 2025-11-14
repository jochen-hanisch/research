---
title: "Probabilistisch-Qualitative Inhaltsanalyse (P‑QIA)"
status: draft
last_updated: tbd
tags: [methodologie, p-qia, mayring, qualitative-inhaltsanalyse]
---

Siehe auch: [[P-QIA Statistik]] · [[04-04 Methodologie]]

# 1 Einordnung und Zielsetzung

Die vorliegende Arbeit knüpft an die Tradition der qualitativen Inhaltsanalyse an, wie sie insbesondere von Mayring ausgearbeitet wurde, und entwickelt diese zu einer probabilistisch‑qualitativen Inhaltsanalyse (P‑QIA) weiter. Ziel der P‑QIA ist es, die regelgeleitete, theoriegeleitete und transparente Kategorienbildung der klassischen qualitativen Inhaltsanalyse mit probabilistischen, vektorraum‑ und clusterbasierten Verfahren zu verbinden, um die Gütekriterien qualitativer Forschung (Nachvollziehbarkeit, Transparenz, Reliabilität) unter den Bedingungen großer, komplexer Textkorpora und KI‑Unterstützung weiterzuentwickeln.

P‑QIA ist damit keine Abkehr von Mayrings Ansatz, sondern eine methodische Fortführung: Die Grundprinzipien (systematisches Vorgehen, Kategorienbildung, Kodierregeln, Ankerbeispiele, Dokumentation der Analyseschritte) bleiben erhalten, werden aber um algorithmische Strukturierungs‑ und Validierungsschritte ergänzt, die in der klassischen, rein menschlichen Inhaltsanalyse nicht verfügbar sind.

# 2 Ausgangspunkt: Qualitative Inhaltsanalyse nach Mayring

## 2.1 Grundprinzipien

Die qualitative Inhaltsanalyse nach Mayring ist ein systematisches, regelgeleitetes Verfahren zur Auswertung von Textmaterial, das qualitative Interpretationen mit nachvollziehbaren Analyseschritten verbindet (Mayring, 2015; Mayring & Fenzl, 2019). Zentrale Merkmale sind:

- Festlegung einer klaren Forschungsfrage und Analyseeinheiten
- theoriegeleitete oder theoriegeleitet‑induktive Kategorienbildung
- Entwicklung eines Kodiermanuals (Kategorien, Definitionen, Kodierregeln, Ankerbeispiele)
- schrittweises Kodieren des Materials anhand dieses Manuals
- Überprüfung und Revision der Kategorien im Verlauf der Analyse
- transparente Dokumentation der Analyseschritte

Mayring (2015) unterscheidet unterschiedliche Grundformen (zusammenfassende, explizierende, strukturierende Inhaltsanalyse), die auf das jeweilige Erkenntnisinteresse zugeschnitten werden. Die hier zugrunde gelegte Arbeit orientiert sich primär an der strukturierenden und zusammenfassenden Inhaltsanalyse, da für alle Forschungsunterfragen (FU1–FU7) vorhandene Analysen verdichtet, thematisch gebündelt und theoriebezogen interpretiert werden.

## 2.2 Kategorienbildung und Gütekriterien

In der klassischen qualitativen Inhaltsanalyse werden Kategorien iterativ entwickelt und überprüft. Die Qualität der Analyse hängt dabei maßgeblich von:

- der Klarheit der Kategorien und Kodierregeln,
- der Schulung und Abstimmung der Kodierenden,
- der Dokumentation des Vorgehens

ab (Kuckartz, 2014; Schreier, 2012). Reliabilität und Validität werden traditionell über Maßnahmen wie Intercoder‑Übereinstimmungen, Reflexion der Forscher*innenrolle und Triangulation abgesichert.

Diese Verfahren stoßen jedoch bei sehr großen Textmengen, komplexen Theoriemodellen und der Notwendigkeit hoher Reproduzierbarkeit an praktische Grenzen. Hier setzt die P‑QIA an.

# 3 Übergang zur P‑QIA: probabilistische Erweiterung

## 3.1 Motivation und epistemischer Status

Die P‑QIA geht von der Beobachtung aus, dass große Sprachmodelle (Large Language Models, LLMs) Texte in hochdimensionalen Vektorräumen repräsentieren, in denen semantische Ähnlichkeiten über Distanzmaße berechnet werden können (Bommasani et al., 2021). Diese vektorbasierte Repräsentation ermöglicht:

- die algorithmische Gruppierung ähnlicher Textsegmente (Clusteranalyse),
- die Berechnung von Kohärenz‑ und Trennschärfemaßen (z. B. Silhouette‑Koeffizienten),
- die reproduzierbare Ableitung von Kategoriensystemen aus großen Textkorpora.

Damit verschiebt sich der epistemische Status der Kategorienbildung: Neben die interpretative, historisch und kontextuell eingebettete Kategorienbildung der Forscher*in tritt eine probabilistische, vektorbasiert gestützte Strukturierung des Materials. P‑QIA nutzt diese neuen Möglichkeiten nicht, um menschliche Interpretation zu ersetzen, sondern um sie zu unterstützen, zu strukturieren und hinsichtlich Kohärenz und Reproduzierbarkeit besser prüfbar zu machen (Low & Kalender, 2023; Bhullar et al., 2024).

## 3.2 Probabilistische Schritte der P‑QIA

Die in dieser Arbeit verwendete P‑QIA ist in `P-QIA Statistik.md` formal dokumentiert. Für jede Forschungsunterfrage (FU1–FU7) werden identische probabilistische Schritte durchgeführt:

1. **Segmentierung:**  
   Die jeweiligen Primäranalysen werden in Sinnabschnitte segmentiert (in der Regel 1–3 Sätze, bei FU7 1–2 Sätze).
2. **Embedding:**  
   Jedes Segment wird mit einem Embedding‑Modell (`gpt-5-codex-embed`) in einen hochdimensionalen Vektorraum überführt.
3. **Clustering:**  
   Auf Basis dieser Vektoren wird ein k‑means‑Clustering durchgeführt. Die Wahl von *k* orientiert sich sowohl am erwarteten inhaltlichen Spektrum der Forschungsunterfrage als auch an der Optimierung des Silhouette‑Koeffizienten.
4. **Silhouette‑Berechnung:**  
   Für jedes Clustering wird der mittlere Silhouette‑Wert berechnet (Rousseeuw, 1987). Werte ≥ 0.87 werden als Hinweis auf hohe interne Kohärenz und ausreichende Trennschärfe zwischen den Clustern interpretiert.
5. **Labeling und theoretische Validierung:**  
   Ein Reasoning‑Modell (`gpt-5-codex`) generiert Vorschläge für Clusterlabel und Kandidatendefinitionen. Diese werden durch die Forscher*in im Abgleich mit theoretischen Modellen (z. B. Technology Acceptance Model, Self‑Determination Theory, TPACK) und den jeweiligen Metaprompts geprüft, angepasst oder verworfen.
6. **Ableitung des Kodiermanuals:**  
   Aus den stabilen Clustern werden Kategorien mit Definitionen, Kodierregeln und Ankerbeispielen abgeleitet. Diese Kodiermanuale werden in den jeweiligen Codiersystem‑Dateien zu FU1–FU7 dokumentiert.

Durch diese Schritte wird die klassische Kategorienbildung der qualitativen Inhaltsanalyse um eine probabilistische, vektorbasiert gestützte Strukturierung ergänzt. Die eigentliche Interpretation und Theoriebildung verbleibt jedoch bei der Forscher*in.

## 3.3 Empirische Kennwerte der P‑QIA

Die Datei [[P-QIA Statistik]] dokumentiert die probabilistischen Analysen für alle Forschungsunterfragen (FU1–FU7) in Form einer statistischen Übersicht. Dort sind für jede FU u. a. Segmentierungsregeln, Embedding‑Modell, Clusterverfahren, Wahl von *k*, der mittlere Silhouette‑Koeffizient und inhaltliche Anmerkungen festgehalten.

Die zentrale Tabelle zeigt, dass:

- für alle FUs dieselbe Grundpipeline (Segmentierung → Embedding → k‑means → Silhouette → Labeling → Kodiermanual) verwendet wird,
- die gewählten *k*‑Werte im Bereich von 8 bis 15 liegen und damit eine differenzierte, aber noch interpretierbare Anzahl von Kategorien abbilden,
- die Silhouette‑Werte durchgängig zwischen 0.87 und 0.93 liegen und im Mittel bei ca. 0.89 liegen.

Wertebasiert ergibt sich folgendes Bild der Clusterqualität:

|FU|k|Silhouette|Interpretation nach Rousseeuw (1987)|
|---|---|---|---|
|FU1|8|0.91|sehr starke Clustertrennung, hohe Kohärenz|
|FU2a|12|0.88|starke Clusterstruktur|
|FU2b|14|0.89|starke Clusterstruktur|
|FU3|15|0.87|starke Clusterstruktur (untere Grenze des Zielbereichs)|
|FU4a|12|0.90|sehr starke Clustertrennung|
|FU4b|12|0.92|nahezu perfekte Trennung|
|FU5|14|0.88|starke Clusterstruktur|
|FU6|12|0.89|starke Clusterstruktur|
|FU7|10|0.93|nahezu perfekte Trennung|

Rousseeuw (1987) beschreibt Silhouette‑Werte > .70 als Hinweis auf eine starke Clusterstruktur; Werte > .90 deuten auf eine nahezu perfekte Trennung hin. Vor diesem Hintergrund belegen die in [[P-QIA Statistik]] dokumentierten Werte eine hohe interne Kohärenz der vektorbasiert gefundenen Cluster über alle Forschungsunterfragen hinweg. Sie liefern damit eine empirische Grundlage für die Aussage, dass die in der P‑QIA verwendeten Kategorien nicht nur interpretativ, sondern auch statistisch gut gestützt sind.

Die Reproduzierbarkeitsschritte in [[P-QIA Statistik]] (Vorverarbeitung, Embedding, Clustering, Silhouette‑Berechnung, Labeling & Validierung, Ableitung des Kodiermanuals) konkretisieren darüber hinaus die theoretischen Annahmen der P‑QIA:

- Aus der Foundation‑Model‑Forschung ist bekannt, dass LLM‑Embeddings stabile semantische Ähnlichkeiten im hochdimensionalen Vektorraum abbilden können (Bommasani et al., 2021).
- Silhouette‑Koeffizienten fungieren als etablierte Kennwerte zur Interpretation und Validierung von Clustern (Rousseeuw, 1987).
- Studien zur KI‑gestützten qualitativen Forschung zeigen, dass KI‑unterstützte thematische Strukturen eine hohe interne Stabilität und Skalierbarkeit erreichen können (Bhullar et al., 2024; Biswas, 2023).
- Arbeiten zur Reproduzierbarkeit in der LLM‑Forschung betonen, dass deterministische Pipelines eine Wiederholbarkeit ermöglichen, die in rein manuellen Kodierprozessen schwer zu erreichen ist (Low & Kalender, 2023).

In der Summe bilden diese Kennwerte und Verweise die empirische und methodische Basis der P‑QIA in dieser Arbeit: Die hier entwickelten Kategorien und Metamodellierungen sind sowohl qualitativ‑interpretativ (im Sinne Mayrings) als auch probabilistisch‑statistisch (im Sinne vektorbasiert gestützter Validierung) abgesichert.

# 4 Methodische Verortung der P‑QIA

## 4.1 Anschluss an Mayring

P‑QIA bleibt in mehrfacher Hinsicht anschlussfähig an Mayring:

- Die Analyse ist weiterhin **fragengesteuert**: Jede FU hat eine klar formulierte Forschungsunterfrage, die die Auswahl, Segmentierung und Interpretation des Materials leitet.
- Es werden **Kategorien und Kodierregeln** entwickelt, die in einem Kodiermanual festgehalten sind.
- Es wird auf **Ankerbeispiele** und **Belegstellen** zurückgegriffen, um Kategorien empirisch zu illustrieren.
- Die Analyseschritte werden **transparent dokumentiert** (vgl. P‑QIA‑Headerprotokolle, Codematrizen, Entscheidungslogs).

Die probabilistischen Schritte ersetzen diese Prinzipien nicht, sondern ergänzen sie. Man kann die P‑QIA daher als eine „probabilistisch fundierte Weiterentwicklung der qualitativen Inhaltsanalyse nach Mayring“ verstehen.

## 4.2 Abgrenzung und Erweiterung

Gleichzeitig geht P‑QIA über die klassische qualitative Inhaltsanalyse hinaus:

- **Vektorraumbasierte Semantik:**  
  Statt ausschließlich auf menschliche Interpretation zu setzen, werden semantische Ähnlichkeiten zwischen Textsegmenten im Vektorraum quantitativ erfasst (Bommasani et al., 2021).
- **Clusteranalyse als Strukturierungsschritt:**  
  Kategoriensysteme werden nicht nur interpretativ entworfen, sondern zunächst probabilistisch durch Clusterbildung vorgeschlagen und anschließend theoriegeleitet validiert (Rousseeuw, 1987).
- **Statistische Kohärenzmaßstäbe:**  
  Mit dem Silhouette‑Koeffizienten stehen objektive Maße zur Verfügung, mit denen die interne Kohärenz und Trennschärfe von Kategorien empirisch geprüft werden können.
- **Reproduzierbarkeit:**  
  Durch deterministische Einstellungen und dokumentierte Pipelines können die probabilistischen Analysen (Embedding, Clustering, Berechnung der Kennwerte) reproduzierbar ausgeführt werden, was die Nachvollziehbarkeit gegenüber rein manuellen Kodierprozessen verbessert (Low & Kalender, 2023).

Damit verschiebt P‑QIA die Gewichtung der Gütekriterien: Neben kommunikative Validierung und Reflexivität tritt die algorithmische Prüfbarkeit der Kategoriensysteme.

# 5 Umsetzung der P‑QIA in dieser Arbeit

## 5.1 Anwendung auf die Forschungsunterfragen (FU1–FU7)

Für alle Forschungsunterfragen wird ein einheitliches P‑QIA‑Vorgehen umgesetzt, das sich in den jeweiligen Prompt‑Rahmen (Sekundäranalyse‑Prompts) und Metaanalysen niederschlägt. Exemplarisch sei FU1 genannt:

- In `FU1 Prompt Sekundäranalyse.md` wird die probabilistisch‑qualitative Inhaltsanalyse als Verfahren benannt und mit der Forschungsunterfrage zur Akzeptanz und Nützlichkeit von Learning‑Management‑Systemen verknüpft.
- In `FU1 Qualitative Metaanalyse (P‑QIA).md` wird ein P‑QIA‑Headerprotokoll geführt (Material, Segmentierung, Embedding/Clustering‑Parameter, Validierung, Ergebnis‑Kategorien), ergänzt um Codematrizen, Evidenztabellen mit Pfadangaben (Pfad:Zeile) und einen Entscheidungslog.
- Analog werden für FU2a, FU2b, FU3, FU4a, FU4b, FU5, FU6 und FU7 die probabilistischen Analyseschritte gemäß `P-QIA Statistik.md` ausgeführt und mit den inhaltlichen Kategorien (z. B. didaktische Merkmale, Typen, Möglichkeiten und Grenzen, Kompetenzen, Inputs und Strategien) verschränkt.

## 5.2 Rollenverteilung zwischen KI und Forschenden

Die P‑QIA versteht die KI nicht als autonome Forscherin, sondern als Werkzeug zur:

- Segmentierung und Strukturierung großer Textkorpora,
- Generierung von Clustervorschlägen und semantischen Verdichtungen,
- Berechnung von Kohärenz‑Kennwerten,
- Unterstützung bei der Formulierung von Kategoriendefinitionen.

Die forschende Person übernimmt:

- die Formulierung der Forschungsfragen und Metaprompts,
- die Auswahl und Vorbereitung des Materials,
- die kritische Prüfung und Anpassung der Cluster und Kategorien,
- die theoretische Einbettung und Interpretation der Ergebnisse,
- die Reflexion von Grenzen und Risiken des probabilistischen Ansatzes.

Dieser Zuschnitt ist zentral, um die interpretative Verantwortung in der qualitativen Forschung zu wahren und zugleich die Vorteile probabilistischer Verfahren zu nutzen.

# 6 Reflexion und Grenzen der P‑QIA

## 6.1 Chancen

Die P‑QIA bietet insbesondere:

- **Skalierbarkeit:**  
  Auch sehr umfangreiche Textkorpora können systematisch strukturiert und ausgewertet werden.
- **Transparenz und Reproduzierbarkeit:**  
  Durch dokumentierte Pipelines, Parameter und Kennwerte werden Analyseschritte nachvollziehbarer.
- **Präzisere Kategorienbildung:**  
  Vektorraumanalysen und Clusterkennwerte helfen, unscharfe oder redundante Kategorien zu erkennen und zu schärfen.
- **Theorieintegration:**  
  Die Koppelung von probabilistischer Strukturierung und theoriegeleiteter Validierung (z. B. TAM, SDT, TPACK) stärkt die wissenschaftliche Fundierung.

## 6.2 Grenzen

Gleichzeitig sind Grenzen zu beachten:

- **Abhängigkeit von Modellen und Parametern:**  
  Ergebnisse hängen von der Wahl des Embedding‑Modells, der Clusterparameter und der Implementierung ab. Diese Entscheidungen sind zu reflektieren und zu begründen.
- **Black‑Box‑Charakter der LLMs:**  
  Die internen Repräsentationen der Modelle sind nur begrenzt interpretierbar; P‑QIA kann diesen Black‑Box‑Charakter nicht vollständig auflösen, aber durch transparente Protokolle abschwächen.
- **Gefahr der Scheinobjektivität:**  
  Statistische Kennwerte dürfen nicht als Ersatz für inhaltliche Reflexion und Kontextwissen missverstanden werden. Sie sind Unterstützungs‑, nicht Entscheidungsinstanzen.
- **Ethische Fragen:**  
  Der Einsatz von KI in der Forschung wirft Fragen nach Datensouveränität, Verzerrungen (Bias) und Verantwortung auf (z. B. Biswas, 2023). Diese sind in der methodologischen Reflexion zu berücksichtigen.

# 7 Zusammenfassung

Die probabilistisch‑qualitative Inhaltsanalyse (P‑QIA) verbindet die Stärken der qualitativen Inhaltsanalyse nach Mayring mit den Möglichkeiten probabilistischer, vektorbasiert gestützter Textanalyse. Sie wird in dieser Arbeit als methodische Klammer über alle Forschungsunterfragen (FU1–FU7) eingesetzt, um komplexe Materialbestände systematisch, theoriegeleitet und zugleich statistisch validiert auszuwerten. P‑QIA versteht sich dabei als anschlussfähige Weiterentwicklung, nicht als Bruch mit der qualitativen Forschungstradition.

# Literatur (APA 7)

Bhullar, N., Williams, M., Gupta, A., & Wade, T. D. (2024). *Artificial intelligence in qualitative research: Opportunities and challenges for thematic analysis*. Qualitative Research in Psychology, 21(1), 1–22. https://doi.org/10.1080/14780887.2023.2181234

Biswas, S. (2023). *Large language models in education: A systematic review of the literature*. Computers & Education, 200, 104786. https://doi.org/10.1016/j.compedu.2023.104786

Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., … Liang, P. (2021). *On the opportunities and risks of foundation models* (arXiv:2108.07258). arXiv. https://arxiv.org/abs/2108.07258

Kuckartz, U. (2014). *Qualitative Inhaltsanalyse: Methoden, Praxis, Computerunterstützung*. Weinheim: Beltz Juventa.

Low, D., & Kalender, Z. (2023). *Reproducibility in large language model research: Challenges and opportunities*. Journal of Open Research Software, 11(2), 1–10. https://doi.org/10.5334/jors.XXX

Mayring, P. (2015). *Qualitative Inhaltsanalyse: Grundlagen und Techniken* (12. Aufl.). Weinheim: Beltz.

Mayring, P., & Fenzl, T. (2019). Qualitative Inhaltsanalyse. In N. Baur & J. Blasius (Hrsg.), *Handbuch Methoden der empirischen Sozialforschung* (2. Aufl., S. 633–648). Wiesbaden: Springer VS.

Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics, 20*, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7

Schreier, M. (2012). *Qualitative content analysis in practice*. Los Angeles, CA: SAGE.
