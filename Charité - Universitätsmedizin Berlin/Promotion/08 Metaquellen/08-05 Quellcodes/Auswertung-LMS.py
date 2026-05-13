import os
import random
import re
import sys
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud

# Pandas-Zukunftsverhalten aktivieren: kein stilles Downcasting mehr
pd.set_option('future.no_silent_downcasting', True)

# Aktuelles Datum
current_date = datetime.now().strftime("%Y-%m-%d")

SCRIPT_DIR = Path(__file__).resolve().parent
COURSE_COLUMN_LABEL = "In welchem Kurs sind Sie eingeschrieben?"
JAHRGANG_REIHENFOLGE = ["21-NFS-09", "22-NFS-09", "23-NFS-09"]
JAHRGANG_MAP = {
    "23-NFS-01": "23-NFS-09",  # Alias für abweichende Bezeichnung
}
PRINT_LOGS = False

def log_info(msg: str, *args) -> None:
    if PRINT_LOGS:
        print(msg % args if args else msg)


def log_warn(msg: str, *args) -> None:
    if PRINT_LOGS:
        print("WARN:", msg % args if args else msg)

# -------------------------------------------------------
# Konfiguration laden
# -------------------------------------------------------
CONFIG_PATH = SCRIPT_DIR / "config-auswertung-lms.py"


def _load_config():
    import importlib.util
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Konfiguration nicht gefunden: {CONFIG_PATH}")
    spec = importlib.util.spec_from_file_location("lms_config", CONFIG_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


cfg = _load_config()

# Stopplisten laden
with open(cfg.stop_words_de_path, 'r', encoding='utf-8') as file:
    stop_words_de = set(file.read().split())

with open(cfg.stop_words_en_path, 'r', encoding='utf-8') as file:
    stop_words_en = set(file.read().split())

# Kombinierte Stoppliste
stop_words = stop_words_de.union(stop_words_en)

def _ensure_ci_template_path() -> None:
    env_path = os.environ.get("CI_TEMPLATE_PATH")
    if env_path and env_path not in sys.path:
        sys.path.append(env_path)
        return

    search_roots = [SCRIPT_DIR] + list(SCRIPT_DIR.parents)
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

try:
    from ci_template import plotly_template  # type: ignore

    ACTIVE_THEME = os.environ.get("CI_TEMPLATE_THEME", cfg.theme)
    plotly_template.set_theme(ACTIVE_THEME, preserve_effects=True)
    colors = plotly_template.get_colors()

    def apply_ci_layout(fig: go.Figure, title: str, x_title: str, y_title: str) -> go.Figure:
        fig.update_layout(**plotly_template.get_standard_layout(title, x_title, y_title))
        return fig

except Exception:
    # Fallback auf lokale Farben, falls CI-Template nicht geladen werden kann
    colors = {
        "background": "#003366",
        "text": "#333333",
        "accent": "#663300",
        "primaryLine": "#660066",
        "secondaryLine": "#cc6600",
        "depthArea": "#006666",
        "brightArea": "#66CCCC",
        "positiveHighlight": "#336600",
        "negativeHighlight": "#990000",
        "white": "#ffffff",
    }

    def apply_ci_layout(fig: go.Figure, title: str, x_title: str, y_title: str) -> go.Figure:
        fig.update_layout(
            title=title,
            xaxis_title=x_title,
            yaxis_title=y_title,
            plot_bgcolor=colors["background"],
            paper_bgcolor=colors["background"],
            font=dict(color=colors["text"]),
        )
        return fig

# -------------------------------------------------------
# Pfade / Export
# -------------------------------------------------------
csv_path = Path(cfg.csv_file)
if not csv_path.is_absolute():
    csv_path = (SCRIPT_DIR / csv_path).resolve()
if not csv_path.exists():
    raise FileNotFoundError(f"CSV nicht gefunden: {csv_path}")

EXPORT_DIR = SCRIPT_DIR / "export"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)
SHOW_IN_BROWSER = getattr(cfg, "show_figures_in_browser", True)


def _slugify(name: str) -> str:
    slug = re.sub(r"[^0-9a-zA-ZäöüÄÖÜß]+", "_", name).strip("_")
    return slug[:120] if slug else "figure"


