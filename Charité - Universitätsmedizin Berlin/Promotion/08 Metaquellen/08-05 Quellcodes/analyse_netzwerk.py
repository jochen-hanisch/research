
from config_netzwerk import theme, export_fig_visual, bib_filename

import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

import sys
sys.path.append('/Users/jochenhanisch-johannsen/Documents/scripte/ci_template')

import bibtexparser
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict, Counter
from itertools import product
from wordcloud import WordCloud
from tabulate import tabulate
import plotly.express as px
import plotly.graph_objects as go
import random
import math
import re
import subprocess

# Template
from ci_template import plotly_template
plotly_template.set_theme(theme)
pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)

# Optional: slugify-Funktion
def slugify(value):
    return re.sub(r'[^a-zA-Z0-9_-]', '', value.replace(' ', '_').lower())

# Zentrale Hilfsfunktion für Figure-Export und Titelergänzung
def prepare_figure_export(fig, name):
    if fig.layout.title and fig.layout.title.text:
        if f"| Quelle: {bib_filename.replace('.bib', '')}" not in fig.layout.title.text:
            fig.update_layout(title_text=f"{fig.layout.title.text} | Quelle: {bib_filename.replace('.bib', '')}")
    safe_filename = slugify(f"{name}_{bib_filename.replace('.bib', '')}")
    return f"{safe_filename}.html"

# Zentraler Schalter für Export-Flags
from config_netzwerk import (
    export_fig_visualize_network,
    export_fig_visualize_tags,
    export_fig_visualize_index,
    export_fig_visualize_research_questions,
    export_fig_visualize_categories,
    export_fig_visualize_time_series,
    export_fig_visualize_top_authors,
    export_fig_visualize_top_publications,
    export_fig_create_path_diagram,
    export_fig_create_sankey_diagram,
    export_fig_visualize_sources_status,
    export_fig_create_wordcloud_from_titles,
    export_fig_visualize_languages,
    export_fig_visualize_relevance_fu,
    export_fig_visualize_relevance_categories,
    export_fig_visualize_relevance_search_terms,
)

from config_netzwerk import export_fig_png

def export_figure_local(fig, name, flag):
    from config_netzwerk import export_path_html, export_path_png
    # Einmalige Definition von safe_filename am Anfang der Funktion
    safe_filename = prepare_figure_export(fig, name).replace(".html", "")
    if flag:
        local_tmp_path = f"/tmp/{safe_filename}.html"
        fig.write_html(local_tmp_path, full_html=True, include_plotlyjs="cdn")
        try:
            subprocess.run(["scp", local_tmp_path, f"{export_path_html}/{safe_filename}.html"], check=True)
            print(f"✅ HTML-Datei erfolgreich übertragen.")
            os.remove(local_tmp_path)
            print(f"🗑️ Lokale HTML-Datei '{local_tmp_path}' wurde gelöscht.")
        except subprocess.CalledProcessError as e:
            print("❌ Fehler bei der Übertragung via SCP:", e)
    if export_fig_png:
        png_path = os.path.join(export_path_png, f"{safe_filename}.png")
        try:
            fig.write_image(png_path, width=1200, height=800, scale=2)
            print(f"✅ PNG-Datei exportiert nach: {png_path}")
        except Exception as e:
            print("❌ Fehler beim PNG-Export:", str(e))

from ci_template.plotly_template import get_colors, get_plot_styles, get_standard_layout

# Farben und Plot-Styles zentral aus Template laden
colors = get_colors()
plot_styles = get_plot_styles()

# Liste der Farben, die für die Wörter verwendet werden sollen
word_colors = [
    colors["white"],
    colors["brightArea"],
    colors["positiveHighlight"],
    colors["negativeHighlight"]
]

# Relevanz-Stufen (1 = gering, 5 = sehr hoch)
RELEVANCE_LEVELS = [5, 4, 3, 2, 1]
RELEVANCE_LEVEL_LABELS = {
    5: "Relevanz 5",
    4: "Relevanz 4",
    3: "Relevanz 3",
    2: "Relevanz 2",
    1: "Relevanz 1",
}
RELEVANCE_COLOR_MAP = {
    "Relevanz 5": colors['positiveHighlight'],
    "Relevanz 4": colors['accent'],
    "Relevanz 3": colors['brightArea'],
    "Relevanz 2": colors['depthArea'],
    "Relevanz 1": colors['negativeHighlight'],
}

# Aktuelles Datum
current_date = datetime.now().strftime("%Y-%m-%d")

# BibTeX-Datei Definitionen
bib_path = os.path.join("Research", "Charité - Universitätsmedizin Berlin", "Systematische Literaturrecherche", "Bibliothek", bib_filename)

