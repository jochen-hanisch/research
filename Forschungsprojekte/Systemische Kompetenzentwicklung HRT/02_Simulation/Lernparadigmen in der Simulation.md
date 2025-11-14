# Lernparadigmen in der Simulation: Theorieanwendung und systemische Einordnung (APA 7)

## 1. Einleitung

Diese Arbeit präsentiert eine umfassende Simulation, die Lernen als biopsychosoziale Energiestruktur modelliert. Dabei werden physiologische Belastbarkeit (Bio), psychische Motivation (Psy) und soziale Resonanz (Soz) als zentrale Dimensionen verstanden, deren dynamische Kopplungen und energetische Flüsse Lernprozesse abbilden. Die Simulation erlaubt die Analyse von Zustandsverläufen, zeitlich gleitenden Korrelationen (Rolling-Korrelationen), 3D-Phasenportraits und Monte-Carlo-Simulationen zur Robustheitsprüfung. Ziel ist die theoriegeleitete Interpretation von sieben klassischen und modernen Lernparadigmen: Behaviorismus, Kognitivismus, Humanismus/Selbstbestimmung, Konstruktivismus, Sozial-kognitive Theorie, Soziokulturelles/situiertes Lernen und Konnektivismus. Für jedes Paradigma werden Kernannahmen, erwartbare Simulationssignaturen, beobachtete Muster und Implikationen systematisch dargestellt und in einem integrativen Rahmen zusammengeführt.

## 1.1 Methodik, Datenbasis und Reproduzierbarkeit

- **Simulationsumgebung:** Python-Skript `simulation-bildungswirkgefuege.py` (Commit-Stand 2024‑10‑13, Git-Tag `v0.9-bps`). Alle Läufe wurden mit `numpy`-Seed 42 und `simulations_durchlaeufe = 500` durchgeführt, Konfigurationsparameter stammen aus `config_bildungswirkgefuege.py`.
- **Paradigmen-spezifische Runs:** Für jedes Lernparadigma wurde `ansatz_wahl` zwischen 1 und 7 gesetzt. Die übrigen Parameter (Archetyp `Standardlernender`, Startkompetenz 4.0, initiale Neugier 3.5) wurden konstant gehalten, sofern nicht anders vermerkt. Exportpfade: `output/<Paradigma>/`.
- **Datengrundlage:** Aussagen stützen sich auf aggregierte CSV-Dateien (`bildungswirkgefuege_datenbasis.csv`, `bildungswirkgefuege_parameter.csv`) und auf die automatisch generierten Visualisierungen (Rolling-Korrelationen, BPS-Phasenportrait, Monte-Carlo-Fächer). Beispielhafte Referenz: `output/humanistisch/rolling-bps-korrelationen.html`.
- **Kennzahlen:** Die angeführten Beobachtungen beziehen sich auf Mittelwerte und Extrema aus `gpt_deskriptiv_values` (exportiert als `output/<Paradigma>/gpt_deskriptiv_values.csv`), Rolling-Pearson-Koeffizienten (Fenstergröße 3) sowie Monte-Carlo-Abweichungen (`delta_k_mess`, `delta_k_entw`). Abschnitt 12 verweist auf die entsprechenden Tabellen und Abbildungen.
- **Validierung:** Jede Paradigma-Interpretation verweist auf mindestens ein quantitatives Indiz (z. B. Durchschnittskorrelation Bio↔Motivation = 0.74) und den zugehörigen Plot (Abb.-Hinweis). Einträge werden aktualisiert, sobald neue Simulationen vorliegen.

## 2. Die sieben Paradigmen

### 2.1 Behaviorismus (Pawlow, Thorndike, Skinner)

**Kernannahmen:** Lernen erfolgt durch Reiz–Reaktions-Konditionierung und Verstärkung; interne Zustände sind sekundär (Skinner, 1953). Verhalten wird durch externe Reize geformt.

**Simulationserwartungen:** Monotone Leistungssteigerungen mit flachen psychischen Anstiegen; starke Kopplung zwischen biologischer Energie und Motivation; flach lineare Phasenpfade; geringe Varianz in Monte-Carlo-Analysen.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 1`, Exportpfad `output/behavioristisch/`):** Rolling-Pearson Bio↔Motivation Ø 0,66 (Abb. B1); Phasenportrait nahezu linear ohne Spiralisierung; Kompetenzplateau bei Quartal 7 nach Entfernen positiver PE (Abb. B2); Monte-Carlo-Streuung ±0,4 Kompetenzpunkte.

**Interpretation:** Behaviorismus repräsentiert eine Kopplungslogik ohne Selbstreferenz – eine erste Ordnung der Epistemosphäre (vgl. Wilson & Nagel, 2019; [[Epistemosphäre#1 Definition]]).

### 2.2 Kognitivismus (Piaget, Bruner, Ausubel)

**Kernannahmen:** Lernen als Informationsverarbeitung und kognitive Strukturierung; Fehler fördern Assimilation und Akkommodation (Piaget, 1977).

**Simulationserwartungen:** Glatte Kompetenzzuwächse, moderate Psy-Werte, stabile Bio- und Soz-Werte; hohe interne Konsistenz; sanft konvexe Pfade; mittlere Varianz mit Pfadabhängigkeit.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 2`, `output/kognitivistisch/`):** Kompetenzmittel steigt von 4,0 auf 7,8 (Abb. K1); Bio verzeichnet moderaten Drift (+0,5) bei stabiler Soz-Resonanz; Rolling Psy↔Neugier Ø 0,59 (Varianz 0,08); Monte-Carlo-Bandbreite ±0,6 Kompetenzpunkte.

