\newpage

## Prompt zur systemisch-forschungsfragengeleiteten Auswertung der Eye-Tracking-Visualisierungen {#sec:A-4}

Dieser Prompt dient der reproduzierbaren, theorie- und forschungsfragengeleiteten Auswertung der im Forschungsdesign verwendeten Eye-Tracking-Daten (Heatmaps, Viewmaps, Fog-Views). Er folgt den methodischen Grundlagen des systemisch-forschungsfragengeleiteten Paradigmas der Arbeit (Kapitel 4.1–4.2) und operationalisiert die qualitative Bildauswertung gemäß Abschnitt 4.2.4 (Eye-Tracking).

**Eingabe je Analysefall**  
- Stimulus-ID und kurze Kontextangabe (UI-Ausschnitt, Ziel-FUs, z.B. FU4b/FU1/FU6).  
- LMS-Screenshot (Kontext), Heatmap, Viewmap/Gaze-Plot (Kreise proportional zur Fixationsdauer + Pfade), Fog-View (invertierte Fixationsdichte, ignorierte Zonen).  
- Optional: AOI-Beschreibung (rechteckige AOIs, identische Auflösung).

 Zweck des Prompts  
Der Prompt ermöglicht eine konsistente, FU4b-zentrierte Analyse der Eye-Tracking-Visualisierungen. Er stellt sicher, dass die Auswertung:

- theoriegeleitet (Salienz, Gestaltgesetze, visuelle Hierarchie),
- systemisch (Interdependenzen der UI-Elemente),
- forschungsfragenorientiert (FU4b: technisch-gestalterische Mechanismen),
- und methodisch transparent erfolgt.

Er wird ausschließlich zur strukturierten Beschreibung verwendet; die Interpretationsverantwortung bleibt bei der forschenden Person.

 Eingabematerial  
Für jede Analyse werden folgende Visualisierungstypen bereitgestellt:

1. **Heatmap**  
   - zeigt Fixationsdichte (Hotspots/Warmspots/Coldspots).
2. **Viewmap / Scanpath / Fixation Plot**  
   - zeigt Blickpfade, Fixationsabfolgen und relative Fixationsdauer (Kreise proportional zur Dauer + Linienverbindungen; keine nummerierte Reihenfolge).
3. **Fog-View**  
   - zeigt nicht beachtete Bereiche (invertierte Fixationsdichte, ignorierte Zonen).
4. **Stimulus-Screenshot**  
   - Kontextualisierung der Bildstruktur des LMS.
- **Stimulusreihe** = Stimulus + die drei Visualisierungstypen (Heatmap, Viewmap/Gaze-Plot, Fog-View). Die referenzierten Stimuli sind im Bildarchiv (`08 Metaquellen/08-01 Abbildungen/eye-traking`) hinterlegt.

 Ziel der Analyse  
Die Auswertung beantwortet die Leitfrage von **FU4b**:

> *Welche technisch-gestalterischen Mechanismen des LMS leiten die visuelle Aufmerksamkeit, strukturieren das Orientierungsgeschehen und beeinflussen die Wahrnehmungslogik der Lernenden?*

 Prompt zur Auswertung der Eye-Tracking-Bilder

**Analyseprompt (für jede Stimulusreihe):**

Bitte analysiere die folgenden Eye-Tracking-Visualisierungen eines LMS-Stimulus (Heatmap, Viewmap/Scanpath, Fog-View) nach den im Methodenabschnitt beschriebenen Prinzipien. Berücksichtige die systemisch-forschungsfragengeleitete Logik aus Kapitel 4.1–4.2 und die Zielsetzung von FU4b.  

Führe dazu die folgenden Schritte aus:

 1. Beschreibung der Heatmap (Fixationsverteilung)
- Identifiziere Hotspots und ordne sie funktionalen UI-Elementen zu.  
- Bewerte die visuelle Salienz und erkennbare Gestaltungsmuster.  
- Bestimme, ob die Fixationen erwartbaren Mustern folgen (z. B. F-Pattern, Z-Pattern, zentral-periphere Steuerung).  
- Analysiere visuelle Konkurrenz (Elemente, die ungewollt Aufmerksamkeit ziehen).

 2. Beschreibung der Viewmap / Scanpath