# BibTeX-Datei laden
with open(bib_path, encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Stopplisten laden
with open('de_complete.txt', 'r', encoding='utf-8') as file:
    stop_words_de = set(file.read().split())

with open('en_complete.txt', 'r', encoding='utf-8') as file:
    stop_words_en = set(file.read().split())

# Kombinierte Stoppliste
stop_words = stop_words_de.union(stop_words_en)

# Hilfsfunktion: Relevanzstufe aus Keywords extrahieren
def extract_relevance_level(entry_keywords):
    for level in RELEVANCE_LEVELS:
        if f'promotion:relevanz:{level}' in entry_keywords:
            return level
    return None

# Funktion zur Berechnung der Stichprobengröße
def calculate_sample_size(N, Z=1.96, p=0.5, e=0.05):
    n_0 = (Z**2 * p * (1 - p)) / (e**2)
    n = n_0 / (1 + ((n_0 - 1) / N))
    return math.ceil(n)

# Visualisierung 1: Netzwerkanalyse
def visualize_network(bib_database):
    search_terms = {
        '0': 'digital:learning',
        '1': 'learning:management:system',
        '2': 'online:Lernplattform',
        '3': 'online:Lernumgebung',
        '4': 'MOOC',
        '5': 'e-learning',
        '6': 'Bildung:Technologie',
        '7': 'digital:Medien',
        '8': 'blended:learning',
        '9': 'digital:lernen',
        'a': 'online:lernen',
        'b': 'online:learning'
    }

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']
    types = [
        'Zeitschriftenartikel',
        'Buch',
        'Buchteil',
        'Bericht',
        'Konferenz-Paper',
        'Studienbrief'
    ]
    
    tags_to_search = set()
    for number, type_ in product(numbers, types):
        search_term = search_terms[number]
        tag = f'#{number}:{type_}:{search_term}'
        tags_to_search.add(tag.lower())

    tag_counts = defaultdict(int)
    for entry in bib_database.entries:
        if 'keywords' in entry:
            entry_keywords = list(map(str.lower, map(str.strip, entry['keywords'].replace('\\#', '#').split(','))))
            for keyword in entry_keywords:
                for tag in tags_to_search:
                    if tag in keyword:
                        tag_counts[tag] += 1

    search_terms_network = {
        "Primäre Begriffe": {
            "learning:management:system": [
                "e-learning",
                "bildung:technologie",
                "online:lernplattform",
                "online:lernumgebung",
                "digital:learning",
                "digital:lernen"
            ]
        },
        "Sekundäre Begriffe": {
            "e-learning": [
                "mooc",
                "online:lernplattform"
            ],
            "bildung:technologie": [
                "digital:learning",
                "digital:lernen",
                "blended:learning"
            ],
            "digital:learning": [
                "digital:medien",
                "online:learning"
            ],
            "digital:lernen": [
                "digital:medien",
                "online:lernen"
            ],
            "blended:learning": ["mooc"]
        },
        "Tertiäre Begriffe": {
            "online:learning": [],
            "online:lernen": []
        }
    }

    # Fundzählung exakt entlang der search_terms-Definition
    fundzahlen = defaultdict(int)

    for number, suchbegriff in search_terms.items():
        for typ in types:
            tag = f'#{number}:{typ}:{suchbegriff}'.lower()
            fundzahlen[suchbegriff.lower()] += tag_counts.get(tag, 0)

    G = nx.Graph()

    hierarchy_colors = {
        "Primäre Begriffe": colors['primaryLine'],
        "Sekundäre Begriffe": colors['secondaryLine'],
        "Tertiäre Begriffe": colors['brightArea']
    }

    def add_terms_to_graph(level, terms):
        for primary_term, related_terms in terms.items():
            if primary_term not in G:
                G.add_node(primary_term, color=hierarchy_colors[level], size=fundzahlen.get(primary_term, 10))
            else:
                if level == "Tertiäre Begriffe":
                    G.nodes[primary_term]['color'] = hierarchy_colors[level]
            for related_term in related_terms:
                if related_term not in G:
                    G.add_node(related_term, color=hierarchy_colors[level], size=fundzahlen.get(related_term, 10))
                else:
                    if level == "Tertiäre Begriffe":
                        G.nodes[related_term]['color'] = hierarchy_colors[level]
                G.add_edge(primary_term, related_term)

    for level, terms in search_terms_network.items():
        add_terms_to_graph(level, terms)

    np.random.seed(42)
    pos = nx.spring_layout(G)

    x_scale_min, x_scale_max = 0, 10
    y_scale_min, y_scale_max = 0, 10

    min_x = min(pos[node][0] for node in pos)
    max_x = max(pos[node][0] for node in pos)
    min_y = min(pos[node][1] for node in pos)
    max_y = max(pos[node][1] for node in pos)

    scale_x_range = x_scale_max - x_scale_min
    scale_y_range = y_scale_max - y_scale_min

    for node in pos:
        x, y = pos[node]
        norm_x = scale_x_range * (x - min_x) / (max_x - min_x) + x_scale_min
        norm_y = scale_y_range * (y - min_y) / (max_y - min_y) + y_scale_min
        pos[node] = (norm_x, norm_y)

    for node in pos:
        x, y = pos[node]
        x = max(min(x, x_scale_max), x_scale_min)
        y = max(min(y, y_scale_max), y_scale_min)
        pos[node] = (x, y)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=plot_styles['linie_secondaryLine'],
        hoverinfo='none',
        mode='lines')

    # Knoten in drei Traces aufteilen: Primär, Sekundär, Tertiär
    primary_nodes = []
    secondary_nodes = []
    tertiary_nodes = []

    total_fundzahlen = sum(fundzahlen.values())

    for node in G.nodes():
        color = G.nodes[node]['color']
        size = math.log(G.nodes[node].get('size', 10) + 1) * 10
        x, y = pos[node]
        count = fundzahlen.get(node, 0)
        percentage = (count / total_fundzahlen * 100) if total_fundzahlen else 0
        hovertext = f"{node}<br>Anzahl Funde: {count}<br>Anteil: {percentage:.1f}%"
        node_data = dict(x=x, y=y, text=node, size=size, hovertext=hovertext)
        if color == colors['primaryLine']:
            primary_nodes.append(node_data)
        elif color == colors['secondaryLine']:
            secondary_nodes.append(node_data)
        elif color == colors['brightArea']:
            tertiary_nodes.append(node_data)

    def create_node_trace(nodes, name, color):
        # Wähle Punktstil je nach color
        if color == colors['primaryLine']:
            marker_style = plot_styles['punkt_primaryLine'].copy()
        elif color == colors['secondaryLine']:
            marker_style = plot_styles['punkt_secondaryLine'].copy()
        elif color == colors['brightArea']:
            marker_style = plot_styles['punkt_brightArea'].copy()
        else:
            marker_style = dict(color=color)
        marker_style['size'] = [n['size'] for n in nodes]
        # Erhöhe Kontrast Marker-Rand zum Hintergrund
        marker_style['line'] = {'width': 1, 'color': colors['background']}
        return go.Scatter(
            x=[n['x'] for n in nodes],
            y=[n['y'] for n in nodes],
            mode='markers+text',
            text=[n['text'] for n in nodes],
            hovertext=[n['hovertext'] for n in nodes],
            hoverinfo='text',
            marker=marker_style,
            textposition="top center",
            textfont=dict(size=12, color=colors['text']),
            name=name
        )

    primary_trace = create_node_trace(primary_nodes, "Primäre Begriffe", colors['primaryLine'])
    secondary_trace = create_node_trace(secondary_nodes, "Sekundäre Begriffe", colors['secondaryLine'])
    tertiary_trace = create_node_trace(tertiary_nodes, "Tertiäre Begriffe", colors['brightArea'])

    fig = go.Figure(data=[edge_trace, primary_trace, secondary_trace, tertiary_trace])
    layout = get_standard_layout(
        title=f"Suchbegriff-Netzwerk nach Relevanz und Semantik (n={total_fundzahlen}, Stand: {current_date})",
        x_title="Technologische Dimension",
        y_title="Pädagogische Dimension"
    )
    layout["margin"] = dict(b=160, l=5, r=5, t=40)
    layout["hovermode"] = "closest"
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["autosize"] = True
    fig.update_layout(**layout)

    fig.show(config={"responsive": True})
    export_figure_local(fig, "visualize_network", export_fig_visualize_network)

    # Einfache Pfadanalyse nach dem Anzeigen der Figur
    if 'e-learning' in G and 'online:lernen' in G:
        try:
            pfad = nx.shortest_path(G, source='e-learning', target='online:lernen')
            print(f"Kürzester Pfad von 'e-learning' zu 'online:lernen': {pfad}")
        except nx.NetworkXNoPath:
            print("Kein Pfad von 'e-learning' zu 'online:lernen' gefunden.")

 # Visualisierung 2: Häufigkeit spezifischer Tags
