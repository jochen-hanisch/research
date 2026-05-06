\newpage

## Korrelationsatlas {#sec:A-4}

Der Korrelationsatlas bündelt die vollständigen Korrelationsmatrizen des Literaturkorpus. Die Darstellungen ergänzen die in Kapitel 4.3 beschriebenen Auswertungen und ermöglichen eine detaillierte Nachvollziehbarkeit der Beziehungen zwischen Forschungsunterfragen, Suchbegriffen, Kategorien und Indizes. Dunklere Farbbereiche markieren höhere positive Zusammenhänge, hellere Bereiche schwächere oder fehlende Korrelationen.

Die Matrizen sind dabei als Strukturübersichten zu verstehen: Sie zeigen Kopplungsstärken und Muster der gemeinsamen Auftretenswahrscheinlichkeit, erlauben keine kausalen Schlussfolgerungen und ersetzen keine inhaltliche Interpretation einzelner Felder. Negative Werte markieren Entkopplungstendenzen im jeweiligen Ausschnitt, nicht „Widerspruch“ im starken Sinn.

Der Rechenweg basiert auf dem aktuellen Export `cluster_data.csv` mit $n=4165$ Zeilen und binär kodierten Tagvariablen. Für jede Matrix wurden die betreffenden Variablengruppen ausgewählt und als Pearson-Korrelationen berechnet; zusätzlich wurden p-Werte ausgewiesen und die Signifikanz markiert. Die FU×FU-Auswertung wurde für die Zusammenfassung auf eindeutige ungeordnete Paare reduziert, weil die Exporttabelle jedes Paar in beiden Richtungen enthält. Dadurch ergeben sich 36 eindeutige FU-Paare. Die paarweisen FU-Korrelationen liegen zwischen $r=-0{,}0575$ und $r=0{,}0394$, die mittlere absolute Korrelation beträgt $|r| \approx 0{,}0214$; neun der 36 Paare sind statistisch signifikant. Diese Signifikanzen werden aufgrund der sehr kleinen Effektstärken als Strukturhinweise gelesen.

Table: Kennwerte der FU×FU-Korrelationsmatrix \label{tab:A-kor-fu-kennwerte}

| Kennwert | Wert |
|---|---:|
| Datenbasis | 4165 |
| Eindeutige FU-Paare | 36 |
| Minimum | -0.0575 |
| Maximum | 0.0394 |
| Mittleres $|r|$ | 0.0214 |
| Signifikante Paare | 9 |

\tabsubcaption{Kennwerte der paarweisen Pearson-Korrelationen zwischen den Forschungsunterfragen, Stand: 2026-05-06. Die Matrix dient der Strukturdiagnostik des Tagraums und wird nicht kausal interpretiert.}

**Forschungsunterfragen und ihre Verknüpfungen**

