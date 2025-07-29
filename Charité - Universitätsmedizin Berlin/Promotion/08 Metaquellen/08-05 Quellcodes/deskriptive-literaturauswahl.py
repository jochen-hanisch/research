# ===============================
# Deskriptive Analyse: Silhouette-Scores & Fallzahlen
# ===============================

# --- System- und Modul-Imports ---
import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import date
from scipy.stats.mstats import winsorize
from scipy.stats import iqr

# --- CI-Template & Konfiguration ---
from ci_template.plotly_template import (
    get_standard_layout,
    get_colors,
    set_theme
)
from ci_template.plotly_template import export_figure
from config_deskriptive_literaturauswahl import theme, export_fig_visual
from config_deskriptive_literaturauswahl import export_fig_png, export_fig_silhouette_plot

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
    line=dict(color=colors["secondaryLine"], width=1),
    marker=dict(size=16, color=colors["secondaryLine"], symbol="square"),
    showlegend=True
))

# Quartile & Bezugslinien
fig.add_trace(go.Scatter(x=years, y=[q1]*len(years), mode='lines', name='SC Q1',
                         line=dict(dash='dot', color=colors["brightArea"]), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[q2]*len(years), mode='lines', name='SC Median (Q2)',
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
layout["margin"] = dict(b=80, t=120, l=60, r=60)
layout["xaxis"] = layout.get("xaxis", {})
layout["xaxis"]["automargin"] = True
layout["autosize"] = True
layout["legend"] = dict(
    x=1.05,
    y=1.0,
    xanchor="left",
    yanchor="top",
    orientation="v",
    traceorder="normal",
    itemclick="toggleothers",
    itemdoubleclick="toggle"
)
fig.update_layout(**layout)

# --- Export ---
export_figure(fig, "silhouette_scores_und_fallzahlen", export_fig_silhouette_plot, export_fig_png)

# (Hinweis: Balkenfarbe wird direkt im Bar-Trace gesetzt)

fig.show(config={"responsive": True})