def visualize_tags(bib_database):
    # Definierte Suchbegriffe
    search_terms = {
        '0': 'digital:learning',
        '1': 'learning:management:system',
        '2': 'online:Lernplattform',
        '3': 'online:Lernumgebung',
        '4': 'MOOC',
        '5': 'e-learning',
        '6': 'Bildung:Technologie',
        '7': 'digital:Medien',
        '8': 'blended:learning',
        '9': 'digital:lernen',
        'a': 'online:lernen',
        'b': 'online:learning'
    }

    # Kombinierte Tags erzeugen
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']
    types = [
        'Zeitschriftenartikel',
        'Buch',
        'Buchteil',
        'Bericht',
        'Konferenz-Paper',
        'Studienbrief'
    ]
    tags_to_search = set(
        f"#{number}:{type_}:{search_terms[number]}".lower()
        for number, type_ in product(numbers, types)
    )

    # Tag-Zählungen initialisieren
    tag_counts = defaultdict(int)
    if not bib_database or not bib_database.entries:
        print("Fehler: Keine Einträge in der Datenbank gefunden.")
        return

    for entry in bib_database.entries:
        if 'keywords' in entry:
            entry_keywords = map(
                str.lower,
                map(str.strip, entry['keywords'].replace('\\#', '#').split(','))
            )
            for keyword in entry_keywords:
                for tag in tags_to_search:
                    if tag in keyword:
                        tag_counts[tag] += 1

    # Daten für Visualisierung aufbereiten
    data_rows = [
        {
            'Tag': tag,
            'Count': count,
            'Type': tag.split(':')[1].lower()
        }
        for tag, count in tag_counts.items()
        if count > 0
    ]

    if not data_rows:
        print("Warnung: Keine Tags gefunden, die den Suchkriterien entsprechen.")
        return

    df = pd.DataFrame(data_rows)
    df['TypeLabel'] = df['Type'].str.replace('-', ' ').str.title()
    total_count = df['Count'].sum()
    df['Percentage'] = df['Count'] / total_count * 100 if total_count else 0

    # Farbzuordnung
    color_map = {
        'zeitschriftenartikel': colors['primaryLine'],
        'konferenz-paper': colors['secondaryLine'],
        'buch': colors['depthArea'],
        'buchteil': colors['brightArea'],
        'bericht': colors['accent'],
        'studienbrief': colors['positiveHighlight']
    }

    # Visualisierung erstellen
    fig = px.bar(
        df,
        x='Tag',
        y='Count',
        title=f'Häufigkeit der Suchbegriffe in der Literaturanalyse (n={total_count}, Stand: {current_date})',
        labels={'Tag': 'Tag', 'Count': 'Anzahl der Vorkommen'},
        color='Type',
        color_discrete_map=color_map,
        text_auto=True,
        custom_data=['TypeLabel', 'Percentage']
    )

    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title='Tag',
        y_title='Anzahl der Vorkommen'
    )
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["xaxis"] = layout.get("xaxis", {})
    layout["xaxis"]["tickangle"] = -45
    layout["xaxis"]["automargin"] = True
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Typ: %{customdata[0]}<br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata[1]:.1f}%<extra></extra>"
        )
    )

    fig.show(config={"responsive": True})
    export_figure_local(fig, "visualize_tags", export_fig_visualize_tags)

 # Visualisierung 3: Häufigkeit Index
def visualize_index(bib_database):
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

    index_counts = defaultdict(int)
    for entry in bib_database.entries:
        if 'keywords' in entry:
            entry_keywords = list(map(str.lower, map(str.strip, entry['keywords'].replace('\\#', '#').split(','))))
            for index_term in index_terms:
                if index_term.lower() in entry_keywords:
                    index_counts[index_term] += 1

    index_data = [{'Index': index, 'Count': count} for index, count in index_counts.items()]
    index_data = sorted(index_data, key=lambda x: x['Count'], reverse=True)

    index_df = pd.DataFrame(index_data)
    total_count = index_df['Count'].sum()
    index_df['Percentage'] = index_df['Count'] / total_count * 100 if total_count else 0
    print(f"Häufigkeit Indizes (Gesamtanzahl: {total_count}):")
    print(tabulate(index_df.to_dict('records'), headers="keys", tablefmt="grid"))

    fig = px.bar(
        index_df,
        x='Index',
        y='Count',
        title=f'Relevanzschlüssel nach Indexkategorien (n={total_count}, Stand: {current_date})',
        labels={'Index': 'Index', 'Count': 'Anzahl der Vorkommen'},
        text_auto=True,
        custom_data=['Percentage']
    )
    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title='Index',
        y_title='Anzahl der Vorkommen'
    )
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["xaxis"] = layout.get("xaxis", {})
    layout["xaxis"]["tickangle"] = -45
    layout["xaxis"]["automargin"] = True
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.update_traces(marker=plot_styles['balken_primaryLine'])
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata[0]:.1f}%<extra></extra>"
        )
    )
    fig.show(config={"responsive": True})
    export_figure_local(fig, "visualize_index", export_fig_visualize_index)

 # Visualisierung 4: Häufigkeit Forschungsunterfragen
def visualize_research_questions(bib_database):
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

    rq_counts = defaultdict(int)
    for entry in bib_database.entries:
        if 'keywords' in entry:
            entry_keywords = list(map(str.lower, map(str.strip, entry['keywords'].replace('\\#', '#').split(','))))
            for keyword in entry_keywords:
                if keyword in research_questions:
                    rq_counts[keyword] += 1

    rq_data = [{'Research_Question': research_questions[keyword], 'Count': count} for keyword, count in rq_counts.items()]
    rq_data = sorted(rq_data, key=lambda x: x['Count'], reverse=True)

    rq_data_df = pd.DataFrame(rq_data, columns=['Research_Question', 'Count'])

    total_count = rq_data_df['Count'].sum()
    rq_data_df['Percentage'] = rq_data_df['Count'] / total_count * 100 if total_count else 0
    print(f"Häufigkeit Forschungsunterfragen (Gesamtanzahl: {total_count}):")
    print(tabulate(rq_data, headers="keys", tablefmt="grid"))

    fig = px.bar(
        rq_data_df,
        x='Research_Question',
        y='Count',
        title=f'Zuordnung der Literatur zu Forschungsunterfragen (n={total_count}, Stand: {current_date})',
        labels={'Research_Question': 'Forschungsunterfrage', 'Count': 'Anzahl der Vorkommen'},
        text_auto=True,
        custom_data=['Percentage']
    )
    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title='Forschungsunterfrage',
        y_title='Anzahl der Vorkommen'
    )
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["xaxis"] = layout.get("xaxis", {})
    layout["xaxis"]["tickangle"] = -45
    layout["xaxis"]["automargin"] = True
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.update_traces(marker=plot_styles['balken_primaryLine'])
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata[0]:.1f}%<extra></extra>"
        )
    )
    fig.show(config={"responsive": True})
    export_figure_local(fig, "visualize_research_questions", export_fig_visualize_research_questions)

 # Visualisierung 5: Häufigkeit spezifischer Kategorien
