\newpage

## Prompt zur probabilistisch-qualitativen Inhaltsanalyse (P‑QIA) {#sec:A-3}

Dieser Prompt beschreibt exemplarisch, wie die in \hyperref[sec:A-2]{Anhang A.2} erzeugten Primäranalysen mittels probabilistisch-qualitativer Inhaltsanalyse (P‑QIA) zu einer Metaanalyse zusammengeführt werden. Er richtet sich an ein KI-Modell, das die im Literaturverzeichnis hinterlegten Analysen erster Ordnung verarbeitet (FU-Tags in `keywords`, Analysen im Feld `annote`). Die hier beschriebene P‑QIA bildet damit die konkrete Operationalisierung der aus den Forschungsunterfragen abgeleiteten Analysekategorien auf der Ebene textbasierter Segmente (siehe auch \hyperref[sec:A-2]{Anhang A.2}).

**Aufgabe**

Führe auf Basis der bereitgestellten Primäranalysen eine probabilistisch-qualitative Inhaltsanalyse durch. Ziel ist es, wiederkehrende Muster zu identifizieren, diese in Kategorien zu überführen und theoriegeleitet zu interpretieren.

**Datenbasis**

- Eingabe sind alle Analysen erster Ordnung einer FU, wie sie im Literaturverzeichnis kodiert sind (Einträge mit `Promotion:FUx` in `keywords` und Analyse-Text im Feld `annote`; vgl. Übersichtstabelle in diesem Anhang).
- Jede Analyse enthält bereits strukturierte Abschnitte (z.B. Kontext, Kernaussagen, Argumentation, Verschlagwortung), die im `annote`-Text verfügbar sind.

**Schritte der P‑QIA**

1. **Segmentierung**
   - Zerlege alle Texte in Sinnabschnitte (1–3 Sätze).
   - Achte darauf, dass jeder Abschnitt eine inhaltlich geschlossene Aussage enthält.

2. **Embedding und Clustering**
   - Erzeuge für jeden Sinnabschnitt einen semantischen Vektor (Embedding).
   - Führe ein k-means-Clustering mit einem FU-spezifischen *k* durch.
   - Bewerte die Clustertrennschärfe mithilfe des Silhouette-Koeffizienten und passe *k* bei sehr niedrigen Werten an.

3. **Kategorienbildung**
   - Interpretiere jedes stabile Cluster inhaltlich und formuliere daraus eine Kategorie mit kurzer Definition.
   - Ordne die Kategorien, wenn sinnvoll, übergeordneten Dimensionen zu (z.B. Akzeptanz, Nützlichkeit, Mechanismen, Grenzen).

4. **Codierschema**
   - Erstelle für jede Kategorie ein Codierschema mit:
     - präziser **Definition**,
     - mindestens zwei **Ankerbeispielen** (Originalsegmente mit Quellenangabe),
     - klaren **Kodierregeln** (Wann gehört ein Segment in diese Kategorie? Wie mit Mehrdeutigkeiten umgehen?).

5. **Kodierung und Synthese**
   - Weise alle Segmente den gebildeten Kategorien zu (Mehrfachkodierungen sind möglich, wenn sachlich begründet).
   - Beschreibe anschließend die wichtigsten Muster, Zusammenhänge und Spannungsfelder zwischen den Kategorien.

6. **Theoretische Einbettung und Reflexion**
   - Ordne die Befunde passenden theoretischen Rahmenmodellen zu (z.B. Technology Acceptance Model, Motivationstheorien, systemisch-konstruktivistische Ansätze).
   - Reflektiere Grenzen der Methode (z.B. mögliche Verzerrungen, Abhängigkeit von Parametern, Interpretationsspielräume).

**Erwartete Ausgabe**

- eine kurze Beschreibung der Datenbasis (Anzahl Analysen, Segmente, Cluster),
- eine Liste der gebildeten Kategorien mit Definitionen,
- ein tabellarisches Codierschema (Kategorie, Definition, Ankerbeispiele, Kodierregeln),
- eine narrative Synthese der zentralen Muster und ihrer Bedeutung für die Forschungsfrage,
- eine kurze kritische Reflexion und Hinweise auf mögliche weiterführende Analysen.

**Reproduzierbares Vorgehen (Agenten-Workflow)**

Die folgenden Schritte dokumentieren das reproduzierbare Vorgehen zur Umsetzung der P‑QIA als **Analyse 3. Ordnung** auf Basis der **Analysen 1. Ordnung** (Zotero-`annote`). Ziel ist, dass die Schritte für jede Forschungsunterfrage (FU1–FU7) identisch nachvollziehbar sind und jederzeit erneut ausgeführt werden können.

