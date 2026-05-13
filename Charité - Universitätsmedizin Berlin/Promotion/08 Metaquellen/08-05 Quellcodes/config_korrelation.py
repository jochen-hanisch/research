# Pfad-Tools
from pathlib import Path

# Konfiguration für analyse_korrelation.py

# Theme: "light" oder "dark"
theme = "dark"

bib_filename = "02-01 Suchergebnisse.bib"

# Exportsteuerung
export_fig_visual = False  # Steuerung, ob Visualisierungen exportiert werden
export_fig_png = False     # Separater Schalter für PNG-Export

# Einzelne Export-Flags (optional überschreibbar)
export_fig_clusteranalyse = export_fig_visual
export_fig_correlation_suchbegriffe_kategorien = export_fig_visual
export_fig_correlation_fu_kategorien = export_fig_visual
export_fig_correlation_fu_suchbegriffe = export_fig_visual
export_fig_correlation_indizes_kategorien = export_fig_visual
export_fig_correlation_indizes_suchbegriffe = export_fig_visual
export_fig_correlation_fu_indizes = export_fig_visual
export_fig_correlation_fu_fu = export_fig_visual
export_fig_correlation_suchbegriffe_suchbegriffe = export_fig_visual
export_fig_correlation_kategorien_kategorien = export_fig_visual
export_fig_correlation_indizes_indizes = export_fig_visual
export_fig_summary_plot = export_fig_visual
export_fig_png = export_fig_png

# Exportpfade
export_path_html = "johajo@sternenflottenakademie.local:/mnt/deep-space-nine/public/plot/promotion"
def _resolve_png_path():
    candidates = [
        Path("/Users/jochenhanisch-johannsen/Documents/Allgemein beruflich/Research/Charité - Universitätsmedizin Berlin/Bilder und Sceenshots"),
        Path(__file__).resolve().parent / "output" / "png"
    ]
    for candidate in candidates:
        if candidate.exists() or candidate.parent.exists():
            return str(candidate)
    return str(candidates[-1])

export_path_png = _resolve_png_path()