def visualize_categories(bib_database):
    categories = {
        'promotion:argumentation': 'Argumentation',
        'promotion:kerngedanke': 'Kerngedanke',
        'promotion:weiterführung': 'Weiterführung',
        'promotion:schlussfolgerung': 'Schlussfolgerung'
    }

    cat_counts = defaultdict(int)
    for entry in bib_database.entries:
        if 'keywords' in entry:
            entry_keywords = list(map(str.lower, map(str.strip, entry['keywords'].replace('\\#', '#').split(','))))
            for keyword in entry_keywords:
                if keyword in categories:
                    cat_counts[keyword] += 1

    cat_data = [{'Category': categories[keyword], 'Count': count} for keyword, count in cat_counts.items()]
    cat_data = sorted(cat_data, key=lambda x: x['Count'], reverse=True)

    cat_data_df = pd.DataFrame(cat_data, columns=['Category', 'Count'])

    total_count = cat_data_df['Count'].sum()
    cat_data_df['Percentage'] = cat_data_df['Count'] / total_count * 100 if total_count else 0
    print(f"Häufigkeit Kategorien (Gesamtanzahl: {total_count}):")
    print(tabulate(cat_data, headers="keys", tablefmt="grid"))

    fig = px.bar(
        cat_data_df,
        x='Category',
        y='Count',
        title=f'Textsortenzuordnung der analysierten Quellen (n={total_count}, Stand: {current_date})',
        labels={'Category': 'Kategorie', 'Count': 'Anzahl der Vorkommen'},
        text_auto=True,
        custom_data=['Percentage']
    )
    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title='Kategorie',
        y_title='Anzahl der Vorkommen'
    )
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["xaxis"] = layout.get("xaxis", {})
    layout["xaxis"]["tickangle"] = -45
    layout["xaxis"]["automargin"] = True
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.update_traces(marker=plot_styles['balken_primaryLine'])
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata[0]:.1f}%<extra></extra>"
        )
    )
    fig.show(config={"responsive": True})
    export_figure_local(fig, "visualize_categories", export_fig_visualize_categories)

# Relevanz-Auswertungen
def build_relevance_distribution(bib_database, tag_to_label):
    records = []

    for entry in bib_database.entries:
        keywords_raw = entry.get('keywords', '')
        if not keywords_raw:
            continue

        entry_keywords = set(map(str.lower, map(str.strip, keywords_raw.replace('\\#', '#').split(','))))
        relevance_level = extract_relevance_level(entry_keywords)
        if relevance_level is None:
            continue

        for tag, label in tag_to_label.items():
            if tag in entry_keywords:
                records.append({
                    'Kategorie': label,
                    'Relevanzstufe': RELEVANCE_LEVEL_LABELS[relevance_level]
                })

    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)
    df = (
        df.groupby(['Kategorie', 'Relevanzstufe'])
        .size()
        .reset_index(name='Count')
    )
    df['Relevanzstufe'] = pd.Categorical(
        df['Relevanzstufe'],
        categories=[RELEVANCE_LEVEL_LABELS[level] for level in RELEVANCE_LEVELS],
        ordered=True
    )
    return df.sort_values(['Kategorie', 'Relevanzstufe'])


def plot_relevance_distribution(df, title, x_title, export_flag, filename):
    if df.empty:
        print(f"⚠️ Keine Relevanzdaten verfügbar für: {title}")
        return

    total_count = df['Count'].sum()
    df['Percentage'] = df['Count'] / total_count * 100 if total_count else 0
    fig = px.bar(
        df,
        x='Kategorie',
        y='Count',
        color='Relevanzstufe',
        color_discrete_map=RELEVANCE_COLOR_MAP,
        category_orders={'Relevanzstufe': [RELEVANCE_LEVEL_LABELS[level] for level in RELEVANCE_LEVELS]},
        title=f"{title} (n={total_count}, Stand: {current_date})",
        labels={'Kategorie': x_title, 'Count': 'Anzahl', 'Relevanzstufe': 'Relevanzstufe'},
        custom_data=['Relevanzstufe', 'Percentage']
    )

    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title=x_title,
        y_title='Anzahl'
    )
    layout['barmode'] = 'stack'
    layout['font'] = {"size": 14, "color": colors['text']}
    layout['title'] = {"font": {"size": 16}}
    layout['margin'] = dict(b=160, t=60, l=40, r=40)
    layout['xaxis'] = layout.get('xaxis', {})
    layout['xaxis']['tickangle'] = -45
    layout['xaxis']['automargin'] = True
    layout['autosize'] = True
    fig.update_layout(**layout)
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Relevanzstufe: %{customdata[0]}<br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata[1]:.1f}%<extra></extra>"
        )
    )

    fig.show(config={"responsive": True})
    export_figure_local(fig, filename, export_flag)


def visualize_relevance_vs_research_questions(bib_database):
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
    tag_to_label = {key.lower(): value for key, value in research_questions.items()}
    df = build_relevance_distribution(bib_database, tag_to_label)
    plot_relevance_distribution(
        df,
        "Relevanzverteilung nach Forschungsunterfragen",
        "Forschungsunterfragen",
        export_fig_visualize_relevance_fu,
        "visualize_relevance_fu"
    )


def visualize_relevance_vs_categories(bib_database):
    categories = {
        'promotion:argumentation': 'Argumentation',
        'promotion:kerngedanke': 'Kerngedanke',
        'promotion:weiterführung': 'Weiterführung',
        'promotion:schlussfolgerung': 'Schlussfolgerung'
    }
    tag_to_label = {key.lower(): value for key, value in categories.items()}
    df = build_relevance_distribution(bib_database, tag_to_label)
    plot_relevance_distribution(
        df,
        "Relevanzverteilung nach Kategorien",
        "Kategorien",
        export_fig_visualize_relevance_categories,
        "visualize_relevance_categories"
    )


def visualize_relevance_vs_search_terms(bib_database):
    search_terms = {
        '0': 'digital:learning',
        '1': 'learning:management:system',
        '2': 'online:lernplattform',
        '3': 'online:lernumgebung',
        '4': 'mooc',
        '5': 'e-learning',
        '6': 'bildung:technologie',
        '7': 'digital:medien',
        '8': 'blended:learning',
        '9': 'digital:lernen',
        'a': 'online:lernen',
        'b': 'online:learning'
    }
    types = [
        'Zeitschriftenartikel',
        'Buch',
        'Buchteil',
        'Bericht',
        'Konferenz-Paper',
        'Studienbrief'
    ]

    tag_to_label = {}
    for number, term in search_terms.items():
        for type_ in types:
            tag = f'#{number}:{type_}:{term}'.lower()
            tag_to_label[tag] = f"#{number}:{term}"

    df = build_relevance_distribution(bib_database, tag_to_label)
    plot_relevance_distribution(
        df,
        "Relevanzverteilung nach Suchbegriffen",
        "Suchbegriffe",
        export_fig_visualize_relevance_search_terms,
        "visualize_relevance_search_terms"
    )

 # Zeitreihenanalyse der Veröffentlichungen
def visualize_time_series(bib_database):
    publication_years = []

    for entry in bib_database.entries:
        if 'year' in entry:
            year_str = entry['year'].strip()
            try:
                # Extrahiere die erste gültige Zahl (z. B. 2017 aus '2017/2018')
                year_match = re.search(r'\b\d{4}\b', year_str)
                if year_match:
                    year = int(year_match.group())
                    publication_years.append(year)
                else:
                    raise ValueError(f"Kein gültiges Jahr gefunden: {year_str}")
            except ValueError as e:
                print(f"Warnung: Ungültiger Jahreswert in Eintrag übersprungen: {year_str}")

    if publication_years:
        year_counts = Counter(publication_years)
        df = pd.DataFrame(year_counts.items(), columns=['Year', 'Count']).sort_values('Year')
        total_publications = df['Count'].sum()
        df['Percentage'] = df['Count'] / total_publications * 100 if total_publications else 0

        fig = px.line(
            df,
            x='Year',
            y='Count',
            title=f'Jährliche Veröffentlichungen in der Literaturanalyse (n={sum(year_counts.values())}, Stand: {current_date})',
            labels={'Year': 'Jahr', 'Count': 'Anzahl der Veröffentlichungen'},
            custom_data=['Percentage']
        )
        layout = get_standard_layout(
            title=fig.layout.title.text,
            x_title='Jahr',
            y_title='Anzahl der Veröffentlichungen'
        )
        layout["xaxis"] = dict(
            tickmode='linear',
            dtick=2,
            tick0=min(publication_years)
        )
        layout["font"] = {"size": 14, "color": colors['text']}
        layout["title"] = {"font": {"size": 16}}
        layout["autosize"] = True
        fig.update_layout(**layout)
        fig.update_traces(line=plot_styles['linie_primaryLine'])
        fig.update_traces(
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Anzahl: %{y}<br>"
                "Anteil: %{customdata[0]:.1f}%<extra></extra>"
            )
        )
        fig.show(config={"responsive": True})
        export_figure_local(fig, "visualize_time_series", export_fig_visualize_time_series)
    else:
        print("Keine gültigen Veröffentlichungsjahre gefunden.")

 # Top Autoren nach Anzahl der Werke
