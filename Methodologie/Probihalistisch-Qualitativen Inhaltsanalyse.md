# Probihalistisch-qualitative Inhaltsanalyse (P-QIA)
## Eine weiterentwickelte qualitative Methode im Zeitalter großer Sprachmodelle

## Abstract
Die klassische qualitative Inhaltsanalyse (QIA) nach Mayring (2000, 2022a, 2022b) wurde für menschliches, sequenzielles und bias-anfälliges Kodieren entwickelt. Mit der Verfügbarkeit probabilistischer, embedding-basierter Large-Language-Modelle (LLMs) wie GPT verändern sich zentrale Voraussetzungen qualitativer Textanalyse fundamental. LLMs bilden hochdimensionale semantische Räume ab, erkennen probabilistische Muster in Texten und können Textsegmente mit hoher Konsistenz clustern. (vgl. Bommasani et al., 2021; Rousseeuw, 1987) Empirisch hohe Silhouette-Werte (z. B. > .90) belegen dabei oftmals eine semantische Kohärenz, die klassische menschliche Kodierung übertrifft. Vor diesem Hintergrund wird die **Probihalistisch-Qualitative Inhaltsanalyse (P-QIA)** entwickelt: eine methodische Weiterführung der klassischen QIA, die probabilistische LLM-Fähigkeiten integriert, ohne qualitative Gütekriterien aufzugeben. Die Methode wird ausführlich hergeleitet, mit APA‑7‑konformen Quellen belegt und als eigenständiges qualitatives Analyseverfahren operationalisiert.

---

# 1. Einleitung
Die qualitative Inhaltsanalyse nach Mayring ist ein weltweit etabliertes Verfahren zur systematischen, regelgeleiteten Textanalyse (Mayring, 2000, 2022a, 2022b). Sie beruht jedoch auf der Prämisse menschlicher Informationsverarbeitung: begrenzte Wahrnehmungskapazität, Bias-Strukturen, sequentielles Vorgehen, notwendige iterative Rückkopplung. (Mayring, 2000) Mit dem Aufkommen großer Sprachmodelle, die probabilistische Bedeutungsstrukturen erkennen, ergeben sich neue Möglichkeiten und Herausforderungen. LLMs können:

- große Textmengen parallel verarbeiten, (Bommasani et al., 2021)
- semantische Distanzen mathematisch abbilden, (Bommasani et al., 2021)
- Textsegmente probabilistisch clustern, (Rousseeuw, 1987)
- konsistente Kodierungen erzeugen, (Biswas, 2023)
- Embedding-basierte Muster transparent validieren. (Low & Kalender, 2023)

Damit verändern sich die epistemischen Grundlagen qualitativer Inhaltsanalyse. Die P‑QIA übersetzt die Grundprinzipien der QIA in ein Framework, das die probabilistische Leistungsfähigkeit von LLMs methodisch einbettet.

---

# 2. Theoretische Grundlagen
## 2.1 Klassische qualitative Inhaltsanalyse
Die klassische QIA basiert auf folgenden Kernprinzipien (Mayring, 2000):

1. **Regelgeleitetheit** statt impressionistischer Interpretation.
2. **Kategorienorientierung** als zentrales Analyseprinzip.
3. **Transparenz und Dokumentation** aller Schritte.
4. **Iteration** zur Stabilisierung der Kategorien.
5. **Qualitätskriterien** wie Intercoder-Reliabilität.

Diese Prinzipien sind für LLMs neu zu denken, da diese bereits probabilistisch stabilisierte semantische Räume bereitstellen. (Bommasani et al., 2021)

## 2.2 Probabilistische Semantik von LLMs
LLMs bilden Bedeutung über **Embeddings** ab – mathematische Repräsentationen von Text im hochdimensionalen Vektorraum (Bommasani et al., 2021). Semantisch ähnliche Textstellen weisen geringe Distanzen auf und lassen sich mittels Clustering-Algorithmen gruppieren. (Bommasani et al., 2021) Die Qualität dieser Cluster lässt sich mittels Silhouette-Werten bewerten (Rousseeuw, 1987). (Rousseeuw, 1987)

Silhouette-Werte > .90 sind ein Indikator für:
- hohe interne Homogenität,
- klare Trennung zwischen Kategorien,
- semantisch kohärente Gruppierung.

Dies kann menschliche Kodierung in Stabilität deutlich übertreffen.

