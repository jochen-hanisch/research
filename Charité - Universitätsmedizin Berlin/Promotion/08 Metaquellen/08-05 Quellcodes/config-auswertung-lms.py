"""
Konfiguration für die LMS-Umfrageauswertung.

Angelehnt an die CI-Configs der anderen Projekte (#NotSan, TEI, Visible Learning),
damit Theme, Pfade und Export-Flags zentral gepflegt werden können.
"""

from pathlib import Path

# Basisverzeichnisse
BASE_DIR = Path(__file__).resolve().parent  # Research/.../LMS Umfrage
ROOT_DIR = BASE_DIR.parents[3]  # /Users/.../Documents/scripte

# -------------------------------------------------------
# Datenquelle
# -------------------------------------------------------
# CSV-Pfad (relativ oder absolut)
csv_file = BASE_DIR / "UmfrageOnline-Beantwortungen.csv"

# Stopplisten (falls woanders abgelegt, hier anpassen)
stop_words_de_path = ROOT_DIR / "de_complete.txt"
stop_words_en_path = ROOT_DIR / "en_complete.txt"

# -------------------------------------------------------
# Visualisierungs-Theme & Export
# -------------------------------------------------------
theme = "light"  # "dark" oder "light" – wird an ci_template übergeben
theme_toggle = {"dark": "light", "light": "dark"}  # Umschalter für schnellen Wechsel

export_fig_html = False  # Plotly-HTMLs nur bei Bedarf erzeugen
export_fig_png = True   # PNG-Export (setzt Kaleido voraus)

# Beim Durchlauf jede Visualisierung automatisch im Browser öffnen
show_figures_in_browser = True

# -------------------------------------------------------
# Analyse-Optionen (Platzhalter für spätere Nutzung im Skript)
# -------------------------------------------------------
enable_yes_no = True
enable_likert = True
enable_freetext = True
enable_correlation = True
enable_wordcloud = True

# Neue Analysen
enable_item_summary = True
enable_scale_analysis = True
enable_collector_comparison = True   # Visualisierungen nach Collector anzeigen
enable_scale_correlation = True      # Skalen-Korrelationen anzeigen

# Skalen-Definitionen (Items genau wie in der CSV benennen)
scale_definitions = {
    "Struktur_Orientierung": [
        "Wie werden komplexe Themen im LMS aufbereitet und wie beeinflusst das Ihre Lernprozesse?",
        "Wie bewerten Sie die Klarheit und Struktur der im LMS präsentierten Informationen?",
        "Wie einfach ist es, auf verschiedene Ressourcen im LMS zuzugreifen?",
        "Wie bewerten Sie die Flexibilität des LMS in Bezug auf individuelle Lernbedürfnisse?\"",
    ],
    "Medien_Inhalte": [
        "Welche Rolle spielen multimediale Inhalte im LMS für Ihr Verständnis?",
        "Wie nahtlos integriert das LMS externe Lernmaterialien oder -werkzeuge?",
        "Gibt es Möglichkeiten im LMS, Lerninhalte nach Ihren Interessen und Stärken zu personalisieren?\"",
    ],
    "Interaktion_Kollaboration": [
        "Auf welche Weise fördert das LMS aktive Diskussionen und Austausch mit anderen?",
        "Wie unterstützt das LMS Gruppenarbeit und Kollaboration unter den Lernenden?",
        "Welchen Einfluss hat die Benutzeroberfläche des LMS auf Ihre Interaktionsmöglichkeiten?",
    ],
    "Feedback_Bewertung": [
        "Wie zeitnah und hilfreich ist das Feedback, das Sie im LMS erhalten?\"",
        "Inwiefern unterstützen die Bewertungssysteme im LMS Ihr Verständnis über Ihren Lernfortschritt?",
        "Welche Rolle spielen Selbstbewertungstools im LMS für Ihre Selbsteinschätzung?",
    ],
    "Barrierefreiheit": [
        "Wie bewerten Sie die Barrierefreiheit und Zugänglichkeit des LMS für alle Lernenden.",
    ],
}

# Tabellenexport
export_tables = False  # nur bei Bedarf aktivieren
