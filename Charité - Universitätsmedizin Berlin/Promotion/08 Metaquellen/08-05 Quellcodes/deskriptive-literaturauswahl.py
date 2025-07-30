# ===============================
# Deskriptive Analyse: Silhouette-Scores & Fallzahlen
# ===============================

# --- System- und Modul-Imports ---
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import date
from scipy.stats.mstats import winsorize
from scipy.stats import iqr
import os
import subprocess

# --- CI-Template & Konfiguration ---
from ci_template.plotly_template import (
    get_standard_layout,
    get_colors,
    set_theme
)
from config_deskriptive_literaturauswahl import (
    theme,
    export_fig_visual,
    export_fig_png,
    export_fig_silhouette_plot,
    export_path_html,
    export_path_png
)

# --- Initialisierung ---
os.system('cls' if os.name == 'nt' else 'clear')
set_theme(theme)
colors = get_colors()
current_date = date.today().isoformat()

# --- Datenbasis ---
years = np.array([
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
])
sc_values = np.array([
    1.0000, 0.9655, 0.8571, 1.0000, 0.9583, 1.0000, 1.0000, 1.0000,
    0.9895, 1.0000, 0.9968, 0.9854, 0.9916, 0.9702, 0.9208, 0.9696
])
n_values = np.array([
    7, 29, 7, 28, 24, 28, 25, 98,
    95, 202, 303, 377, 430, 899, 780, 192
])

# --- Berechnung der euklidischen Distanz zwischen SC und n ---
distances = np.sqrt((sc_values - sc_values.mean())**2 + (n_values - n_values.mean())**2)

# --- Berechnungen ---
# Berechne IQR und automatische untere/obere Grenzen
sc_iqr = iqr(sc_values)
q1_val = np.percentile(sc_values, 25)
q3_val = np.percentile(sc_values, 75)
lower_bound = q1_val - 1.5 * sc_iqr
upper_bound = q3_val + 1.5 * sc_iqr
sc_winsorized = np.clip(sc_values, lower_bound, upper_bound)
median_winsorized = np.median(sc_winsorized)

# Quartile
q1 = q1_val
q2 = np.median(sc_values)
q3 = q3_val
max_value = np.max(sc_values)
min_value = np.min(sc_values)

# Schwellenwerte datenbasiert
fatigue_threshold = q1  # oder eine alternative datenbasierte Schwelle
circadian_optimum = q3  # oder np.percentile(sc_values, 90)

# Neue Berechnung von delta_raw und delta_z
delta_raw = sc_values - (n_values / np.max(n_values))
delta_z = (delta_raw - np.mean(delta_raw)) / np.std(delta_raw)

# --- Quartilsbasierte Schwellenwerte für delta_raw ---
q1_delta = np.percentile(delta_raw, 25)
q2_delta = np.median(delta_raw)
q3_delta = np.percentile(delta_raw, 75)

# --- Visualisierung ---
fig = go.Figure()

from ci_template.plotly_template import get_plot_styles
styles = get_plot_styles()

fig.add_trace(go.Scatter(
    x=years,
    y=n_values,
    name='Fallzahlen (n)',
    yaxis='y2',
    mode='lines+markers',
    line=dict(color=colors["primaryLine"], width=1),
    marker=dict(size=16, color=colors["primaryLine"], symbol="square"),
    showlegend=True
))

# Quartile & Bezugslinien
fig.add_trace(go.Scatter(x=years, y=[q1]*len(years), mode='lines', name='SC Q1',
                         line=dict(dash='dot', color=colors["brightArea"]), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[q2]*len(years), mode='lines', name='SC Q2',
                         line=dict(dash='dot', color=colors["depthArea"]), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[q3]*len(years), mode='lines', name='SC Q3',
                         line=dict(dash='dot', color=colors["accent"]), yaxis='y1'))
fig.add_trace(go.Scatter(
    x=years,
    y=[min_value]*len(years),
    mode='lines',
    name='SC Min',
    line=dict(dash='dash', color=colors["negativeHighlight"]),
    yaxis='y1'
))
fig.add_trace(go.Scatter(
    x=years,
    y=[max_value]*len(years),
    mode='lines',
    name='SC Max',
    line=dict(dash='dash', color=colors["positiveHighlight"]),
    yaxis='y1'
))

fig.add_trace(go.Scatter(
    x=years,
    y=sc_values,
    name='Silhouette-Scores',
    yaxis='y1',
    mode='lines+markers',
    line=dict(color=colors["primaryLine"], width=1),
    marker=dict(size=16, color=colors["primaryLine"], symbol="circle"),
    showlegend=True
))