def visualize_top_authors(bib_database):
    top_n = 25  # Anzahl der Top-Autoren, die angezeigt werden sollen
    author_counts = defaultdict(int)
    for entry in bib_database.entries:
        if 'author' in entry:
            authors = [author.strip() for author in entry['author'].split(' and ')]
            for author in authors:
                author_counts[author] += 1

    top_authors = Counter(author_counts).most_common(top_n)
    if top_authors:
        df = pd.DataFrame(top_authors, columns=['Author', 'Count'])
        overall_total = sum(author_counts.values())
        df['Percentage'] = df['Count'] / overall_total * 100 if overall_total else 0

        fig = px.bar(
            df,
            x='Author',
            y='Count',
            title=f'Meistgenannte Autor:innen in der Literaturanalyse (Top {top_n}, n={overall_total}, Stand: {current_date})',
            labels={'Author': 'Autor', 'Count': 'Anzahl der Werke'},
            text_auto=True,
            custom_data=['Percentage']
        )
        layout = get_standard_layout(
            title=fig.layout.title.text,
            x_title='Autor',
            y_title='Anzahl der Werke'
        )
        layout["font"] = {"size": 14, "color": colors['text']}
        layout["title"] = {"font": {"size": 16}}
        layout["margin"] = dict(b=160, t=60, l=40, r=40)
        layout["xaxis"] = layout.get("xaxis", {})
        layout["xaxis"]["tickangle"] = -45
        layout["xaxis"]["automargin"] = True
        layout["autosize"] = True
        fig.update_layout(**layout)
        fig.update_traces(marker=plot_styles['balken_primaryLine'])
        fig.update_traces(
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Anzahl: %{y}<br>"
                "Anteil: %{customdata[0]:.1f}%<extra></extra>"
            )
        )
        fig.show(config={"responsive": True})
        export_figure_local(fig, "visualize_top_authors", export_fig_visualize_top_authors)
    else:
        print("Keine Autoren gefunden.")

##########

# Daten vorbereiten
def prepare_path_data(bib_database):
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

    categories = {
        'promotion:argumentation': 'Argumentation',
        'promotion:kerngedanke': 'Kerngedanke',
        'promotion:weiterführung': 'Weiterführung',
        'promotion:schlussfolgerung': 'Schlussfolgerung'
    }

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

    entry_types = [
        'Zeitschriftenartikel',
        'Buch',
        'Buchteil',
        'Bericht',
        'Konferenz-Paper',
        'Studienbrief'
    ]

    data = []

    for entry in bib_database.entries:
        entry_data = {
            'FU': None,
            'Category': None,
            'Index': None,
            'Type': entry.get('ENTRYTYPE', '').lower()
        }

        if 'keywords' in entry:
            entry_keywords = list(map(str.lower, map(str.strip, entry['keywords'].replace('\\#', '#').split(','))))

            for key, value in research_questions.items():
                if key in entry_keywords:
                    entry_data['FU'] = value

            for key, value in categories.items():
                if key in entry_keywords:
                    entry_data['Category'] = value

            for index_term in index_terms:
                if index_term.lower() in entry_keywords:
                    entry_data['Index'] = index_term

        if all(value is not None for value in entry_data.values()):
            data.append(entry_data)

    return data

 # Pfaddiagramm erstellen
def create_path_diagram(data):
    labels = []
    sources = []
    targets = []
    values = []
    node_counts = Counter()
    color_map = {
        'zeitschriftenartikel': colors['primaryLine'],
        'konferenz-paper': colors['secondaryLine'],
        'buch': colors['depthArea'],
        'buchteil': colors['brightArea'],
        'bericht': colors['accent'],
        'studienbrief': colors['positiveHighlight']
    }

    def add_to_labels(label):
        if label not in labels:
            labels.append(label)
        return labels.index(label)

    for entry in data:
        fu_idx = add_to_labels(entry['FU'])
        category_idx = add_to_labels(entry['Category'])
        index_idx = add_to_labels(entry['Index'])
        type_idx = add_to_labels(entry['Type'])

        sources.extend([fu_idx, category_idx, index_idx])
        targets.extend([category_idx, index_idx, type_idx])
        values.extend([1, 1, 1])
        node_counts.update([entry['FU'], entry['Category'], entry['Index'], entry['Type']])

    node_colors = [color_map.get(label, colors['primaryLine']) for label in labels]
    total_paths = len(data)
    total_flows = sum(values)
    node_percentages = [
        node_counts.get(label, 0) / total_paths * 100 if total_paths else 0
        for label in labels
    ]
    link_percentages = [
        value / total_flows * 100 if total_flows else 0
        for value in values
    ]

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color=node_colors,
            customdata=node_percentages,
            hovertemplate=(
                "%{label}<br>"
                "Anzahl: %{value}<br>"
                "Anteil der Pfade: %{customdata:.1f}%<extra></extra>"
            )
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            customdata=link_percentages,
            hovertemplate=(
                "%{source.label} → %{target.label}<br>"
                "Anzahl: %{value}<br>"
                "Anteil der Verbindungen: %{customdata:.1f}%<extra></extra>"
            )
        )
    )])
    layout = get_standard_layout(
        title=f'Kategorischer Analysepfad der Literatur (n={len(data)}, Stand: {current_date})',
        x_title='',
        y_title=''
    )
    # Erhöhe Lesbarkeit: größere Schrift, weißer Text
    layout["font"] = dict(size=12, color=colors['text'])
    layout["title"] = {"font": {"size": 16}}
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.show(config={"responsive": True})
    export_figure_local(fig, "create_path_diagram", export_fig_create_path_diagram)

#############