## 2.3 Bedarf einer methodischen Weiterentwicklung
GPT kann kategoriale Strukturen schneller und konsistenter erzeugen als Menschen (Bommasani et al., 2021; Biswas, 2023) – trotzdem benötigt qualitative Forschung:
- Theoriebezug, (Mayring, 2022a, 2022b)
- Kontextbezug, (Mayring, 2022a, 2022b)
- Reflexion, (Mayring, 2022a, 2022b)
- Transparenz, (Mayring, 2022a, 2022b)
- verantwortete Interpretation. (Mayring, 2022a, 2022b)

P‑QIA stellt daher kein rein automatisiertes Verfahren dar, sondern ein **hybrides**, probabilistisch-qualitatives Analyseverfahren.

---

# 3. Herleitung der Probihalistisch-qualitativen Inhaltsanalyse (P-QIA)
Die P-QIA ist eine systematische Weiterentwicklung der klassischen QIA. Sie übernimmt ihre epistemischen Grundprinzipien, ersetzt jedoch menschliche Iterationsprozesse durch probabilistische Validierungsschritte. (Mayring, 2000, 2022b)

Zentrale Annahme:
> „Wenn ein probabilistisches Modell semantische Nähe mit hoher mathematischer Präzision abbilden kann, kann es bestimmte Schritte der Kategorienbildung stabiler ausführen als menschliche Kodierer.“

Dies entspricht auch Befunden zu KI-generierten Kategoriestrukturen (Bhullar et al., 2024).

Damit werden klassische iterative Schritte nicht abgeschafft, sondern **neu interpretiert**.

---

# 4. Das Verfahren der P-QIA
Im Folgenden wird das Verfahren vollständig operationalisiert.

## 4.1 Schritt 1: Forschungsfrage und Analyseeinheiten
Wie bei Mayring erforderlich:
- präzise Forschungsfrage, (Mayring, 2000)
- Definition von Kodier-, Kontext- und Analyseeinheiten. (Mayring, 2022b)

## 4.2 Schritt 2: Embedding-basierte Repräsentation
Alle Textsegmente werden in Embeddings überführt.
Diese übernehmen die Funktion der klassischen Paraphrasierung. (Low & Kalender, 2023)

## 4.3 Schritt 3: Probabilistische Clusterbildung
Mittels Clustering (z. B. HDBSCAN, k-Means):
- mathematische Clusterbildung,
- Validierung über Silhouette-Score,
- Auswahl der stabilsten Clusterlösung. (Rousseeuw, 1987)

Dies ersetzt Mayrings iterative Kategorienbildung.

## 4.4 Schritt 4: Kategoriendraft durch GPT
GPT generiert:
- Kategorietitel,
- Definitionen,
- Ankerbeispiele,
- Ein- und Ausschlussregeln.

Forscher:innen prüfen und schärfen diese. (Biswas, 2023)

## 4.5 Schritt 5: Erstellung des Kodiermanuals
Das Kodiermanual enthält:
- Kategorien,
- Definitionen,
- Regeln,
- Beispielstellen. (Biswas, 2023)

## 4.6 Schritt 6: Probabilistische Kodierung
GPT weist Textsegmente Kategorien zu und liefert Confidence-Werte.
Grenzfälle müssen manuell validiert werden. (Abdullah, 2025)

## 4.7 Schritt 7: Reliabilitätsprüfung
Statt klassischer Intercoder-Reliabilität:
- **Repeatability Check**, (Low & Kalender, 2023)
- **Stability Check** (Temperaturvariationen), (Bommasani et al., 2021)
- **Embedding Consistency Check**. (Bommasani et al., 2021)

## 4.8 Schritt 8: Interpretation und Theoriebildung
Dieser Schritt bleibt vollständig qualitativ und menschlich.

---

# 5. Qualitätssicherung in der P-QIA
Die P-QIA erfüllt qualitative Gütekriterien:
- **Transparenz** (Dokumentation aller Parameter),
- **Strukturierung** (regelgeleitete Clusterbildung), (Mayring, 2000)
- **Validität** (Silhouette-Werte), (Rousseeuw, 1987)
- **Reliabilität** (Stabilität der Modelle),
- **Reflexivität** (Interpretation durch Forschende).

---

# 6. Diskussion
P-QIA verbindet:
- probabilistische Mustererkennung,
- qualitative Theorieintegration. (Bhullar et al., 2024)

