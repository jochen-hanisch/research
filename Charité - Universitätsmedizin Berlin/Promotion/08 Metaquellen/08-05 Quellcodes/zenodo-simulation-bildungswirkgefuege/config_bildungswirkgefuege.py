# config_bildungswirkgefuege.py

quartale = 12  # Anzahl der Simulationsquartale
simulations_durchlaeufe = 25  # Anzahl der Wiederholungen (z. B. für Monte-Carlo)
initial_neugier = 3.066  # Startwert für die Neugier (z.B. aus 5DCR abgeleitet 3.066)
start_kompetenz = 1.333  # Startwert für die Kompetenz (z.B. aus APrVO 1.333)
theme = "dark"  # Visualisierungsthema: "dark" oder "light"
ansatz_wahl = 5  # Auswahl des didaktischen Ansatzes (1–7)
selected_archetyp = "Standardlernender"  # Auswahl des Lernenden-Archetyps
export_fig_visual = False  # Steuerung, ob Visualisierungen exportiert werden
export_fig_png = False  # Separater Schalter für PNG-Export
modellpruefung_aktiv = False  # Steuerung, ob nach der Simulation automatisch eine Modellprüfung durchgeführt wird

# Hinweis: Exportpfade können via Umgebungsvariablen gesetzt werden:
# - `BILDWIRK_EXPORT_ROOT` (CSV/Logs; Standard: ~/Documents/scripte/.../Modellpruefung)
# - `BILDWIRK_PNG_DIR` (PNG; Standard: ~/Documents/Allgemein beruflich/Research/Forschungsprojekte/Systemische Kompetenzentwicklung für High Responsibility Teams)
# - `BILDWIRK_HTML_DIR` (HTML; Standard: <EXPORT_ROOT>/html)
# - `BILDWIRK_REMOTE_SCP_DEST` (optional: scp-Ziel für HTML; wenn nicht gesetzt, bleibt HTML lokal)
# - `BILDWIRK_REPORT_DIR` (Modellprüfungs-Report; absolut oder relativ zu Obsidian-Root, Fallback: <EXPORT_ROOT>/berichte)

"""
1: "Instruktional",
2: "Kognitivistisch",
3: "Behavioristisch",
4: "Humanistisch",
5: "Konstruktivistisch",
6: "Soziokulturell",
7: "Systemisch"

 "Standardlernender"  # Basisprofil, ausgeglichene Parameter
 "Pechvogel"          # häufig widrige Bedingungen, hohe Belastung
 "Glückspilz"         # günstige Ausgangslage, profitiert stark
 "Überambitioniert"   # hohe Ziele, Gefahr von Überforderung
 "Zögerlich"          # zurückhaltend, hohe Unsicherheit
 "Sozial"             # interaktionsorientiert, profitiert von Gemeinschaft
 "Kreativ"            # ideenreich, hohe Offenheit für Neues
 "Pragmatisch"        # lösungsorientiert, handlungsfokussiert
 "Reflektiert"        # metakognitiv stark, gute Selbsteinschätzung
 "Resilient"          # widerstandsfähig, stabil trotz Belastungen
 "Innovativ"          # neugierig, experimentierfreudig
 "Skeptisch"          # kritisch, eher zurückhaltend bei Neuem

 Konsistenzprüfungen
 "AllesPositiv"       # alle Parameter positiv
 "AllesNeutral"       # alle Parameter neutral
 "AllesNegativ"       # alle Parameter negativ
"""