def create_sankey_diagram(bib_database):
    def extract_year(entry):
        """
        Extrahiert ein gültiges Jahr aus dem `year`-Feld eines Eintrags.
        """
        year_str = entry.get('year', '').strip()
        try:
            # Suche nach einer 4-stelligen Jahreszahl
            year_match = re.search(r'\b\d{4}\b', year_str)
            if year_match:
                return int(year_match.group())
            else:
                raise ValueError(f"Kein gültiges Jahr gefunden: {year_str}")
        except ValueError:
            print(f"Warnung: Ungültiger Jahreswert in Eintrag übersprungen: {year_str}")
            return None

    current_year = datetime.now().year

    # Schätzungen und Filterkriterien mit sicheren Zugriffen
    initial_sources = len(bib_database.entries)
    screened_sources = sum(
        1 for entry in bib_database.entries if 'Promotion:Literaturanalyse' in entry.get('keywords', '')
    )
    quality_sources = sum(
        1 for entry in bib_database.entries
        if entry.get('ENTRYTYPE') in ['article', 'phdthesis'] and 'Promotion:Literaturanalyse' in entry.get('keywords', '')
    )
    relevance_sources = sum(
        1 for entry in bib_database.entries
        if any(kw in entry.get('keywords', '') for kw in ['Promotion:FU3', 'Promotion:Kerngedanke'])
    )
    thematic_sources = sum(
        1 for entry in bib_database.entries
        if any(kw in entry.get('keywords', '') for kw in ['digital', 'learning'])
    )
    recent_sources = sum(
        1 for entry in bib_database.entries
        if (year := extract_year(entry)) and year >= current_year - 5
    )
    classic_sources = sum(
        1 for entry in bib_database.entries
        if (year := extract_year(entry)) and year < current_year - 5 and 'classic' in entry.get('keywords', '').lower()
    )
    selected_sources = recent_sources + classic_sources

    # Stichprobengröße berechnen
    sample_size = calculate_sample_size(initial_sources)

    # Phasen und Verbindungen definieren
    phases = [
        "Identifizierte Quellen",
        "Nach Screening (Literaturanalyse-Markierung)",
        "Nach Qualitätsprüfung (Artikel und Dissertationen)",
        "Nach Relevanzprüfung (FU3 und Kerngedanken)",
        "Nach thematischer Prüfung (Digital & Learning)",
        "Aktuelle Forschung (letzte 5 Jahre)",
        "Klassische Werke",
        "Ausgewählte Quellen (Endauswahl)"
    ]

    sources = [0, 1, 2, 3, 4, 4, 4]
    targets = [1, 2, 3, 4, 5, 6, 7]
    values = [
        screened_sources,
        quality_sources,
        relevance_sources,
        thematic_sources,
        recent_sources,
        classic_sources,
        selected_sources
    ]

    # Prozentsätze berechnen für die Labels
    percentages = [
        "100.0%",  # Startwert
        f"{screened_sources / initial_sources * 100:.1f}%",
        f"{quality_sources / screened_sources * 100:.1f}%" if screened_sources > 0 else "0.0%",
        f"{relevance_sources / quality_sources * 100:.1f}%" if quality_sources > 0 else "0.0%",
        f"{thematic_sources / relevance_sources * 100:.1f}%" if relevance_sources > 0 else "0.0%",
        f"{recent_sources / thematic_sources * 100:.1f}%" if thematic_sources > 0 else "0.0%",
        f"{classic_sources / thematic_sources * 100:.1f}%" if thematic_sources > 0 else "0.0%",
        f"{selected_sources / (recent_sources + classic_sources) * 100:.1f}%" if (recent_sources + classic_sources) > 0 else "0.0%"
    ]

    # Labels für Knoten anpassen, um Prozentsätze anzuzeigen
    node_labels = [f"{ph} ({pct})" for ph, pct in zip(phases, percentages)]

    # Farben für die einzelnen Phasen
    node_colors = [
        colors['primaryLine'],          # Identifizierte Quellen
        colors['secondaryLine'],        # Nach Screening
        colors['brightArea'],           # Nach Qualitätsprüfung
        colors['depthArea'],            # Nach Relevanzprüfung
        colors['positiveHighlight'],    # Nach thematischer Prüfung
        colors['negativeHighlight'],    # Aktuelle Forschung
        colors['accent'],               # Klassische Werke
        colors['positiveHighlight']     # Ausgewählte Quellen
    ]

    node_values = [
        initial_sources,
        screened_sources,
        quality_sources,
        relevance_sources,
        thematic_sources,
        recent_sources,
        classic_sources,
        selected_sources
    ]
    node_percentages = [
        value / initial_sources * 100 if initial_sources else 0
        for value in node_values
    ]
    link_percentages = [
        value / initial_sources * 100 if initial_sources else 0
        for value in values
    ]

    # Sankey-Diagramm erstellen
    node_config = {
        **plot_styles["sankey_node"],
        "label": node_labels,
        "color": node_colors,
        "customdata": node_percentages,
        "hovertemplate": (
            "%{label}<br>"
            "Anzahl: %{value}<br>"
            "Anteil an Ausgangsmenge: %{customdata:.1f}%<extra></extra>"
        )
    }
    # Remove any invalid 'font' key if present
    node_config.pop("font", None)
    link_config = {
        **plot_styles["sankey_link"],
        "source": sources,
        "target": targets,
        "value": values,
        "customdata": link_percentages,
        "hovertemplate": (
            "%{source.label} → %{target.label}<br>"
            "Anzahl: %{value}<br>"
            "Anteil an Ausgangsmenge: %{customdata:.1f}%<extra></extra>"
        )
    }
    fig = go.Figure(go.Sankey(
        node=node_config,
        link=link_config
    ))
    # Layout anpassen
    layout = get_standard_layout(
        title=f"Flussdiagramm der Literaturselektion (Stichprobe: n={sample_size}, Stand: {current_date})",
        x_title='',
        y_title=''
    )
    # Erhöhe Lesbarkeit: größere Schrift, weißer Text
    layout["font"] = dict(size=12, color=colors['text'])
    layout["title"] = {"font": {"size": 16}}
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.show(config={"responsive": True})
    export_figure_local(fig, "create_sankey_diagram", export_fig_create_sankey_diagram)

##########

def calculate_sample_size(N, Z=1.96, p=0.5, e=0.05):
    """
    Berechnet die Stichprobengröße basierend auf der Gesamtanzahl der Einträge (N).
    """
    if N <= 0:
        return 0
    n_0 = (Z**2 * p * (1 - p)) / (e**2)
    n = n_0 / (1 + ((n_0 - 1) / N))
    return math.ceil(n)