- Rekonstruiere die Reihenfolge der Fixationen (Blickpfadlogik).  
- Identifiziere Orientierungswechsel zwischen UI-Bereichen.  
- Bestimme, ob der Blickfluss linear, fragmentiert oder sprunghaft wirkt.  
- Leite daraus gestalterische Implikationen ab (z. B. Navigierbarkeit, Blickführung, Kohärenz).

 3. Beschreibung der Fog-View (Nichtbeachtung)
- Markiere alle Bereiche, die systematisch nicht beachtet werden.  
- Beurteile deren Funktionalität (z. B. wichtige vs. unwichtige Elemente).  
- Leite daraus ab, ob Elemente überflüssig, zu wenig salienzstark oder gestalterisch unterrepräsentiert sind.

 4. Systemische Analyse (Interdependenzen)
- Zeige wechselseitige Wirkungen zwischen UI-Bereichen auf.  
- Analysiere die Relation zwischen Text, Navigation, Icons, interaktiven Elementen und Weißraum.  
- Identifiziere Muster, die auf emergente Wahrnehmungslogiken hinweisen (z. B. ungewollte Priorisierung eines Elements).

 5. Ableitung technisch-gestalterischer Mechanismen (FU4b)
Formuliere präzise Mechanismen, z. B.:

- *Salienzsteuerung (Farbkontrast, Bildanteile, ikonische Signale)*  
- *Orientierungslogiken (Sequenzialität, Blickanfangszonen)*  
- *Affordances und visuelle Zugänglichkeit*  
- *Gestaltgesetze (Nähe, Ähnlichkeit, Geschlossenheit)*  
- *Kohärenz oder Fragmentierung des UI*  
- *Ablenkungszonen und visuelle Störungen*

 6. Kurzdiagnose für die Forschungsunterfrage FU4b
Erstelle eine prägnante Zusammenfassung:

- Was zeigt der Stimulus über die Wahrnehmungslogik des LMS?  
- Welche gestalterischen Faktoren wirken förderlich/hemmend?  
- Welche systemischen Muster sind relevant?  
- Welche Hypothesen ergeben sich für Kapitel 5?

 Ausgabeformat (empfohlen)
- Heatmap: …  
- Viewmap/Gaze-Plot: …  
- Fog-View: …  
- Mechanismen (FU4b): …  
- Kurzdiagnose FU4b: … (Bezug zu FU und Stimulus-ID nennen)

 Wichtige Hinweise zur Nutzung
1. Der Prompt dient der **strukturierenden Unterstützung**, nicht der automatischen Interpretation.  
2. Alle KI-generierten Beschreibungen sind durch die forschende Person zu prüfen.  
3. Die Auswertung erfolgt **relativ**, nicht metrisch.  
4. Die Interpretation muss an FU4b und die theoretischen Grundlagen rückgebunden werden.
5. Artefakte/Ausreißer (Off-Center, Trackloss) benennen und nicht überinterpretieren.  
6. Detailauswertung erfolgt in Abschnitt 4.3.9; Befunde fließen narrativ in Kapitel 5.
7. RealEye-Hinweise: Heatmap-Farben kodieren Intensität, nicht Dauer; Viewmap/Fog-View zeigen Verteilung ohne nummerierte Reihenfolge. Zentralfixations-Bias zu Beginn ggf. berücksichtigen; Ausreißer/Teilnehmende mit schlechter Qualität aussortieren.
8. Zeitfenster: Bei Bedarf die ersten ~0,5 s (central fixation bias) ausblenden; Zeitintervall verschieben/verkürzen, wenn Sequenzdetails relevant sind.
9. Filter: Teilnehmerqualität/Tags/AOI-Fokus in RealEye prüfen; keine automatischen CSVs genutzt, daher Filter nur zur visuellen Sichtung.
todo Stimulusreihe-Hinweis anpassen/streichen, wenn die Abbildungen komplett im Haupttext eingebettet sind.

 Abschlussbemerkung

Diese Datei bildet den verbindlichen Auswertungsrahmen für alle Eye-Tracking-Analysen im Rahmen der Dissertation.