**Agentenlogik (Werkbank-Prinzip)**

Die P‑QIA wird als „Werkbank“ verstanden: Ein Analyse‑Agent (bzw. eine standardisierte Pipeline) ist **kein eigenständiger Autor**, sondern führt die festgelegten Verarbeitungsschritte mechanisch aus und dokumentiert sie transparent. Interpretative Entscheidungen (z.B. finale Kategorienamen, theoretische Einbettung, Umgang mit Grenzfällen) verbleiben bei der Forschenden.

Kernprinzipien:

- **Rollenverständnis:** Kurator/Analyst, nicht „allwissender“ Theoretiker. Keine neuen Inhalte erfinden, sondern vorhandenes Material verdichten.
- **Regelgebundenheit:** Pro FU wird strikt dieselbe Prozesslogik abgearbeitet (Segmentierung -> Vektorisierung -> Clustering -> Qualität -> Codierschema -> Synthese).
- **Transparenz:** Parameter (z.B. $k$, Segmentierungsregeln, Seed/Run), Abweichungen und Abbruchgründe werden protokolliert.
- **Entscheidungslog:** Jede nachgelagerte Entscheidung (z.B. Umbenennung, Zusammenlegung/Splitting von Clustern zu Kategorien, Verschiebung von Grenzfällen) wird als Changelog je FU festgehalten.
- **Reproduzierbarkeit:** Identischer Input + identische Parameter => identische Outputs (sofern die genutzten Modelle/Tools deterministisch konfiguriert sind).

**Datenbasis und Auswahlregel (Analysen 1. Ordnung)**

**Quelle der Primäranalysen:** `08 Metaquellen/Matadaten/Literaturverzeichnis.bib`

**Auswahlregel pro FU:**

- Ein Eintrag gehört zur FU, wenn im Feld `keywords` der Tag `Promotion:FUx` vorkommt.
- Ein Eintrag zählt als **Analyse 1. Ordnung**, wenn zusätzlich ein Analyse-Text im Feld `annote` vorhanden ist.

**Ergebnis:** FU-spezifischer Korpus aus Analysen 1. Ordnung (Primäranalysen).

**FU‑spezifische Arbeitsdateien (Input)**

Für jede FU wird eine Arbeitsdatei gepflegt (Beispielnamen: „P‑QIA Arbeitsdatei FU1.md“, „… FU2a.md“ usw.). Jeder Quellenblock beginnt mit dem **BibTeX-Key** als Referenzanker (z.B. `### <bib-key>`), darunter folgt der vollständige `annote`-Text.

Damit sind Ankerbeispiele später eindeutig referenzierbar (über den BibTeX-Key).

**Protokoll (Pflichtangaben je FU‑Run)**

Vor (oder spätestens nach) jedem FU‑Durchlauf werden folgende Angaben festgehalten (z.B. am Anfang des FU‑Abschnitts in \hyperref[sec:A-9]{Anhang A.9}):

- FU, Datum/Version, Umfang (n Analysen 1. Ordnung), Segmentanzahl
- verwendetes $k$ (und ggf. getestete Alternativen)
- verwendetes Embedding‑Verfahren/Modell (Name/Version) und Random‑Seed (falls relevant)
- Silhouette‑Kennwerte und Begründung bei Abweichungen vom Standard
- Changelog: Kategorie-Namen, Clusterzusammenlegungen/-splits (falls vorgenommen) + kurze Begründung

**Segmentierung**

- Zerlege alle `annote`-Texte in Sinnabschnitte.
- Standard: **1–3 Sätze pro Segment** (FU7: **1–2 Sätze**).
- Jedes Segment trägt weiterhin den BibTeX-Key der Quelle als Referenz.

Segmentierungsregeln (minimal):

- Segmente müssen inhaltstragend sein (keine reinen Template‑Überschriften wie „Methoden und Datenquellen“, keine reinen Metadatenzeilen).
- Template-/Metasektionen werden konsequent ausgeschlossen (z.B. „Methoden und Datenquellen“, „Zusammenfassung“, „Verschlagwortung“, „Zuordnung“, reine Relevanzbewertungen).
- Artefakte aus der Datenbasis werden bereinigt (z.B. abgeschnittene Textreste/„…“, alleinstehende Trennzeichen wie `---`, offene Klammern).
- Mehrfachkodierungen sind zulässig, wenn mehrere Dimensionen tatsächlich angesprochen werden.

