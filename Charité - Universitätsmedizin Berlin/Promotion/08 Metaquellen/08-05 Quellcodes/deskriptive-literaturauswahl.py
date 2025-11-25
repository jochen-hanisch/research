# ===============================
# Deskriptive Analyse: Silhouette-Scores & Fallzahlen
# ===============================

# --- System- und Modul-Imports ---
import os
import sys
from pathlib import Path
import numpy as np
import plotly.graph_objects as go
from datetime import date
from scipy.stats.mstats import winsorize
from scipy.stats import iqr
import subprocess
import pandas as pd
import bibtexparser
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

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
    export_path_png,
    bib_filename
)

# --- Initialisierung ---
os.system('cls' if os.name == 'nt' else 'clear')
set_theme(theme, preserve_effects=True)
colors = get_colors()
current_date = date.today().isoformat()

# --- Datenbasis aus der gewählten Bib-Datei ---
BASE_DIR = Path(__file__).resolve().parent
BIB_PATH = BASE_DIR / "Bibliothek" / bib_filename

if not BIB_PATH.exists():
    print(f"❌ Bib-Datei nicht gefunden: {BIB_PATH}")
    sys.exit(1)

tags_to_search = [
    '#0:Zeitschriftenartikel:digital:learning',
    '#0:Buch:digital:learning',
    '#0:Buchteil:digital:learning',
    '#0:Konferenz-Paper:digital:learning',
    '#1:Zeitschriftenartikel:learning:management:system',
    '#1:Buch:learning:management:system',
    '#1:Buchteil:learning:management:system',
    '#1:Konferenz-Paper:learning:management:system',
    '#2:Zeitschriftenartikel:online:Lernplattform',
    '#2:Buch:online:Lernplattform',
    '#2:Buchteil:online:Lernplattform',
    '#2:Konferenz-Paper:online:Lernplattform',
    '#3:Zeitschriftenartikel:online:Lernumgebung',
    '#3:Buch:online:Lernumgebung',
    '#3:Buchteil:online:Lernumgebung',
    '#3:Konferenz-Paper:online:Lernumgebung',
    '#4:Zeitschriftenartikel:MOOC',
    '#4:Buch:MOOC',
    '#4:Buchteil:MOOC',
    '#4:Konferenz-Paper:MOOC',
    '#5:Zeitschriftenartikel:e-learning',
    '#5:Buch:e-learning',
    '#5:Buchteil:e-learning',
    '#5:Konferenz-Paper:e-learning',
    '#6:Zeitschriftenartikel:Bildung:Technologie',
    '#6:Buch:Bildung:Technologie',
    '#6:Buchteil:Bildung:Technologie',
    '#6:Konferenz-Paper:Bildung:Technologie',
    '#7:Zeitschriftenartikel:digital:Medien',
    '#7:Buch:digital:Medien',
    '#7:Buchteil:digital:Medien',
    '#7:Konferenz-Paper:digital:Medien',
    '#8:Zeitschriftenartikel:blended:learning',
    '#8:Buch:blended:learning',
    '#8:Buchteil:blended:learning',
    '#8:Konferenz-Paper:blended:learning',
    '#9:Zeitschriftenartikel:digital:lernen',
    '#9:Buch:digital:lernen',
    '#9:Buchteil:digital:lernen',
    '#9:Konferenz-Paper:digital:lernen',
    '#a:Zeitschriftenartikel:online:lernen',
    '#a:Buch:online:lernen',
    '#a:Buchteil:online:lernen',
    '#a:Konferenz-Paper:online:lernen',
    '#b:Zeitschriftenartikel:online:learning',
    '#b:Buch:online:learning',
    '#b:Buchteil:online:learning',
    '#b:Konferenz-Paper:online:learning'
]
tags_to_search_processed = [tag.lower().replace('\\#', '#').strip() for tag in tags_to_search]

index_terms = [
    'Lernsystemarchitektur',
    'Bildungstheorien',
    'Lehr- und Lerneffektivität',
    'Kollaboratives Lernen',
    'Bewertungsmethoden',
    'Technologieintegration',
    'Datenschutz und IT-Sicherheit',
    'Systemanpassung',
    'Krisenreaktion im Bildungsbereich',
    'Forschungsansätze'
]
index_terms_processed = [term.lower().strip() for term in index_terms]