def export_figure(fig: go.Figure, name: str) -> None:
    base = EXPORT_DIR / _slugify(name)
    if getattr(cfg, "export_fig_html", False):
        fig.write_html(f"{base}.html", include_plotlyjs="cdn", auto_open=False)
    if getattr(cfg, "export_fig_png", False):
        try:
            fig.write_image(f"{base}.png", scale=2)
        except Exception:
            log_warn("PNG-Export fehlgeschlagen (Kaleido nicht verfügbar?)")
    if SHOW_IN_BROWSER:
        try:
            fig.show(renderer="browser")
        except Exception:
            fig.show()


def export_table(df: pd.DataFrame, name: str) -> None:
    """Exportiert Tabellen als CSV/JSON, falls aktiviert."""
    if not getattr(cfg, "export_tables", False):
        return
    base = EXPORT_DIR / _slugify(name)
    df.to_csv(f"{base}.csv", index=False)
    df.to_json(f"{base}.json", orient="records", force_ascii=False)

# CSV-Datei laden
if not csv_path.is_absolute():
    csv_path = (SCRIPT_DIR / csv_path).resolve()
survey_data = pd.read_csv(csv_path)
log_info("Spalten geladen: %s", list(survey_data.columns))

# Bereinigung der Spalten, Konvertierung von Ja/Nein-Fragen in numerische Werte
survey_data_cleaned = survey_data.copy()

# Saubere Handhabung von Ja/Nein-Fragen, Konvertierung zu 1 und 0
for column in survey_data_cleaned.columns:
    series = survey_data_cleaned[column]
    if series.dtype == 'object':
        mask = series.isin({'Ja', 'Nein'})
        if mask.any():
            # Nur Ja/Nein-Werte zu 1/0 mappen, Rest unverändert lassen
            mapped = series.where(~mask, series.map({'Ja': 1, 'Nein': 0}))
            survey_data_cleaned[column] = mapped
            # Falls Spalte danach ausschließlich aus 0/1 besteht, in nullable Int umwandeln
            non_na = mapped.dropna()
            if not non_na.empty and non_na.isin({0, 1}).all():
                survey_data_cleaned[column] = pd.to_numeric(mapped, errors='coerce').astype('Int64')
    else:
        survey_data_cleaned[column] = series

# Funktion zur Berechnung der statistischen Werte
def calculate_statistics(df, question):
    stats = {}
    col = _resolve_column(question, alias_map)
    if not col or col not in df.columns:
        log_warn("Spalte für Statistik nicht gefunden: %s", question)
        return stats
    valid_data = pd.to_numeric(df[col], errors="coerce").dropna()
    if valid_data.shape[0] > 0:
        stats['mean'] = valid_data.mean()
        stats['std_dev'] = valid_data.std()
    return stats

# Funktion zur Visualisierung der numerischen Daten mit den richtigen Beschriftungen und statistischen Werten
def analyze_and_plot_data(df, question, question_text, answer_labels, xaxis_label, yaxis_label, x_tick_labels):
    col = _resolve_column(question, alias_map)
    if not (col and col in df.columns):
        log_warn("Frage '%s' enthält keine numerischen Daten oder ist nicht vorhanden.", question)
        return
    # Likert-Werte als numerisch erzwingen
    valid_data = pd.to_numeric(df[col], errors='coerce').dropna()
    if valid_data.shape[0] > 0:
        # Berechne die Statistik
        stats = calculate_statistics(df, question)
        mean = stats.get('mean', 0)
        std_dev = stats.get('std_dev', 0)
        counts = valid_data.value_counts()
        y_max = counts.max()
        y_range = [0, y_max + max(2, int(y_max * 0.2))]

        fig = px.histogram(
            valid_data,
            x=valid_data,
            category_orders={question: answer_labels},
            labels={question: question_text},
            color_discrete_sequence=[colors["primaryLine"]]
        )
        apply_ci_layout(fig, f"{question_text} (n={valid_data.shape[0]:.0f})", xaxis_label, yaxis_label)
        fig.update_layout(bargap=0.2)

        # Summe der Antworten über den Balken
        fig.update_traces(texttemplate='%{y}', textposition='outside')

        # Skalierung der Achsen
        fig.update_xaxes(
            tickmode='array',
            tickvals=[1, 2, 3, 4, 5],
            ticktext=x_tick_labels,
            range=[0.5, 5.5]  # Einheitliche Skalierung der x-Achse (1–5)
        )
        fig.update_yaxes(
            tickmode='linear',
            tick0=0,
            dtick=max(1, round(y_max / 5)),
            range=y_range,
            title="Anzahl der Antworten"
        )

        # Mittelwert als Linie hinzufügen
        fig.add_shape(
            type="line",
            x0=mean, x1=mean,
            y0=0, y1=20,  # y-Achse skalieren
            line=dict(color=colors["secondaryLine"], width=2, dash="dash"),
            name="Mittelwert"
        )

        # Streuung als gefärbter Bereich hinzufügen
        fig.add_shape(
            type="rect",
            x0=mean - std_dev, x1=mean + std_dev,
            y0=0, y1=20,
            fillcolor=colors["brightArea"], opacity=0.3,
            line_width=0,
            name="Streuung"
        )

        export_figure(fig, f"likert_{question_text}")
    else:
        log_warn("Keine gültigen Daten für die Frage '%s'.", question)