**Embedding (semantische Vektorisierung)**

- Erzeuge für jedes Segment ein semantisches Embedding (Vektorraumrepräsentation).
- Ergebnis ist eine Vektor-Menge, die semantische Ähnlichkeit rechnerisch abbildet.

Reproduzierbarkeit:

- Ein Modell und eine Konfiguration pro Analysephase festlegen und beibehalten (nur bei begründetem Methodikwechsel ändern).
- Wenn das Embedding‑Verfahren stochastisch ist: Random‑Seed fixieren und dokumentieren.

**Clustering (k‑means)**

- Führe ein **k‑means‑Clustering** der Segment‑Embeddings durch.
- Verwende ein **FU-spezifisches $k$** (siehe Tabelle „P‑QIA‑Einstellungen je Forschungsunterfrage“).
- Random‑Seed/Initialisierung fixieren und dokumentieren.

**Qualitätsprüfung (Silhouette)**

- Berechne den **Silhouette‑Koeffizienten** als Maß der Clustertrennschärfe.
- Wenn der Wert auffällig niedrig ist: $k$ in engem Rahmen variieren (z.B. $k \pm 1$) und die Auswirkungen dokumentieren.
- **Abbruchregel für k‑Tuning:** maximal 3 Varianten testen; finale Wahl bleibt eine begründete Entscheidung der Forschenden (keine automatische „Optimierung“).

**Outputstruktur (pro FU)**

Für jede FU werden die Ergebnisse in einem einheitlichen Schema dokumentiert (\hyperref[sec:A-9]{Anhang A.9}):

1. **Datenbasis:** Anzahl Analysen 1. Ordnung (n), Segmentanzahl, $k$, Silhouette.
2. **Kategorienliste:** Name + Kurzdefinition je Cluster/Kategorie.
3. **Codierschema:** Kategorie | Definition | mind. 2 Ankerbeispiele (Segment + BibKey) | Kodierregeln.
4. **Narrative Synthese:** zentrale Muster, Spannungsfelder, Zusammenhänge.
5. **Theoretische Einbettung:** Zuordnung zu passenden Rahmenmodellen (FU-spezifisch).
6. **Reflexion:** Grenzen/Bias/Parameterabhängigkeit.
7. **Qualitätsgate:** Vollständigkeit + Ankerqualität + narrative Qualität (siehe unten).

**Vollständigkeits- und Qualitätsgate (Pflicht vor „fertig“)**

Bevor ein FU‑Abschnitt als „fertig“ gilt, werden die Outputs gegen folgende Kriterien geprüft (und bei Bedarf korrigiert):

**Vollständigkeit**

- Jede Kategorie aus dem Kategorienüberblick erscheint auch im Codierschema (Definition, Kodierregel, mindestens 2 Ankerbeispiele).
- Jede Kategorie aus dem Kategorienüberblick hat im narrativen Teil mindestens einen eigenständigen Syntheseabsatz (nicht nur eine Liste von Quellen).
- Für jede FU sind Theorie und Reflexion als eigene Unterabschnitte vorhanden.

**Ankerqualität**

- Pro Kategorie mindestens zwei Ankerbeispiele aus unterschiedlichen BibTeX-Keys.
- Anker stammen aus inhaltstragenden Segmenten, nicht aus Template-Teilen („Methoden“, „Zusammenfassung“, „Verschlagwortung“, reine Relevanzbewertungen).
- Zitationen sind technisch sauber: `[@bibkey]`, keine offenen Klammern, keine abgeschnittenen Textreste, keine Artefakte (`-{\textgreater}`, `---` o.ä.).

**Narrative Qualität (deskriptiv, nicht interpretativ)**

- Pro Kategorie: 2–5 Sätze Verdichtung (wiederkehrende Muster, Spannungsfelder, Bedingungen), anschließend 1–2 Anker (Zitat oder sehr nahe Paraphrase) mit Quellenangabe.
- Keine Meta-Sätze ohne Benennung der Muster (z.B. nicht nur „verdichtet sich zu Mustern“, sondern die Muster explizit benennen).

**Template: FU‑Abschnitt (zum Kopieren)**