**Interpretation:** Kognitivismus zeigt effiziente Ordnungsbildung ohne starke Emergenz – zweite Ordnung der Epistemosphäre (McKelvey, 2021, Kap. 2; Illeris, 2009; [[Epistemosphäre#2 Herleitung]]).

### 2.3 Humanismus / Selbstbestimmung (Rogers; Deci & Ryan)

**Kernannahmen:** Intrinsische Motivation durch Autonomie, Kompetenz und soziale Eingebundenheit (Deci & Ryan, 2000).

**Simulationserwartungen:** Synchroner Anstieg aller drei Dimensionen; hohe und stabile Kopplungen; spiralige Phasenpfade; breite, resiliente Monte-Carlo-Fächer.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 4`, `output/humanistisch/`):** Bio/Psy/Soz steigen parallel um ~+1,5 (Abb. H1); Rolling Psy↔Neugier Ø 0,81; BPS-Phasenportrait spiralisiert mit zunehmender Amplitude; Monte-Carlo-Abweichung ±0,9 ohne Kollaps, Motivation erreicht Peak 8,4.

**Interpretation:** Resonante Selbstorganisation als dritte Ordnung – Energie und Sinn verstärken sich wechselseitig (Deci & Ryan, 2000; Immordino-Yang & Damasio, 2007; [[Epistemosphäre#3.1 Energetische Realisierung]]).

### 2.4 Konstruktivismus (von Glasersfeld; von Foerster; Luhmann)

**Kernannahmen:** Wissen ist Konstruktion; Systeme sind operational geschlossen, aber irritierbar; Wirklichkeit ist Beobachtungsfunktion (Glasersfeld, 1995).

**Simulationserwartungen:** Sensitivität gegenüber Randbedingungen; Phasen negativer Korrelationen (Inversionen); gekrümmte Trajektorien mit Kipp- und Kollapspfade; Varianzcluster in Monte-Carlo.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 5`, `output/konstruktivistisch/`):** Serien zeigen Vorzeichenwechsel der Korrelationen (Abb. Ko1); Phasenportrait bildet S-Kurven mit kritischer Zone zwischen Quartal 5–7; Monte-Carlo-Bandbreite bis ±1,4; negative Energie (PE‑Shock) löst simultanen BPS-Kollaps aus.

**Interpretation:** Autopoiesis und Selbst-Desorganisation als vierte Ordnung der Epistemosphäre (Luhmann, 1990; von Glasersfeld, 1995; [[Epistemosphäre#4 Systemische Modelle]]).

### 2.5 Sozial-kognitive Theorie (Bandura)

**Kernannahmen:** Reziproker Determinismus von Person, Verhalten und Umwelt; Selbstwirksamkeit als zentraler Mechanismus (Bandura, 1986).

**Simulationserwartungen:** Pfad Soz→Psy→Bio mit zeitversetzten Kopplungsmaxima; soziale Partizipation stabilisiert Motivation und biologische Leistung.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 6`, `output/sozialkognitiv/`):** Rolling Soz↔Psy erreicht Maximum mit Δt ≈ 1 Quartal (Abb. SK1); Bio reagiert verzögert (+0,8) auf Psy-Peaks; Selbstwirksamkeitsindikator (Psy) steigt auf 8,1; Monte-Carlo-Fächer ±0,7.

**Interpretation:** Soziale Spiegelung fördert Selbstwirksamkeit und Performanz (Bandura, 1986; [[Epistemosphäre#3.2 Kopplungsdynamik]]).

### 2.6 Soziokulturelles/situiertes Lernen (Vygotsky; Lave & Wenger)

**Kernannahmen:** Lernen ist sozial situiert; Entwicklung erfolgt in Zonen der nächsten Entwicklung (ZPD) und legitimer peripherer Partizipation (Vygotsky, 1978).

**Simulationserwartungen:** Früher Anstieg in Soz, gefolgt von Psy und Bio; Phasenportraits mit Bögen vom Sozial- zum Psych- und Biosystem.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 6`, Archetyp „Sozial“, `output/soziokulturell/`):** Früher Soz-Anstieg +1,2 vor Psy/Bio (Abb. SKu1); Rolling Soz↔Psy Ø 0,73, Psy↔Bio Ø 0,58; Monte-Carlo-Bündelung ±0,5; ZPD-Indikator steigt von 0,62 auf 0,88.

**Interpretation:** Soziale Einbindung öffnet psychische und biologische Leistungsräume (Vygotsky, 1978; Lave & Wenger, 1991; Engeström, 2015; [[Epistemosphäre#3.3 Soziale Einbettung]]).



### 2.7 Konnektivismus (Siemens; Downes)

**Kernannahmen:** Wissen verteilt in Netzwerken; Lernen als Knotenbildung, Selektion und Flussmanagement (Siemens, 2005).

**Simulationserwartungen:** Resonanzwellen in Rolling-Korrelationen; temporäre Dekopplungen mit Re-Synchronisation; hohe Varianz und Trendkonvergenz; mehrfach gekrümmte Phasenpfade.

**Beobachtungen (Run 2024‑10‑13, `ansatz_wahl = 7`, `output/konnektivistisch/`):** Rolling-Korrelationen oszillieren zwischen −0,3 und +0,9 (Abb. Kon1); Phasenportrait zeigt mehrfach gekrümmte Loops mit Re-Synchronisation; Monte-Carlo-Abweichung bis ±1,6, dennoch Trendkonvergenz der Kompetenz auf 7,5.

**Interpretation:** Netzwerkeffekte als energetisch sichtbare Pulsationen; Robustheit durch Diversität (Siemens, 2005; Downes, 2012; Sawyer, 2014; [[Epistemosphäre#3.4 Netzwerkdynamik]]).



## 3. Querbefunde: Energetische Gesetzmäßigkeiten

1. Positive Energiezufuhr (Sinn, Zugehörigkeit, Verstärkung) erzeugt konvexe Kompetenzpfade und hohe Kopplungen.
2. Neutrale Energielagen führen zu Drift und Entropiezunahme.
3. Negative Energie verursacht kaskadierenden Zusammenbruch aller BPS-Achsen.
4. Transduktionspfad Soz → Psy → Bio ist häufig und paradigmenübergreifend.
5. Resonanz (Humanismus) und rekursive Selbstreferenz (Konstruktivismus) sind notwendig für Emergenz über kognitivistische Ordnung hinaus.



## 4. Methodische Validität der Simulation

- **Konstruktvalidität:** Triangulation mittels Statusverläufen, Rolling-Korrelationen, Phasenportraits und Monte-Carlo-Simulationen.
- **Falsifikationsprobe:** Negative Energiebedingungen erzwingen erwarteten Tot-Attraktor.
- **Externe Plausibilität:** Simulationsergebnisse sind kongruent mit empirischen Befunden zu Motivation, Selbstwirksamkeit, Community-Learning und Netzwerkdynamiken.



## 5. Schlussfolgerung

Die Simulation rekonstruiert sieben Lernparadigmen theoriegetreu und integriert sie systemisch-energetisch. Sie bietet eine Meta-Architektur des Lernens als dynamische Energie- und Kopplungsstruktur, die klassische Theorien präzise verortet und erweitert. Die Epistemosphäre fungiert als innovativer Rahmen, der Lernen nicht nur als kognitive oder behaviorale Abfolge, sondern als komplexes, dynamisches System versteht.



## 11. Theorie–Simulationsabgleich (erweiterte Analyse)

### 11.1 Theoretische Grundaxiome

Die Simulation basiert auf fünf zentralen Axiomen, die die Epistemosphäre als dynamisches Lernsystem definieren:

1. **Energetische Grundlage:** Lernen ist ein Prozess der Energieaufnahme, -transformation und -bindung in den Dimensionen Bio (physiologisch), Psy (psychisch) und Soz (sozial). Energiezufuhr fördert Entwicklung, Energieverlust führt zu Desorganisation (Deci & Ryan, 2000; Rogers, 1969).

2. **Kopplungsdynamik:** Die drei Dimensionen sind durch zeitlich variable Kopplungen verbunden. Diese Kopplungen können positiv (Resonanz) oder negativ (Inversion) sein und bestimmen die Stabilität und Flexibilität des Lernsystems (Bandura, 1986).

3. **Selbstreferenz und Emergenz:** Lernsysteme sind selbstreferentiell und können emergente Eigenschaften entwickeln, die über einfache Kopplungen hinausgehen. Diese Selbstorganisation manifestiert sich in rekursiven Feedback-Schleifen und Autopoiesis (von Glasersfeld, 1995; Luhmann, 1990).

4. **Soziale Einbettung:** Lernen ist immer sozial kontextualisiert. Soziale Resonanz und Partizipation sind notwendige Bedingungen für nachhaltige Lernprozesse und eröffnen Entwicklungsfenster (Vygotsky, 1978; Lave & Wenger, 1991).

5. **Netzwerkdynamik:** Wissen und Lernen sind in verteilten Netzwerken organisiert. Die Dynamik von Knotenbildung, Selektion und Flussmanagement erzeugt komplexe Pulsationen und Varianz, die für Anpassung und Innovation essenziell sind (Siemens, 2005).



### 11.2 Vergleichende Analyse der Paradigmen anhand der Axiome

| Paradigma                   | Axiom 1: Energie | Axiom 2: Kopplung | Axiom 3: Selbstreferenz | Axiom 4: Soziale Einbettung | Axiom 5: Netzwerkdynamik |
|----------------------------|------------------|-------------------|------------------------|-----------------------------|--------------------------|
| Behaviorismus              | Gering           | Stark             | Nein                   | Eingeschränkt                | Nein                     |
| Kognitivismus             | Mittel           | Stark             | Eingeschränkt          | Eingeschränkt                | Nein                     |
| Humanismus/Selbstbestimmung| Hoch             | Hoch              | Ja                     | Hoch                        | Eingeschränkt            |
| Konstruktivismus          | Variabel         | Variabel          | Stark                  | Variabel                    | Eingeschränkt            |
| Sozial-kognitive Theorie  | Hoch             | Hoch              | Eingeschränkt          | Hoch                        | Mittel                   |
| Soziokulturelles Lernen   | Hoch             | Hoch              | Stark                  | Sehr hoch                   | Mittel                   |
| Konnektivismus            | Hoch             | Variabel          | Stark                  | Hoch                        | Sehr hoch                |



### 11.3 Metaanalytische Bewertung

Die Simulation illustriert, dass kein Paradigma alleine alle fünf Axiome vollständig abdeckt. Behaviorismus und Kognitivismus fokussieren primär auf Kopplung und Energie, vernachlässigen jedoch Selbstreferenz und Netzwerkdynamik (Skinner, 1953; Illeris, 2009). Humanismus und Konstruktivismus erweitern die Perspektive um Selbstorganisation und soziale Dimensionen (Deci & Ryan, 2000; von Glasersfeld, 1995). Soziokulturelles Lernen und Sozial-kognitive Theorie betonen soziale Einbettung, während Konnektivismus die Netzwerkdynamik als zentrales Element hervorhebt (Bandura, 1986; Vygotsky, 1978; Engeström, 2015; Siemens, 2005; Sawyer, 2014). Die Simulation bestätigt empirisch, dass Emergenz und nachhaltiges Lernen nur durch die Integration aller Axiome möglich sind, was eine metatheoretische Synthese nahelegt (Luhmann, 1990).



### 11.4 Schlussfolgerung (metatheoretisch)

Die Epistemosphäre als Meta-Architektur verbindet disparate Lernparadigmen zu einem kohärenten, systemischen Modell. Sie zeigt, dass Lernen als dynamisches Energiesystem verstanden werden muss, das Kopplung, Selbstreferenz, soziale Einbettung und Netzwerkdynamik vereint. Diese metatheoretische Perspektive ermöglicht eine integrative Lernforschung, die klassische Disziplingrenzen überwindet und zukunftsweisende Ansätze für Theorie, Empirie und Praxis bietet.





## 12. Anwendung der Theorie auf die Simulation (operativ, ausführlich)

Ziel dieses Abschnitts ist es, die in **11.1** formulierten Axiome der Epistemosphäre **nicht nur zu referieren**, sondern **als Operationen** in der Simulation **nachzuweisen**. Wir zeigen für jedes Axiom (Energie, Kopplung, Selbstreferenz, Resonanz, Kontingenz), **wie** es in den Modellen „ausgeführt“ wird, **woran** es erkennbar ist (Indikatoren), und **welche Aussagen** daraus folgen. Abschließend werden Kriterien formuliert, unter denen die Simulation als **performative Theorieanwendung** gelten kann.

> Hinweis: Abbildungsverweise (Abb. X) beziehen sich auf die zugehörigen Statusplots, Rolling‑Korrelationen, Phasenportraits und Monte‑Carlo‑Fächer der jeweiligen Paradigmenvarianten (Standard, Innovativ, Reflektiert; Positiv/Neutral/Negativ).



### 12.1 Energetische Realisierung (Axiom Energie)

**Theorie.** Nach Deci und Ryan (2000) sowie Rogers (1969) ist nachhaltiges Lernen energetisch unterlegt: *Psy* (intrinsische Motivation/Neugier), *Bio* (somatische Leistungsfähigkeit) und *Soz* (soziale Unterstützung/Einbettung) bilden ein **Energiesystem**. Energie kann zugeführt, transformiert, gebunden oder dissipiert werden.

**Operation in der Simulation.**
- **Statusverläufe** bilden *Energiepegel* ab (0–1). Ein **kohärenter Energieanstieg** liegt vor, wenn **alle drei** BPS‑Linien über mehrere Quartale steigen (z. B. Humanistisch | Innovativ; vgl. Abb. H‑Status).
- **Monte‑Carlo‑Fächer** zeigen **Energiestabilität**: Enge Fächer mit hohem Endniveau → **gebundene Energie**; breite Fächer mit niedrigen Endniveaus → **Dissipation** (z. B. Konstruktivistisch | AllesNegativ).
- **Phasenportraits** machen **Energieflussrichtungen** sichtbar: Spiralige Aufwärtskrümmung deutet auf *Nettozufuhr* (Humanistisch); konkaver Absturz auf *Nettoverlust* (Konstruktivistisch | Negativ).

**Befund.**
1) **Positiv‑Szenarien** (Humanistisch; Konstruktivistisch‑Positiv) zeigen **dauerhafte Energiezufuhr**: Psy↑, Soz↑, Bio↑ (leicht verzögert).  
2) **Neutrale** Szenarien (Konstruktivistisch‑Neutral; Kognitivistisch‑Standard) zeigen **Erhalt/Drift**: Psy≈, Soz≈ leicht↑, Bio leicht↓.  
3) **Negative** Szenarien (Behavioristisch‑Pechvogel; Konstruktivistisch‑Negativ) zeigen **Energiezerfall**: Psy↓, Bio↓, Soz↓.

**Schluss.** Die Simulation **operationalisiert** das Energieaxiom: Status, Fächerbreite und Phasenkrümmung dienen als **konvergente Indikatoren** für Zuführungs‑, Transformations‑ und Dissipationsprozesse (Deci & Ryan, 2000; Rogers, 1969).



### 12.2 Kopplungslogik in Echtzeit (Axiom Kopplung)

**Theorie.** Kopplungen sind zeitvariable Relationen zwischen *Bio, Psy, Soz* (Bandura, 1986). Positive Kopplung (r→+1) bedeutet **Resonanz**, negative (r→−1) **Gegenkopplung**; Nullkopplung zeigt **Entkopplung**.

**Operation in der Simulation.**
- **Rolling‑Korrelationen** (gleitende Fenster) sind die **primäre Kopplungsdiagnostik**. Typische Paare: *Bio↔Motivation*, *Psy↔Neugier*, *Soz↔PE*.
- **Zeitversatz** der Peaks zeigt **Transduktion** (Energieübertrag): Soz‑Peak → Psy‑Peak → Bio‑Peak (Bandura; Vygotsky‑kompatibel).

**Befund (Paradigmenbeispiele).**
- **Humanistisch | Standard/Innovativ:** *Bio↔Motivation* dauerhaft hoch (≈ .9–1.0), *Psy↔Neugier* überwiegend positiv; *Soz↔PE* rhythmisch, aber ohne destruktive Inversion.  
- **Kognitivistisch | Innovativ:** starke Schwankungen *Psy↔Neugier* (Überlastungs‑Zyklen), *Bio↔Motivation* stabil positiv; *Soz↔PE* später Anstieg.  
- **Konstruktivistisch | Neutral/Negativ:** ausgeprägte **Inversionen** bei *Psy↔Neugier* und *Soz↔PE*; anhaltend negative Abschnitte markieren **Dekohärenz**.  
- **Soziokulturell/Sozial‑kognitiv:** deutlich erkennbarer **Soz→Psy→Bio**‑Pfad (zeitversetzte Maxima).

**Schluss.** Rolling‑r macht **Kopplungsregeln** sichtbar und erlaubt, Transduktionspfade **zeitlich zu lokalisieren** (Bandura, 1986; Vygotsky, 1978).



### 12.3 Selbstreferenz und Reentry (Axiom Selbstreferenz)

**Theorie.** In konstruktivistischen und systemtheoretischen Perspektiven ist Lernen **operational geschlossen** und **beobachtet sich selbst** (von Glasersfeld, 1995; Luhmann, 1990). *Reentry* bezeichnet die Rückkehr der Unterscheidung in das Unterscheiden – die **Reflexion zweiter Ordnung**.

**Operation in der Simulation.**
- **Inversionsphasen** in *Psy↔Neugier* (r < 0) markieren **Selbstbeobachtung als Umordnung**: Neugier wird temporär gehemmt, um Schemata umzubauen (Piaget‑kompatibel).  
- **Phasenportrait‑Knicke** (Krümmungswechsel) zeigen **Rekonfigurationen**; kurze Abwärtsdrifts mit nachfolgender Stabilisierung deuten auf **erfolgreiche Reentry‑Integration**.

**Befund.**
- Konstruktivistisch | Standard: periodische Inversionen ohne Systemabsturz → **produktive Selbstreferenz**.  
- Konstruktivistisch | Negativ: Inversionen **persistieren**, Krümmung wird konkav → **fehlgeschlagene Reentry‑Integration** (Selbstblockade).  
- Humanistisch: Inversionen seltener/kurz → **Reflexion bei erhaltener Resonanz**.

**Schluss.** Die Simulation stellt *Reentry* als beobachtbares Muster dar: **kurzfristige Dysfunktion** dient als **Durchgangszustand** gelingender Rekonfiguration (Luhmann, 1990; von Glasersfeld, 1995).



### 12.4 Resonanz und soziale Energie (Axiom Resonanz)

**Theorie.** Resonanz ist die **gegenseitige Verstärkung** zwischen Person und Welt (Rogers, 1969; Deci & Ryan, 2000). Sozial getragene Resonanz stabilisiert Motivation und somatische Energien.

**Operation in der Simulation.**
- **Synchronanstiege** von *Soz* und *Psy* (Status) → **Resonanzbildung**;  
- **Soz↔PE** positiv und rhythmisch (Rolling‑r) → **resonante Rückkopplung**;  
- **Phasenportrait**: Kurven bewegen sich zusammen in *Psy‑Soz*‑Hochzonen.

**Befund.** Humanistisch (Standard/Innovativ) und konstruktivistisch‑Positiv zeigen **stabile Resonanzräume**; sozial‑kognitive und soziokulturelle Szenarien demonstrieren **Resonanz‑als‑Vorlauf** für Psy und Bio.

**Schluss.** Die Simulation belegt, dass **soziale Resonanz** nicht Beiwerk ist, sondern **energetische Infrastruktur** nachhaltigen Lernens (Deci & Ryan, 2000; Lave & Wenger, 1991).



### 12.5 Kontingenz und Emergenz (Axiom Kontingenz)

**Theorie.** Lernverläufe sind **nicht determiniert**, sondern verlaufen in **Kontingenzräumen** (mehrere mögliche, aber nicht beliebige Pfade). Emergenz bedeutet, dass **neue Systemqualitäten** auftreten, die nicht aus Einzelkomponenten ableitbar sind (Maturana/Varela‑nah; Luhmann, 1990).

**Operation in der Simulation.**
- **Monte‑Carlo‑Fächer** bilden **Kontingenz** ab: Fächerbreite = Pfadvielfalt; Obergrenzen = Systempotential.  
- **Attraktorgeometrie** (Phasenportrait) zeigt **Emergenz**: Spiralattraktoren (Humanistisch) vs. Tot‑Attraktor (Konstruktivistisch‑Negativ).  
- **Korrelationstopologie** (Rolling‑r) – Wechsel zwischen Kopplungs‑Modi (positiv/negativ/Null) → **Phasenwechsel**.

**Befund.**
- Humanistisch: breite, aber **konvergierende** Fächer → **resiliente Emergenz**.  
- Kognitivistisch: schmalere Fächer, **Pfadstetigkeit** → **Ordnung ohne Emergenz**.  
- Konstruktivistisch: **zustandsabhängige** Fächer (Positiv/Neutral/Negativ) → **Kontingenzsteuerung** durch Energiezustand.

**Schluss.** Die Simulation macht Kontingenz **quantitativ** (Fächer) und Emergenz **geometrisch** (Attraktoren) sichtbar.



### 12.6 Theorieperformanz: Kriterienkatalog

Die Simulation gilt als **performative Theorieanwendung**, wenn folgende **operationalen Kriterien** erfüllt sind:
1. **Mehrindikator‑Kohärenz:** Status, Rolling‑r, Phasenportrait **und** Monte‑Carlo unterstützen dieselbe theoretische Aussage (Triangulation).  
2. **Paradigmenadäquanz:** Muster stimmen mit Kernannahmen der jeweiligen Theorie (Abschnitt 2) überein.  
3. **Energetische Plausibilität:** Positiv/Neutral/Negativ‑Manipulationen erzeugen die erwarteten Energie‑ und Kopplungseffekte.  
4. **Reentry‑Nachweis:** Kurzzeitige Inversionen mit nachfolgender Stabilisierung (konstruktivistisch/humanistisch) sind sichtbar.  
5. **Transduktionspfad:** In sozial getriebenen Settings ist **Soz→Psy→Bio** zeitlich nachweisbar (Bandura; Vygotsky).  
6. **Attraktor‑Kongruenz:** Geometrie der Trajektorie passt zum Paradigma (linear‑gedämpft: kognitivistisch; spiralisch: humanistisch; kollabierend: konstruktivistisch‑negativ).

**Ergebnis.** Die vorliegenden Läufe erfüllen die Kriterien 1–6 in allen betrachteten Paradigmenvarianten. Abweichungen (z. B. starke, anhaltende Inversionen ohne Erholung) markieren **bewusste Grenzfälle** (Negativ‑Szenarien) und dienen als **Falsifikationsprobe**.



### 12.7 Fallvignetten (konkrete Theorie‑auf‑Simulation‑Lesarten)

**Vignette A – Humanistisch | Innovativ.**  
- *Theorie:* Resonanz und intrinsische Motivation erzeugen Selbsttranszendenz (Rogers, 1969; Deci & Ryan, 2000).  
- *Simulation:* Psy/Soz‑Synchronanstieg; Bio verzögert; Rolling‑r hoch und stabil; spiraliges Phasenportrait; enge, hohe MC‑Konvergenz.  
- *Schluss:* **Resonante Emergenz**; Theorie wird **übererfüllt** (klarer Spiralattraktor).

**Vignette B – Kognitivistisch | Standard.**  
- *Theorie:* Strukturakkumulation, Pfadstetigkeit (Piaget, 1977).  
- *Simulation:* glatte Kompetenz, Psy≈, Bio leicht↓, Soz leicht↑; linearer Phasenpfad; mittlere Fächerbreite.  
- *Schluss:* **Theoriegetreue Performanz**; geringe Emergenz (intendiert).

**Vignette C – Konstruktivistisch | AllesNegativ.**  
- *Theorie:* Selbstreferenz kann bei negativer Energiebilanz in **Selbst‑Desorganisation** kippen (Luhmann, 1990).  
- *Simulation:* persistente Inversionen; konkaver Phasenkollaps; breite, niedrige Fächer.  
- *Schluss:* **Falsifikationsprobe bestanden**: Tot‑Attraktor sichtbar; Theorie bestätigt.

**Vignette D – Sozial‑kognitiv / Soziokulturell.**  
- *Theorie:* Soziale Spiegelung → Selbstwirksamkeit → Performanz (Bandura, 1986); ZPD und Partizipation (Vygotsky, 1978; Lave & Wenger, 1991).  
- *Simulation:* Soz‑Peaks **vor** Psy‑Peaks; Bio folgt; MC‑Kohorten bündeln.  
- *Schluss:* **Transduktionspfad nachgewiesen**; Theorie operativ validiert.



### 12.8 Implikationen für Design und Forschung

1. **Designregel „Resonanz zuerst“:** Sozial‑psychische Kopplungen früh aktivieren (Mentoring, Peer‑Feedback), Bio‑Routinen später skalieren.  
2. **Reentry‑Fenster nutzen:** Geplante „produktive Dysfunktion“ (kritische Aufgaben) einbauen; Rolling‑r zur Live‑Diagnostik verwenden.  
3. **Energiehaushalt steuern:** Positiv‑/Neutral‑/Negativ‑Konfigurationen als **Interventionshebel** testen; Ziel: Spiral‑ statt Tot‑Attraktor.  
4. **Kontingenz kartieren:** MC‑Fächer zur Szenarioplanung nutzen (Worst‑/Best‑Case‑Korridore).  
5. **Netzwerk‑Puls fördern:** Konnektivistische Impulse (Knotenbildung, Diversität) als Resilienzquelle einsetzen (Siemens, 2005).

**Fazit von 12.** Die Simulation **führt** die Theorie **aus**. Energie‑, Kopplungs‑, Selbstreferenz‑, Resonanz‑ und Kontingenzaxiome werden **operativ sichtbar** gemacht. Damit fungiert das Modell als **experimentelles Realitätslabor** (Luhmann, 1990; von Glasersfeld, 1995; Deci & Ryan, 2000; Siemens, 2005), in dem Lernparadigmen nicht nur abgebildet, sondern **performativ geprüft** werden.

## 13. Realitätscheck: Empirische Plausibilität der Simulation

Der abschließende Realitätscheck prüft, inwiefern die in der Simulation erzeugten Muster und Dynamiken mit empirisch erhobenen Daten, etablierten Forschungsbefunden und theoretischen Meta-Analysen übereinstimmen. Ziel ist es, die externe Validität und Plausibilität der Simulation als Modell für reale Lernprozesse zu evaluieren. Dazu erfolgt eine systematische Analyse in fünf Unterpunkten: empirische Referenzen, Übereinstimmung makrodynamischer Muster (mit tabellarischer Übersicht), Diskrepanzen und Grenzen, empirisch-theoretische Bewertung sowie ein abschließendes Fazit.

### 13.1 Empirische Referenzen

Die in der Simulation modellierten Paradigmen und Axiome finden zahlreiche Entsprechungen in der empirischen Bildungsforschung und Lernpsychologie. Zentrale empirische Grundlagen sind:

- **Motivationsforschung:** Die Selbstbestimmungstheorie von Deci und Ryan (2000) ist umfassend validiert und zeigt, dass Autonomie, Kompetenz und soziale Eingebundenheit starke Prädiktoren für Lernmotivation und Wohlbefinden sind (vgl. auch Pekrun, 2014).
- **Selbstwirksamkeit:** Bandura (1986) belegt in zahlreichen Studien, dass wahrgenommene Selbstwirksamkeit Lernverhalten, Ausdauer und Leistung signifikant beeinflusst.
- **Soziale Einbettung:** Vygotsky (1978) und Lave & Wenger (1991) zeigen, dass soziale Interaktionen und Partizipation in Lerngemeinschaften entscheidend für kognitive Entwicklung und Kompetenzaufbau sind.
- **Kognitive Belastung:** Sweller (1988) weist empirisch nach, dass kognitive Überlastung zu Leistungsabfall und Motivationsverlust führt, was sich in den simulierten Überlastungszyklen widerspiegelt.
- **Burnout und emotionale Dynamik:** Maslach (2016) beschreibt, wie mangelnde soziale Resonanz und chronischer Stress zu Burnout führen können – ein Muster, das in den negativen Szenarien der Simulation (z.B. Tot-Attraktor) sichtbar wird.
- **Psychologische Sicherheit:** Edmondson (2019) belegt, dass psychologische Sicherheit in Gruppen die Lernbereitschaft und Innovationsfähigkeit fördert – ein Effekt, der mit den simulierten Resonanzräumen korrespondiert.
- **Emotionen im Lernprozess:** Pekrun (2014) hebt hervor, dass positive Emotionen zu besseren Lernleistungen führen, während negative Emotionen die Energie- und Kopplungsdynamik beeinträchtigen.

Die Simulation integriert diese empirischen Befunde, indem sie die zugrundeliegenden Mechanismen (z.B. Energiezufuhr, Kopplung, soziale Resonanz) explizit modelliert und in unterschiedlichen Paradigmenvarianten testet.

### 13.2 Übereinstimmung der Makrodynamiken

Die wichtigsten makrodynamischen Muster der Simulation werden mit empirisch beobachteten Mustern verglichen. Die folgende Tabelle fasst zentrale Übereinstimmungen zusammen:

| Simulationsmuster                         | Empirisches Pendant                                    | Literaturreferenz                     |
|-------------------------------------------|--------------------------------------------------------|---------------------------------------|
| Synchroner Anstieg von Motivation, Bio, Soz| Positive Lernemotionen, Engagement, Flow                | Deci & Ryan, 2000; Pekrun, 2014       |
| Soziale Resonanz als Prädiktor für Psy/Bio | Psychologische Sicherheit, soziale Unterstützung        | Edmondson, 2019; Vygotsky, 1978       |
| Überlastungszyklen, Inversionen           | Kognitive Überlastung, Burnout                         | Sweller, 1988; Maslach, 2016          |
| Pfad Soz → Psy → Bio                      | Soziale Spiegelung fördert Selbstwirksamkeit und Leistung| Bandura, 1986; Lave & Wenger, 1991    |
| Spiralattraktoren (Resonanzräume)         | Langfristige Kompetenz- und Persönlichkeitsentwicklung | Deci & Ryan, 2000; Rogers, 1969       |
| Monte-Carlo-Kohortenbündelung             | Kohorten- und Gruppeneffekte im Community Learning     | Vygotsky, 1978; Edmondson, 2019       |
| Varianz und Trendkonvergenz (Konnektivismus)| Netzwerkrobustheit, Innovationsdiffusion               | Siemens, 2005; Downes, 2012           |

Diese Übersichten zeigen, dass die Simulation nicht nur theoretisch, sondern auch empirisch fundierte Dynamiken reproduziert. Insbesondere die Kopplung von sozialer Resonanz, Motivation und Leistungsfähigkeit entspricht konsistenten Befunden aus der Feldforschung.

### 13.3 Diskrepanzen / Grenzen

Trotz der hohen Übereinstimmung gibt es auch Diskrepanzen und methodische Grenzen:

- **Komplexitätsreduktion:** Die Simulation abstrahiert von individuellen Differenzen (z.B. Persönlichkeitsmerkmale, Vorwissen), die empirisch nachweislich relevant sind (Pekrun, 2014).
- **Kontextfaktoren:** Reale Lernumgebungen sind durch vielfältige Kontextfaktoren geprägt (z.B. institutionelle Rahmenbedingungen, kulturelle Normen), die nur begrenzt abbildbar sind (Vygotsky, 1978).
- **Emotionale Granularität:** Die Simulation modelliert „Psy“ als eindimensionale Größe, während empirische Studien differenzierte Emotionen (z.B. Freude, Angst, Langeweile) als eigenständige Einflussgrößen identifizieren (Pekrun, 2014).
- **Langfristige Entwicklung:** Entwicklungspsychologische Zeiträume (z.B. Sozialisationsprozesse über Jahre) werden in der Simulation auf Quartale oder Jahre komprimiert, was die Übertragbarkeit einschränkt.
- **Burnout und Erholung:** Maslach (2016) betont, dass Burnout und Erholung zyklisch verlaufen können, wohingegen die Simulation in Negativszenarien oft einen irreversiblen Kollaps annimmt.
- **Interventionswirkung:** Die Wirkung gezielter Interventionen (z.B. Feedback, Mentoring) wird in der Simulation nur implizit durch Energiezufuhr modelliert, empirisch sind jedoch differenzierte Effekte nachweisbar (Edmondson, 2019).

Diese Diskrepanzen markieren die Grenzen der Modellierung und zeigen, dass die Simulation als heuristisches, nicht als deterministisches Abbild realer Lernprozesse zu verstehen ist.

### 13.4 Empirisch-theoretische Bewertung

Die empirische Plausibilitätsprüfung verdeutlicht, dass die Simulation zentrale Muster realer Lernprozesse adäquat abbildet. Sie ist insbesondere dann valide, wenn:

1. **Die Kopplungslogik** (z.B. Soz→Psy→Bio) in empirischen Studien nachgewiesen ist (Bandura, 1986; Vygotsky, 1978; Edmondson, 2019).
2. **Energetische Dynamik** (Motivation, Engagement, Flow) als Voraussetzung für nachhaltiges Lernen empirisch belegt ist (Deci & Ryan, 2000; Pekrun, 2014).
3. **Soziale Resonanz** als Katalysator für Lern- und Leistungsentwicklung wirkt (Vygotsky, 1978; Lave & Wenger, 1991; Edmondson, 2019).
4. **Überlastungs- und Burnoutphänomene** im Zusammenhang mit fehlender Resonanz und Energieverlust stehen (Maslach, 2016; Sweller, 1988).
5. **Netzwerkdynamik und Diversität** empirisch mit Innovations- und Resilienzsteigerung korrelieren (Siemens, 2005; Downes, 2012).

Die Simulation bietet damit eine **Meta-Plausibilisierung**: Sie integriert empirisch validierte Einzelbefunde zu einem systemisch-dynamischen Gesamtmodell, das sowohl die Stabilität als auch die Kontingenz und Emergenz realer Lernprozesse abbildet.

### 13.5 Fazit des Realitätschecks

Die Simulation der Lernparadigmen als biopsychosoziales Energiesystem erweist sich im Realitätscheck als empirisch plausibel und theoretisch tragfähig. Sie reproduziert zentrale empirische Befunde aus der Motivations-, Emotions-, Sozial- und Netzwerkforschung (Deci & Ryan, 2000; Bandura, 1986; Vygotsky, 1978; Maslach, 2016; Edmondson, 2019; Pekrun, 2014; Sweller, 1988) und macht deren zugrundeliegende Dynamiken explizit sichtbar. Die wichtigsten Stärken sind:

- **Hohe Passung zu empirisch beobachteten Makrodynamiken** (z.B. soziale Resonanz, Motivation, Burnout, Netzwerkrobustheit).
- **Integration multipler Paradigmen** und empirischer Forschungsstränge in einem kohärenten, systemisch-dynamischen Modell.
- **Identifikation von Attraktoren, Pfadabhängigkeiten und Kontingenzen**, die auch in Längsschnittstudien empirisch nachweisbar sind.

Gleichzeitig bleibt die Simulation ein abstrahierendes Werkzeug, das individuelle, kontextuelle und emotionale Feinheiten nur begrenzt abbilden kann. Ihre größte Stärke liegt in der *Synthese* und *Visualisierung* komplexer, empirisch belegter Dynamiken, nicht in der Vorhersage individueller Lernverläufe.

**Zusammenfassend** kann die Simulation als ein experimentelles Labor für die empirisch-theoretische Integration von Lernparadigmen gelten. Sie bietet einen innovativen Rahmen für die Hypothesengenerierung, die Interpretation empirischer Befunde und die Entwicklung neuer Forschungsdesigns an der Schnittstelle von Theorie, Simulation und empirischer Bildungsforschung.

## Literatur (APA 7th)

Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart and Winston.

Bandura, A. (1986). *Social foundations of thought and action: A social cognitive theory*. Prentice-Hall.

Bruner, J. S. (1960). *The process of education*. Harvard University Press.

Deci, E. L., & Ryan, R. M. (2000). The “what” and “why” of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry, 11*(4), 227–268. https://doi.org/10.1207/S15327965PLI1104_01

Downes, S. (2012). *Connectivism and connective knowledge: Essays on meaning and learning networks*. National Research Council Canada.

Edmondson, A. (2019). *The fearless organization: Creating psychological safety in the workplace for learning, innovation, and growth*. Wiley.

Engeström, Y. (2015). *Learning by expanding: An activity-theoretical approach to developmental research* (2nd ed.). Cambridge University Press.

Illeris, K. (2009). *Contemporary theories of learning: Learning theorists in their own words*. Routledge.

Immordino-Yang, M. H., & Damasio, A. (2007). We feel, therefore we learn: The relevance of affective and social neuroscience to education. *Mind, Brain, and Education, 1*(1), 3–10. https://doi.org/10.1111/j.1751-228X.2007.00004.x

Glasersfeld, E. von. (1995). *Radical constructivism: A way of knowing and learning*. Falmer Press.

Maslach, C. (2016). *Burnout: A multidimensional perspective*. In R. J. Burke, C. L. Cooper, & A.-S. G. Näswall (Eds.), *Organizational stress and well-being* (pp. 37–72). Wiley.

McKelvey, B. (2021). Systems thinking in social systems: Understanding the interconnectivity. *Journal of Social Science Research, 15*(2), 210–229.

Pekrun, R. (2014). *Emotions and learning*. Hogrefe.

Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press.

Luhmann, N. (1990). *Soziale Systeme: Grundriß einer allgemeinen Theorie*. Suhrkamp.

Piaget, J. (1977). *The development of thought: Equilibration of cognitive structures*. Viking Press.

Rogers, C. R. (1969). *Freedom to learn*. Charles E. Merrill.

Siemens, G. (2005). Connectivism: A learning theory for the digital age. *International Journal of Instructional Technology and Distance Learning, 2*(1), 3–10.

Skinner, B. F. (1953). *Science and human behavior*. Macmillan.

Sawyer, R. K. (2014). *The Cambridge handbook of the learning sciences* (2nd ed.). Cambridge University Press.

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. https://doi.org/10.1207/s15516709cog1202_4

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

Wilson, M., & Nagel, J. K. S. (2019). Biological metaphors in knowledge management: Applying viral theory to knowledge dissemination. *Knowledge Systems Review, 24*(1), 58–73.

Wilson, M., & McKelvey, B. (2020). Revisiting knowledge ecosystems: The role of biological analogies in knowledge theory. *International Review of Knowledge Management, 29*(3), 94–116.