# Funktion zur Visualisierung von Ja/Nein-Fragen
def analyze_and_plot_yes_no(df, question, question_text, xaxis_label, yaxis_label):
    col = _resolve_column(question, alias_map)
    if not (col and col in df.columns):
        log_warn("Frage '%s' ist nicht vorhanden.", question)
        return
    valid_data = df[col].dropna()
    if valid_data.shape[0] > 0:
        counts = valid_data.value_counts()
        y_max = counts.max()
        y_range = [0, y_max + max(1, int(y_max * 0.3))]

        # Balkendiagramm erstellen
        fig = px.bar(
            x=counts.index,
            y=counts.values,
            labels={'x': xaxis_label, 'y': yaxis_label},
            color_discrete_sequence=[colors["primaryLine"]],
            text=counts.values  # Summe der Antworten über den Balken
        )

        # Summe der Antworten über den Balken
        fig.update_traces(texttemplate='%{text}', textposition='outside')

        apply_ci_layout(fig, f"{question_text} (n={valid_data.shape[0]:.0f})", xaxis_label, yaxis_label)
        fig.update_layout(bargap=0.2)
        fig.update_yaxes(range=y_range)
        export_figure(fig, f"yes_no_{question_text}")
    else:
        log_warn("Keine gültigen Daten für die Ja/Nein-Frage '%s'.", question)

# Funktion zur Darstellung von Freitextantworten
def display_freetext_answers(df, question, question_text):
    col = _resolve_column(question, alias_map)
    if not (col and col in df.columns):
        log_warn("Frage '%s' ist nicht vorhanden.", question)
        return
    valid_data = df[col].dropna()
    if valid_data.shape[0] > 0:
        fig = go.Figure()
        for idx, answer in enumerate(valid_data):
            fig.add_trace(go.Scatter(
                x=[0], y=[idx], text=[answer], mode='markers+text',
                textposition="top left", showlegend=False
            ))

        fig.update_layout(
            title=question_text,
            xaxis=dict(showticklabels=False),
            yaxis=dict(showticklabels=False),
            plot_bgcolor=colors["background"],
            paper_bgcolor=colors["background"],
            font=dict(color=colors["text"]),
            showlegend=False
        )
        export_figure(fig, f"freetext_{question_text}")
    else:
        log_warn("Keine gültigen Freitextantworten für '%s'.", question)

# Funktion zur Erstellung der Wortwolke für Freitextantworten
def generate_wordcloud(df, freitext_column, stop_words):
    if freitext_column in df.columns:
        text_data = " ".join(df[freitext_column].dropna())
        if text_data.strip():
            text_data = re.sub(r"[^0-9a-zA-ZäöüÄÖÜß]+", " ", text_data.lower())
            # Wortfrequenzen ermitteln
            word_counts = WordCloud(stopwords=stop_words).process_text(text_data)

            # Wortwolke erstellen mit benutzerdefiniertem Farb-Schema
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color=colors['background'],
                color_func=lambda *args, **kwargs: random.choice([colors["white"], colors["brightArea"], colors["positiveHighlight"], colors["negativeHighlight"]])
            ).generate_from_frequencies(word_counts)

            # Anzeige der Wortwolke
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')  # Keine Achsen anzeigen
            plt.show()
        else:
            print(f"Keine Wörter für die Wortwolke vorhanden.")
    else:
        print(f"Freitextspalte '{freitext_column}' ist nicht vorhanden.")