![Korrelationsmatrix der Forschungsunterfragen im Literaturkorpus.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-forschungsunterfragen-02-01-suchergebnisse.png>){#fig:A-kor-fu}

```{=latex}
\figsubcaption{Korrelationsmatrix der paarweisen Zusammenhänge zwischen Forschungsunterfragen (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). Achsen: FU; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen.}
```

![Korrelationsmatrix zwischen Forschungsunterfragen und Suchbegriffen.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-forschungsunterfragen-und-suchbegriffen-02-01-suchergebnisse.png>){#fig:A-kor-fu-suchbegriffe}

```{=latex}
\figsubcaption{Korrelationen zwischen Forschungsunterfragen und Suchbegriffen (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). x-Achse: FU; y-Achse: Suchbegriffe; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen.}
```

![Korrelationsmatrix zwischen Forschungsunterfragen und Kategorien.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-forschungsunterfragen-und-kategorien-02-01-suchergebnisse.png>){#fig:A-kor-fu-kategorien}

```{=latex}
\figsubcaption{Korrelationen zwischen Forschungsunterfragen und Textsorten/Kategorien (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). x-Achse: FU; y-Achse: Kategorien (Kerngedanke, Argumentation, Weiterführung, Schlussfolgerung); Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen.}
```

![Korrelationsmatrix zwischen Forschungsunterfragen und Indizes.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-forschungsunterfragen-und-indizes-02-01-suchergebnisse.png>){#fig:A-kor-fu-indizes}

```{=latex}
\figsubcaption{Korrelationen zwischen Forschungsunterfragen und Indexkategorien (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). x-Achse: FU; y-Achse: Indizes; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen. Dient als Plausibilitätscheck, ob deduktive FU an inhaltliche Indexachsen koppeln.}
```

**Suchbegriffe, Kategorien und Indizes**

![Korrelationsmatrix der Suchbegriffe im Literaturkorpus.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-suchbegriffen-02-01-suchergebnisse.png>){#fig:A-kor-suchbegriffe}

```{=latex}
\figsubcaption{Paarweise Korrelationen zwischen Suchbegriffen (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). Achsen: Suchbegriffe; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen. Dient zur Sichtbarmachung von Suchbegriff-Clustern und komplementären Suchstrings.}
```

![Korrelationsmatrix zwischen Suchbegriffen und Kategorien.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-suchbegriffen-und-kategorien-02-01-suchergebnisse.png>){#fig:A-kor-suchbegriffe-kategorien}

```{=latex}
\figsubcaption{Korrelationen zwischen Suchbegriffen und Textsorten/Kategorien (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). x-Achse: Suchbegriffe; y-Achse: Kategorien; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen.}
```

![Korrelationsmatrix der Kategorien im Literaturkorpus.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-kategorien-02-01-suchergebnisse.png>){#fig:A-kor-kategorien}

```{=latex}
\figsubcaption{Paarweise Korrelationen der Textsorten/Kategorien (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). Achsen: Kategorien; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen.}
```

![Korrelationsmatrix der Indizes im Literaturkorpus.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-indizes-02-01-suchergebnisse.png>){#fig:A-kor-indizes}

```{=latex}
\figsubcaption{Paarweise Korrelationen zwischen Indexkategorien (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). Achsen: Indizes; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen. Dient zur Identifikation gemeinsam auftretender Indexachsen und potenzieller Achsenbündel.}
```

![Korrelationsmatrix zwischen Indizes und Kategorien.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-indizes-und-kategorien-02-01-suchergebnisse.png>){#fig:A-kor-indizes-kategorien}

```{=latex}
\figsubcaption{Korrelationen zwischen Indexkategorien und Textsorten/Kategorien (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). x-Achse: Indizes; y-Achse: Kategorien; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen.}
```

![Korrelationsmatrix zwischen Indizes und Suchbegriffen.](<08 Metaquellen/08-01 Abbildungen/methodik/korrelation-zwischen-indizes-und-suchbegriffen-02-01-suchergebnisse.png>){#fig:A-kor-indizes-suchbegriffe}

```{=latex}
\figsubcaption{Korrelationen zwischen Indexkategorien und Suchbegriffen (Quelle: lokale Zotero-Datenbank, Tagfilter `Promotion:Literaturanalyse`, Stand: 2026-05-06; $n=4165$). x-Achse: Indizes; y-Achse: Suchbegriffe; Farbwerte kodieren Richtung und Stärke der Pearson-Korrelationen. Zeigt, welche Suchstrings welche Inhaltsachsen besonders stark erschließen.}
```

**Strukturelle Übersichten der Relationen**

Die strukturellen Übersichten des Literaturkorpus – insbesondere das Pfaddiagramm der Datenflüsse und Kategorien sowie das Suchbegriffsnetz – werden im Methodik-Kapitel ausführlich visualisiert und erläutert (vgl. Abb.~\ref{fig:path-diagram} und Abb.~\ref{fig:network-suchergebnisse} in Abschnitt 4.2/4.3). Um Redundanzen und zusätzliche Dateilasten zu vermeiden, sind diese Abbildungen im Korrelationsatlas nicht erneut eingebunden.