research_questions = {
    'promotion:fu1': 'Akzeptanz und Nützlichkeit (FU1)',
    'promotion:fu2a': 'Effekt für Lernende (FU2a)',
    'promotion:fu2b': 'Effekt-Faktoren für Lehrende (FU2b)',
    'promotion:fu3': 'Konzeption und Merkmale (FU3)',
    'promotion:fu4a': 'Bildungswissenschaftliche Mechanismen (FU4a)',
    'promotion:fu4b': 'Technisch-gestalterische Mechanismen (FU4b)',
    'promotion:fu5': 'Möglichkeiten und Grenzen (FU5)',
    'promotion:fu6': 'Beurteilung als Kompetenzerwerbssystem (FU6)',
    'promotion:fu7': 'Inputs und Strategien (FU7)'
}
research_questions_processed = list(research_questions.keys())

categories = {
    'promotion:argumentation': 'Argumentation',
    'promotion:kerngedanke': 'Kerngedanke',
    'promotion:weiterführung': 'Weiterführung',
    'promotion:schlussfolgerung': 'Schlussfolgerung'
}
categories_processed = list(categories.keys())

feature_columns = (
    tags_to_search_processed
    + index_terms_processed
    + research_questions_processed
    + categories_processed
)


def load_entries():
    with open(BIB_PATH, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    rows = []
    for entry in bib_database.entries:
        keywords_raw = entry.get("keywords")
        year_raw = entry.get("year")
        if not keywords_raw or not year_raw:
            continue
        try:
            year = int(str(year_raw)[:4])
        except ValueError:
            continue
        entry_keywords = set(
            map(str.lower, map(str.strip, keywords_raw.replace("\\#", "#").split(",")))
        )
        row = {"year": year}
        row.update({tag: int(tag in entry_keywords) for tag in tags_to_search_processed})
        row.update({index: int(index in entry_keywords) for index in index_terms_processed})
        row.update({rq: int(rq in entry_keywords) for rq in research_questions_processed})
        row.update({cat: int(cat in entry_keywords) for cat in categories_processed})
        rows.append(row)
    df = pd.DataFrame(rows)
    if df.empty:
        print(f"⚠️ Keine gültigen Einträge mit Jahr/Keywords in {bib_filename} gefunden.")
    return df


def compute_silhouette_per_year(df_features):
    years = []
    sc_values = []
    n_values = []
    for year, group in df_features.groupby("year"):
        n = len(group)
        n_values.append(n)
        years.append(year)
        if n < 2:
            sc_values.append(np.nan)
            continue
        X = group[feature_columns]
        if X.nunique().sum() == 0:
            sc_values.append(np.nan)
            continue
        try:
            scaler = StandardScaler()
            scaled = scaler.fit_transform(X)
            k = min(4, n)
            if k < 2:
                sc_values.append(np.nan)
                continue
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = kmeans.fit_predict(scaled)
            if len(set(labels)) < 2:
                sc_values.append(np.nan)
                continue
            score = silhouette_score(scaled, labels)
            sc_values.append(score)
        except Exception as e:
            print(f"⚠️ Silhouette für Jahr {year} übersprungen ({e})")
            sc_values.append(np.nan)
    years_arr = np.array(years, dtype=int)
    sc_arr = np.array(sc_values, dtype=float)
    n_arr = np.array(n_values, dtype=int)
    sort_idx = np.argsort(years_arr)
    return years_arr[sort_idx], sc_arr[sort_idx], n_arr[sort_idx]


df_features = load_entries()
if df_features.empty:
    sys.exit(0)

years, sc_values, n_values = compute_silhouette_per_year(df_features)

# Nur Jahre mit gültigen Silhouette-Scores verwenden
valid_mask = ~np.isnan(sc_values)
years = years[valid_mask]
sc_values = sc_values[valid_mask]
n_values = n_values[valid_mask]

if len(years) == 0:
    print("⚠️ Keine ausreichenden Daten für Silhouette-Scores vorhanden.")
    sys.exit(0)

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
delta_std = np.std(delta_raw)
delta_z = (delta_raw - np.mean(delta_raw)) / delta_std if delta_std > 0 else np.zeros_like(delta_raw)

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
    title=dict(text="Abweichung (ΔSCₙ)", font=dict(color=colors["text"])),
    overlaying="y",
    side="right",
    showgrid=False,
    zeroline=True,
    zerolinewidth=2,
    zerolinecolor='grey',
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