# Funktion zur Erstellung der Korrelationsmatrix mit abgewinkelter x-Achsenbeschriftung
def plot_correlation_matrix(df):
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        log_warn("Keine numerischen Daten für die Korrelationsmatrix verfügbar.")
        return

    # Korrelationsmatrix berechnen
    correlation_matrix = numeric_df.corr(method="spearman")
    correlation_matrix_masked = correlation_matrix.mask(correlation_matrix.abs() < 0.2)

    # Benutzerdefinierte Farbskala
    custom_colorscale = [
        [0.0, colors["negativeHighlight"]],  # Negativste Werte
        [0.5, colors["white"]],              # 0 Werte
        [1.0, colors["positiveHighlight"]]   # Positivste Werte
    ]

    # Plotly-Heatmap erstellen
    fig = px.imshow(
        correlation_matrix_masked,
        text_auto=True,
        aspect="auto",
        color_continuous_scale=custom_colorscale
    )

    apply_ci_layout(fig, "Korrelationsmatrix der Umfragefragen (Spearman, |r|<0.2 ausgeblendet)", "Fragen", "Fragen")

    # Achsenbeschriftungen abwinkeln
    fig.update_xaxes(tickangle=45)
    fig.update_yaxes(autorange="reversed")  # Y-Achse umkehren
    export_figure(fig, "korrelation_lms")


# -------------------------------------------------------
# Zusätzliche Analysen: Deskriptive Tabellen, Skalen, Collector-Vergleiche
# -------------------------------------------------------
def _normalize_label(label: str) -> str:
    return re.sub(r"\s+", " ", str(label).strip().strip('"').replace("\n", " ")).strip()


def _build_column_alias_map(df: pd.DataFrame) -> dict[str, str]:
    return {_normalize_label(col): col for col in df.columns}


def _resolve_column(label: str, alias_map: dict[str, str]) -> str | None:
    return alias_map.get(_normalize_label(label))

# Global Alias-Map (wird nach Einlesen gesetzt)
alias_map: dict[str, str] = {}


def summarize_items(df: pd.DataFrame, questions: list[str], alias_map: dict[str, str]) -> pd.DataFrame:
    rows = []
    for question in questions:
        col = _resolve_column(question, alias_map)
        if not col:
            log_warn("Spalte nicht gefunden für Item '%s'", question)
            continue
        values = pd.to_numeric(df[col], errors="coerce").dropna()
        if values.empty:
            continue
        q25, q75 = values.quantile(0.25), values.quantile(0.75)
        rows.append(
            {
                "Item": question,
                "Spalte": col,
                "n": int(values.shape[0]),
                "Mittelwert": values.mean(),
                "SD": values.std(),
                "Median": values.median(),
                "IQR": q75 - q25,
                "Pct_Zustimmung_>=4": float((values >= 4).mean() * 100),
                "Pct_Ablehnung_<=2": float((values <= 2).mean() * 100),
            }
        )
    item_df = pd.DataFrame(rows)
    if not item_df.empty:
        export_table(item_df, "items_summary")
    return item_df