# 3. Abweichung ΔSCₙ – farbcodiert
fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
    line=dict(color=colors["positiveHighlight"], width=5),
    name='ΔSCₙ: Optimal'
))
fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
    line=dict(color=colors["secondaryLine"], width=5),
    name='ΔSCₙ: Q2+ Bereich'
))
fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
    line=dict(color=colors["text"], width=5),
    name='ΔSCₙ: Ambivalent'
))
fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
    line=dict(color=colors["negativeHighlight"], width=5),
    name='ΔSCₙ: Kritisch'
))

# Berechne Quartile für SC und n
sc_q2 = np.percentile(sc_values, 50)
sc_q3 = np.percentile(sc_values, 75)
n_q2 = np.percentile(n_values, 50)
n_q3 = np.percentile(n_values, 75)

for year, sc, n in zip(years, sc_values, n_values):
    delta = sc - (n / max(n_values))

    if sc >= sc_q3 and n >= n_q3:
        color = colors["positiveHighlight"]
        label = "Optimal (SC & n ≥ Q3)"
    elif sc < sc_q2 and n < n_q2:
        color = colors["negativeHighlight"]
        label = "Kritisch (SC & n < Q2)"
    elif sc >= sc_q2 and n >= n_q2:
        color = colors["secondaryLine"]
        label = "Pragmatisch gut (Q2 ≤ SC & n < Q3)"
    else:
        color = colors["text"]
        label = "Ambivalent (alle übrigen Fälle)"

    if np.isclose(delta, q2_delta, atol=1e-3):
        line_width = 7  # Bonus: Medianlinie hervorheben
    else:
        line_width = 5

    fig.add_trace(go.Scatter(
        x=[year, year],
        y=[0, delta],
        mode='lines',
        line=dict(color=color, width=line_width),
        hoverinfo='text',
        text=[f"Jahr: {year}, ΔSCₙ: {delta:.4f}, {label}"]*2,
        yaxis='y3',
        showlegend=False
    ))
    print(f"Jahr: {year}, SC: {sc:.4f}, n: {n}, Kategorie: {label}")

# Layout
layout = get_standard_layout(
    title="Silhouette-Scores und Fallzahlen pro Jahr",
    x_title='Jahr',
    y_title='Silhouette-Score',
    yaxis2=dict(
        title="Fallzahlen (n)",
        showgrid=False,
        title_standoff=20
    )
)
layout["font"] = {"size": 14, "color": colors['text']}
layout["title"] = dict(text="Silhouette-Scores und Fallzahlen pro Jahr", font=dict(color=colors["text"]))
layout["margin"] = dict(b=80, t=120, l=60, r=100)
layout["xaxis"] = layout.get("xaxis", {})
layout["xaxis"]["automargin"] = True
layout["autosize"] = True
layout["legend"] = dict(
    x=1.1,
    y=1.0,
    xanchor="left",
    yanchor="top",
    orientation="v",
    traceorder="normal",
    itemclick="toggleothers",
    itemdoubleclick="toggle"
)
layout["yaxis3"] = dict(
    title="Abweichung (ΔSCₙ)",
    overlaying="y",
    side="right",
    showgrid=False,
    zeroline=True,
    zerolinewidth=2,
    zerolinecolor='grey',
    titlefont=dict(color=colors["text"]),
    tickfont=dict(color=colors["text"]),
    anchor="free",
    position=1.0
)
fig.update_layout(**layout)

# --- Export-Funktion ---
def export_figure(fig, name, export_flag_html, export_flag_png):
    from slugify import slugify
    safe_name = slugify(name)
    html_path = f"/tmp/{safe_name}.html"
    if export_flag_html:
        fig.write_html(html_path, include_plotlyjs='cdn', config={"responsive": True})
        try:
            subprocess.run(["scp", html_path, export_path_html], check=True)
            print(f"✅ HTML-Datei '{html_path}' erfolgreich übertragen.")
            os.remove(html_path)
            print(f"🗑️ Lokale HTML-Datei '{html_path}' wurde gelöscht.")
        except subprocess.CalledProcessError as e:
            print("❌ Fehler beim HTML-Übertragen:")
            print(e.stderr)
    if export_flag_png:
        png_path = os.path.join(export_path_png, f"{safe_name}.png")
        try:
            fig.write_image(png_path, scale=2)
            print(f"✅ PNG-Datei lokal gespeichert: '{png_path}'")
        except Exception as e:
            print("❌ Fehler beim PNG-Export:", str(e))

# --- Export ---
export_figure(fig, "silhouette_scores_und_fallzahlen", export_fig_silhouette_plot, export_fig_png)

fig.show()