def visualize_sources_status(bib_database):
    """
    Visualisiert den Status der analysierten und nicht analysierten Quellen pro Suchordner.
    """
    search_terms = {
        '0': 'digital:learning',
        '1': 'learning:management:system',
        '2': 'online:lernplattform',
        '3': 'online:lernumgebung',
        '4': 'mooc',
        '5': 'e-learning',
        '6': 'bildung:technologie',
        '7': 'digital:medien',
        '8': 'blended:learning',
        '9': 'digital:lernen',
        'a': 'online:lernen',
        'b': 'online:learning'
    }
    numbers_order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']
    type_order = [
        'Zeitschriftenartikel',
        'Buch',
        'Buchteil',
        'Bericht',
        'Konferenz-Paper',
        'Studienbrief'
    ]
    search_folder_tags = [
        f"#{number}:{type_}:{search_terms[number]}".lower()
        for type_ in type_order
        for number in numbers_order
    ]

    category_tags = {"promotion:argumentation", "promotion:kerngedanke", "promotion:weiterführung", "promotion:schlussfolgerung"}
    source_data = defaultdict(lambda: {'Identifiziert': 0, 'Analysiert': 0})

    if not bib_database or not bib_database.entries:
        print("Fehler: Die Datenbank enthält keine Einträge.")
        return

    for entry in bib_database.entries:
        keywords = entry.get('keywords', '')
        if not keywords:
            continue

        entry_keywords = set(map(str.lower, map(str.strip, keywords.replace('\\#', '#').split(','))))

        for tag in search_folder_tags:
            if tag.lower() in entry_keywords:
                source_data[tag]['Identifiziert'] += 1
                if entry_keywords & category_tags:
                    source_data[tag]['Analysiert'] += 1

    table_data = []
    analysiert_values = []
    nicht_analysiert_values = []
    analysiert_colors = []
    tags = []

    for tag, counts in sorted(source_data.items(), key=lambda item: item[1]['Identifiziert'], reverse=True):
        stichprobe = calculate_sample_size(counts['Identifiziert'])
        noch_zu_analysieren = counts['Identifiziert'] - counts['Analysiert']
        noch_benoetigt_fuer_stichprobe = max(0, stichprobe - counts['Analysiert'])

        table_data.append([
            tag,
            counts['Identifiziert'],
            counts['Analysiert'],
            noch_zu_analysieren,
            stichprobe,
            noch_benoetigt_fuer_stichprobe
        ])

        analysiert_values.append(counts['Analysiert'])
        nicht_analysiert_values.append(noch_zu_analysieren)
        tags.append(tag)

        analysiert_colors.append(colors['positiveHighlight'] if counts['Analysiert'] >= stichprobe else colors['negativeHighlight'])

    print(tabulate(
        table_data,
        headers=['Suchordner', 'Identifiziert', 'Analysiert', 'nicht-Analysiert', 'Stichprobe', 'Noch benötigt für Stichprobe'],
        tablefmt='grid'
    ))

    total_identifiziert = sum(counts["Identifiziert"] for counts in source_data.values())
    analysiert_percentages = [
        value / total_identifiziert * 100 if total_identifiziert else 0
        for value in analysiert_values
    ]
    nicht_analysiert_percentages = [
        value / total_identifiziert * 100 if total_identifiziert else 0
        for value in nicht_analysiert_values
    ]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=tags,
        y=analysiert_values,
        name='Analysiert',
        marker=dict(color=analysiert_colors),
        customdata=analysiert_percentages,
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Status: Analysiert<br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata:.1f}%<extra></extra>"
        )
    ))
    fig.add_trace(go.Bar(
        x=tags,
        y=nicht_analysiert_values,
        name='Nicht-Analysiert',
        marker=plot_styles['balken_primaryLine'],
        customdata=nicht_analysiert_percentages,
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Status: Nicht-Analysiert<br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata:.1f}%<extra></extra>"
        )
    ))
    layout = get_standard_layout(
        title=f'Analyse- und Stichprobenstatus je Suchordner (n={total_identifiziert}, Stand: {current_date})',
        x_title='Suchbegriffsordner',
        y_title='Anzahl der Quellen'
    )
    layout["barmode"] = "stack"
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["xaxis"] = dict(
        categoryorder='array',
        categoryarray=search_folder_tags,
        tickangle=-45,
        automargin=True
    )
    layout["autosize"] = True
    fig.update_layout(**layout)
    fig.show(config={"responsive": True})
    export_figure_local(fig, "visualize_sources_status", export_fig_visualize_sources_status)

#############

# Visualisierung der Sprachverteilung der Quellen
def visualize_languages(bib_database):
    """
    Zeigt die Sprachverteilung der Quellen in einem Balkendiagramm an, inklusive Gruppierung nach Sprachgruppen.
    """
    language_counts = defaultdict(int)
    for entry in bib_database.entries:
        if 'language' in entry:
            lang = entry['language'].strip().lower()
            language_counts[lang] += 1

    if not language_counts:
        print("⚠️ Keine Sprachinformationen in den Einträgen gefunden.")
        return

    # Mapping von Spracheinträgen auf normalisierte ISO-Codes
    languageMap = {
        "de": "de-DE",
        "de-de": "de-DE",
        "deutsch": "de-DE",
        "german": "de-DE",
        "ger": "de-DE",
        "en": "en-GB",
        "en-gb": "en-GB",
        "en-us": "en-US",
        "englisch": "en-GB",
        "eng": "en-GB",
        "id": "id",
        "ms": "ms",
        "de-ch": "de-CH",
        "de-a": "de-A",
    }

    # Sprachgruppen-Definition
    language_groups = {
        "de-DE": "Deutsch",
        "de-A": "Deutsch",
        "de-CH": "Deutsch",
        "en-GB": "Englisch",
        "en-US": "Englisch",
        "id": "Sonstige",
        "ms": "Sonstige"
    }

    # Funktion zur robusten Normalisierung
    def normalize_lang(lang):
        l = lang.strip().lower()
        return languageMap.get(l, l)

    # Normalisierte Sprachen und Zählung
    norm_counts = defaultdict(int)
    for lang, count in language_counts.items():
        norm_lang = normalize_lang(lang)
        norm_counts[norm_lang] += count

    df = pd.DataFrame([
        {'Sprache': lang, 'Anzahl': count} for lang, count in norm_counts.items()
    ])
    # Nach Häufigkeit absteigend sortieren
    df = df.sort_values('Anzahl', ascending=False)

    # Neue Spalte: Sprachgruppe
    df['Gruppe'] = df['Sprache'].map(language_groups).fillna("Sonstige")

    # Neue Spalte: Anteil (%) mit zwei Nachkommastellen
    df["Anteil (%)"] = (df["Anzahl"] / df["Anzahl"].sum() * 100).round(2)

    # Farbzuordnung für Gruppen
    color_discrete_map = {
        "Deutsch": colors["primaryLine"],
        "Englisch": colors["secondaryLine"],
        "Sonstige": colors["depthArea"]
    }

    fig = px.bar(
        df,
        x='Sprache',
        y='Anzahl',
        text='Anzahl',
        color='Gruppe',
        color_discrete_map=color_discrete_map,
        title=f'Sprachverteilung der analysierten Quellen (n={sum(norm_counts.values())}, Stand: {current_date})',
        barmode="stack",
        custom_data=['Gruppe', 'Anteil (%)']
    )

    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title='Sprachcode (ISO 639-1 + Ländercode)',
        y_title='Anzahl der Quellen'
    )
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["autosize"] = True
    # Ergänzung: Y-Achse logarithmisch skalieren
    layout["yaxis_type"] = "log"
    fig.update_layout(**layout)
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Sprachgruppe: %{customdata[0]}<br>"
            "Anzahl: %{y}<br>"
            "Anteil: %{customdata[1]:.2f}%<extra></extra>"
        )
    )
    fig.show(config={"responsive": True})
    # Tabelle ausgeben
    print(tabulate(df.sort_values("Anzahl", ascending=False), headers="keys", tablefmt="grid", showindex=False))
    export_figure_local(fig, "visualize_languages", export_fig_visualize_languages)

