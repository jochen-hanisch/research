# Anleitung: LimeSurvey

## Ziel

Dieses Dokument beschreibt die Einrichtung, Durchführung und Auswertung einer systemischen Datenerhebung mithilfe von LimeSurvey. Ziel ist es, die drei zentralen Modellvariablen der [[Systemintelligenz]] zu erfassen:

- Strukturelle Kopplung (x)
- Kommunikationsdichte (y)
- Entwicklungspotenzial (z)

## 1. Vorbereitung des Fragebogens

### Fragegruppen

Erstelle eine Fragegruppe mit dem Titel:  
**Systemische Einschätzung Notfallteam**

### Fragen

Lege folgende Fragen an:

1. **Strukturelle Kopplung**  
   Fragetext: „Wie klar und verbindlich waren die Rollen und Zuständigkeiten im Team geregelt?“  
   Fragetyp: Numerisch (Ganzzahl)  
   Skala: 0–10  
   Pflichtfeld: Ja

2. **Kommunikationsdichte**  
   Fragetext: „Wie intensiv und kontinuierlich wurde im Team kommuniziert?“  
   Fragetyp: Numerisch (Ganzzahl)  
   Skala: 0–10  
   Pflichtfeld: Ja

3. **Entwicklungspotenzial**  
   Fragetext: „Wie offen war das Team für situatives Lernen und Anpassung?“  
   Fragetyp: Numerisch (Ganzzahl)  
   Skala: 0–10  
   Pflichtfeld: Ja

### Hinweise zur Skalierung
Die Skala 0–10 ist für Teilnehmende intuitiv verständlich. Im Python-Modell wird sie anschließend durch Division mit 10 auf einen Wertebereich von 0.0–1.0 normiert.

## 2. Durchführung der Erhebung

- Befragung im Anschluss an reale Einsätze, Simulationen oder Teambesprechungen
- Optional: Einzelbefragung pro Teammitglied oder aggregierte Einschätzung durch eine Beobachterin oder einen Beobachter
- Die Umfrage kann anonym oder personenbezogen erfolgen, je nach Datenschutzkontext

## 3. Export der Ergebnisse

- Format: CSV oder XLSX (bevorzugt)
- Exportierte Spalten: je eine Spalte für strukturelle Kopplung, Kommunikationsdichte und Entwicklungspotenzial
- Optional: Zusatzspalten für Datum, Team-ID, Kontextbeschreibung

## 4. Import in das Modell

Die numerischen Werte werden in Python wie folgt normiert:

```python
    import pandas as pd

    df = pd.read_csv("ergebnisse.csv")
    x = df["struktur"].to_numpy() / 10
    y = df["kommunikation"].to_numpy() / 10
    z = df["entwicklung"].to_numpy() / 10
```

Diese Werte können dann direkt in das Systemintelligenz-Modell zur Visualisierung und Analyse überführt werden.

## 5. Weiterführende Schritte

- Integration in Simulationsdesigns
- Vergleich mehrerer Teams oder Zeitpunkte
- Visualisierung systemischer Stabilität über S(c)

## Hinweis

Diese Methode basiert auf einem konzeptionellen Modell und eignet sich für explorative, reflexive und wissenschaftlich fundierte Analysen systemischer Teamkonfigurationen.

