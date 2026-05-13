import os
import sys
import math
from pathlib import Path

import plotly.graph_objects as go

from config_eye_tracking import plotly_theme, export_fig_visual, export_fig_png


def _ensure_ci_template_path():
    """Sucht das lokale CI-Paket und hängt es an sys.path."""
    env_path = os.environ.get("CI_TEMPLATE_PATH")
    if env_path and env_path not in sys.path:
        sys.path.append(env_path)
        return
    base_dir = Path(__file__).resolve().parent
    search_roots = [base_dir] + list(base_dir.parents)
    for root in search_roots:
        candidates = [
            root / "ci_template",
            root / "CI" / "ci_template",
            root / "Jochen-Hanisch" / "CI" / "ci_template",
        ]
        for candidate in candidates:
            if (candidate / "__init__.py").exists():
                package_root = candidate.parent
            elif (candidate / "ci_template" / "__init__.py").exists():
                package_root = candidate
            else:
                continue
            package_root_str = str(package_root)
            if package_root_str not in sys.path:
                sys.path.append(package_root_str)
            return


_ensure_ci_template_path()

from ci_template.plotly_template import (  # type: ignore
    get_colors,
    get_standard_layout,
    set_theme,
)


set_theme(plotly_theme, preserve_effects=True)
colors = get_colors()

BASE_DIR = Path(__file__).resolve().parent
EXPORT_DIR = BASE_DIR / "export"
EXPORT_DIR.mkdir(exist_ok=True)


def export_figure(fig: go.Figure, name: str) -> None:
    """Exportiert die Figuren optional als HTML/PNG in den lokalen Export-Ordner."""
    if export_fig_visual:
        html_path = EXPORT_DIR / f"{name}.html"
        fig.write_html(html_path, include_plotlyjs="cdn")
    if export_fig_png:
        png_path = EXPORT_DIR / f"{name}.png"
        try:
            fig.write_image(png_path, scale=2)
        except Exception:
            # PNG-Export erfordert zusätzliche Abhängigkeiten (z.B. kaleido)
            pass

# Funktion zur Berechnung des Konfidenzintervalls
def calculate_ci(percentage, n):
    Z = 1.96
    p = percentage / 100
    margin_of_error = Z * math.sqrt((p * (1 - p)) / n)
    lower_bound = percentage - (margin_of_error * 100)
    upper_bound = percentage + (margin_of_error * 100)
    return (lower_bound, upper_bound)

# Ursprungsdaten
total_1st_year = 24  # 1. Ausbildungsjahr
total_2nd_year = 11  # 2. Ausbildungsjahr
total_3rd_year = 10  # 3. Ausbildungsjahr

participants_per_course = 8
total_sample_size = participants_per_course * 3
total_population_size = total_1st_year + total_2nd_year + total_3rd_year

# Prozentuale Verteilung
p_1st_year = (participants_per_course / total_1st_year) * 100
p_2nd_year = (participants_per_course / total_2nd_year) * 100
p_3rd_year = (participants_per_course / total_3rd_year) * 100

# Konfidenzintervalle berechnen
ci_1st_year = calculate_ci(p_1st_year, total_1st_year)
ci_2nd_year = calculate_ci(p_2nd_year, total_2nd_year)
ci_3rd_year = calculate_ci(p_3rd_year, total_3rd_year)

# Daten für die Darstellung
courses = [f'1. Ausbildungsjahr\n(n=8, N={total_1st_year})',
           f'2. Ausbildungsjahr\n(n=8, N={total_2nd_year})',
           f'3. Ausbildungsjahr\n(n=8, N={total_3rd_year})']
percentages = [p_1st_year, p_2nd_year, p_3rd_year]
lower_bounds = [ci[0] for ci in [ci_1st_year, ci_2nd_year, ci_3rd_year]]
upper_bounds = [ci[1] for ci in [ci_1st_year, ci_2nd_year, ci_3rd_year]]

# Dynamischer Titel für prozentuale Verteilung
title = (f'Prozentuale Verteilung und 95% Konfidenzintervalle der Stichproben (n={total_sample_size}) '
         f'im Vergleich zur Kursgröße (N={total_population_size})')

# Berechnungen für mögliche Bilder
stimuli_per_view = 11
views_per_participant = 3  # Heatmap, View Map, Fog View
recordings_per_participant = 1

# Berechnung pro Jahrgang und View Type
images_per_view_type = stimuli_per_view * participants_per_course
recording_images = recordings_per_participant * participants_per_course

# Gesamtanzahl der Bilder pro Jahrgang
total_images_per_year = images_per_view_type * views_per_participant + recording_images

# Gesamtanzahl der Bilder für alle Jahrgänge
total_images_all_years = total_images_per_year * 3

# Dynamischer Titel für kumulative Bilder
title_images = (f'Kumulative Anzahl der möglichen Bilder (gesamt: {total_images_all_years}) '
                f'pro Jahrgang und nach Geschlecht')

# Erstellen der Grafik für prozentuale Verteilung
fig = go.Figure()

# Fehlerbalken hinzufügen
fig.add_trace(go.Bar(
    x=['1. Ausbildungsjahr', '2. Ausbildungsjahr', '3. Ausbildungsjahr'],
    y=percentages,
    error_y=dict(
        type='data',
        symmetric=False,
        array=[upper - perc for upper, perc in zip(upper_bounds, percentages)],
        arrayminus=[perc - lower for perc, lower in zip(percentages, lower_bounds)],
        color=colors['secondaryLine']
    ),
    marker=dict(color=colors['primaryLine'])
))

# Layout anpassen
fig.update_layout(
    get_standard_layout(
        title=title,
        x_title='Kurs',
        y_title='Prozentuale Verteilung (%)',
    )
)

export_figure(fig, "eye_tracking_verteilung_konfidenz")
fig.show()

# Visualisierung der möglichen Bilder
fig_images = go.Figure()

# Kumulativ für die View Types und Aufnahmen pro Jahrgang und für alle Jahrgänge
fig_images.add_trace(go.Bar(
    x=['Einzelner Jahrgang', 'Alle Jahrgänge'],
    y=[images_per_view_type, images_per_view_type * 3],
    name='Heatmap',
    marker=dict(color=colors['primaryLine'])
))

fig_images.add_trace(go.Bar(
    x=['Einzelner Jahrgang', 'Alle Jahrgänge'],
    y=[images_per_view_type, images_per_view_type * 3],
    name='View Map',
    marker=dict(color=colors['secondaryLine'])
))

fig_images.add_trace(go.Bar(
    x=['Einzelner Jahrgang', 'Alle Jahrgänge'],
    y=[images_per_view_type, images_per_view_type * 3],
    name='Fog View',
    marker=dict(color=colors['depthArea'])
))

fig_images.add_trace(go.Bar(
    x=['Einzelner Jahrgang', 'Alle Jahrgänge'],
    y=[recording_images, recording_images * 3],
    name='Recording',
    marker=dict(color=colors['brightArea'])
))

# Layout anpassen
fig_images.update_layout(
    get_standard_layout(
        title=title_images,
        x_title='Kategorie',
        y_title='Anzahl der möglichen Bilder',
    ),
    barmode='stack'
)

export_figure(fig_images, "eye_tracking_bildanzahl")
fig_images.show()
