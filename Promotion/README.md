# Promotion / Dissertation

Dieses Verzeichnis enthält die Arbeitsmaterialien, Kapiteltexte und Build-Artefakte der Dissertation.

## Struktur (Kurzüberblick)

- `dissertation.md` – zentrales Hauptdokument (Steuer-/Klammerdokument).
- `04 Kapitelstruktur/` – Kapiteldateien (Einleitung, Theorieteil, Methodologie, …) + Anhänge.
- `08 Metaquellen/` – Daten, Metadaten, Literaturverzeichnis/Exports.
- `build-dissertation.sh` – baut die Dissertation als PDF (Pandoc → LaTeX).

## GitHub-Projekt: Aufgaben aus `#todo`

Empfehlung: **ein** GitHub Project für die ganze Dissertation, mit Feldern wie `Status`, `Kapitel`, `Typ`, `Priorität`.

### Schnell-Workflow (manuell, aber schnell)

1. In VS Code den `#todo`-Text markieren (oder Cursor in der Zeile).
2. `Cmd+Shift+P` → `GitHub Issues: Create Issue`.
3. Issue-Titel/Body aus dem Todo ableiten, Issue erstellen.
4. Im Markdown den Bezug festhalten, z. B. `#todo: Erkenntnisinteresse skizzieren (#123)`.

Optional (wenn du am Todo “sauber” arbeiten willst): Branch + PR erstellen und in der PR-Beschreibung `Closes #123` setzen.

## Zeitplan (Roadmap bis 20.03.2026)

```mermaid
gantt
  title Dissertation-Roadmap (Ziel: 20.03.2026)
  dateFormat  YYYY-MM-DD
  axisFormat  %d.%m.

  section Puffer
  Feiertage/Familie (low intensity) :done, s0, 2025-12-20, 2026-01-06

  section Schreiben & Konsolidierung (Sprint-Fenster)
  Kap. 5 Ergebnisse (Milestone 5)        :crit, s1, 2026-01-07, 2026-01-27
  Kap. 6 Diskussion (Milestone 6)        :crit, s2, 2026-01-28, 2026-02-10
  Kap. 7 Conclusio (Milestone 7)         :crit, s3, 2026-02-11, 2026-02-17
  Kap. 2 Theorieteil (Milestone 2)       :      s4, 2026-02-18, 2026-02-24
  Kap. 4 Methodologie (Milestone 4)      :      s5, 2026-02-25, 2026-03-03
  Kap. 3 Forschungsgegenstand (Milestone 3) :   s6, 2026-03-04, 2026-03-10
  Kap. 1 Einleitung (Milestone 1)        :      s7, 2026-03-11, 2026-03-17

  section Abschluss
  Gesamt-Korrektur, Layout, Voll-PDF      :crit, s8, 2026-03-18, 2026-03-20
```

## PDF Build

Voraussetzungen (lokal installiert): `pandoc`, `pandoc-crossref`, `latexmk` und XeLaTeX.

- Fast build (Standard): `./build-dissertation.sh` oder `./build-dissertation.sh fast`
- Full build (inkl. großer Anhänge): `./build-dissertation.sh full`