def summarize_scales(df: pd.DataFrame, scale_definitions: dict[str, list[str]], alias_map: dict[str, str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    scale_scores = {}
    rows = []
    for scale, items in scale_definitions.items():
        cols = []
        for item in items:
            col = _resolve_column(item, alias_map)
            if col:
                cols.append(col)
            else:
                log_warn("Spalte nicht gefunden für Skala '%s': %s", scale, item)
        if not cols:
            continue
        values = df[cols].apply(pd.to_numeric, errors="coerce")
        score = values.mean(axis=1)
        scale_scores[scale] = score
        valid = score.dropna()
        if valid.empty:
            continue
        q25, q75 = valid.quantile(0.25), valid.quantile(0.75)
        rows.append(
            {
                "Skala": scale,
                "Items": ", ".join(cols),
                "n": int(valid.shape[0]),
                "Mittelwert": valid.mean(),
                "SD": valid.std(),
                "Median": valid.median(),
                "IQR": q75 - q25,
                "Pct_Zustimmung_>=4": float((valid >= 4).mean() * 100),
                "Pct_Ablehnung_<=2": float((valid <= 2).mean() * 100),
            }
        )
    scale_df = pd.DataFrame(rows)
    scale_scores_df = pd.DataFrame(scale_scores)
    if not scale_df.empty:
        export_table(scale_df, "scales_summary")
    if not scale_scores_df.empty:
        export_table(scale_scores_df, "scale_scores_raw")
    return scale_scores_df, scale_df


def plot_scale_correlation(scale_scores_df: pd.DataFrame):
    if scale_scores_df.empty:
        log_warn("Keine Skalen-Scores für die Skalen-Korrelation vorhanden.")
        return
    corr = scale_scores_df.corr(method="spearman").mask(lambda x: x.abs() < 0.2)
    custom_colorscale = [
        [0.0, colors["negativeHighlight"]],
        [0.5, colors["white"]],
        [1.0, colors["positiveHighlight"]],
    ]
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale=custom_colorscale,
    )
    apply_ci_layout(fig, "Skalen-Korrelation (Spearman, |r|<0.2 ausgeblendet)", "Skalen", "Skalen")
    fig.update_xaxes(tickangle=45)
    fig.update_yaxes(autorange="reversed")
    export_figure(fig, "korrelation_skalen")


def compare_scales_by_collector(scale_scores_df: pd.DataFrame, collector_series: pd.Series):
    if scale_scores_df.empty or collector_series is None:
        log_warn("Keine Skalen-Scores oder Collector-Angaben für Gruppenvergleich vorhanden.")
        return
    combined = scale_scores_df.copy()
    combined = combined.copy()
    # Ausbildungsjahr aus Kurs-Spalte ableiten
    course_col = _resolve_column(COURSE_COLUMN_LABEL, alias_map)
    if not course_col or course_col not in survey_data_cleaned.columns:
        log_warn("Kurs-Spalte für Ausbildungsjahr nicht gefunden.")
        return
    jahrgang = survey_data_cleaned[course_col].astype(str).str.strip().replace(JAHRGANG_MAP)
    combined["Ausbildungsjahr"] = jahrgang
    combined = combined[combined["Ausbildungsjahr"].isin(JAHRGANG_REIHENFOLGE)]
    combined = combined.dropna(subset=["Ausbildungsjahr"])
    if combined.empty:
        log_warn("Keine Daten nach Jahrgangs-Bereinigung vorhanden.")
        return

    # Tabellen-Summary
    rows = []
    for scale in scale_scores_df.columns:
        grouped = combined.groupby("Ausbildungsjahr")[scale].agg(["count", "mean", "std", "median"])
        grouped["IQR"] = combined.groupby("Ausbildungsjahr")[scale].quantile(0.75) - combined.groupby("Ausbildungsjahr")[scale].quantile(0.25)
        grouped = grouped.reset_index().rename(columns={"count": "n", "mean": "Mittelwert", "std": "SD"})
        grouped["Skala"] = scale
        rows.append(grouped)
    if rows:
        table = pd.concat(rows, ignore_index=True)
        export_table(table, "scales_nach_ausbildungsjahr")

    # Boxplots je Skala
    collector_order = JAHRGANG_REIHENFOLGE
    for scale in scale_scores_df.columns:
        data = combined[["Ausbildungsjahr", scale]].dropna()
        if data.empty:
            continue
        color_sequence = [
            colors["primaryLine"],
            colors.get("secondaryLine", colors["primaryLine"]),
            colors.get("accent", colors["primaryLine"]),
            colors.get("brightArea", colors["primaryLine"]),
        ]
        fig = px.box(
            data,
            x="Ausbildungsjahr",
            y=scale,
            category_orders={"Ausbildungsjahr": collector_order} if collector_order else None,
            color="Ausbildungsjahr",
            color_discrete_sequence=color_sequence,
        )
        apply_ci_layout(fig, f"{scale} nach Ausbildungsjahr", "Ausbildungsjahr", scale)
        export_figure(fig, f"jahrgang_{scale}")


# Fragen mit ihren individuellen Achsenbeschriftungen
questions_with_labels = {
    "Wie werden komplexe Themen im LMS aufbereitet und wie beeinflusst das Ihre Lernprozesse?": (
        "Wie werden komplexe Themen im LMS aufbereitet und wie beeinflusst das Ihre Lernprozesse?",
        ["1", "2", "3", "4", "5"],
        "Komplexität der Themen",
        "Anzahl der Antworten",
        ["sehr schlecht", "eher schlecht", "neutral", "eher gut", "sehr gut"]
    ),
    "Welche Rolle spielen multimediale Inhalte im LMS für Ihr Verständnis?": (
        "Welche Rolle spielen multimediale Inhalte im LMS für Ihr Verständnis?",
        ["1", "2", "3", "4", "5"],
        "Rolle der Multimedia-Inhalte",
        "Anzahl der Antworten",
        ["keine Rolle", "geringe Rolle", "neutral", "wichtige Rolle", "sehr wichtige Rolle"]
    ),
    "Wie bewerten Sie die Klarheit und Struktur der im LMS präsentierten Informationen?": (
        "Wie bewerten Sie die Klarheit und Struktur der im LMS präsentierten Informationen?",
        ["1", "2", "3", "4", "5"],
        "Klarheit/Struktur",
        "Anzahl der Antworten",
        ["sehr unklar/unstrukturiert", "eher unklar/unstrukturiert", "neutral", "eher klar/strukturiert", "sehr klar/strukturiert"]
    ),
    "Auf welche Weise fördert das LMS aktive Diskussionen und Austausch mit anderen?": (
        "Auf welche Weise fördert das LMS aktive Diskussionen und Austausch mit anderen?",
        ["1", "2", "3", "4", "5"],
        "Diskussionsförderung",
        "Anzahl der Antworten",
        ["fördert gar nicht", "fördert wenig", "neutral", "fördert ziemlich", "fördert sehr stark"]
    ),
    "Wie unterstützt das LMS Gruppenarbeit und Kollaboration unter den Lernenden?": (
        "Wie unterstützt das LMS Gruppenarbeit und Kollaboration unter den Lernenden?",
        ["1", "2", "3", "4", "5"],
        "Unterstützung der Gruppenarbeit",
        "Anzahl der Antworten",
        ["unterstützt gar nicht", "unterstützt wenig", "neutral", "unterstützt ziemlich", "unterstützt sehr stark"]
    ),
    "Welchen Einfluss hat die Benutzeroberfläche des LMS auf Ihre Interaktionsmöglichkeiten?": (
        "Welchen Einfluss hat die Benutzeroberfläche des LMS auf Ihre Interaktionsmöglichkeiten?",
        ["1", "2", "3", "4", "5"],
        "Einfluss der Benutzeroberfläche",
        "Anzahl der Antworten",
        ["keinen Einfluss", "geringen Einfluss", "neutral", "deutlichen Einfluss", "sehr großen Einfluss"]
    ),
    "Wie zeitnah und hilfreich ist das Feedback, das Sie im LMS erhalten?": (
        "Wie zeitnah und hilfreich ist das Feedback, das Sie im LMS erhalten?",
        ["1", "2", "3", "4", "5"],
        "Zeitnahes Feedback",
        "Anzahl der Antworten",
        ["sehr schlecht", "schlecht", "neutral", "gut", "sehr gut"]
    ),
    "Inwiefern unterstützen die Bewertungssysteme im LMS Ihr Verständnis über Ihren Lernfortschritt?": (
        "Inwiefern unterstützen die Bewertungssysteme im LMS Ihr Verständnis über Ihren Lernfortschritt?",
        ["1", "2", "3", "4", "5"],
        "Verständnis über Lernfortschritt",
        "Anzahl der Antworten",
        ["sehr schlecht", "schlecht", "neutral", "gut", "sehr gut"]
    ),
    "Welche Rolle spielen Selbstbewertungstools im LMS für Ihre Selbsteinschätzung?": (
        "Welche Rolle spielen Selbstbewertungstools im LMS für Ihre Selbsteinschätzung?",
        ["1", "2", "3", "4", "5"],
        "Selbsteinschätzung durch Tools",
        "Anzahl der Antworten",
        ["keine Rolle", "geringe Rolle", "neutral", "wichtige Rolle", "sehr wichtige Rolle"]
    ),
    "Wie passt sich das LMS an Ihre individuellen Lernbedürfnisse an?": (
        "Wie passt sich das LMS an Ihre individuellen Lernbedürfnisse an?",
        ["1", "2", "3", "4", "5"],
        "Anpassung an Lernbedürfnisse",
        "Anzahl der Antworten",
        ["sehr schlecht", "schlecht", "neutral", "gut", "sehr gut"]
    ),
    "Gibt es Möglichkeiten im LMS, Lerninhalte nach Ihren Interessen und Stärken zu personalisieren?": (
        "Gibt es Möglichkeiten im LMS, Lerninhalte nach Ihren Interessen und Stärken zu personalisieren?",
        ["1", "2", "3", "4", "5"],
        "Personalisierung von Lerninhalten",
        "Anzahl der Antworten",
        ["keine Möglichkeiten", "geringe Möglichkeiten", "neutral", "viele Möglichkeiten", "sehr viele Möglichkeiten"]
    ),
    "Wie bewerten Sie die Flexibilität des LMS in Bezug auf individuelle Lernbedürfnisse?": (
        "Wie bewerten Sie die Flexibilität des LMS in Bezug auf individuelle Lernbedürfnisse?",
        ["1", "2", "3", "4", "5"],
        "Flexibilität des LMS",
        "Anzahl der Antworten",
        ["sehr unflexibel", "eher unflexibel", "neutral", "eher flexibel", "sehr flexibel"]
    ),
    "Wie einfach ist es, auf verschiedene Ressourcen im LMS zuzugreifen?": (
        "Wie einfach ist es, auf verschiedene Ressourcen im LMS zuzugreifen?",
        ["1", "2", "3", "4", "5"],
        "Zugänglichkeit von Ressourcen",
        "Anzahl der Antworten",
        ["sehr schwierig", "eher schwierig", "neutral", "eher einfach", "sehr einfach"]
    ),
    "Wie nahtlos integriert das LMS externe Lernmaterialien oder -werkzeuge?": (
        "Wie nahtlos integriert das LMS externe Lernmaterialien oder -werkzeuge?",
        ["1", "2", "3", "4", "5"],
        "Integration externer Materialien",
        "Anzahl der Antworten",
        ["gar nicht integriert", "wenig integriert", "neutral", "gut integriert", "sehr gut integriert"]
    ),
    "Wie bewerten Sie die Barrierefreiheit und Zugänglichkeit des LMS für alle Lernenden.": (
        "Wie bewerten Sie die Barrierefreiheit und Zugänglichkeit des LMS für alle Lernenden.",
        ["1", "2", "3", "4", "5"],
        "Barrierefreiheit und Zugänglichkeit",
        "Anzahl der Antworten",
        ["sehr schlecht", "schlecht", "neutral", "gut", "sehr gut"]
    )
}

COLLECTOR_ORDER = ["21-NFS-09", "22-NFS-09", "23-NFS-09"]
COLLECTOR_MAP = {
    "23-NFS-01": "23-NFS-09",  # Alias auf gewünschte 23er-Bezeichnung
}

alias_map = _build_column_alias_map(survey_data_cleaned)

if cfg.enable_yes_no:
    analyze_and_plot_yes_no(
        survey_data_cleaned,
        "Ich erkläre mich freiwillig dazu bereit, an der oben genannten Umfrage teilzunehmen. Die Ziele der Umfrage, Datenschutzbestimmungen und meine Rechte wurden ausführlich erläutert und sind mir verständlich.",
        "Teilnahmebereitschaft",
        "Antworten",
        "Anzahl",
    )

if cfg.enable_freetext:
    display_freetext_answers(
        survey_data_cleaned,
        "(fehlende) Möglichkeiten im LMS, Lerninhalte nach Ihren Interessen und Stärken zu personalisieren.",
        "Ihre Meinung zum LMS",
    )

if cfg.enable_likert:
    for question, (question_text, answer_labels, xaxis_label, yaxis_label, x_tick_labels) in questions_with_labels.items():
        analyze_and_plot_data(
            survey_data_cleaned,
            question,
            question_text,
            answer_labels,
            xaxis_label,
            yaxis_label,
            x_tick_labels,
        )

if cfg.enable_correlation:
    plot_correlation_matrix(survey_data_cleaned)

if cfg.enable_item_summary:
    summarize_items(survey_data_cleaned, list(questions_with_labels.keys()), alias_map)

scale_scores_df = pd.DataFrame()
if cfg.enable_scale_analysis:
    scale_scores_df, scale_summary_df = summarize_scales(survey_data_cleaned, cfg.scale_definitions, alias_map)

if cfg.enable_scale_correlation and not scale_scores_df.empty:
    plot_scale_correlation(scale_scores_df)

if cfg.enable_collector_comparison and not scale_scores_df.empty:
    compare_scales_by_collector(scale_scores_df, survey_data_cleaned.get("Collector"))

# Wortwolke am Schluss
if cfg.enable_wordcloud:
    generate_wordcloud(survey_data_cleaned, "Welche Anmerkungen oder Feedback haben Sie?", stop_words)
