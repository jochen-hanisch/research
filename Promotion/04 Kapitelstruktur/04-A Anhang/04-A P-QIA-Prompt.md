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

### Übersicht der P‑QIA-Einstellungen je Forschungsunterfrage

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

Damit ist die Überführung der Analysen 1. Ordnung aus dem Literaturverzeichnis in die P‑QIA und die FU-spezifisch Parametrisierung dokumentiert.
