# Pfad-Tools
from pathlib import Path

# Konfiguration für deskriptive-literaturauswahl.py

# Theme: "light" oder "dark"
theme = "dark"

# Datenquelle
bib_filename = "02-01 Suchergebnisse.bib"

# Exportsteuerung
export_fig_visual = False  # Steuerung, ob Visualisierungen exportiert werden
export_fig_png = False     # Separater Schalter für PNG-Export

# Einzelne Exportflags (optional überschreibbar)
export_fig_silhouette_plot = export_fig_visual
export_fig_n_jahresverteilung = export_fig_visual
export_fig_quartile_trendlinien = export_fig_visual
export_fig_balkenverteilung_n = export_fig_visual
export_fig_winsor_median = export_fig_visual
export_fig_delta_plot = export_fig_visual

# Exportpfade
export_path_html = "johajo@sternenflottenakademie.local:/mnt/deep-space-nine/public/plot/promotion"
export_path_png = str(
    Path.home()
    / "Documents"
    / "Allgemein beruflich"
    / "Research"
    / "Charité - Universitätsmedizin Berlin"
    / "Bilder und Sceenshots"
)
