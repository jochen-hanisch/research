\newpage

## Prompt/Vorlage zur systemisch-forschungsfragengeleiteten Auswertung der LMS-Umfrage (UM1) {#sec:A-10}

Diese Vorlage dient der reproduzierbaren, theorie- und forschungsfragengeleiteten Auswertung der LMS‑Umfrage (Selbstauskünfte). Sie folgt dem methodischen Paradigma der Arbeit (Kapitel 4.1–4.3) und operationalisiert die itemweise Auswertung gemäß Abschnitt \hyperref[sec:Umfrage-LMS]{4.2.5}.

Eingabe (pro Auswertungsfall)

- Datenexport (CSV): `08 Metaquellen/08-04 Daten/UmfrageOnline-Beantwortungen.csv`
- Itemliste/Deskription (optional): `08 Metaquellen/08-04 Daten/items_summary.csv`
- Zuordnung „Frage → Begriffspaar → Einfluss“ (Gewichtungs-Synopse): `00 Projektstruktur/00-03 Theorieansatz/Umfragen und Versuche/Umfrage zum LMS/Synopse der Gewichtungen (für den Python Code) mit Bezug zu den einzelnen ….md`

**Einheit der Analyse (Fall):** `Item × Jahrgang` (Jg. 21 / Jg. 22 / Jg. 23) + Kurzvergleich über alle drei Jahrgänge.

**Ziel der Analyse**

Die Umfrageauswertung liefert eine strukturierte Evidenzbasis zur Triangulation:

- **FU1/FU2a/FU2b:** subjektive Bewertungen zu Klarheit, Interaktion, Kollaboration, Feedback, Fortschritt, Personalisierung, Zugänglichkeit und Tool‑Integration.
- **FU4b‑Triangulation:** Abgleich von Selbstauskünften mit beobachteten Aufmerksamkeitsmustern (Abschnitt \hyperref[sec:EyeTracking-Umfrage-Vergleich]{4.3.9}).

Die Vorlage standardisiert Bericht und Kennzahlen; die Interpretationsverantwortung bleibt bei der forschenden Person.

**Auswertungsschritte (pro Item)**

1. **Subgruppenbildung (Jahrgänge):** Jahrgang über Kurskennung (z.B. `21‑…`, `22‑…`, `23‑…`) bestimmen.
2. **Skalentyp bestimmen:**
   - Likert 1–5: Kennzahlen + Zustimmung/Ablehnung
   - Binär (Ja/Nein): Ja‑Anteil
3. **Kennzahlen berechnen (pro Jahrgang und gesamt):**
   - `n` (gültige Antworten)
   - Mittelwert, SD, Median, IQR (bei Likert)
   - Zustimmung `>=4` und Ablehnung `<=2` (bei Likert)
   - Ja‑Anteil (bei binär)
4. **Artefakte benennen:** ungleiche `n` je Jahrgang, Teilabbrüche/fehlende Werte, sehr kleine Jahrgangsstichprobe (Tendenz).
5. **Systemische Einordnung:** falls in Synopse vorhanden: Begriffspaar + Einfluss; sonst Einordnung über Triangulation (Kapitel 5).
6. **Kurzvergleich Jg. 21–23:** je Jahrgang `M` (oder Ja‑Anteil) plus Hinweis auf ungleiche Stichprobengrößen.

**Ausgabeformat (verbindlich)**

Für jedes Item wird die folgende Struktur verwendet (jeweils dreimal: Jg. 21/22/23) und anschließend ein Kurzvergleich ergänzt:

**Kurztext**
- Datenbasis, Skalentyp, Artefakte/Qualität, Konfidenz (aus `n` abgeleitet)

**Auswertung (A1O)**
- Deskriptive Kennzahlen (siehe oben)
- Interpretation als Tendenz (keine inferenzstatistische Ableitung)
- Systemische Interdependenzen (Synopse/Tria­ngulation)
- Kurzdiagnose (1 Satz)

**Qualitätsgate (Haken dran)**
- Datenbasis + Skala benannt
- `n` ausgewiesen
- zentrale Kennzahlen berichtet
- Artefakte/fehlende Werte benannt
- Interpretation vorsichtig formuliert
- Konfidenz begründet

**Konfidenzregel (pragmatisch)**

- `n >= 30`: mittel
- `15 <= n < 30`: niedrig bis mittel
- `n < 15`: niedrig

 Template: UM1‑Item (zum Kopieren)

```markdown
 UM1 – Item QXX – Jg. 2Y (n=…)

**Frage**
- …

**Kurztext**
- Datenbasis: …
- Skala: …
- Artefakte/Qualität: …
- Konfidenz: …

**Auswertung (A1O)**
- Deskriptiv: …
- Interpretation: …
- Systemische Interdependenzen: …
- Kurzdiagnose: …

**Qualitätsgate (Haken dran)**
- [x] Datenbasis + Skala benannt
- [x] n ausgewiesen
- [x] zentrale Kennzahlen berichtet
- [x] Artefakte/fehlende Werte benannt
- [x] Interpretation vorsichtig formuliert
- [x] Konfidenz begründet

 UM1 – Item QXX – Kurzvergleich (Jg. 21–23)
- Jg. 21: …
- Jg. 22: …
- Jg. 23: …
- Hinweis: Stichprobenumfänge sind ungleich; Vergleiche nur als Tendenz.
```

Abschlussbemerkung: Diese Datei bildet den verbindlichen Auswertungsrahmen für die Umfrageauswertung (UM1) im Rahmen der Dissertation.

