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

# --- CI-Template & Konfiguration ---
from ci_template.plotly_template import (
    get_standard_layout,
    get_colors,
    set_theme
)
from ci_template.plotly_template import export_figure
from config_deskriptive_literaturauswahl import theme, export_fig_visual

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
q1 = np.percentile(sc_values, 25)
q2 = np.percentile(sc_values, 50)
q3 = np.percentile(sc_values, 75)
max_value = np.max(sc_values)
min_value = np.min(sc_values)

sc_winsorized = winsorize(sc_values, limits=[0.1, 0.1])
median_winsorized = np.median(sc_winsorized)

fatigue_threshold = 0.96
circadian_optimum = 0.99

# --- Visualisierung ---
fig = go.Figure()

# SC-Linie
fig.add_trace(go.Scatter(x=years, y=sc_values, name='Silhouette-Scores',
                         mode='lines+markers', yaxis='y1'))

# n-Balken
fig.add_trace(go.Bar(x=years, y=n_values, name='n-Werte (Fallzahlen)',
                     yaxis='y2', opacity=0.3, marker_color=colors["depthArea"]))

# Quartile & Bezugslinien
fig.add_trace(go.Scatter(x=years, y=[q1]*len(years), mode='lines', name=f'SC Q1 = {q1:.4f}',
                         line=dict(dash='dot', color='green'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[q2]*len(years), mode='lines', name=f'SC Median (Q2) = {q2:.4f}',
                         line=dict(dash='dot', color='blue'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[q3]*len(years), mode='lines', name=f'SC Q3 = {q3:.4f}',
                         line=dict(dash='dot', color='purple'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[min_value]*len(years), mode='lines', name=f'SC Min = {min_value:.4f}',
                         line=dict(dash='dash', color='red'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[max_value]*len(years), mode='lines', name=f'SC Max = {max_value:.4f}',
                         line=dict(dash='dash', color='orange'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[fatigue_threshold]*len(years), mode='lines',
                         name=f'Schwelle: Erschöpfungs-Bias = {fatigue_threshold:.4f}',
                         line=dict(dash='dashdot', color='firebrick'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[circadian_optimum]*len(years), mode='lines',
                         name=f'Idealer Wert (circadian) = {circadian_optimum:.4f}',
                         line=dict(dash='dashdot', color='darkcyan'), yaxis='y1'))
fig.add_trace(go.Scatter(x=years, y=[median_winsorized]*len(years), mode='lines',
                         name=f'Winsorisierter Median = {median_winsorized:.4f}',
                         line=dict(dash='dot', color='black'), yaxis='y1'))

# Layout
fig.update_layout(
    **get_standard_layout(
        title=f"Silhouette-Scores und Fallzahlen (n={sum(n_values)}, Stand: {current_date})",
        x_title="Jahr",
        y_title="Silhouette-Score",
        yaxis2=dict(
            title="Fallzahlen (n)",
            showgrid=False
        )
    )
)

# Anzeige
fig.show(config={"responsive": True})

# --- Export ---
export_figure(fig, "silhouette_scores_und_fallzahlen", export_fig_silhouette_plot, export_fig_png)