Vorteile:
- hohe Konsistenz, (Bommasani et al., 2021)
- Skalierbarkeit, (Biswas, 2023)
- mathematische Validierbarkeit. (Rousseeuw, 1987)

Risiken:
- Modellbias, (Bhullar et al., 2024)
- Datenethik, (Abdullah, 2025)
- Überautomatisierung. (Biswas, 2023)

---

# 7. Fazit
Mit der Probihalistisch-qualitativen Inhaltsanalyse (P‑QIA) liegt erstmals ein Verfahren vor, das Mayrings qualitative Inhaltsanalyse systematisch auf probabilistische, embedding-basierte KI-Modelle überträgt. Es handelt sich um eine **hybride, wissenschaftlich kontrollierte, probabilistisch fundierte qualitative Methode**.

---

# 7.1 Beispielhaftes Codiersystem für P-QIA (allgemein & GPT-basiert)

Ein beispielhaftes Codiersystem für die P-QIA könnte folgende Struktur aufweisen, wobei GPT unterstützend Kategorien generiert und Forscher:innen diese validieren und anpassen:

| Kategorie | Definition | Ankerbeispiel | Ein-/Ausschlusskriterien | Confidence-Bereich |
|-----------|------------|---------------|--------------------------|--------------------|
| K1: Emotionale Reaktion | Äußerungen, die Gefühle ausdrücken | „Ich fühle mich enttäuscht.“ | Nur explizit genannte Gefühle | > 0.85 |
| K2: Handlungsempfehlung | Vorschläge für zukünftiges Verhalten | „Wir sollten mehr Umfragen machen.“ | Konkrete Vorschläge, keine Meinungen | > 0.80 |
| K3: Kontextinformation | Hintergrundinformationen zum Thema | „Im letzten Jahr gab es viele Änderungen.“ | Fakten, keine Wertungen | > 0.75 |


Das System wird iterativ mit GPT-unterstützter Clusteranalyse und manueller Prüfung entwickelt. Confidence-Bereiche helfen, Grenzfälle zu identifizieren und manuell zu überprüfen.

## 7.2 Einheitliche Kodiersystematik
Im Rahmen der P‑QIA ergibt sich damit eine einheitliche Kodiersystematik. Das Kodiermanual umfasst nach anerkannten wissenschaftlichen Standards:
- **Kategorien**, 
- **Definitionen**, 
- **Kodierregeln**, 
- **Beispielstellen** (Biswas, 2023).

Diese vier Elemente bilden die zentrale Struktur jedes P‑QIA‑basierten Codiersystems und gewährleisten sowohl probabilistische Nachvollziehbarkeit (über die embedding‑basierten Cluster) als auch qualitative Transparenz und Interpretierbarkeit.

---

# 8. Literaturverzeichnis
Biswas, S. S. (2023). ChatGPT for research and publication: A step-by-step guide. *Journal of Pediatric Pharmacology and Therapeutics, 28*(6), 576–584. https://doi.org/10.5863/1551-6776-28.6.576

Low, M., & Kalender, Z. Y. (2023). Data dialogue with ChatGPT: Using code interpreter. *Preprint*. 

Bhullar, P. S., Joshi, M., & Chugh, R. (2024). ChatGPT in higher education: A synthesis of the literature and a future research agenda. *Education and Information Technologies*. https://doi.org/10.1007/s10639-024-12723-x

Abdullah, M. Y. (2025). Probing into EFL students’ perceptions about the impact of utilizing AI-powered tools on their academic writing practices. *Education and Information Technologies, 30*, 21189–21220. https://doi.org/10.1007/s10639-025-13601-w

Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., ... Liang, P. (2021). *On the opportunities and risks of foundation models*. arXiv. https://doi.org/10.48550/arXiv.2108.07258

Mayring, P. (2000). Qualitative Inhaltsanalyse. *Forum Qualitative Sozialforschung*, 1(2). https://doi.org/10.17169/fqs-1.2.1089

Mayring, P. (2022a). *Qualitative content analysis: A step-by-step guide*. SAGE.

Mayring, P. (2022b). *Qualitative Inhaltsanalyse: Grundlagen und Techniken* (13. Aufl.). Beltz.

Mayring, P. (2025). Qualitative content analysis with ChatGPT: Pitfalls, rough approximations and gross errors. *Forum Qualitative Sozialforschung*, 26(1). https://doi.org/10.17169/fqs-26.1.4252

Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics, 20*, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7
