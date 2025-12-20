# CONTRIBUTING

Dieses Projekt entsteht in Markdown und wird mit Pandoc + XeLaTeX gebaut. Die folgenden Konventionen sichern einen konsistenten Workflow und reproduzierbare Ergebnisse.

## Workflow & Branching
- Branching: Feature-Branches pro Thema (`feature/<kurzbeschreibung>`), Merge per Pull Request.
- Commits: Klarer Betreff im Imperativ, bei Bedarf kurze Body-Notizen zu Motivation/Impact.
- Reviews: PRs enthalten Zusammenfassung, betroffene Dateien und ggf. Screenshots/PDF-Hinweise.

## Build & Tests
- PDF-Build lokal über `./build-dissertation.sh` im Repo-Root. Der Build nutzt `pandoc --filter pandoc-crossref --citeproc --pdf-engine=xelatex`.
- Fehlende Dateien (z.B. `literaturverzeichnis.md`) verhindern den Build; Platzhalter anlegen oder Pfade korrigieren.
- Mermaid bleibt als Codeblock; nur `![...](...)`-Abbildungen landen im Abbildungsverzeichnis.

## Struktur & Pfade
- Kapitel liegen in `04 Kapitelstruktur/<Kapitel>/<Datei>.md`, Titelseite/Verzeichnisse in `dissertation.md`, Literatur in `literaturverzeichnis.md`.
- Abbildungen: `08 Metaquellen/08-01 Abbildungen/<bereich>/...`; Pfade im Markdown relativ zum Projektroot angeben.
- Metadaten und Hinweise: `08 Metaquellen/Matadaten/README.md`.

## Inhaltliche Konventionen
- Labels: Abschnitte `{#sec:x-y}`, Abbildungen `{#fig:...}`, Tabellen `{#tab:...}`, Gleichungen `\label{eq:...}`.
- Verweise: bevorzugt `\hyperref[label]{...}` für Abschnitte, Abbildungen und Tabellen; Gleichungen mit `\eqref{eq:mass}`.
- Zitationen: CSL via `citeproc`. Inline `@quelle_2024` (eingebettet im Satz), parenthetisch `[@quelle_2024, Seite 4–5]`; Kapitelangaben z.B. `[@doring_forschungsmethoden_2023, Kapitel 10.6]`.
- Hyperrefs: Beispiel Abschnitt `\hyperref[sec:4-3]{Abschnitt 4.3}`, Abbildung `\hyperref[fig:xyz]{Abbildung xyz}`, Tabelle `\hyperref[tab:xyz]{Tabelle xyz}`.
- Obsidian: „Strict line breaks“ aus, damit Pandoc Absätze korrekt erkennt; YAML-Frontmatter nur in `dissertation.md`.
- Mermaid bleibt als Codeblock, zählt nicht als Abbildung.
- YAML-Frontmatter nur in `dissertation.md`; Einzelkapitel starten ohne eigenes YAML.
- UTF-8, keine Emojis; Leerzeilen zwischen Absätzen, keine Hardwraps erzwingen.
- Pandoc/YAML-Defaults: global in `dissertation.md` (XeLaTeX, STIX-Schriften, csquotes, hyperref, draft watermark, 1,5-zeilig).
- Build-Filter: `pandoc-crossref` + `citeproc`, CSL-Datei `08 Metaquellen/Matadaten/apa-no-initials.csl`, Bibliographie `08 Metaquellen/Matadaten/Literaturverzeichnis.bib`.
- Formulierungen/Stil: kohärente, längere Satzstrukturen, kein „nicht … sondern“, konsistenter Verweis- und Zitationsstil, sachlich-analytischer Ton ohne Umgangssprache.
- Wortwahl: Prüfliste für typische Problemwörter in `00 Projektstruktur/00-05 Dokumentation/Wortliste wissenschaftlich vermeiden.md`.

## Analyse- und Such-Workflow
- Literaturmanagement: Zotero mit Tagging (`Promotion:Literaturanalyse` + Argumentkategorie), Suchordner nach primären/sekundären/tertiären Begriffen, Quoten 80/50/15.
- Dokumentation: Memos/Notizen in Obsidian; Suchlogik und Workflows sind in `08 Metaquellen/Matadaten/README.md` beschrieben.

## Beiträge & PRs
- Vor dem PR: Build laufen lassen, offensichtliche Warnungen beheben.
- PR-Beschreibung: kurz Ziel, Änderungen, Tests/Builds. Falls neue Abbildungen: Pfad nennen, Einbindung zeigen.
- Stil: längere, kohärente Satzstrukturen, keine „nicht … sondern“-Formulierungen, konsistenter Verweis- und Zitationsstil.

## Daten und Skripte
- Skripte und Analysen (z.B. Python, Notebook) sind extern versioniert; hier nur Verweise/Pfade nutzen.
- Keine großen Binärdateien oder sensiblen Daten ins Repo einchecken.
