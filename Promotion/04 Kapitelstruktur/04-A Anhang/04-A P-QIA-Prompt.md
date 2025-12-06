\newpage

## Prompt zur probabilistisch-qualitativen Inhaltsanalyse (P‑QIA) {#sec:A-3}

Dieser Prompt beschreibt exemplarisch, wie die in \hyperref[sec:A-2]{Anhang A.2} erzeugten Primäranalysen mittels probabilistisch-qualitativer Inhaltsanalyse (P‑QIA) zu einer Metaanalyse zusammengeführt werden. Er richtet sich an ein KI-Modell, das eine Datei mit bereits strukturierten Quellenanalysen (z.B. `FU1 Primäranalysen (58).md`) verarbeitet. Die hier beschriebene P‑QIA bildet damit die konkrete Operationalisierung der aus den Forschungsunterfragen abgeleiteten Analysekategorien auf der Ebene textbasierter Segmente (siehe auch \hyperref[sec:A-2]{Anhang A.2}).

**Aufgabe**

Führe auf Basis der bereitgestellten Primäranalysen eine probabilistisch-qualitative Inhaltsanalyse durch. Ziel ist es, wiederkehrende Muster zu identifizieren, diese in Kategorien zu überführen und theoriegeleitet zu interpretieren.

**Datenbasis**

- Eingabe ist eine Markdown-Datei mit mehreren Analysen erster Ordnung (siehe \hyperref[sec:A-2]{Anhang A.2}).
- Jede Analyse enthält bereits strukturierte Abschnitte (z.B. Kontext, Kernaussagen, Argumentation, Verschlagwortung).

**Schritte der P‑QIA**

1. **Segmentierung**
   - Zerlege alle Texte in Sinnabschnitte (1–3 Sätze).
   - Achte darauf, dass jeder Abschnitt eine inhaltlich geschlossene Aussage enthält.

2. **Embedding und Clustering**
   - Erzeuge für jeden Sinnabschnitt einen semantischen Vektor (Embedding).
   - Führe ein k-means-Clustering mit einem forschungsfragen-spezifischen *k* durch.
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
