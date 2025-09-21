
import os

# Neue Exportfunktion: HTML in /tmp speichern, per SCP übertragen, PNG lokal speichern
def export_figure(fig, name, export_flag_html, export_flag_png):
    # Lokale Implementierung der Exportlogik inkl. Bib-Quelle im Titel und Dateinamen
    from config_korrelation import export_path_png, bib_filename
    from slugify import slugify
    remote_path = "johajo@sternenflottenakademie.local:/mnt/deep-space-nine/public/plot/promotion/"

    # Titel ggf. um Quelle ergänzen
    if fig.layout.title and fig.layout.title.text:
        if f"| Quelle: {bib_filename.replace('.bib', '')}" not in fig.layout.title.text:
            fig.update_layout(title_text=f"{fig.layout.title.text} | Quelle: {bib_filename.replace('.bib', '')}")

    safe_filename = slugify(f"{name}_{bib_filename.replace('.bib', '')}")

    if export_flag_html:
        export_path_html = f"/tmp/{safe_filename}.html"
        fig.write_html(export_path_html, full_html=True, include_plotlyjs="cdn")
        try:
            subprocess.run(["scp", export_path_html, remote_path], check=True)
            print(f"✅ HTML-Datei '{export_path_html}' erfolgreich übertragen.")
            os.remove(export_path_html)
            print(f"🗑️ Lokale HTML-Datei '{export_path_html}' wurde gelöscht.")
        except subprocess.CalledProcessError as e:
            print("❌ Fehler beim HTML-Übertragen:")
            print(e.stderr)

    if export_flag_png:
        export_path_png_full = os.path.join(export_path_png, f"{safe_filename}.png")
        try:
            fig.write_image(export_path_png_full, width=1200, height=800, scale=2)
            print(f"✅ PNG-Datei lokal gespeichert: '{export_path_png_full}'")
        except Exception as e:
            print("❌ Fehler beim PNG-Export:", str(e))

# Import theme and all export_fig_... variables from central config before any use
from config_korrelation import (
    theme,
    export_fig_visual,
    export_fig_png,
    export_fig_clusteranalyse,
    export_fig_correlation_suchbegriffe_kategorien,
    export_fig_correlation_fu_kategorien,
    export_fig_correlation_fu_suchbegriffe,
    export_fig_correlation_indizes_kategorien,
    export_fig_correlation_indizes_suchbegriffe,
    export_fig_correlation_fu_indizes,
    export_fig_correlation_fu_fu,
    export_fig_correlation_suchbegriffe_suchbegriffe,
    export_fig_correlation_kategorien_kategorien,
    export_fig_correlation_indizes_indizes,
    export_fig_summary_plot,
    bib_filename,
    export_path_html
)

# Terminal leeren
os.system('cls' if os.name == 'nt' else 'clear')

from ci_template import plotly_template
from datetime import datetime
import bibtexparser
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

import subprocess
from slugify import slugify

# Machine Learning Tools
from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score

# Visualization
import plotly.express as px
import matplotlib.pyplot as plt

# Debugging and Output
from tabulate import tabulate

# Universelle Hilfsfunktion für Export und Titelmanipulation
def prepare_figure_export(fig, name):
    # Titel ergänzen
    if fig.layout.title and fig.layout.title.text:
        if f"| Quelle: {bib_filename.replace('.bib', '')}" not in fig.layout.title.text:
            fig.update_layout(title_text=f"{fig.layout.title.text} | Quelle: {bib_filename.replace('.bib', '')}")
    # Dateiname generieren
    safe_filename = slugify(f"{name}_{bib_filename.replace('.bib', '')}")
    return f"{safe_filename}.html"

def export_and_transfer_figure(fig, function_name, export_flag):
    export_figure(
        fig,
        function_name,
        export_flag,
        export_fig_png
    )
    fig.show()