# Visualisierung der Verteilung von ENTRYTYPE innerhalb jeder Sprache
def visualize_language_entrytypes(bib_database):
    """
    Zeigt die Verteilung von Eintragstyp (ENTRYTYPE) innerhalb jeder Sprache als gruppiertes Balkendiagramm.
    """
    # Sprach-Mapping wie in visualize_languages
    languageMap = {
        "de": "de-DE",
        "de-de": "de-DE",
        "deutsch": "de-DE",
        "german": "de-DE",
        "ger": "de-DE",
        "en": "en-GB",
        "en-gb": "en-GB",
        "en-us": "en-US",
        "englisch": "en-GB",
        "eng": "en-GB",
        "id": "id",
        "ms": "ms",
        "de-ch": "de-CH",
        "de-a": "de-A",
    }
    # Funktion zur Normalisierung
    def normalize_lang(lang):
        l = lang.strip().lower()
        return languageMap.get(l, l)

    # Sammle (normierte Sprache, normierter Eintragstyp)
    data = []
    for entry in bib_database.entries:
        lang = entry.get('language', '').strip()
        if not lang:
            continue
        norm_lang = normalize_lang(lang)
        entrytype = entry.get('ENTRYTYPE', '').strip().lower()
        data.append({'Sprache': norm_lang, 'ENTRYTYPE': entrytype})

    if not data:
        print("⚠️ Keine Sprache/ENTRYTYPE-Daten in den Einträgen gefunden.")
        return

    df = pd.DataFrame(data)
    # Gruppieren und zählen
    grouped = df.groupby(['Sprache', 'ENTRYTYPE']).size().reset_index(name='Anzahl')
    # Spalte ENTRYTYPE zu Eintragstyp umbenennen
    grouped.rename(columns={'ENTRYTYPE': 'Eintragstyp'}, inplace=True)
    # Anteil innerhalb Sprache (%)
    grouped["Anteil innerhalb Sprache (%)"] = grouped.groupby("Sprache")["Anzahl"].transform(lambda x: (x / x.sum() * 100).round(2))
    total_entrytypes = grouped['Anzahl'].sum()
    grouped["Anteil Gesamt (%)"] = grouped['Anzahl'] / total_entrytypes * 100 if total_entrytypes else 0

    # Mapping Eintragstyp zu Typgruppe
    eintragstyp_gruppen = {
        'article': 'Artikelbasiert',
        'inproceedings': 'Artikelbasiert',
        'incollection': 'Buchbasiert',
        'book': 'Buchbasiert',
        'phdthesis': 'Graue Literatur',
        'techreport': 'Graue Literatur',
        'misc': 'Sonstige',
        'unpublished': 'Sonstige'
    }
    grouped["Typgruppe"] = grouped["Eintragstyp"].map(eintragstyp_gruppen)

    # Sortiere Sprachen nach Gesamtanzahl
    sprache_order = grouped.groupby('Sprache')['Anzahl'].sum().sort_values(ascending=False).index.tolist()
    # Eintragstypen nach Häufigkeit
    eintragstyp_order = grouped.groupby('Eintragstyp')['Anzahl'].sum().sort_values(ascending=False).index.tolist()
    # Typgruppen-Farben
    typgruppen_colors = {
        'Artikelbasiert': colors['primaryLine'],
        'Buchbasiert': colors['depthArea'],
        'Graue Literatur': colors['accent'],
        'Sonstige': colors['negativeHighlight']
    }
    # Plot
    fig = px.bar(
        grouped,
        x='Sprache',
        y='Anzahl',
        color='Typgruppe',
        category_orders={'Sprache': sprache_order, 'Eintragstyp': eintragstyp_order, 'Typgruppe': list(typgruppen_colors.keys())},
        color_discrete_map=typgruppen_colors,
        barmode="group",
        title=f'Verteilung der Eintragstypen pro Sprache (n={len(df)}, Stand: {current_date})',
        text='Anzahl',
        labels={'Sprache': 'Sprache', 'Eintragstyp': 'Eintragstyp', 'Anzahl': 'Anzahl', 'Typgruppe': 'Typgruppe'},
        custom_data=['Eintragstyp', 'Typgruppe', 'Anteil Gesamt (%)', 'Anteil innerhalb Sprache (%)']
    )
    layout = get_standard_layout(
        title=fig.layout.title.text,
        x_title='Sprache (ISO 639-1 + Ländercode)',
        y_title='Anzahl der Quellen'
    )
    layout["font"] = {"size": 14, "color": colors['text']}
    layout["title"] = {"font": {"size": 16}}
    layout["margin"] = dict(b=160, t=60, l=40, r=40)
    layout["autosize"] = True
    # Ergänzung: Y-Achse logarithmisch skalieren
    layout["yaxis_type"] = "log"
    fig.update_layout(**layout)
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Eintragstyp: %{customdata[0]}<br>"
            "Typgruppe: %{customdata[1]}<br>"
            "Anzahl: %{y}<br>"
            "Anteil gesamt: %{customdata[2]:.2f}%<br>"
            "Anteil innerhalb Sprache: %{customdata[3]:.2f}%<extra></extra>"
        )
    )
    fig.show(config={"responsive": True})
    print(tabulate(grouped.sort_values(["Sprache", "Eintragstyp"]), headers=["Sprache", "Eintragstyp", "Anzahl", "Anteil innerhalb Sprache (%)", "Typgruppe"], tablefmt="grid", showindex=False))
    export_figure_local(fig, "visualize_language_entrytypes", export_fig_visualize_languages)

#############

# Funktion zur Erstellung einer Wortwolke aus Überschriften
def create_wordcloud_from_titles(bib_database, stop_words):
    global bib_filename
    titles = [entry.get('title', '') for entry in bib_database.entries]

    # Wörter zählen
    word_counts = defaultdict(int)
    for title in titles:
        for word in title.split():
            word = word.lower().strip(",.!?\"'()[]{}:;")
            if word and word not in stop_words:
                word_counts[word] += 1

    # Wortwolke erstellen
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color=colors['background'],
        color_func=lambda *args, **kwargs: random.choice(word_colors)
    ).generate_from_frequencies(word_counts)

    # Wortwolke anzeigen
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Häufigkeitsanalyse von Titelwörtern (Stand: {current_date}) | Quelle: {bib_filename.replace(".bib", "")}', color=colors['text'])
    plt.show()

    if export_fig_create_wordcloud_from_titles and bib_filename:
        export_filename = f"wordcloud_{slugify(bib_filename.replace('.bib', ''))}.png"
        wordcloud.to_file(export_filename)
        print(f"✅ Wortwolke exportiert als '{export_filename}'")

# Aufrufen der Visualisierungsfunktionen
visualize_network(bib_database)
visualize_tags(bib_database)
visualize_index(bib_database)
visualize_research_questions(bib_database)
visualize_categories(bib_database)
visualize_relevance_vs_research_questions(bib_database)
visualize_relevance_vs_categories(bib_database)
visualize_relevance_vs_search_terms(bib_database)
visualize_time_series(bib_database)
visualize_top_authors(bib_database)
data = prepare_path_data(bib_database)
create_path_diagram(data)
create_sankey_diagram(bib_database)
visualize_sources_status(bib_database)
visualize_languages(bib_database)
visualize_language_entrytypes(bib_database)
create_wordcloud_from_titles(bib_database, stop_words)