```markdown
**FUx – Analyse dritter Ordnung (P‑QIA)**

**Kurztext**

- Datenbasis: n = …
- Segmentierung: N = … (Regel: …; Ausschlüsse: …)
- Parameter: k = …; Silhouette: S = …

**Protokoll (Run-Parameter)**

- Datum:
- Segmentierungsregeln (kurz):
- Embedding (Modell/Version/Seed):
- k‑Tuning (falls ja/nein + getestete Varianten):
- Besonderheiten/Bereinigung:
- Changelog (Umbenennungen/Merge/Split):

**Kategorienüberblick (Tabelle)**

| Kategorie | Segmente (n) | Beispielquellen |
| --- | ---: | --- |
| … | … | [@…] [@…] |

**Codierschema (Tabelle)**

| Kategorie | Definition | Kodierregel (kurz) | Ankerbeispiele |
| --- | --- | --- | --- |
| … | … | … | „…“ [@…]<br><br>„…“ [@…] |

**Ausführlicher Fließtext (Synthese mit BibTeX-Ankern)**

**Kategorie 1**

2–5 Sätze Verdichtung (deskriptiv) … [@…] [@…]
> „…“ [@…]
> „…“ [@…]

**Barrieren, Risiken & Grenzen**

2–5 Sätze Verdichtung (deskriptiv) … [@…] [@…]
> „…“ [@…]
> „…“ [@…]

**Theoretische Einbettung**

Kurze Zuordnung … [@…]

**Reflexion**

Grenzen/Bias (Segmentierung, Modell-/Parameterabhängigkeit, Korpuszuschnitt, FU‑Tagging) …

**Qualitätsgate (Haken dran)**

- [ ] Kategorienüberblick == Codierschema == Narrative Unterabschnitte
- [ ] Pro Kategorie >=2 Anker aus unterschiedlichen BibTeX-Keys
- [ ] Keine Template-/Meta-Anker, keine Artefakte, saubere Zitationen
```

**Übersicht der P‑QIA-Einstellungen je Forschungsunterfrage**

Die konkrete Anwendung dieses Prompts erfolgt für jede Forschungsunterfrage (FU1–FU7) auf Basis der im Literaturverzeichnis hinterlegten Primäranalysen. Technisch werden dafür jeweils alle Zotero-Einträge verwendet, die

- im Feld `keywords` den entsprechenden FU-Tag (`Promotion:FUx`) tragen und
- eine Analyse 1. Ordnung im Feld `annote` enthalten.

Die konkrete Wahl der Clusteranzahl $k$ je FU orientiert sich an den in \hyperref[sec:P-QIA]{Abschnitt 4.3.4} dokumentierten Silhouette-Kennwerten und der inhaltlichen Interpretierbarkeit der Cluster.

Table: P‑QIA-Einstellungen je Forschungsunterfrage \label{tab:p-qia-settings}

Die folgende Tabelle fasst die P‑QIA-Einstellungen je FU zusammen:

| FU   | Filter im Literaturverzeichnis                    | Analysen 1. Ordnung            | $k$ für P‑QIA |
| :--- | :------------------------------------------------ | ------------------------------: | ----------: |
| FU1  | `keywords` enthält `Promotion:FU1` + `annote`     |                            58  |          8  |
| FU2a | `keywords` enthält `Promotion:FU2a` + `annote`    |                            85  |         12  |
| FU2b | `keywords` enthält `Promotion:FU2b` + `annote`    |                            27  |         14  |
| FU3  | `keywords` enthält `Promotion:FU3` + `annote`     |                           115  |         15  |
| FU4a | `keywords` enthält `Promotion:FU4a` + `annote`    |                           211  |         12  |
| FU4b | `keywords` enthält `Promotion:FU4b` + `annote`    |                            92  |         12  |
| FU5  | `keywords` enthält `Promotion:FU5` + `annote`     |                           125  |         14  |
| FU6  | `keywords` enthält `Promotion:FU6` + `annote`     |                            65  |         12  |
| FU7  | `keywords` enthält `Promotion:FU7` + `annote`     |                             8  |         10  |

```{=latex}
\tabsubcaption{FU-spezifische Parametrisierung der P-QIA. Aufgeführt sind die Filterkriterien im Literaturverzeichnis (Zotero), die Anzahl verfügbarer Analysen 1. Ordnung sowie die gewählte Clusterzahl $k$; $k$ wird entlang der Silhouette-Kennwerte und der interpretativen Trennschärfe je FU festgelegt (vgl. Abschnitt 4.3.4).}
```

Damit ist die Überführung der Analysen 1. Ordnung aus dem Literaturverzeichnis in die P‑QIA und die FU-spezifisch Parametrisierung dokumentiert.