# BibTeX-Datei laden
bib_path = os.path.join("Research", "Charité - Universitätsmedizin Berlin", "Systematische Literaturrecherche", "Bibliothek", bib_filename)
with open(bib_path, encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Template aktivieren und Farben/Styles setzen
plotly_template.set_theme(theme)
from ci_template.plotly_template import get_colors, get_plot_styles, get_standard_layout
colors = get_colors()
plot_styles = get_plot_styles()

# Aktuelles Datum
current_date = datetime.now().strftime("%Y-%m-%d")

# Suchbegriffe
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

# Indizes
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

# Forschungsunterfragen
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

# Kategorien
categories = {
    'promotion:argumentation': 'Argumentation',
    'promotion:kerngedanke': 'Kerngedanke',
    'promotion:weiterführung': 'Weiterführung',
    'promotion:schlussfolgerung': 'Schlussfolgerung'
}
categories_processed = list(categories.keys())

# Daten sammeln
data = []

# Verarbeiten der Einträge aus der BibTeX-Datenbank
for entry in bib_database.entries:
    if 'keywords' in entry:
        # Extrahieren und Verarbeiten der Schlagwörter
        entry_keywords = set(map(str.lower, map(str.strip, entry['keywords'].replace('\\#', '#').split(','))))
        row = {}

        # Zuordnung der Schlagwörter zu Tags
        row.update({tag: int(tag in entry_keywords) for tag in tags_to_search_processed})

        # Zuordnung der Schlagwörter zu Index-Begriffen
        row.update({index: int(index in entry_keywords) for index in index_terms_processed})

        # Zuordnung der Schlagwörter zu Forschungsfragen
        row.update({rq: int(rq in entry_keywords) for rq in research_questions_processed})

        # Zuordnung der Schlagwörter zu Kategorien
        row.update({cat: int(cat in entry_keywords) for cat in categories_processed})

        # Titel des Eintrags hinzufügen
        row['title'] = entry.get('title', 'No Title')

        # Zeile zur Datenliste hinzufügen
        data.append(row)


# Daten in ein DataFrame umwandeln
df = pd.DataFrame(data).fillna(0).set_index('title')

# Debugging: Zeige die ersten Zeilen des DataFrames
print("Erste Zeilen des DataFrames:")
print(df.head())

# Funktion zur Berechnung und Visualisierung bivariater Korrelationen mit Interpretation
def interpret_correlation(x_term, y_term, correlation, min_corr, max_corr):
    if min_corr == max_corr:
        return "Keine Variation"
    third = (max_corr - min_corr) / 3
    if correlation > min_corr + 2 * third:
        return "Stark verbunden"
    elif correlation > min_corr + third:
        return "Schwach verbunden"
    else:
        return "Negativ verbunden"

def visualize_bivariate_correlation(df, x_terms, y_terms, title, x_label, y_label, export_flag):
    """
    Visualisiert bivariate Korrelationen und zeigt Interpretationen sowie Signifikanz im Tooltip an.

    Args:
        df (DataFrame): Der DataFrame mit den Daten.
        x_terms (list): Liste der Variablen für die x-Achse.
        y_terms (list): Liste der Variablen für die y-Achse.
        title (str): Titel der Visualisierung.
        x_label (str): Beschriftung der x-Achse.
        y_label (str): Beschriftung der y-Achse.
    """
    correlations = []
    for x_term in x_terms:
        for y_term in y_terms:
            if x_term != y_term and x_term in df.columns and y_term in df.columns:
                # Daten für x und y extrahieren
                x_data = df[x_term]
                y_data = df[y_term]

                # Robuster Prüf- und Berechnungsblock für Korrelation und Signifikanz (p-Wert)
                if len(x_data) > 1 and len(y_data) > 1:
                    x_data = pd.to_numeric(x_data, errors='coerce')
                    y_data = pd.to_numeric(y_data, errors='coerce')
                    valid = x_data.notna() & y_data.notna()
                    x_valid, y_valid = x_data[valid], y_data[valid]

                    if x_valid.nunique() > 1 and y_valid.nunique() > 1:
                        corr, p_value = pearsonr(x_valid, y_valid)
                        if pd.notnull(corr):
                            abs_corr = abs(corr)
                            significance = 'Signifikant' if p_value < 0.05 else 'Nicht signifikant'
                            hover_color = colors['brightArea'] if p_value < 0.05 else colors['depthArea']
                            correlations.append({
                                'x_term': x_term,
                                'y_term': y_term,
                                'correlation': corr,
                                'abs_correlation': abs_corr,
                                'p_value': p_value,
                                'significance': significance,
                                'hover_color': hover_color,
                                'interpretation': (
                                    f"Die Korrelation zwischen '{x_term}' und '{y_term}' beträgt {corr:.2f}. "
                                    f"p-Wert: {p_value:.3e} ({significance})"
                                )
                            })

    correlation_df = pd.DataFrame(correlations)
    if correlation_df.empty:
        print(f"⚠️ Keine exportierbare Visualisierung für: {title} – DataFrame ist leer.")
        return

    # Berechnung des min und max Korrelationswerts
    min_corr = correlation_df['correlation'].min()
    max_corr = correlation_df['correlation'].max()

    # Sicherstellen, dass 0 innerhalb des Bereichs von min_corr und max_corr liegt
    if min_corr > 0:
        min_corr = 0
    if max_corr < 0:
        max_corr = 0

    # Berechnung des zero_position
    zero_position = (0 - min_corr) / (max_corr - min_corr)

    # Dynamische Farbskala, die sicherstellt, dass 0 immer weiß ist
    color_scale = [
        [0.0, colors['negativeHighlight']],  # Start bei min_corr
        [zero_position, colors['white']],    # Weiß bei 0
        [1.0, colors['positiveHighlight']]   # Ende bei max_corr
    ]

    # Tabelle im Terminal ausgeben
    print(f"Korrelationen für: {title}")
    print(tabulate(correlation_df[['x_term', 'y_term', 'correlation', 'p_value', 'significance']],
                   headers=['Variable X', 'Variable Y', 'Korrelation', 'p-Wert', 'Signifikanz'],
                   tablefmt='grid'))

    # Export als CSV-Datei
    csv_filename = f"Research/Charité - Universitätsmedizin Berlin/Systematische Literaturrecherche/Tabellen/correlations_{title.replace(' ', '_')}.csv"
    correlation_df[['x_term', 'y_term', 'correlation', 'p_value', 'significance']].to_csv(csv_filename, index=False)
    print(f"Die Ergebnisse wurden als CSV-Datei gespeichert: {csv_filename}")

    # Visualisierung
    fig = px.scatter(
        correlation_df,
        x='x_term',
        y='y_term',
        size='abs_correlation',
        color='correlation',
        hover_data={
            'correlation': True,
            'p_value': True,
            'significance': True,
            'interpretation': True,  # Interpretation im Tooltip anzeigen
        },
        title=f'{title} (n={len(correlation_df)}, Stand: {current_date}) | Quelle: {bib_filename.replace(".bib", "")}',
        labels={'x_term': x_label, 'y_term': y_label, 'correlation': 'Korrelation'},
        color_continuous_scale=color_scale  # Dynamische Farbskala
    )

    fig.update_traces(
        marker=dict(
            line=dict(width=1, color=colors['background'])
        ),
        hovertemplate=(
            '<b>%{customdata[0]}</b><br>'
            'Korrelation: %{marker.color:.2f}<br>'
            'p-Wert: %{customdata[1]:.3e}<br>'
            'Signifikanz: %{customdata[2]}'
        ),
        customdata=correlation_df[['x_term', 'p_value', 'significance']].to_numpy()
    )

    # Standardlayout verwenden und ggf. ergänzen, Margin dynamisch für Responsivität
    fig.update_layout(
        get_standard_layout(
            title=f'{title} (n={len(correlation_df)}, Stand: {current_date}) | Quelle: {bib_filename.replace(".bib", "")}',
            x_title=x_label,
            y_title=y_label
        ),
        xaxis=dict(
            tickangle=-45,
            automargin=True
        ),  # Einheitlicher Winkel für X-Achsenbeschriftungen
        yaxis=dict(
            automargin=True
        ),
        coloraxis_colorbar=dict(title='Korrelationswert'),
        autosize=True,
        margin=dict(l=0, r=0, t=60, b=60),
        height=None,
        width=None
    )
    export_and_transfer_figure(
        fig,
        title.replace(" ", "_"),
        export_flag
    )

# --- Einzelne Visualisierungsfunktionen für jede bivariate Korrelation ---
def visualize_suchbegriffe_vs_kategorien(export_flag):
    visualize_bivariate_correlation(
        df, tags_to_search_processed, categories_processed,
        'Korrelation zwischen Suchbegriffen und Kategorien',
        'Suchbegriffe', 'Kategorien',
        export_flag
    )

def visualize_forschungsunterfragen_vs_kategorien(export_flag):
    visualize_bivariate_correlation(
        df, research_questions_processed, categories_processed,
        'Korrelation zwischen Forschungsunterfragen und Kategorien',
        'Forschungsunterfragen', 'Kategorien',
        export_flag
    )

def visualize_forschungsunterfragen_vs_suchbegriffe(export_flag):
    visualize_bivariate_correlation(
        df, research_questions_processed, tags_to_search_processed,
        'Korrelation zwischen Forschungsunterfragen und Suchbegriffen',
        'Forschungsunterfragen', 'Suchbegriffe',
        export_flag
    )

def visualize_indizes_vs_kategorien(export_flag):
    visualize_bivariate_correlation(
        df, index_terms_processed, categories_processed,
        'Korrelation zwischen Indizes und Kategorien',
        'Indizes', 'Kategorien',
        export_flag
    )

def visualize_indizes_vs_suchbegriffe(export_flag):
    visualize_bivariate_correlation(
        df, index_terms_processed, tags_to_search_processed,
        'Korrelation zwischen Indizes und Suchbegriffen',
        'Indizes', 'Suchbegriffe',
        export_flag
    )

def visualize_forschungsunterfragen_vs_indizes(export_flag):
    visualize_bivariate_correlation(
        df, research_questions_processed, index_terms_processed,
        'Korrelation zwischen Forschungsunterfragen und Indizes',
        'Forschungsunterfragen', 'Indizes',
        export_flag
    )

def visualize_forschungsunterfragen_vs_forschungsunterfragen(export_flag):
    visualize_bivariate_correlation(
        df, research_questions_processed, research_questions_processed,
        'Korrelation zwischen Forschungsunterfragen',
        'Forschungsunterfragen', 'Forschungsunterfragen',
        export_flag
    )

def visualize_suchbegriffe_vs_suchbegriffe(export_flag):
    visualize_bivariate_correlation(
        df, tags_to_search_processed, tags_to_search_processed,
        'Korrelation zwischen Suchbegriffen',
        'Suchbegriffe', 'Suchbegriffe',
        export_flag
    )

def visualize_kategorien_vs_kategorien(export_flag):
    visualize_bivariate_correlation(
        df, categories_processed, categories_processed,
        'Korrelation zwischen Kategorien',
        'Kategorien', 'Kategorien',
        export_flag
    )

def visualize_indizes_vs_indizes(export_flag):
    visualize_bivariate_correlation(
        df, index_terms_processed, index_terms_processed,
        'Korrelation zwischen Indizes',
        'Indizes', 'Indizes',
        export_flag
    )

#======================================

cluster_colors = {
    "0": colors['primaryLine'],    # Cluster 0
    "1": colors['secondaryLine'],  # Cluster 1
    "2": colors['depthArea'],      # Cluster 2
    "3": colors['brightArea']      # Cluster 3
}

# Vorbereitung: Positionierung entlang deduktiver Dimensionen
df['X_Dimension'] = df[[tag for tag in tags_to_search_processed if tag in df.columns]].sum(axis=1)
df['Y_Dimension'] = df[[cat for cat in categories_processed if cat in df.columns]].sum(axis=1)
df['Z_Dimension'] = df[[rq for rq in research_questions_processed if rq in df.columns]].sum(axis=1)

# Clusteranalyse mit K-Means basierend auf den deduktiven Dimensionen
# Prüfung auf konstante deduktive Dimensionen
if df[['X_Dimension', 'Y_Dimension', 'Z_Dimension']].nunique().eq(1).all():
    print("⚠️ Alle deduktiven Dimensionen sind konstant. K-Means-Clustering wird übersprungen.")
    df['KMeans_Cluster'] = 'Nicht gültig'
    silhouette_avg = None
else:
    try:
        features = df[['X_Dimension', 'Y_Dimension', 'Z_Dimension']]
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        # Prüfen, ob genügend Datenpunkte für das Clustering vorliegen
        if len(features) < 2:
            raise ValueError("Zu wenige Datenpunkte für die Clusteranalyse. Mindestens zwei Punkte erforderlich.")

        # K-Means ausführen
        kmeans = KMeans(n_clusters=4, random_state=42)
        df['KMeans_Cluster'] = kmeans.fit_predict(scaled_features)

        # Cluster als Strings umwandeln (kategorisch)
        df['KMeans_Cluster'] = df['KMeans_Cluster'].astype(str)

        # Dynamische Punktgröße basierend auf Wertigkeit (Summen der Dimensionen), mit klarer Klammerung und Skalierung
        df['Point_Size'] = (df['X_Dimension'] + df['Y_Dimension'] + df['Z_Dimension']) * 100

        # Statistik der Punktgröße ausgeben
        print("Statistik der Punktgrößen:")
        print(df['Point_Size'].describe())

        # Silhouette-Analyse zur Bewertung der Clusterqualität
        silhouette_avg = silhouette_score(scaled_features, df['KMeans_Cluster'].astype(int))
        print(f"Silhouette-Score: {silhouette_avg:.4f}")

        # Speichern der Clusterdaten als CSV-Datei
        output_path = "Research/Charité - Universitätsmedizin Berlin/Systematische Literaturrecherche/Tabellen/cluster_data.csv"
        df.to_csv(output_path, index=False)
        print(f"Clusterdaten wurden als CSV gespeichert: {output_path}")

    except ValueError as e:
        # Fehler aufgrund unsauberer Daten
        print(f"Fehler bei der Clusteranalyse: {e}")
        print("Bitte überprüfen Sie die Eingabedaten. Die Clusteranalyse konnte nicht durchgeführt werden.")
        # Optionale Handlung, z.B. einen Default-Wert setzen oder den Prozess erneut starten
        df['KMeans_Cluster'] = 'Nicht gültig'
        silhouette_avg = None
    except Exception as e:
        # Allgemeiner Fehler
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        df['KMeans_Cluster'] = 'Fehler'
        silhouette_avg = None

num_clusters = df['KMeans_Cluster'].nunique() if 'KMeans_Cluster' in df.columns else 0
plot_title = f"3D-deduktiv-statistische Clusteranalyse (K-Means) (n={len(df)}, Cluster={num_clusters})"
if silhouette_avg is not None:
    plot_title += f" | Silhouette-Score: {silhouette_avg:.4f}"

# Relevante Spalten für die Clusterbeschreibung
relevant_columns = tags_to_search_processed + index_terms_processed + research_questions_processed + list(categories.keys())

# Cluster-Beschriftungen basierend auf den Top-Merkmalen mit Umbrüchen
cluster_means = df[relevant_columns + ['KMeans_Cluster']].groupby('KMeans_Cluster').mean()
cluster_labels = {}
for cluster in cluster_means.index:
    # Sortiere relevante Spalten nach höchsten Mittelwerten
    top_features = cluster_means.loc[cluster].sort_values(ascending=False).head(3)
    # Erstelle die Beschriftung mit HTML-Zeilenumbrüchen
    label = "<br>".join([col for col in top_features.index])  # Zeilenumbrüche einfügen
    cluster_labels[str(cluster)] = label

# Statische Cluster-Beschriftungen in den DataFrame einfügen
df['Cluster_Label'] = df['KMeans_Cluster'].map(cluster_labels)
df['Cluster_Label'] = df['Cluster_Label'].fillna(df['KMeans_Cluster'])

# Farbzuordnung für die Clusterlabels aus den CI-Farben ableiten
fallback_color = cluster_colors.get("0", colors.get('primaryLine', '#1f77b4'))
color_map = {}
for cluster_key, label in cluster_labels.items():
    base_color = cluster_colors.get(str(cluster_key), fallback_color)
    color_map[label] = base_color

# Sicherstellen, dass auch eventuelle Restlabels (z.B. "Nicht gültig") erfasst werden
for label in df['Cluster_Label'].dropna().unique():
    if label not in color_map:
        color_map[label] = cluster_colors.get(str(label), fallback_color)

# Ausgabe der statischen Cluster-Beschriftungen
print("Cluster-Beschriftungen (inhaltlich):")
for cluster, label in cluster_labels.items():
    print(f"Cluster {cluster}: {label.replace('<br>', ', ')}")  # Umbrüche für die Ausgabe ersetzen

# Plotly 3D-Scatter-Plot mit deduktiven Dimensionen und dynamischer Punktgröße
plot_title += f" | Quelle: {bib_filename.replace('.bib', '')}"
fig_cluster = px.scatter_3d(
    df,
    x='X_Dimension',
    y='Y_Dimension',
    z='Z_Dimension',
    color='Cluster_Label',
    size='Point_Size',
    size_max=100,
    color_discrete_map=color_map,
    hover_data={
        'Cluster_Label': True,
        'X_Dimension': True,
        'Y_Dimension': True,
        'Z_Dimension': True,
        'Point_Size': True
    },
    title=plot_title,
    labels={
        'X_Dimension': 'Suchbegriffe',
        'Y_Dimension': 'Kategorien',
        'Z_Dimension': 'Forschungsfragen',
        'Point_Size': 'Punktgröße',
        'Cluster_Label': 'Cluster-Beschreibung'
    }
)


# Layout mit Standardlayout und konsistenten CI-konformen Ergänzungen
layout_cluster = get_standard_layout(
    title=plot_title,
    x_title='Suchbegriffe',
    y_title='Kategorien',
    z_title='Forschungsfragen'
)
fig_cluster.update_layout(**layout_cluster)

export_and_transfer_figure(
    fig_cluster,
    "clusteranalyse_kmeans_deduktiv",
    export_fig_clusteranalyse
)

# Berechnung der Korrelationen und Erstellung der Übersicht

def analyze_correlation_quality(df, x_terms, y_terms):
    """
    Berechnet die Signifikanz und Qualität der Korrelationen zwischen zwei Gruppen von Variablen.
    
    Args:
        df (DataFrame): Der DataFrame mit den Daten.
        x_terms (list): Liste der Variablen für die x-Achse.
        y_terms (list): Liste der Variablen für die y-Achse.
        
    Returns:
        dict: Eine strukturierte Zusammenfassung der Korrelationsergebnisse.
    """
    correlation_data = []
    
    for x_term in x_terms:
        for y_term in y_terms:
            if x_term != y_term and x_term in df.columns and y_term in df.columns:
                x_data = df[x_term]
                y_data = df[y_term]

                if len(x_data) > 1 and len(y_data) > 1:
                    x_data = pd.to_numeric(x_data, errors='coerce')
                    y_data = pd.to_numeric(y_data, errors='coerce')
                    valid = x_data.notna() & y_data.notna()
                    x_valid, y_valid = x_data[valid], y_data[valid]

                    if x_valid.nunique() > 1 and y_valid.nunique() > 1:
                        corr, p_value = pearsonr(x_valid, y_valid)
                        if pd.notnull(corr):
                            correlation_data.append({
                                "x_term": x_term,
                                "y_term": y_term,
                                "correlation": corr,
                                "p_value": p_value
                            })

    correlation_df = pd.DataFrame(correlation_data)
    
    if correlation_df.empty:
        print("Keine signifikanten Korrelationen gefunden.")
        return {}

    # Berechnung von Metriken
    significant_count = correlation_df[correlation_df["p_value"] < 0.05].shape[0]
    highly_significant_count = correlation_df[correlation_df["p_value"] < 0.01].shape[0]
    very_highly_significant_count = correlation_df[correlation_df["p_value"] < 0.001].shape[0]
    total_count = correlation_df.shape[0]

    correlation_quality_results = {
        "total_count": total_count,
        "significant_count": significant_count,
        "highly_significant_count": highly_significant_count,
        "very_highly_significant_count": very_highly_significant_count,
        "significant_ratio": significant_count / total_count if total_count > 0 else 0,
        "highly_significant_ratio": highly_significant_count / total_count if total_count > 0 else 0,
        "very_highly_significant_ratio": very_highly_significant_count / total_count if total_count > 0 else 0,
        "avg_correlation": correlation_df["correlation"].mean(),
        "non_significant_ratio": (total_count - significant_count) / total_count if total_count > 0 else 0,
    }

    return correlation_quality_results

# Berechnung für verschiedene Korrelationstypen
correlation_quality_results = {
    "Forschungsunterfragen & Kategorien": analyze_correlation_quality(df, research_questions_processed, categories_processed),
    "Forschungsunterfragen & Suchbegriffe": analyze_correlation_quality(df, research_questions_processed, tags_to_search_processed),
    "Forschungsunterfragen & Indizes": analyze_correlation_quality(df, research_questions_processed, index_terms_processed),
    "Indizes & Kategorien": analyze_correlation_quality(df, index_terms_processed, categories_processed),
    "Indizes & Suchbegriffe": analyze_correlation_quality(df, index_terms_processed, tags_to_search_processed),
    "Suchbegriffe & Kategorien": analyze_correlation_quality(df, tags_to_search_processed, categories_processed),
    "Indizes & Indizes": analyze_correlation_quality(df, index_terms_processed, index_terms_processed),
    "Suchbegriffe & Suchbegriffe": analyze_correlation_quality(df, tags_to_search_processed, tags_to_search_processed),
    "Kategorien & Kategorien": analyze_correlation_quality(df, categories_processed, categories_processed),
}

# Entferne leere Einträge aus dem Dictionary
correlation_quality_results = {k: v for k, v in correlation_quality_results.items() if v}

summary_df = pd.DataFrame({
    "Korrelationstyp": correlation_quality_results.keys(),
    "Gesamtanzahl": [res["total_count"] for res in correlation_quality_results.values()],
    "Signifikante Korrelationen (%)": [res["significant_ratio"] * 100 for res in correlation_quality_results.values()],
    "Hoch signifikante Korrelationen (%)": [res["highly_significant_ratio"] * 100 for res in correlation_quality_results.values()],
    "Sehr hoch signifikante Korrelationen (%)": [res["very_highly_significant_ratio"] * 100 for res in correlation_quality_results.values()],
    "Durchschnittliche Korrelation": [res["avg_correlation"] for res in correlation_quality_results.values()],
    "Nicht signifikante Korrelationen (%)": [res["non_significant_ratio"] * 100 for res in correlation_quality_results.values()],
})

# Plotly-Version für interaktive Darstellung
def plot_average_correlation_plotly(summary_df):
    from config_korrelation import export_path_png
    from config_korrelation import bib_filename as global_bib_filename
    from slugify import slugify
    fig = px.bar(
        summary_df,
        x="Korrelationstyp",
        y="Durchschnittliche Korrelation",
        title=f"Durchschnittliche Korrelationen pro Korrelationstyp (n={len(summary_df)}, Stand: {current_date}) | Quelle: {global_bib_filename.replace('.bib', '')}",
        labels={"Korrelationstyp": "Korrelationstyp", "Durchschnittliche Korrelation": "Durchschnittliche Korrelation"},
        color="Durchschnittliche Korrelation",
        color_continuous_scale=[
            [0.0, colors['negativeHighlight']],
            [0.5, colors['white']],
            [1.0, colors['positiveHighlight']]
        ]
    )

    fig.update_layout(
        get_standard_layout(
            title=f"Durchschnittliche Korrelationen pro Korrelationstyp (n={len(summary_df)}, Stand: {current_date}) | Quelle: {global_bib_filename.replace('.bib', '')}",
            x_title="Korrelationstyp",
            y_title="Durchschnittliche Korrelation"
        ),
        xaxis=dict(
            tickangle=-45,
            automargin=True
        ),
        yaxis=dict(
            automargin=True
        ),
        coloraxis_colorbar=dict(title="Korrelationswert"),
        autosize=True,
        margin=dict(l=60, r=40, t=80, b=80),
        height=None,
        width=None
    )
    export_and_transfer_figure(
        fig,
        "summary_plot",
        export_fig_summary_plot
    )
    # PNG-Export ergänzen
    png_path = os.path.join(export_path_png, f"{slugify('summary_plot_' + global_bib_filename.replace('.bib', ''))}.png")
    try:
        fig.write_image(png_path, width=1200, height=800, scale=2)
        print(f"✅ PNG-Summary-Datei gespeichert unter: {png_path}")
    except ValueError as err:
        if "kaleido" in str(err).lower():
            print("⚠️ PNG-Export übersprungen: Plotly benötigt das Paket 'kaleido'.")
            print("   Installation (falls gewünscht): pip install -U kaleido")
        else:
            print(f"⚠️ PNG-Export fehlgeschlagen: {err}")
    except Exception as err:
        print(f"⚠️ PNG-Export fehlgeschlagen: {err}")

#============================
# Aufruf Alle möglichen bivariaten Korrelationen visualisieren

visualize_suchbegriffe_vs_kategorien(export_flag=export_fig_correlation_suchbegriffe_kategorien)
visualize_forschungsunterfragen_vs_kategorien(export_flag=export_fig_correlation_fu_kategorien)
visualize_forschungsunterfragen_vs_suchbegriffe(export_flag=export_fig_correlation_fu_suchbegriffe)
visualize_indizes_vs_kategorien(export_flag=export_fig_correlation_indizes_kategorien)
visualize_indizes_vs_suchbegriffe(export_flag=export_fig_correlation_indizes_suchbegriffe)
visualize_forschungsunterfragen_vs_indizes(export_flag=export_fig_correlation_fu_indizes)
visualize_forschungsunterfragen_vs_forschungsunterfragen(export_flag=export_fig_correlation_fu_fu)
visualize_suchbegriffe_vs_suchbegriffe(export_flag=export_fig_correlation_suchbegriffe_suchbegriffe)
visualize_kategorien_vs_kategorien(export_flag=export_fig_correlation_kategorien_kategorien)
visualize_indizes_vs_indizes(export_flag=export_fig_correlation_indizes_indizes)
plot_average_correlation_plotly(summary_df)

# Visualisierungsoption für Plotly: Immer im Browser öffnen
import plotly.io as pio
pio.renderers.default = 'browser'
