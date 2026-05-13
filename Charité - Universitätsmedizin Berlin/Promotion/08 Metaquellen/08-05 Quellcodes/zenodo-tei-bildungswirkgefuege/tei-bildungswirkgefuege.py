# =========================================
# Import
# -----------------------------------------

import os
import sys
from pathlib import Path

os.system('cls' if os.name == 'nt' else 'clear')

BASE_DIR = Path(__file__).resolve().parent


def _ensure_ci_template_path():
    """Sucht nach dem lokalen CI-Package und hängt es bei Fund an sys.path an.

    Reihenfolge:
    1) Umgebungsvariable `CI_TEMPLATE_PATH` (falls gesetzt)
    2) Heuristische Suche relativ zum Skriptstandort
    """
    # 1) Expliziter Pfad via Umgebungsvariable
    env_path = os.environ.get("CI_TEMPLATE_PATH")
    if env_path:
        if env_path not in sys.path:
            sys.path.append(env_path)
        return
    search_roots = [BASE_DIR] + list(BASE_DIR.parents)
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

# Gemeinsamer Export-Pfad
# Standard: bisheriger Speicherort in iCloud/Documents
# Übersteuerbar via Umgebungsvariable `BILDWIRK_EXPORT_ROOT`
EXPORT_ROOT_ENV = os.environ.get("BILDWIRK_EXPORT_ROOT")
if EXPORT_ROOT_ENV:
    EXPORT_ROOT = Path(EXPORT_ROOT_ENV)
else:
    EXPORT_ROOT = (
        Path.home()
        / "Documents"
        / "scripte"
        / "Research"
        / "Eigene Forschungsprojekte"
        / "Kompetenzentwicklung"
        / "Modellpruefung"
    )
EXPORT_ROOT.mkdir(parents=True, exist_ok=True)

TEI_EXPORT_ROOT_ENV = os.environ.get("BILDWIRK_TEI_EXPORT_ROOT")
if TEI_EXPORT_ROOT_ENV:
    TEI_EXPORT_ROOT = Path(TEI_EXPORT_ROOT_ENV)
else:
    TEI_EXPORT_ROOT = EXPORT_ROOT / "tei-modellpruefung"
TEI_EXPORT_ROOT.mkdir(parents=True, exist_ok=True)

# PNG-Exportordner (übersteuerbar via Umgebungsvariable `BILDWIRK_PNG_DIR`)
PNG_DIR_ENV = os.environ.get("BILDWIRK_PNG_DIR")
if PNG_DIR_ENV:
    PNG_EXPORT_DIR = Path(PNG_DIR_ENV).expanduser()
else:
    PNG_EXPORT_DIR = (
        Path.home()
        / "Documents"
        / "Allgemein beruflich"
        / "Research"
        / "Forschungsprojekte"
        / "Systemische Kompetenzentwicklung für High Responsibility Teams"
    )
PNG_EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# Gemeinsamer CSV-Export-Ordner im Repo
CSV_EXPORT_DIR = (BASE_DIR / "Modellpruefung" / "output")
CSV_EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# Standardbibliotheken
import random  # Zufallsbibliothek
import unicodedata
import re

import logging

# Flask-Framework für Webanwendungen
from flask import Flask, request, render_template

# Datenverarbeitung und Analyse
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score

# Signalanalyse und mathematische Funktionen
from scipy.signal import find_peaks, savgol_filter
from scipy.interpolate import interp1d, make_interp_spline
from scipy.stats import gaussian_kde, norm, pearsonr
from statsmodels.nonparametric.smoothers_lowess import lowess
from math import pi
from collections import defaultdict
from copy import deepcopy

# Visualisierung
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Hinweis: Matplotlib/Seaborn werden aktuell nicht benötigt

# Netzwerkmodellierung
import networkx as nx
import subprocess

# Zeitstempel und Datum
import datetime
import warnings

# =========================================
# Eingaben
# -----------------------------------------

# Konfiguration laden
from config_bildungswirkgefuege import (
    quartale,
    initial_neugier,
    start_kompetenz,
    export_fig_visual,
    export_fig_png,
    theme,
    ansatz_wahl,
    selected_archetyp,
)

TEI_EXCEL_PATH = os.environ.get("BILDWIRK_TEI_EXCEL_PATH")
TEI_EXCEL_SHEET = os.environ.get("BILDWIRK_TEI_EXCEL_SHEET", "TEI")
TEI_EXCEL_DIR = os.environ.get("BILDWIRK_TEI_DIR")
TEI_FILE_GLOB = os.environ.get("BILDWIRK_TEI_FILE_GLOB", "*.xlsx")
TEI_SCALE_MIN = float(os.environ.get("BILDWIRK_TEI_SCALE_MIN", "1"))
TEI_SCALE_MAX = float(os.environ.get("BILDWIRK_TEI_SCALE_MAX", "5"))

# Wenn kein Env für den TEI-Ordner gesetzt ist, verwende Projekt-Default
if not TEI_EXCEL_DIR:
    _default_dir = (BASE_DIR / "TEI" / "Daten")
    if _default_dir.exists():
        TEI_EXCEL_DIR = str(_default_dir)
# Konfigurierbare Parameter für das dynamische Archetypenmatching
TEI_MATCH_WINDOW = int(os.environ.get("BILDWIRK_TEI_MATCH_WINDOW", "3"))
TEI_MATCH_HYSTERESIS = float(os.environ.get("BILDWIRK_TEI_MATCH_HYSTERESIS", "0.03"))
USE_KTT_FOR_MESS = int(os.environ.get("BILDWIRK_USE_KTT", "0"))

# Optionale TEI-Reliabilitäten (Cronbach's α) je Dimension – überschreibbar via Env
TEI_ALPHA_DEFAULTS = {
    "training_content": float(os.environ.get("TEI_ALPHA_CONTENT", "0.82")),
    "training_design": float(os.environ.get("TEI_ALPHA_DESIGN", "0.80")),
    "trainer_behavior": float(os.environ.get("TEI_ALPHA_TRAINER", "0.78")),
    "training_outcome": float(os.environ.get("TEI_ALPHA_OUTCOME", "0.85")),
}

relative_schedule = [
    ("H-NFS-01", 7), ("H-NFS-02", 32), ("H-NFS-03", 17), ("H-NFS-04", 31),
    ("H-NFS-05", 53), ("H-NFS-06", 15), ("H-NFS-07", 67), ("H-NFS-08", 77),
    ("H-NFS-09", 13), ("H-NFS-10", 42), ("H-NFS-11", 2), ("H-NFS-12", 7),
    ("H-NFS-13", 4), ("H-NFS-14", 20), ("H-NFS-15", 31), ("H-NFS-16", 48),
    ("H-NFS-17", 7), ("H-NFS-18", 12), ("H-NFS-19", 29), ("H-NFS-20-1", 39),
    ("H-NFS-20-2", 51), ("H-NFS-21", 2), ("H-NFS-22-1", 37), ("H-NFS-22-2", 16),
    ("H-NFS-23", 5), ("H-NFS-24", 2), ("H-NFS-25", 42), ("H-NFS-26", 18),
    ("H-NFS-27", 2), ("H-NFS-28", 93), ("H-NFS-29", 100), ("H-NFS-30", 5),
    ("H-NFS-31", 54), ("H-NFS-32", 40)
]
# Quartale aus der Config als Anzeige-/Skalierungsbasis sichern
CONFIG_QUARTALE = quartale
# Interne Schrittzahl entspricht der Anzahl Handlungssituationen (32)
quartale = len(relative_schedule)

tei_scores = {
    "training_content": 0.72,
    "trainer_behavior": 0.66,
    "training_design": 0.63,
    "training_outcome": 0.58
}

DIMENSION_KEY_MAP = {
    "trainingcontent": "training_content",
    "training content": "training_content",
    "content": "training_content",
    "trainerbehavior": "trainer_behavior",
    "trainer behavior": "trainer_behavior",
    "behavior": "trainer_behavior",
    "trainingdesign": "training_design",
    "training design": "training_design",
    "design": "training_design",
    "trainingoutcome": "training_outcome",
    "training outcome": "training_outcome",
    "outcome": "training_outcome",
}

PARAM_KEY_MAP = {
    "initialneugier": "initial_neugier",
    "initial_neugier": "initial_neugier",
    "neugier": "initial_neugier",
    "startkompetenz": "start_kompetenz",
    "start_kompetenz": "start_kompetenz",
    "kompetenz": "start_kompetenz",
    "archetyp": "selected_archetyp",
    "selectedarchetyp": "selected_archetyp",
    "ansatzwahl": "ansatz_wahl",
    "ansatz_wahl": "ansatz_wahl",
    "ansatz": "ansatz_wahl",
}

def _normalize_key(value):
    return re.sub(r'[^a-z0-9]', '', value.strip().lower())

def load_tei_scores_from_excel(path, sheet_name="TEI"):
    try:
        df = pd.read_excel(path, sheet_name=sheet_name)
    except Exception as exc:
        logging.warning("TEI-Excel konnte nicht geladen werden (%s): %s", sheet_name, exc)
        return {}, {}

    scores = {}
    params = {}
    present_dim_cols = [c for c in ("Dimension", "Key", "Variablenname") if c in df.columns]
    present_param_cols = [c for c in ("Parameter",) if c in df.columns]
    present_key_cols = present_dim_cols + present_param_cols
    present_val_cols = [c for c in ("Score", "Value", "Wert", "Messwert") if c in df.columns]
    for _, row in df.iterrows():
        key = ""
        for candidate in present_key_cols:
            if candidate in row.index and not pd.isna(row[candidate]):
                key = str(row[candidate])
                break
        if not key:
            continue
        value = None
        for candidate in present_val_cols:
            if candidate in row.index and not pd.isna(row[candidate]):
                value = row[candidate]
                break
        if value is None:
            continue

        norm = _normalize_key(key)
        target_dim = DIMENSION_KEY_MAP.get(norm)
        target_param = PARAM_KEY_MAP.get(norm)
        if target_dim:
            try:
                scores[target_dim] = float(value)
            except (TypeError, ValueError):
                continue
        elif target_param:
            params[target_param] = value
    return scores, params

excel_scores = {}
excel_params = {}
if TEI_EXCEL_PATH:
    excel_path = Path(TEI_EXCEL_PATH)
    if excel_path.exists():
        excel_scores, excel_params = load_tei_scores_from_excel(excel_path, TEI_EXCEL_SHEET)
        if excel_scores:
            tei_scores.update(excel_scores)
            logging.info("TEI-Scores aus Excel geladen: %s", list(excel_scores.keys()))
        if excel_params:
            logging.info("TEI-Parameter aus Excel geladen: %s", list(excel_params.keys()))
    else:
        logging.warning("TEI-Excelpfad existiert nicht: %s", excel_path)

# Excel-Parameter übernehmen
if "initial_neugier" in excel_params:
    try:
        initial_neugier = float(excel_params["initial_neugier"])
    except (TypeError, ValueError):
        logging.warning("Initiale Neugier aus Excel nicht numerisch: %s", excel_params["initial_neugier"])

if "start_kompetenz" in excel_params:
    try:
        start_kompetenz = float(excel_params["start_kompetenz"])
    except (TypeError, ValueError):
        logging.warning("Startkompetenz aus Excel nicht numerisch: %s", excel_params["start_kompetenz"])

if "selected_archetyp" in excel_params:
    selected_archetyp = str(excel_params["selected_archetyp"])

if "ansatz_wahl" in excel_params:
    try:
        ansatz_wahl = int(excel_params["ansatz_wahl"])
    except (TypeError, ValueError):
        logging.warning("Ansatzwahl aus Excel nicht ganzzahlig: %s", excel_params["ansatz_wahl"])

DIM_COLUMNS_CANDIDATES = ("Dimension", "Skala", "Konstrukt", "Scale", "Bereich", "Kategorie", "Bezeichner", "Frage")

def _norm_str(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode("ascii").lower())

DIM_NAME_MAP = {
    "trainingcontent": "training_content",
    "trainingsinhalt": "training_content",
    "content": "training_content",
    "trainerbehavior": "trainer_behavior",
    "trainerverhalten": "trainer_behavior",
    "trainingdesign": "training_design",
    "trainingsgestaltung": "training_design",
    "design": "training_design",
    "trainingoutcome": "training_outcome",
    "trainingsergebnis": "training_outcome",
    "outcome": "training_outcome",
}

LEGACY_DIMENSION_KEYWORDS = {
    "training_content": [
        "handlungsituation", "lernatmosphäre", "lernen", "spaß", "inhalt", "verständ", "sprache",
        "mitkommen", "zeit", "wissen", "themen", "problem", "beispiele", "operator", "konzept",
        "ziel", "diskussion", "durchführung"
    ],
    "trainer_behavior": [
        "lernbegleiter", "trainer", "feedback", "kolleg", "gruppe", "input", "vertrauen",
        "diskussion", "reflekt", "erfahrung", "persönlich", "ansprech", "begleitung"
    ],
    "training_design": [
        "medien", "auftrag", "struktur", "ziele", "operator", "aufgabe", "präsentation",
        "diskussionen", "ausprobieren", "design", "bearbeitung", "durchführung", "szenario",
        "fall", "beispiele", "zeit"
    ],
    "training_outcome": [
        "beruf", "anwenden", "nutzen", "nützlich", "erweit", "merken", "bericht", "ergebnis",
        "transfer", "umsetzen", "relevant", "kompeten", "praxis", "anwender", "lernen"
    ],
}

def _assign_legacy_dimension(text: str) -> str:
    if not text:
        return "training_content"
    text_l = unicodedata.normalize("NFKD", text).lower()
    scores = {dim: sum(keyword in text_l for keyword in keywords) for dim, keywords in LEGACY_DIMENSION_KEYWORDS.items()}
    best_dim, best_score = max(scores.items(), key=lambda pair: pair[1])
    if best_score == 0:
        return "training_content"
    return best_dim

def _parse_legacy_tei_csv(path: Path) -> dict:
    try:
        df = pd.read_csv(path, sep=";", encoding="utf-8", engine="python", skiprows=4)
    except Exception as exc:
        logging.warning("Legacy TEI-CSV konnte nicht gelesen werden (%s): %s", path.name, exc)
        return {}
    avg_col = next((c for c in df.columns if df[c].astype(str).str.contains("Mittelwert", case=False, na=False).any()), df.columns[-1])
    rows = df.reset_index(drop=True)
    entries = []
    # Aggregatoren pro Dimension: Summe der Bewertungen, Summe der Quadrate, Anzahl
    agg = defaultdict(lambda: {"sum": 0.0, "sum2": 0.0, "n": 0.0})
    # Kandidatenspalten für 6-stufige Likert-Zählungen (Antworten 1..6)
    count_cols = [c for c in df.columns if c not in ("Bezeichner", "Frage", avg_col)]
    for i in range(0, len(rows) - 1, 2):
        question = str(rows.iloc[i].get("Frage", "")).strip()
        avg_raw = rows.iloc[i + 1].get(avg_col)
        if not question or pd.isna(avg_raw):
            continue
        try:
            avg = float(str(avg_raw).replace(",", "."))
        except Exception:
            continue
        entries.append((question, avg))
        # Versuche, Zähler je Kategorie zu lesen (1..6)
        try:
            counts = []
            for col in count_cols:
                val = rows.iloc[i + 1].get(col)
                if pd.isna(val):
                    continue
                try:
                    counts.append(float(str(val).replace(',', '.')))
                except Exception:
                    counts.append(0.0)
            # Heuristik: nimm die ersten 6 numerischen Counts als 1..6
            counts = [c for c in counts if np.isfinite(c)]
            if len(counts) >= 6:
                counts = counts[:6]
                vals = np.arange(1, 7, dtype=float)
                n = float(np.sum(counts))
                if n > 0:
                    m = float(np.sum(vals * counts) / n)
                    m2 = float(np.sum((vals ** 2) * counts) / n)
                    var = max(0.0, m2 - m ** 2)
                    sd = float(np.sqrt(var))
                else:
                    sd = 0.0
            else:
                sd = 0.0
        except Exception:
            sd = 0.0
        # Auf Dimension mappen und Aggregate fortschreiben
        dim_key = _assign_legacy_dimension(question)
        agg_dim = agg[dim_key]
        # Für Aggregation über Items: addiere Verteilungen über second-moment (approx durch item-sd und mean)
        # Hier vereinfachen wir: addieren varianzbeiträge und n als 1 pro Item
        agg_dim["sum"] += avg
        agg_dim["sum2"] += sd ** 2
        agg_dim["n"] += 1.0
    if not entries:
        return {}
    grouped = defaultdict(list)
    for question, avg in entries:
        dim = _assign_legacy_dimension(question)
        grouped[dim].append(avg)
    result = {}
    for dim in ("training_content", "trainer_behavior", "training_design", "training_outcome"):
        values = grouped.get(dim)
        agg_dim = agg.get(dim, {"sum": 0.0, "sum2": 0.0, "n": 0.0})
        if not values:
            result[dim] = 0.5
            result[f"sd_{dim}"] = 0.0
            continue
        avg = float(np.mean(values))
        # Item-gemittelte Varianz (vereinfachte Aggregation)
        n_items = max(1.0, agg_dim.get("n", 1.0))
        sd_items = float(np.sqrt(max(0.0, agg_dim.get("sum2", 0.0) / n_items)))
        # Normalisieren auf 0..1
        m01 = float(np.clip((avg - TEI_SCALE_MIN) / max(TEI_SCALE_MAX - TEI_SCALE_MIN, 1.0), 0.0, 1.0))
        sd01 = float(np.clip(sd_items / max(TEI_SCALE_MAX - TEI_SCALE_MIN, 1.0), 0.0, 1.0))
        result[dim] = m01
        result[f"sd_{dim}"] = sd01
    logging.info("Legacy-TEI (%s) in Dimensionen distribuiert: %s", path.name, {k: len(v) for k, v in grouped.items()})
    return result

def extract_dims_from_excel_file(path, sheet_name="TEI"):
    def _read_dataframe(p):
        if p.suffix.lower() in {".csv", ".txt"}:
            return pd.read_csv(p, sep=";", encoding="utf-8", engine="python")
        return pd.read_excel(p, sheet_name=sheet_name)
    try:
        df = _read_dataframe(path)
    except Exception:
        try:
            df = _read_dataframe(path)
            logging.info("Fallback: TEI-Datei %s mit erster Quelle gelesen", path.name)
        except Exception as exc:
            logging.warning("TEI-Datei konnte nicht gelesen werden (%s): %s", path, exc)
            return {}
    if "Mittelwert" not in [str(c).strip() for c in df.columns]:
        logging.info("Keine explizite 'Mittelwert'-Spalte in %s erkannt", path)
    dim_col = next((c for c in DIM_COLUMNS_CANDIDATES if c in df.columns), None)
    if dim_col is None:
        # Fallback: try to decode the special TEI csv structure and derive dims from question text
        dims = _parse_legacy_tei_csv(path)
        if dims:
            return dims
        logging.warning("Keine Dimensionsspalte in %s gefunden", path)
        return {}
    avg_col = next((c for c in df.columns if "mittelwert" in str(c).strip().lower()), None)
    if avg_col is None:
        avg_col = df.columns[-1]
    temp = defaultdict(list)
    for _, row in df.iterrows():
        key_raw = row.get(dim_col)
        if pd.isna(key_raw):
            continue
        key = DIM_NAME_MAP.get(_norm_str(key_raw))
        if not key:
            continue
        try:
            m = float(str(row[avg_col]).replace(",", "."))
        except Exception:
            continue
        temp[key].append(m)
    out = {}
    for key, values in temp.items():
        if not values:
            continue
        avg = float(np.nanmean(values))
        m01 = float(np.clip((avg - TEI_SCALE_MIN) / max(TEI_SCALE_MAX - TEI_SCALE_MIN, 1.0), 0.0, 1.0))
        out[key] = m01
    return out

def _extract_hs_index_from_filename(p: Path) -> int:
    s = p.stem
    m = re.search(r"H[-_]?NFS[-_]?(\d{2})", s, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m2 = re.search(r"(\d{2})(?!.*\d)", s)  # letzte zwei Ziffern
    return int(m2.group(1)) if m2 else -1

def load_tei_sequence_from_dir(dir_path: str, pattern: str, sheet_name="TEI", series_len: int = 0):
    seq = [{} for _ in range(series_len)]
    p = Path(dir_path)
    supported_suffixes = {".csv", ".txt", ".xlsx", ".xls"}

    def _valid(candidate: Path) -> bool:
        return (
            candidate.is_file()
            and candidate.suffix.lower() in supported_suffixes
            and not candidate.name.startswith("~$")
        )

    files = []
    if p.exists():
        if pattern:
            files.extend(sorted(f for f in p.glob(pattern) if _valid(f)))
        else:
            files.extend(sorted(f for f in p.iterdir() if _valid(f)))
        for ext in supported_suffixes:
            for candidate in sorted(p.glob(f"*{ext}")):
                if _valid(candidate) and candidate not in files:
                    files.append(candidate)
    else:
        files = []
    loaded = []
    for f in files:
        if f.name.startswith("~$"):
            continue
        idx = _extract_hs_index_from_filename(f)
        if idx <= 0:
            continue
        dims = extract_dims_from_excel_file(f, sheet_name)
        if not dims:
            continue
        pos = min(max(idx - 1, 0), series_len - 1)
        seq[pos] = dims if dims else None
        loaded.append(idx)
    if series_len > 0 and loaded:
        missing = sorted(set(range(1, series_len + 1)) - set(loaded))
        logging.info("TEI geladen: %s | Fehlend: %s", sorted(loaded), missing)
    return seq

def export_tei_diagnostic(tei_seq, output_dir):
    rows = []
    dims = ["training_content", "trainer_behavior", "training_design", "training_outcome"]
    for idx, item in enumerate(tei_seq, start=1):
        row = {"Handlungssituation": idx}
        if item:
            for dim in dims:
                row[dim] = item.get(dim)
            row["HasData"] = True
        else:
            for dim in dims:
                row[dim] = np.nan
            row["HasData"] = False
        rows.append(row)
    df_diag = pd.DataFrame(rows)
    df_diag.to_csv(output_dir / "tei_sequence_summary.csv", index=False)


# Logging-Konfiguration
log_dir = TEI_EXPORT_ROOT
log_dir.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=str(log_dir / "modellpruefung.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Terminal leeren
os.system('cls' if os.name == 'nt' else 'clear')

# Template
from ci_template import plotly_template
plotly_template.set_theme(theme, preserve_effects=True)
pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)

quartale_range = np.arange(0, quartale + 1)


def safe_fig_show(fig):
    """Zeigt Plotly-Figuren robust an und protokolliert Berechtigungsfehler."""
    try:
        fig.show()
    except PermissionError as exc:
        logging.warning("Plotly-Anzeige konnte nicht geöffnet werden: %s", exc)


def compute_initial_bereitschaft(initial_neugier, start_kompetenz, w_n=0.55, w_k=0.45):
    """Berechnet die initiale Bereitschaft aus Neugier und Kompetenz."""
    n = float(np.clip(initial_neugier / 10.0, 0.0, 1.0))
    k = float(np.clip(start_kompetenz / 10.0, 0.0, 1.0))
    if n + k > 0.0:
        h = 2.0 * n * k / (n + k + 1e-9)
    else:
        h = 0.0
    s = w_n * n + w_k * k
    base = 0.8 * h + 0.2 * s
    return float(np.clip(10.0 * base, 0.0, 10.0))


def compute_tei_dimension_means(tei_sequence, dims=None):
    """Aggregiert TEI-Dimensionen über alle Handlungssituationen."""
    dims = dims or ("training_content", "trainer_behavior", "training_design", "training_outcome")
    aggregated = {dim: [] for dim in dims}
    for item in tei_sequence:
        if not item:
            continue
        for dim in dims:
            val = item.get(dim)
            if val is None or (isinstance(val, float) and np.isnan(val)):
                continue
            aggregated[dim].append(float(val))
    means = {}
    for dim, values in aggregated.items():
        means[dim] = float(np.nanmean(values)) if values else float("nan")
    return means


def derive_ansatz_from_dimensions(dim_means):
    """Leitet einen didaktischen Ansatz heuristisch aus TEI-Mittelwerten ab."""
    if not dim_means:
        return None, {}
    content = _clip01(dim_means.get("training_content", 0.5))
    trainer = _clip01(dim_means.get("trainer_behavior", 0.5))
    design = _clip01(dim_means.get("training_design", 0.5))
    outcome = _clip01(dim_means.get("training_outcome", 0.5))
    values = np.array([content, trainer, design, outcome], dtype=float)
    spread = float(np.nanstd(values)) if values.size else 0.0
    scores = {
        "Instruktional": 0.6 * content + 0.4 * outcome,
        "Kognitivistisch": 0.5 * content + 0.3 * design + 0.2 * outcome,
        "Behavioristisch": 0.5 * outcome + 0.3 * trainer + 0.2 * design,
        "Humanistisch": 0.5 * trainer + 0.3 * outcome + 0.2 * content,
        "Konstruktivistisch": 0.6 * design + 0.2 * content + 0.2 * trainer,
        "Soziokulturell": 0.5 * trainer + 0.3 * design + 0.2 * outcome,
        "Systemisch": 0.25 * (content + trainer + design + outcome) + 0.1 * spread,
    }
    best = max(scores, key=scores.get) if scores else None
    return best, scores


def derive_pe_profile_from_codes(pe_codes):
    """Erstellt ein PE-Profil (PFE/PLE/PFV/PGV/PSE/PEE) aus den TEI-Codes."""
    if not pe_codes:
        return {}
    profile = {}
    for key in ("PFE", "PLE", "PFV", "PGV", "PSE", "PEE"):
        values = pe_codes.get(key)
        if values is None:
            continue
        arr = np.asarray(values, dtype=float)
        if arr.size == 0 or np.isnan(arr).all():
            continue
        profile[key] = float(np.clip(np.nanmean(arr), 0.0, 1.0))
    return profile

# Basis-Helper früh bereitstellen, bevor sie in der HS-Schleife genutzt werden
try:
    _clip01  # type: ignore[name-defined]
except NameError:
    def _clip01(x):
        try:
            return float(np.clip(x, 0.0, 1.0))
        except Exception:
            return 0.0

# CI-konforme Style-Helfer (einheitliche, zentrale Definition)
_LINE_STYLE_KEYS = {
    "primary": ("line_primaryLine", "linie_primaryLine"),
    "secondary": ("line_secondaryLine", "linie_secondaryLine"),
    "accent": ("line_accent", "linie_accent"),
    "positive": ("line_positiveHighlight", "linie_positiveHighlight"),
    "negative": ("line_negativeHighlight", "linie_negativeHighlight"),
}
_MARKER_STYLE_KEYS = {
    "primary": ("marker_primaryLine",),
    "secondary": ("marker_secondaryLine",),
    "accent": ("marker_accent",),
    "positive": ("marker_positiveHighlight",),
    "negative": ("marker_negativeHighlight",),
}

def ci_line(role="primary", **overrides):
    styles = plotly_template.get_plot_styles()
    colors = plotly_template.get_colors()
    color = colors.get(
        {
            "primary": "primaryLine",
            "secondary": "secondaryLine",
            "accent": "accent",
            "positive": "positiveHighlight",
            "negative": "negativeHighlight",
        }.get(role, "primaryLine"),
        colors.get("primaryLine", "#4c78a8"),
    )
    # Default-Fall
    style = {"color": color, "width": 3}
    # Versuche, CI-Style zu übernehmen
    for key in _LINE_STYLE_KEYS.get(role, ("line_primaryLine",)):
        if key in styles:
            base = deepcopy(styles[key])
            # Sicherstellen, dass mindestens Farbe/Breite gesetzt sind
            base.setdefault("color", color)
            base.setdefault("width", 3)
            base.update(overrides)
            return base
    style.update(overrides)
    return style

def ci_marker(role="primary", **overrides):
    styles = plotly_template.get_plot_styles()
    # Default
    style = {"size": 8}
    for key in _MARKER_STYLE_KEYS.get(role, ("marker_primaryLine",)):
        if key in styles:
            base = deepcopy(styles[key])
            base.update(overrides)
            return base
    style.update(overrides)
    return style

# Archetyp → Farbzuordnung (persistente, CI-konforme Zuordnung)
# Bekannte kanonische Archetypen werden über feste Color-Keys gemappt.
ARCHETYPE_COLOR_KEYS = {
    "Pragmatisch": "primaryLine",
    "Reflektiert": "secondaryLine",
    "Resilient": "positiveHighlight",
    "Kreativ": "accent",
    "Sozial": "secondaryLine",
    "Skeptisch": "negativeHighlight",
    "Innovativ": "accent",
    "Standardlernender": "primaryLine",
    "Pechvogel": "negativeHighlight",
    "Glückspilz": "positiveHighlight",
    "Überambitioniert": "accent",
    "Zögerlich": "secondaryLine",
}

def _stable_idx(name: str, mod: int) -> int:
    # Deterministischer Index ohne Python-Hash-Zufälligkeit
    return sum(ord(c) for c in name) % max(1, mod)

def archetype_color(name: str):
    cols = plotly_template.get_colors()
    key = ARCHETYPE_COLOR_KEYS.get(name)
    if key and key in cols:
        return cols[key]
    # Fallback-Palette (deterministisch nach Name)
    palette = [
        cols.get("primaryLine"),
        cols.get("secondaryLine"),
        cols.get("accent"),
        cols.get("positiveHighlight"),
        cols.get("negativeHighlight"),
    ]
    return palette[_stable_idx(name, len(palette))]

# Mapping von ansatz_wahl auf den Namen des Ansatzes (nur ein Wort)
ansatz_namen = {
    1: "Instruktional",
    2: "Kognitivistisch",
    3: "Behavioristisch",
    4: "Humanistisch",
    5: "Konstruktivistisch",
    6: "Soziokulturell",
    7: "Systemisch"
}
ansatz_name_to_id = {v: k for k, v in ansatz_namen.items()}

gewaehlter_ansatz = ansatz_namen.get(ansatz_wahl, f"Ansatz {ansatz_wahl}")

# Strukturierte Konsolenausgabe der gewählten Parameter
"""Strukturierte Konsolenausgabe der gewählten Parameter erfolgt, sobald
die Archetypdaten (inkl. BPS) vorliegen, damit alles zusammenhängend
ausgegeben wird."""

from archetypen import archetypen, hole_archetyp, motivation_params_for, map_report_pe_to_internal

ARCHETYPE_MATCH_BLACKLIST = {"AllesPositiv", "AllesNeutral", "AllesNegativ"}
ARCHETYPEN_MATCH_REF = {
    name: data for name, data in archetypen.items()
    if name not in ARCHETYPE_MATCH_BLACKLIST
}

# =========================================
# Export Visualisierungen
# -----------------------------------------

export_fig_verhaeltnis                             = export_fig_visual
export_fig_dreidimensionale_unsicherheitsrelation  = export_fig_visual
export_fig_durchlaeufe                             = export_fig_visual
export_fig1_unsicherheiten                         = export_fig_visual
export_fig2_unsicherheitsrelation                  = export_fig_visual
export_fig3_unsicherheitsrelation                  = export_fig_visual
export_3d_unsicherheitsrelation                    = export_fig_visual
export_fig_entwicklung_neugier_motivation          = export_fig_visual
export_fig_korrelationsdynamik_neugier_motivation  = export_fig_visual
export_fig_mc                                      = export_fig_visual
export_fig_summary                                 = export_fig_visual
export_fig_kumulative_kompetenz                    = export_fig_visual
export_fig_kumulativer_vergleich                   = export_fig_visual
export_fig_histogramm                              = export_fig_visual
export_fig_einfluss                                = export_fig_visual
export_fig_einfluss_netto                          = export_fig_visual
export_fig_pe                                      = export_fig_visual
export_fig_kompetenzniveau                         = export_fig_visual
export_fig_clusters                                = export_fig_visual
export_fig_bildungswirkgefuege                     = export_fig_visual
export_bildungswirkdynamik                         = export_fig_visual
export_fig_flussdiagramm                           = export_fig_visual
export_fig_trajektorie                             = export_fig_visual
export_fig_morphologische_kompetenzentwicklung     = export_fig_visual
export_fig_spiral_combined                         = export_fig_visual
export_fig_dashboard                               = export_fig_visual
export_fig_bereitschaft                            = export_fig_visual
export_fig_bps_status                              = export_fig_visual
export_fig_bps_korrelationen                       = export_fig_visual
export_fig_bps_phase                               = export_fig_visual

export_fig_png_verhaeltnis                             = export_fig_png
export_fig_png_dreidimensionale_unsicherheitsrelation  = export_fig_png
export_fig_png_durchlaeufe                             = export_fig_png
export_fig_png1_unsicherheiten                         = export_fig_png
export_fig_png2_unsicherheitsrelation                  = export_fig_png
export_fig_png3_unsicherheitsrelation                  = export_fig_png
export_png_3d_unsicherheitsrelation                    = export_fig_png
export_fig_png_entwicklung_neugier_motivation          = export_fig_png
export_fig_png_korrelationsdynamik_neugier_motivation  = export_fig_png
export_fig_png_mc                                      = export_fig_png
export_fig_png_summary                                 = export_fig_png
export_fig_png_kumulative_kompetenz                    = export_fig_png
export_fig_png_kumulativer_vergleich                   = export_fig_png
export_fig_png_histogramm                              = export_fig_png
export_fig_png_einfluss                                = export_fig_png
export_fig_png_einfluss_netto                          = export_fig_png
export_fig_png_pe                                      = export_fig_png
export_fig_png_kompetenzniveau                         = export_fig_png
export_fig_png_clusters                                = export_fig_png
export_fig_png_bildungswirkgefuege                     = export_fig_png
export_png_bildungswirkdynamik                         = export_fig_png
export_fig_png_flussdiagramm                           = export_fig_png
export_fig_png_trajektorie                             = export_fig_png
export_fig_png_morphologische_kompetenzentwicklung     = export_fig_png
export_fig_png_spiral_combined                         = export_fig_png
export_fig_png_dashboard                               = export_fig_png
export_fig_png_bereitschaft                            = export_fig_png
export_fig_png_bps_status                              = export_fig_png
export_fig_png_bps_korrelationen                       = export_fig_png
export_fig_png_bps_phase                               = export_fig_png

# =========================================
# Funktionen
# -----------------------------------------

def slugify(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text.strip().lower()

# Hilfsfunktionen zur späteren Analyse
def flatten_and_sum(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return sum(flat_list)

def identify_extrema_and_inflection_points(data):
    maxima, _ = find_peaks(data)
    minima, _ = find_peaks(-data)
    derivative = np.gradient(data)
    inflection_points, _ = find_peaks(np.abs(np.gradient(derivative)))
    return maxima, minima, inflection_points

# Einfacher Glättungsfilter (originale Definition weiter unten entfällt)
def smooth_curve(
    data,
    polyorder=3,
    window_length=None,
    clip_max=None,
    clip_min=None,
    force_odd=True
):
    """
    Glättet eine Kurve mittels Savitzky-Golay-Filter.

    Parameter:
    - data: Array-ähnlich (Liste oder np.array)
    - polyorder: Ordnung des Polynoms (Standard: 3)
    - window_length: Länge des Glättungsfensters. Falls None, wird automatisch gesetzt.
    - clip_max: Optionaler Maximalwert zum Begrenzen (z. B. 10)
    - clip_min: Optionaler Minimalwert zum Begrenzen (z. B. 0)
    - force_odd: Ob window_length auf ungerade Zahl angepasst werden soll

    Rückgabe:
    - Geebnete und ggf. begrenzte Kurve
    """
    data = np.asarray(data, dtype=float)
    if data.size < 5:
        return data

    if clip_min is not None or clip_max is not None:
        data = np.clip(data, clip_min, clip_max)

    n = len(data)
    if window_length is None:
        window_length = min(21, n) if n % 2 == 1 else min(21, n - 1)
    if window_length >= n:
        window_length = n if n % 2 == 1 else n - 1
    if force_odd and window_length % 2 == 0:
        window_length -= 1
    if window_length < 3:
        return data

    return savgol_filter(data, window_length, polyorder)

# Erweiterte Exportfunktion für Plotly-Figuren (HTML und PNG)
def export_figure(fig, name, export_flag_html, export_flag_png):
    filename_part = f"{gewaehlter_ansatz} {selected_archetyp}"
    safe_filename = slugify(f"{name}_{filename_part}")
    remote_path = "johajo@sternenflottenakademie.local:/mnt/deep-space-nine/public/plot/"

    if export_flag_html:
        export_path_html = f"/tmp/{safe_filename}.html"
        fig.write_html(export_path_html, full_html=True, include_plotlyjs="cdn")
        try:
            subprocess.run(["scp", export_path_html, remote_path], check=True, timeout=15)
            print(f"✅ HTML-Datei '{export_path_html}' erfolgreich übertragen.")
            os.remove(export_path_html)
            print(f"🗑️ Lokale HTML-Datei '{export_path_html}' wurde gelöscht.")
        except subprocess.TimeoutExpired:
            print("⏱️ Übertragung abgebrochen (Timeout). HTML verbleibt lokal:", export_path_html)
        except subprocess.CalledProcessError as e:
            print("❌ Fehler beim HTML-Übertragen:")
            print(e.stderr)

    if export_flag_png:
        export_path_png = str(PNG_EXPORT_DIR / f"{safe_filename}.png")
        try:
            fig.write_image(export_path_png, width=1200, height=800, scale=2)
            print(f"✅ PNG-Datei lokal gespeichert: '{export_path_png}'")
        except Exception as e:
            print("❌ Fehler beim PNG-Export:", str(e))

# -----------------------------------------
# Power-Law-Modell zur Berechnung von C
# -----------------------------------------

def gamma(c):
    gamma_0 = 0.1161
    A = 0.0436
    alpha = 0.1101
    c_crit = 1.5800
    val = gamma_0 + A * np.abs(c - c_crit) ** alpha
    if np.any(np.isnan(val)) or np.any(np.isinf(val)):
        logging.error("Ungültiger Wert in gamma-Berechnung. Eingabe c=%s, Ergebnis=%s", c, val)
    return val

# -----------------------------------------
# Archetypen
# -----------------------------------------

# -----------------------------------------
# Aufgaben pro Handlungssituation (Gesamt 484)
# -----------------------------------------

task_counts = [
    6, 16, 28, 37, 31, 14, 47, 36, 11, 25, 12, 18, 15, 18, 24, 26,
    24, 36, 20, 28, 29, 15, 5, 6, 17, 19, 11, 22, 9, 61, 55, 13, 54, 60
]


# =========================================
# Zeit & Indexvorbereitung
# -----------------------------------------

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

quartale_range = np.arange(0, quartale + 1)
schedule_durations = np.array([duration for _, duration in relative_schedule], dtype=float)
total_duration = float(schedule_durations.sum()) if schedule_durations.size else 1.0
duration_ratios = (
    schedule_durations / total_duration
    if total_duration > 0 and schedule_durations.size
    else np.full(len(schedule_durations), 1.0 / max(len(schedule_durations), 1), dtype=float)
)
# Zeitachse in Quartalen, aber die Punkte liegen zum Ende jeder HS
# (kumulierte Tage → auf Quartalsskala [0..quartale] skaliert)
time_axis_quartale = (
    np.insert(np.cumsum(schedule_durations), 0, 0.0) / (total_duration if total_duration > 0 else 1.0)
) * float(CONFIG_QUARTALE)
std_ddof = 0

tei_content = float(tei_scores.get("training_content", 0.5))
tei_trainer = float(tei_scores.get("trainer_behavior", 0.5))
tei_design = float(tei_scores.get("training_design", 0.5))
tei_outcome = float(tei_scores.get("training_outcome", 0.5))

competence_series = [start_kompetenz]
motivation_series = [min(10.0, initial_neugier + 0.5 * tei_trainer)]
neugier_series = [initial_neugier]
initial_bereitschaft = compute_initial_bereitschaft(initial_neugier, start_kompetenz)
bereitschafts_values = [initial_bereitschaft]
print(f"  🚀 Start-Bereitschaft (aus N & K): {initial_bereitschaft:.2f}")

# TEI-Sequenz vorbereiten (ohne Env, mit Projekt-Default), damit jede HS empirisch gespeist wird
len_series = quartale
if TEI_EXCEL_DIR:
    tei_seq = load_tei_sequence_from_dir(TEI_EXCEL_DIR, TEI_FILE_GLOB, TEI_EXCEL_SHEET, len_series)
    # Logging der geladenen und fehlenden Handlungssituationen
    _loaded_idx = [i + 1 for i, d in enumerate(tei_seq) if d]
    _missing_idx = [i + 1 for i, d in enumerate(tei_seq) if not d]
    logging.info("TEI-Loader: geladen=%s | fehlend=%s", _loaded_idx, _missing_idx)
else:
    tei_seq = [tei_scores for _ in range(len_series)]
export_tei_diagnostic(tei_seq, CSV_EXPORT_DIR)
pe_effects = [0.0]

# BPS-Startwerte empirisch aus Startgrößen (K, N, Bereitschaft) und erstem TEI ableiten
def _norm01(v):
    try:
        return float(np.clip(v, 0.0, 1.0))
    except Exception:
        return 0.0

def _n10(v):
    try:
        return _norm01((float(v) if v is not None else 0.0) / 10.0)
    except Exception:
        return 0.0

_first = tei_seq[0] if tei_seq and tei_seq[0] else {}
_c = _norm01(_first.get("training_content", 0.5))
_t = _norm01(_first.get("trainer_behavior", 0.5))
_d = _norm01(_first.get("training_design", 0.5))
_o = _norm01(_first.get("training_outcome", 0.5))

_K0 = _n10(start_kompetenz)
_N0 = _n10(initial_neugier)
_B0 = _n10(initial_bereitschaft)

bio_startstatus = _norm01(0.5 * _K0 + 0.3 * _o + 0.2 * _c)
psy_startstatus = _norm01(0.5 * _N0 + 0.3 * _t + 0.2 * _o)
soz_startstatus = _norm01(0.6 * _B0 + 0.4 * _d)

bio_status = [bio_startstatus]
psy_status = [psy_startstatus]
soz_status = [soz_startstatus]
mikro_motivation = []

for idx in range(1, quartale + 1):
    ratio = duration_ratios[idx - 1] if idx - 1 < duration_ratios.size else 1.0
    design_factor = ratio
    # TEI-Werte pro Handlungssituation (empirisch, 0..1), Fallback 0.5
    tei_vals = tei_seq[idx - 1] if idx - 1 < len(tei_seq) and tei_seq[idx - 1] else {}
    tei_content = _clip01(tei_vals.get("training_content", 0.5))
    tei_trainer = _clip01(tei_vals.get("trainer_behavior", 0.5))
    tei_design = _clip01(tei_vals.get("training_design", 0.5))
    tei_outcome = _clip01(tei_vals.get("training_outcome", 0.5))

    # Kompetenzzuwachs: Content × Design × Trainer (skalierter Effekt)
    competence_gain = (1.0 + tei_content) * design_factor * (1.0 + tei_design * 0.5) * 0.4
    competence_gain += 0.1 * tei_outcome  # Outcome trägt moderat zu beobachtbarem Zuwachs bei
    competence_gain = min(competence_gain, 1.4)
    new_competence = np.clip(competence_series[-1] + competence_gain, 0.0, 10.0)
    competence_series.append(new_competence)

    # Motivation: Trainer × Design × Outcome, mit Dämpfung bei hohem K‑Niveau
    motivation_gain = 0.35 * tei_trainer * design_factor + 0.25 * tei_outcome
    motivation_gain -= 0.02 * ((new_competence - start_kompetenz) / 10.0)
    new_motivation = np.clip(motivation_series[-1] + motivation_gain, 0.0, 10.0)
    motivation_series.append(new_motivation)

    # Neugier: Content + Outcome (kognitive Aktivierung), etwas Trainer
    neugier_gain = 0.18 * tei_content + 0.10 * tei_outcome + 0.06 * tei_trainer
    neugier_gain += 0.04 * design_factor
    neugier_gain -= 0.02 * (new_competence / 10.0)
    new_neugier = np.clip(neugier_series[-1] + neugier_gain, 0.0, 10.0)
    neugier_series.append(new_neugier)

    mikro_motivation.append(new_motivation - motivation_series[-2])

    pe_val = (tei_outcome - 0.5) * design_factor
    pe_effects.append(pe_val)

    bio_status.append(np.clip(bio_status[-1] + 0.02 * pe_val, 0.0, 1.0))
    psy_status.append(np.clip(psy_status[-1] + 0.03 * (tei_trainer - 0.5), 0.0, 1.0))
    soz_status.append(np.clip(soz_status[-1] + 0.02 * (design_factor - 0.4), 0.0, 1.0))

    bereit = design_factor + new_motivation + new_neugier + pe_val
    bereitschafts_values.append(bereit)

delta_m_micro_series = np.array([0.0] + mikro_motivation)

simulations_ergebnisse_pe = pd.DataFrame(
    {"TEI_Kompetenz": competence_series},
    index=quartale_range
)
bereitschaftssteigerungen = pd.DataFrame(
    {"Bereitschaft": bereitschafts_values},
    index=quartale_range
)
kompetenzniveaus_df = pd.DataFrame(
    {"TEI_Kompetenz": competence_series},
    index=quartale_range
)
neugier_entwicklung_df = pd.DataFrame(
    {"TEI_Neugier": neugier_series},
    index=quartale_range
)
pe_auswirkungen_df = pd.DataFrame(
    {"PE": pe_effects},
    index=quartale_range
)
veranderungen_neugier = [neugier_series]
veranderungen_motivation = [motivation_series]
mikro_motivation_lauf = [delta_m_micro_series.tolist()]
bio_status_lauf = [bio_status]
psy_status_lauf = [psy_status]
soz_status_lauf = [soz_status]

# =========================================
# Post-Processing & Ableitungen
# -----------------------------------------

# Sicherstellen, dass alle Kompetenzniveaus auf maximal 10 beschränkt sind
simulations_ergebnisse_pe_clipped = simulations_ergebnisse_pe.clip(upper=10)

# Index zurücksetzen, falls der Startindex nicht 0 ist
if simulations_ergebnisse_pe_clipped.index[0] > 0:
    simulations_ergebnisse_pe_clipped.reset_index(drop=True, inplace=True)

# Konvertierung der Datentypen falls notwendig
bereitschaftssteigerungen = bereitschaftssteigerungen.infer_objects(copy=False)
pe_auswirkungen_df = pe_auswirkungen_df.infer_objects(copy=False)

# Berechnung der Mittelwerte für Bereitschaft und PE-Auswirkungen
mittelwerte_bereitschaft = bereitschaftssteigerungen.mean(axis=0)
mittelwerte_pe = pe_auswirkungen_df.mean(axis=1)

# Berechnung der Median- und Mittelwerte sowie der Standardabweichung für die beschränkten Kompetenzwerte
mediane_kompetenz = simulations_ergebnisse_pe_clipped.median(axis=1)
mittelwerte_kompetenz = simulations_ergebnisse_pe_clipped.mean(axis=1)
# Streuung als rollierende Std der Residuen (aus der TEI-basierten Kompetenzreihe)
_comp_raw = pd.Series(competence_series, dtype='float')
_comp_trend = pd.Series(smooth_curve(competence_series, clip_max=10), dtype='float')
_comp_resid = _comp_raw - _comp_trend
stddev_kompetenz = (
    _comp_resid.rolling(window=3, min_periods=1).std(ddof=0)
    .fillna(0.0)
    .clip(lower=0.0, upper=10.0)
)

competence_array_np = np.asarray(competence_series, dtype=float)
delta_k_entw = np.diff(competence_array_np, prepend=competence_array_np[0])
# Messunsicherheit als Std der Residuen (raw minus Trend) mit kleinem Rolling‑Fenster
_trend_comp = np.asarray(smooth_curve(competence_array_np, clip_max=10), dtype=float)
_resid_comp = competence_array_np - _trend_comp
rolling_std = (
    pd.Series(_resid_comp)
    .rolling(window=3, min_periods=1)
    .std(ddof=0)
    .fillna(0.0)
    .to_numpy(dtype=float)
)
delta_k_mess = np.clip(rolling_std, 1e-6, None)
messunsicherheiten_lauf = [delta_k_mess.tolist()]

pe_wirkungen = pe_effects

# Mittelwerte Neugier und Motivation sowie deren Differenz
mittelwerte_neugier = np.mean(veranderungen_neugier, axis=0)
mittelwerte_motivation = np.mean(veranderungen_motivation, axis=0)
diff_neugier_motivation = np.array(mittelwerte_neugier) - np.array(mittelwerte_motivation)
kumulative_diff_neugier_motivation = np.cumsum(diff_neugier_motivation)

# Pearson-Korrelation Neugier/Motivation
neugier_zeitpunkt = np.array(mittelwerte_neugier)
motivation_zeitpunkt = np.array(mittelwerte_motivation)
r_neugier_motivation = np.nan if np.std(neugier_zeitpunkt) == 0 or np.std(motivation_zeitpunkt) == 0 else pearsonr(neugier_zeitpunkt, motivation_zeitpunkt)[0]

messunsicherheiten_array = np.asarray(messunsicherheiten_lauf, dtype=float)
mikro_motivation_array = np.asarray(mikro_motivation_lauf, dtype=float)
delta_m_micro_series = np.nanmean(mikro_motivation_array, axis=0)
if delta_m_micro_series.ndim == 0:
    delta_m_micro_series = np.array([float(delta_m_micro_series)])
if delta_m_micro_series.shape[0] < len(quartale_range):
    pad_width = len(quartale_range) - delta_m_micro_series.shape[0]
    delta_m_micro_series = np.pad(
        delta_m_micro_series,
        (pad_width, 0),
        mode='constant',
        constant_values=0.0
    )

bio_status_array = np.asarray(bio_status_lauf, dtype=float)
psy_status_array = np.asarray(psy_status_lauf, dtype=float)
soz_status_array = np.asarray(soz_status_lauf, dtype=float)
mittelwerte_bio_status = np.nanmean(bio_status_array, axis=0)
mittelwerte_psy_status = np.nanmean(psy_status_array, axis=0)
mittelwerte_soz_status = np.nanmean(soz_status_array, axis=0)
bps_index = quartale_range[: len(mittelwerte_bio_status)]
bps_status_df = pd.DataFrame(
    {
        "Bio": mittelwerte_bio_status[: len(bps_index)],
        "Psy": mittelwerte_psy_status[: len(bps_index)],
        "Soz": mittelwerte_soz_status[: len(bps_index)]
    },
    index=bps_index
)
bps_status_df.index.name = "Quartal"
time_x = time_axis_quartale[: len(simulations_ergebnisse_pe.index)]
time_x_list = time_x.tolist()
bps_time_x = time_axis_quartale[: len(bps_status_df.index)]
bio_status_mean = round(float(np.nanmean(mittelwerte_bio_status)), 3)
psy_status_mean = round(float(np.nanmean(mittelwerte_psy_status)), 3)
soz_status_mean = round(float(np.nanmean(mittelwerte_soz_status)), 3)
logging.info(
    "BPS mean status: bio=%s, psy=%s, soz=%s",
    bio_status_mean,
    psy_status_mean,
    soz_status_mean
)

# =========================================
# TEI → Dynamischer Archetyp (PE+BPS-basiert)
# -----------------------------------------
def _clip01(x):
    try:
        return float(np.clip(x, 0.0, 1.0))
    except Exception:
        return 0.0

def derive_pe_from_tei(tei_sequence, length):
    """
    Leitet PE-Komponenten je Handlungssituation aus TEI-Scores ab.
    Erwartet eine Sequenz von Dicts mit Schlüsseln
    {training_content, trainer_behavior, training_design, training_outcome}.

    Rückgabe: dict mit Arrays [0..1] für motivation, volition, regulation, emotion.
    """
    # Broadcast eines einzelnen Dicts auf die Länge der Zeitreihe
    if isinstance(tei_sequence, dict):
        tei_sequence = [tei_sequence for _ in range(length)]

    mot, vol, reg, emo = [], [], [], []
    for item in tei_sequence[:length]:
        c = _clip01(item.get("training_content", 0.5))
        tr = _clip01(item.get("trainer_behavior", 0.5))
        d = _clip01(item.get("training_design", 0.5))
        o = _clip01(item.get("training_outcome", 0.5))
        # Heuristische Ableitung (transparent):
        # Motivation ~ Trainerunterstützung × Outcome
        mot.append(_clip01(0.6 * tr + 0.4 * o))
        # Volition ~ Design × Outcome (Transfer-/Umsetzungsneigung)
        vol.append(_clip01(0.7 * d + 0.3 * o))
        # Regulation ~ Design × (1 + Trainer/2)
        reg.append(_clip01(0.7 * d + 0.3 * tr))
        # Emotion ~ Outcome − Frustration, approximiert über (Trainer, Outcome)
        emo.append(_clip01(0.5 * tr + 0.5 * o))
    return {
        "motivation": np.array(mot, dtype=float),
        "volition": np.array(vol, dtype=float),
        "regulation": np.array(reg, dtype=float),
        "emotion": np.array(emo, dtype=float),
    }

def derive_pe_codes_from_tei(tei_sequence, length, weights=None):
    """
    Leitet PE-Codes (PFV, PGV, PSE, PEE, PFE, PLE) je HS aus TEI ab und
    liefert deren Mittelwerte über die Zeit (0..1). PFE/PLE werden als
    inverse Proxies zu Content/Outcome konservativ geschätzt.
    """
    if isinstance(tei_sequence, dict):
        tei_sequence = [tei_sequence for _ in range(length)]
    vals = {k: [] for k in ("PFV","PGV","PSE","PEE","PFE","PLE")}
    for item in tei_sequence[:length]:
        c = _clip01(item.get("training_content", 0.5))
        tr = _clip01(item.get("trainer_behavior", 0.5))
        d = _clip01(item.get("training_design", 0.5))
        o = _clip01(item.get("training_outcome", 0.5))
        vals["PFV"].append(c)
        vals["PGV"].append(d)
        vals["PSE"].append(tr)
        vals["PEE"].append(o)
        vals["PFE"].append(_clip01(1.0 - c))
        vals["PLE"].append(_clip01(1.0 - o))
    out = {}
    for k, v in vals.items():
        arr = np.array(v, dtype=float)
        if arr.size == 0:
            out[k] = 0.0
        elif weights is not None and len(weights) >= arr.size:
            w = np.array(weights[:arr.size], dtype=float)
            out[k] = float(np.average(arr, weights=w))
        else:
            out[k] = float(np.nanmean(arr))
    return out

def _cosine_distance(a, b, eps=1e-8):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    na = np.linalg.norm(a) + eps
    nb = np.linalg.norm(b) + eps
    return 1.0 - float(np.dot(a, b) / (na * nb))

def match_archetype_dynamic(pe_components, bps_bio, bps_psy, bps_soz,
                            archetypen_ref,
                            w_pe=0.6, w_bps=0.4,
                            window=3, hysteresis_margin=0.03):
    """
    Weist je Zeitindex t den nächsten Archetyp zu, basierend auf PE+BPS.
    - pe_components: dict mit Arrays (motivation, volition, regulation, emotion)
    - bps_*: Arrays 0..1
    - archetypen_ref: dict aus archetypen.py
    Rückgabe: (trace:list[str], confidence:np.ndarray, dist_matrix:dict[name->np.ndarray])
    """
    T = int(min(len(pe_components["motivation"]), len(bps_bio), len(bps_psy), len(bps_soz)))
    # Referenzvektoren der Archetypen aus PE und biosozialem Profil ableiten
    ref_vectors = {}
    names = []
    for name, data in archetypen_ref.items():
        pe = data.get("PE", {})
        bps = data.get("biosozial", {})
        # Heuristische Reduktion der 6 PE-Schlüssel auf 4 Komponenten
        # Motivation ~ PSE + PEE
        pe_mot = _clip01(0.5 * float(pe.get("PSE", 0.0)) + 0.5 * float(pe.get("PEE", 0.0)))
        # Volition ~ PFV
        pe_vol = _clip01(float(pe.get("PFV", 0.0)))
        # Regulation ~ PGV (Gruppendynamik/Organisation)
        pe_reg = _clip01(float(pe.get("PGV", 0.0)))
        # Emotion ~ PEE − PFE (positiv minus Frustration)
        pe_emo = _clip01(0.7 * float(pe.get("PEE", 0.0)) - 0.3 * float(pe.get("PFE", 0.0)))
        v_pe = np.array([pe_mot, pe_vol, pe_reg, pe_emo], dtype=float)
        v_bps = np.array([
            _clip01(bps.get("bio", 0.5)),
            _clip01(bps.get("psy", 0.5)),
            _clip01(bps.get("soz", 0.5))
        ], dtype=float)
        ref_vectors[name] = (v_pe, v_bps)
        names.append(name)

    trace = []
    confidence = np.zeros(T, dtype=float)
    dist_hist = {n: np.zeros(T, dtype=float) for n in names}

    def best_match(v_pe_t, v_bps_t):
        scores = {}
        for n in names:
            r_pe, r_bps = ref_vectors[n]
            d_pe = _cosine_distance(v_pe_t, r_pe)
            d_bps = _cosine_distance(v_bps_t, r_bps)
            scores[n] = w_pe * d_pe + w_bps * d_bps
        best = min(scores, key=scores.get)
        return best, scores

    prev = None
    for t in range(T):
        v_pe_t = np.array([
            pe_components["motivation"][t],
            pe_components["volition"][t],
            pe_components["regulation"][t],
            pe_components["emotion"][t]
        ], dtype=float)
        v_bps_t = np.array([bps_bio[t], bps_psy[t], bps_soz[t]], dtype=float)
        # Ergänzung: NaN-Check für PE/BPS
        if any(np.isnan(v) for v in v_pe_t) or any(np.isnan(v) for v in v_bps_t):
            trace.append(prev if prev else "Unbekannt")
            confidence[t] = 0.0
            continue
        cand, scores = best_match(v_pe_t, v_bps_t)
        for n in names:
            dist_hist[n][t] = scores[n]
        # Rolling Window-Mehrheit (wenn verfügbar)
        if t+1 >= window:
            last = trace[-(window-1):] if window > 1 else []
            pool = last + [cand]
            maj = max(set(pool), key=pool.count)
        else:
            maj = cand
        # Hysterese: Wechsle nur bei ausreichendem Distanzgewinn
        if prev is not None and maj != prev and prev in scores:
            if scores[maj] >= scores[prev] - hysteresis_margin:
                maj = prev
        trace.append(maj)
        prev = maj
        # Confidence-Berechnung: Top-2-Distanzformel
        sorted_d = sorted(scores.values())
        d1, d2 = sorted_d[0], sorted_d[1] if len(sorted_d) > 1 else (sorted_d[0], sorted_d[0]+1e-6)
        confidence[t] = float(np.clip((d2 - d1) / (d2 + 1e-6), 0.0, 1.0))

    return trace, confidence, dist_hist

def analyze_archetype_trace(trace, confidence, title_prefix="Archetyp-Dynamik", x_axis=None):
    """
    Erstellt einfache Diagnostikplots: Zeitverlauf (numerisch codiert),
    Übergangsmatrix (Heatmap) und Confidence-Linie.
    """
    names = list(dict.fromkeys(trace))  # Reihenfolge der ersten Auftritte
    name_to_idx = {n: i for i, n in enumerate(sorted(set(trace)))}
    y_vals = [name_to_idx[n] for n in trace]

    fig_timeline = go.Figure()
    x_vals = list(range(len(trace))) if x_axis is None else list(x_axis[: len(trace)])
    fig_timeline.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines+markers',
        line=ci_line("primary"),
        name='Archetyp (Index)'
    ))
    fig_timeline.update_layout(**plotly_template.get_standard_layout(
        title=f'{title_prefix}: Zeitverlauf',
        x_title='Zeit (Quartale)', y_title='Archetyp (Index)'
    ))

    # Übergangsmatrix
    uniq = sorted(set(trace))
    k = len(uniq)
    mat = np.zeros((k, k), dtype=int)
    idx = {n: i for i, n in enumerate(uniq)}
    for a, b in zip(trace[:-1], trace[1:]):
        mat[idx[a], idx[b]] += 1
    fig_trans = go.Figure(data=go.Heatmap(
        z=mat, x=uniq, y=uniq, colorscale='Blues'
    ))
    fig_trans.update_layout(**plotly_template.get_standard_layout(
        title=f'{title_prefix}: Übergangsmatrix', x_title='nach', y_title='von'
    ))

    # Confidence
    fig_conf = go.Figure()
    fig_conf.add_trace(go.Scatter(
        x=(list(range(len(confidence))) if x_axis is None else list(x_axis[: len(confidence)])), y=confidence,
        mode='lines+markers', line=ci_line("secondary"), name='Confidence'
    ))
    conf_layout = plotly_template.get_standard_layout(
        title=f'{title_prefix}: Confidence', x_title='Zeit (Quartale)', y_title='Confidence (0..1)'
    )
    # Achsenskalierung: 0..1 für Confidence, 0..CONFIG_QUARTALE für Zeitachse (wenn vorhanden)
    conf_layout['yaxis'] = {**conf_layout.get('yaxis', {}), 'range': [0, 1]}
    if x_axis is not None and 'CONFIG_QUARTALE' in globals():
        conf_layout['xaxis'] = {**conf_layout.get('xaxis', {}), 'range': [0, float(CONFIG_QUARTALE)]}
    fig_conf.update_layout(**conf_layout)

    return fig_timeline, fig_trans, fig_conf

# Ableitung für aktuelle TEI-Zeitreihe anwenden (tei_seq/len_series wurden vor der HS-Schleife gesetzt)
pe_time = derive_pe_from_tei(tei_seq, len_series)
# TEI-abgeleitete Matching-Parameter: Gewichtung nach Varianz, Fenster/Hysterese datengetrieben
def _series_var(a):
    try:
        aa = np.asarray(a, dtype=float)
        return float(np.nanstd(aa))
    except Exception:
        return 0.0
pe_var = np.mean([
    _series_var(pe_time.get('motivation', [])),
    _series_var(pe_time.get('volition', [])),
    _series_var(pe_time.get('regulation', [])),
    _series_var(pe_time.get('emotion', [])),
])
bps_var = np.mean([
    _series_var(mittelwerte_bio_status[:len_series]),
    _series_var(mittelwerte_psy_status[:len_series]),
    _series_var(mittelwerte_soz_status[:len_series]),
])
_den = max(1e-6, pe_var + bps_var)
_w_pe = float(np.clip(pe_var / _den, 0.2, 0.8))
_w_bps = 1.0 - _w_pe
# Fenster abhängig von Gesamtdispersion (3..6), Hysterese gegensinnig (0.01..0.08)
disp = float(np.clip(pe_var + bps_var, 0.0, 1.0))
_win = int(np.clip(round(3 + 3*disp), 3, 6))
_hys = float(np.clip(0.08 - 0.07*disp, 0.01, 0.08))
trace, trace_conf, trace_dists = match_archetype_dynamic(
    pe_time,
    mittelwerte_bio_status[:len_series],
    mittelwerte_psy_status[:len_series],
    mittelwerte_soz_status[:len_series],
    ARCHETYPEN_MATCH_REF,
    w_pe=_w_pe, w_bps=_w_bps,
    window=_win,
    hysteresis_margin=_hys
)

# TEI-PE-Profil (Codes) als Basis für Visualisierungen/Parameter bevorzugen
try:
    # Dauer-basierte Gewichtung je HS
    schedule_durations = np.array([duration for _, duration in relative_schedule], dtype=float)
    total_duration = float(schedule_durations.sum()) if schedule_durations.size else 1.0
    weights = (schedule_durations / total_duration) if total_duration > 0 else None
except Exception:
    weights = None
PE_CODES_VISUALS = derive_pe_codes_from_tei(tei_seq, len_series, weights=weights)

dimension_means = compute_tei_dimension_means(tei_seq)
derived_ansatz_name, ansatz_scores = derive_ansatz_from_dimensions(dimension_means)
if derived_ansatz_name and derived_ansatz_name in ansatz_name_to_id:
    ansatz_wahl = ansatz_name_to_id[derived_ansatz_name]
    gewaehlter_ansatz = derived_ansatz_name
    logging.info("TEI-Ansatz-Scores: %s", ansatz_scores)
TEI_ANSATZ = gewaehlter_ansatz

from collections import Counter as _Counter
_n_trace = len(trace)
TEI_ARCH_START = trace[0] if _n_trace else None
TEI_ARCH_MODAL = (max(_Counter(trace), key=_Counter(trace).get) if _n_trace else None)
TEI_ARCH_END = trace[-1] if _n_trace else None
TEI_ARCH_WECHSEL = sum(1 for i in range(1, _n_trace) if trace[i] != trace[i-1]) if _n_trace else 0
TEI_ARCH_CONF_MEAN = float(np.nanmean(trace_conf)) if _n_trace else float('nan')

derived_archetyp_name = TEI_ARCH_MODAL or TEI_ARCH_START or selected_archetyp
base_archetyp_template = hole_archetyp(derived_archetyp_name) or hole_archetyp(selected_archetyp) or {}
selected_archetyp = derived_archetyp_name or selected_archetyp

derived_pe_profile = derive_pe_profile_from_codes(PE_CODES_VISUALS)
if not derived_pe_profile and "PE" in base_archetyp_template:
    derived_pe_profile = {k: float(v) for k, v in base_archetyp_template["PE"].items()}
if not derived_pe_profile:
    derived_pe_profile = {k: 0.5 for k in ("PFE", "PLE", "PFV", "PGV", "PSE", "PEE")}
pe_auswirkungen = derived_pe_profile

bio_startstatus = float(np.clip(bio_status[0], 0.0, 1.0)) if bio_status else float('nan')
psy_startstatus = float(np.clip(psy_status[0], 0.0, 1.0)) if psy_status else float('nan')
soz_startstatus = float(np.clip(soz_status[0], 0.0, 1.0)) if soz_status else float('nan')
if not np.isfinite(bio_startstatus):
    bio_startstatus = float(base_archetyp_template.get("biosozial", {}).get("bio", 0.5))
if not np.isfinite(psy_startstatus):
    psy_startstatus = float(base_archetyp_template.get("biosozial", {}).get("psy", 0.5))
if not np.isfinite(soz_startstatus):
    soz_startstatus = float(base_archetyp_template.get("biosozial", {}).get("soz", 0.5))
biosoziales_profil = {
    "bio": float(np.clip(bio_startstatus, 0.0, 1.0)),
    "psy": float(np.clip(psy_startstatus, 0.0, 1.0)),
    "soz": float(np.clip(soz_startstatus, 0.0, 1.0))
}

bereitschafts_std = float(np.nanstd(bereitschafts_values, ddof=1)) if len(bereitschafts_values) > 1 else 0.0
if not np.isfinite(bereitschafts_std) or bereitschafts_std == 0.0:
    bereitschafts_std = float(base_archetyp_template.get("Bereitschafts_Std", 0.3))
delta_bereitschaft = bereitschafts_std

_mot = motivation_params_for(selected_archetyp, pe_auswirkungen)
alpha_c = _mot["alpha_c"]
alpha_dm = _mot["alpha_dm"]
alpha_dk = _mot["alpha_dk"]
alpha_pe = _mot["alpha_pe"]
alpha_n = _mot["alpha_n"]
eta_motivation = _mot["eta_motivation"]
sigma_C = _mot["sigma_C"]
C_opt = _mot["C_opt"]

print("🧩 TEI-basierte Parametrisierung aktiviert:")
print(f"  📊 Handlungssituationen: {len(relative_schedule)}")
print(f"  🧠 Initiale Neugier: {initial_neugier:.3f} | 🎯 Startkompetenz: {start_kompetenz:.3f}")
print(f"  🎨 Theme: {plotly_template.get_theme()} | Export: HTML={export_fig_visual} PNG={export_fig_png}")
print(f"  🧭 Ansatz (TEI): {gewaehlter_ansatz} (ID {ansatz_wahl})")
print(f"  🧬 Archetyp (TEI): {selected_archetyp} | Confidence Ø {TEI_ARCH_CONF_MEAN:.3f}")
print(
    f"  🧱 BPS-Profil Start: Bio {biosoziales_profil['bio']:.2f} | "
    f"Psy {biosoziales_profil['psy']:.2f} | Soz {biosoziales_profil['soz']:.2f}"
)
print(
    "  🔧 PE-Profile (Mean): "
    + ", ".join(f"{k}={v:.2f}" for k, v in pe_auswirkungen.items())
)

fig_arch_timeline, fig_arch_trans, fig_arch_conf = analyze_archetype_trace(trace, trace_conf, x_axis=time_x)
safe_fig_show(fig_arch_timeline)
safe_fig_show(fig_arch_trans)
safe_fig_show(fig_arch_conf)
export_figure(fig_arch_timeline, "tei-archetyp-timeline", export_fig_visual, export_fig_png)
export_figure(fig_arch_trans, "tei-archetyp-transitions", export_fig_visual, export_fig_png)
export_figure(fig_arch_conf, "tei-archetyp-confidence", export_fig_visual, export_fig_png)

# Berechnung der Bereitschaft für jedes Quartal
bereitschaft = bereitschafts_values[1:]
if len(bereitschaft) > quartale:
    bereitschaft = bereitschaft[:quartale]

# Umwandlung der Kompetenzentwicklung in eine Liste
kompetenzentwicklung = simulations_ergebnisse_pe.mean(axis=1).tolist()

# Logging für ΔK_entw und ΔK_mess
logging.info(
    "delta_k_entw range: min=%s, max=%s",
    np.nanmin(delta_k_entw),
    np.nanmax(delta_k_entw)
)
logging.info(
    "delta_k_mess range: min=%s, max=%s",
    np.nanmin(delta_k_mess),
    np.nanmax(delta_k_mess)
)
# Mikro-dynamische Motivation protokollieren (falls vorhanden)
if delta_m_micro_series.size and not np.all(np.isnan(delta_m_micro_series)):
    logging.info(
        "delta_m_micro range: min=%s, max=%s",
        np.nanmin(delta_m_micro_series),
        np.nanmax(delta_m_micro_series)
    )
# Runden der Werte auf 3 Dezimalstellen
delta_k_mess_mean = round(np.mean(delta_k_mess), 3)
delta_k_entw_mean = round(np.mean(delta_k_entw), 3)
if np.all(np.isnan(delta_m_micro_series)):
    delta_m_micro_mean = 0.0
else:
    delta_m_micro_mean = round(float(np.nanmean(delta_m_micro_series)), 3)

unschaerfe_produkt = float(np.nanmean(np.array(delta_k_entw) * np.array(delta_k_mess)))


# =========================================
# TEI-basierte Kalibrierungen (K0/N0 und ΔK-Gewichte)
# -----------------------------------------
def _safe_array(seq):
    try:
        arr = np.asarray(seq, dtype=float)
        return arr[~np.isnan(arr)]
    except Exception:
        return np.array([], dtype=float)

def _fit_least_squares(X, y):
    try:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        yhat = X @ beta
        ss_res = float(np.sum((y - yhat) ** 2))
        ss_tot = float(np.sum((y - np.mean(y)) ** 2)) if y.size else 0.0
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
        return beta, r2
    except Exception:
        return None, np.nan

# Feature-Matrix aus TEI-Dimensionen je HS (1..len_series)
tei_c = []
tei_d = []
tei_t = []
tei_o = []
ratios = []
for i in range(1, len_series + 1):
    item = tei_seq[i - 1] if i - 1 < len(tei_seq) and tei_seq[i - 1] else {}
    tei_c.append(float(item.get("training_content", 0.5)))
    tei_d.append(float(item.get("training_design", 0.5)))
    tei_t.append(float(item.get("trainer_behavior", 0.5)))
    tei_o.append(float(item.get("training_outcome", 0.5)))
    ratios.append(float(duration_ratios[i - 1] if i - 1 < len(duration_ratios) else 1.0))

X_base = np.column_stack([
    np.ones(len(tei_c)),
    np.asarray(tei_c),
    np.asarray(tei_d),
    np.asarray(tei_t),
    np.asarray(tei_o),
    np.asarray(ratios),
    np.asarray(tei_c) * np.asarray(tei_d),
    np.asarray(tei_t) * np.asarray(tei_o),
]) if len(tei_c) else np.empty((0, 1))

# KTT-basierte Messunsicherheit (Delta_K_mess_KTT) per Fehlerfortpflanzung
try:
    # SD der TEI-Dimensionen über die HS (Proxy für Skalen-SD)
    sd_c = float(np.nanstd(tei_c)) if tei_c else 0.0
    sd_d = float(np.nanstd(tei_d)) if tei_d else 0.0
    sd_t = float(np.nanstd(tei_t)) if tei_t else 0.0
    sd_o = float(np.nanstd(tei_o)) if tei_o else 0.0
    # KTT: SE_x = SD_x * sqrt(1 - alpha_x)
    se_c = sd_c * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("training_content", 0.8)))
    se_d = sd_d * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("training_design", 0.8)))
    se_t = sd_t * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("trainer_behavior", 0.8)))
    se_o = sd_o * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("training_outcome", 0.8)))

    # Ableitungen des Kompetenz-Gain f(c,d,t,o) w.r.t. Inputs je HS
    dK_mess_ktt = []
    for i in range(len(tei_c)):
        c_i, d_i, t_i, o_i = tei_c[i], tei_d[i], tei_t[i], tei_o[i]
        ratio_i = ratios[i] if i < len(ratios) else 1.0
        # Partielle Ableitungen des Kompetenz-Gains (wie im Lauf verwendet)
        dc = ratio_i * (1.0 + 0.5 * d_i) * 0.4
        dd = (1.0 + c_i) * ratio_i * 0.4 * 0.5
        dt = 0.0
        do = 0.1
        # TEI‑spezifische SE je HS, fallback: globale SE
        item = tei_seq[i] if i < len(tei_seq) and tei_seq[i] else {}
        se_c_i = float(item.get("sd_training_content", np.nan))
        se_d_i = float(item.get("sd_training_design", np.nan))
        se_t_i = float(item.get("sd_trainer_behavior", np.nan))
        se_o_i = float(item.get("sd_training_outcome", np.nan))
        # KTT‑Überlagerung: SE_dim = sd01 * sqrt(1 - alpha)
        se_c_i = (se_c_i if np.isfinite(se_c_i) else se_c) * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("training_content", 0.8)))
        se_d_i = (se_d_i if np.isfinite(se_d_i) else se_d) * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("training_design", 0.8)))
        se_t_i = (se_t_i if np.isfinite(se_t_i) else se_t) * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("trainer_behavior", 0.8)))
        se_o_i = (se_o_i if np.isfinite(se_o_i) else se_o) * np.sqrt(max(0.0, 1.0 - TEI_ALPHA_DEFAULTS.get("training_outcome", 0.8)))
        var_gain = (dc**2) * (se_c_i**2) + (dd**2) * (se_d_i**2) + (dt**2) * (se_t_i**2) + (do**2) * (se_o_i**2)
        dK_mess_ktt.append(float(np.sqrt(max(0.0, var_gain))))
    # auf Quartalsindex (Startpunkt 0) auffüllen
    delta_k_mess_ktt = [0.0] + dK_mess_ktt
except Exception:
    delta_k_mess_ktt = [0.0] * (len_series + 1)

# 1) K0/N0 Schätzung über lineare Kalibrierung gegen beobachtete Niveaus (0..1)
K_series = _safe_array(competence_series[1:]) / 10.0
N_series = _safe_array(neugier_series[1:]) / 10.0
if X_base.shape[0] >= len(K_series) and K_series.size >= 4:
    beta_K, r2_K = _fit_least_squares(X_base[:K_series.size, :4+1], K_series)  # Bias + c,d,t,o
else:
    beta_K, r2_K = (None, np.nan)
if X_base.shape[0] >= len(N_series) and N_series.size >= 4:
    beta_N, r2_N = _fit_least_squares(X_base[:N_series.size, :4+1], N_series)
else:
    beta_N, r2_N = (None, np.nan)

K0_est = None
N0_est = None
first_vec = np.array([1.0, tei_c[0] if tei_c else 0.5, tei_d[0] if tei_d else 0.5, tei_t[0] if tei_t else 0.5, tei_o[0] if tei_o else 0.5])
if isinstance(beta_K, np.ndarray):
    K0_est = float(np.clip((first_vec @ beta_K) * 10.0, 0.0, 10.0))
if isinstance(beta_N, np.ndarray):
    N0_est = float(np.clip((first_vec @ beta_N) * 10.0, 0.0, 10.0))

# 2) ΔK-Entwicklung: Gewichte per Least Squares auf ΔK_entw fitten
y_dk = _safe_array(delta_k_entw)
if X_base.shape[0] >= y_dk.size and y_dk.size >= 4:
    beta_dK, r2_dK = _fit_least_squares(X_base[:y_dk.size, :], y_dk)
else:
    beta_dK, r2_dK = (None, np.nan)

# Logging der Kalibrierung
try:
    logging.info("Kalibrierung K0/N0: r2_K=%s r2_N=%s | K0_est=%s N0_est=%s", r2_K, r2_N, K0_est, N0_est)
    logging.info("ΔK-Entw-Gewichte (r2=%.3f): %s", r2_dK, beta_dK.tolist() if isinstance(beta_dK, np.ndarray) else None)
except Exception:
    pass


# =========================================
# Systemindikatoren & Dynamik
# -----------------------------------------
# Bildungswirkfaktor als geglättete erste Ableitung der Kompetenzmitte
kompetenz_array = simulations_ergebnisse_pe.mean(axis=1).to_numpy(dtype=float)
bildungswirkfaktoren = np.gradient(kompetenz_array)
bildungswirkfaktoren_smooth = smooth_curve(bildungswirkfaktoren, clip_max=10)

# Logging/Berechnung für Dynamic_C (datengetrieben aus Korrelation und Streuungen)
# Optional: KTT-Serie als Messunsicherheit verwenden
delta_k_mess_eff = np.array((delta_k_mess_ktt if USE_KTT_FOR_MESS else delta_k_mess), dtype=float)
c_values = np.array(delta_k_entw) * delta_k_mess_eff
def _dynamic_C_from_data(dke, dkm):
    a = np.asarray(dke, dtype=float)
    b = np.asarray(dkm, dtype=float)
    out = np.zeros_like(a, dtype=float)
    for i in range(a.size):
        aa = a[: i + 1]
        bb = b[: i + 1]
        if aa.size < 2 or np.std(aa) == 0 or np.std(bb) == 0:
            out[i] = 0.0
        else:
            r = pearsonr(aa, bb)[0]
            out[i] = abs(r) * (np.std(aa) * np.std(bb))
    return out
dynamic_C = _dynamic_C_from_data(delta_k_entw, delta_k_mess_eff)
logging.info("dynamic_C (data) range: min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))

# Unschärfe-Marge und Erfüllungsquote vorbereiten
unschaerfe_marge = np.array(delta_k_entw, dtype=float) * delta_k_mess_eff - np.array(dynamic_C, dtype=float)
unschaerfe_erfuellt = np.where(unschaerfe_marge >= 0, 1, 0)
unschaerfe_anteil_erfuellt = float(np.nanmean(unschaerfe_erfuellt) * 100.0) if unschaerfe_erfuellt.size else float('nan')
unschaerfe_marge_mean = float(np.nanmean(unschaerfe_marge)) if unschaerfe_marge.size else float('nan')
unschaerfe_marge_min = float(np.nanmin(unschaerfe_marge)) if unschaerfe_marge.size else float('nan')
unschaerfe_marge_max = float(np.nanmax(unschaerfe_marge)) if unschaerfe_marge.size else float('nan')

# Berechnung der ersten Ableitung der geglätteten Bildungswirkfaktoren
steigungen_bildungswirkfaktor = np.gradient(bildungswirkfaktoren_smooth)

# Glättung der Steigungen
steigungen_bildungswirkfaktor_smooth = smooth_curve(steigungen_bildungswirkfaktor, clip_max=10)

# Berechnung des Integrals des Bildfaktors
integral_bildungswirkfaktor = np.trapezoid(bildungswirkfaktoren_smooth, dx=1)

# Berechnung der Wendepunkte, Minima und Maxima für den Bildungswirkindikator (ι)
erste_ableitung_bildungswirkfaktor = steigungen_bildungswirkfaktor_smooth
zweite_ableitung_bildungswirkfaktor = np.gradient(steigungen_bildungswirkfaktor_smooth)

wendepunkte_bildungswirkfaktor = np.where(np.diff(np.sign(zweite_ableitung_bildungswirkfaktor)))[0]
maxima_bildungswirkfaktor, _ = find_peaks(bildungswirkfaktoren_smooth)
minima_bildungswirkfaktor, _ = find_peaks(-bildungswirkfaktoren_smooth)

# Berechnung des Bildungswirkindikators als die Ableitung des Bildungswirkfaktors
bildungswirkindikator = np.gradient(bildungswirkfaktoren_smooth)
integral_bildungswirkindikator = np.trapezoid(bildungswirkindikator, dx=1)

# Glättung der Kurven des Bildungswirkindikators
bildungswirkindikatoren_smooth = smooth_curve(bildungswirkindikator, clip_max=10)
steigungen_bildungswirkindikator_smooth = smooth_curve(np.gradient(bildungswirkindikator), clip_max=10)

# Berechnung der Wendepunkte, Minima und Maxima des Bildungswirkindikators
erste_ableitung_bildungswirkindikator = bildungswirkindikatoren_smooth
zweite_ableitung_bildungswirkindikator = np.gradient(bildungswirkindikatoren_smooth)

wendepunkte_bildungswirkindikator = np.where(np.diff(np.sign(zweite_ableitung_bildungswirkfaktor)))[0]

maxima_bildungswirkindikator, _ = find_peaks(bildungswirkindikatoren_smooth)
minima_bildungswirkindikator, _ = find_peaks(-bildungswirkindikatoren_smooth)

# Berechnung der Extrema und Wendepunkte für ν und ι
maxima_nu, minima_nu, inflection_points_nu = identify_extrema_and_inflection_points(bildungswirkfaktoren_smooth)
maxima_iota, minima_iota, inflection_points_iota = identify_extrema_and_inflection_points(steigungen_bildungswirkfaktor_smooth)

# Berechnung der Bildungswirkdynamik als zweite Ableitung der geglätteten Bildungswirkfaktoren
bildungswirkdynamik = np.gradient(np.gradient(bildungswirkfaktoren_smooth))

# Glättung der Bildungswirkdynamik
bildungswirkdynamik_smooth = smooth_curve(bildungswirkdynamik, clip_max=10)

# Glättung der Ergebnisse durch rollierende Mittelwerte
smoothed_results = simulations_ergebnisse_pe_clipped.rolling(window=3, min_periods=1).mean()
mittelwerte = smoothed_results.mean(axis=1)
_y_int = smooth_curve(mittelwerte, clip_max=10)
_x_int = time_axis_quartale[: len(_y_int)] if 'time_axis_quartale' in globals() else np.arange(len(_y_int))
flaeche_unter_mittelwert = float(np.trapezoid(_y_int, x=_x_int))
quartale_range = np.arange(0, quartale + 1)

# Zusatzkennzahlen für die Interpretation des Integrals
_mw_vals = mittelwerte.to_numpy(dtype=float)
_dauer = max(1, len(_mw_vals) - 1)
avg_kompetenz_niveau = float(flaeche_unter_mittelwert / _dauer)
delta_k_total = float((_mw_vals[-1] - _mw_vals[0]) if len(_mw_vals) >= 2 else 0.0)

# Theoriegeleitete Basisparameter (lokal) und Archetyp/PE‑gekoppelte Ableitung


# Berechnung der mittleren Steigungen der Kompetenzentwicklung
mittlere_steigungen = mittelwerte_kompetenz.diff().fillna(0).infer_objects().tolist()

# Bestimmung des besten und schlechtesten Ergebnisses sowie der Flächen unter den Kurven
bestes_ergebnis = simulations_ergebnisse_pe_clipped.max(axis=1)
schlechtestes_ergebnis = simulations_ergebnisse_pe_clipped.min(axis=1)
flaeche_unter_bestes = np.trapezoid(smooth_curve(bestes_ergebnis, clip_max=10), dx=1)
flaeche_unter_schlechtestes = np.trapezoid(smooth_curve(schlechtestes_ergebnis, clip_max=10), dx=1)

# =========================================
# Verteilungen & Wahrscheinlichkeiten
# -----------------------------------------

# Analyse der Endkompetenzen
end_kompetenzen = simulations_ergebnisse_pe.iloc[-1].dropna().apply(pd.to_numeric, errors='coerce')

# Histogrammdaten bereinigen und numerisch sicherstellen
data_histogramm = end_kompetenzen.dropna()
data_histogramm = data_histogramm.apply(pd.to_numeric, errors='coerce').dropna()
if not np.issubdtype(data_histogramm.dtype, np.number):
    raise ValueError("Histogrammdaten sind nicht numerisch.")

# Erstellung der KDE und Normalverteilung für die Endkompetenzen
print("Anzahl der Werte:", len(data_histogramm))
print("Min:", np.min(data_histogramm), "Max:", np.max(data_histogramm))
print("Mittelwert:", np.mean(data_histogramm))
print("Standardabweichung:", np.std(data_histogramm))
print("Eindeutige Werte:", len(np.unique(data_histogramm)))
if np.std(data_histogramm) == 0:  # Falls alle Werte exakt gleich sind
    print("Warnung: Alle Werte sind identisch, minimale Variation wird hinzugefügt.")
    data_histogramm += np.random.normal(0, 0.001, size=data_histogramm.shape)  # Sehr kleines zufälliges Rauschen hinzufügen

if len(data_histogramm) >= 2:
    density_kde = gaussian_kde(data_histogramm)
    x_kde = np.linspace(min(data_histogramm), max(data_histogramm), 1000)
    y_kde = density_kde(x_kde)
    mean, std = norm.fit(data_histogramm)
    y_norm = norm.pdf(x_kde, mean, std)
else:
    print("Hinweis: Zu wenige Datenpunkte für KDE/Normalverteilung – Visualisierung wird vereinfacht.")
    x_kde = np.asarray(data_histogramm, dtype=float)
    if x_kde.size == 0:
        x_kde = np.array([0.0])
    y_kde = np.zeros_like(x_kde, dtype=float)
    mean = float(x_kde[0])
    std = 0.0
    y_norm = np.zeros_like(x_kde, dtype=float)

# Behandeln von NaN-Werten in den Bereitschaftssteigerungen-Daten
# Ersetze NaN-Werte durch den Median oder entferne fehlende Daten
bereitschaftssteigerungen.fillna(bereitschaftssteigerungen.median(), inplace=True)

# Behandeln von NaN-Werten in den PE Auswirkungen-Daten
# Ersetze NaN-Werte durch den Median oder entferne fehlende Daten
pe_auswirkungen_df.fillna(pe_auswirkungen_df.median(), inplace=True)

# =========================================
# Korrelationsanalysen
# -----------------------------------------

# Berechnung der Korrelationsmatrix (nur sinnvoll bei mehr als einem Durchlauf)
bereitschafts_matrix = bereitschaftssteigerungen.to_numpy(dtype=float)
pe_matrix = pe_auswirkungen_df.to_numpy(dtype=float)

korrelations_matrix_bereitschaft = np.array([[1.0]])
korrelations_matrix_pe = np.array([[1.0]])

# Berechnung der minimalen und maximalen Werte für die Farbskala
zmin_bereitschaft = np.nanmin(korrelations_matrix_bereitschaft)
zmax_bereitschaft = np.nanmax(korrelations_matrix_bereitschaft)
zmin_pe = np.nanmin(korrelations_matrix_pe)
zmax_pe = np.nanmax(korrelations_matrix_pe)

# Berechnung der Korrelationskoeffizienten für ΔK_entw und ΔK_mess
if np.std(delta_k_entw) == 0 or np.std(delta_k_mess) == 0:
    basis_korrelation = np.nan
else:
    basis_korrelation = pearsonr(delta_k_entw, delta_k_mess)[0]
korrelationskoeffizienten = [basis_korrelation]

# Daten für das Streudiagramm
durchlauf_df = pd.DataFrame({
    'Durchlauf': [1],
    'Korrelationskoeffizient': korrelationskoeffizienten
})

# Zählen der positiven, negativen und nahe Null Korrelationskoeffizienten (NaN ignorieren)
gueltige_korrelationen = [k for k in korrelationskoeffizienten if not np.isnan(k)]
positive_korrelationskoeffizienten = sum(1 for k in gueltige_korrelationen if k > 0.1)
negative_korrelationskoeffizienten = sum(1 for k in gueltige_korrelationen if k < -0.1)
nahe_null_korrelationskoeffizienten = max(0, len(gueltige_korrelationen) - positive_korrelationskoeffizienten - negative_korrelationskoeffizienten)

# Daten für das Verhältnis
verhaeltnis_daten = {
    'Korrelationskoeffizient': ['Positiv', 'Negativ', 'Nahe Null'],
    'Anzahl': [positive_korrelationskoeffizienten, negative_korrelationskoeffizienten, nahe_null_korrelationskoeffizienten]
}

verhaeltnis_df = pd.DataFrame(verhaeltnis_daten)


# =========================================
# Vorbereitende Berechnung für CSV-Export: delta_n und dynamic_C
# =========================================
# Falls noch nicht berechnet: delta_n und dynamic_C
# Explorative Unsicherheit ΔN aus der Streuung der Neugierverläufe ableiten
_neugier_np = np.asarray(neugier_series, dtype=float)
delta_n = np.diff(_neugier_np, prepend=_neugier_np[0]).tolist()

# Berechne dynamic_C, damit es überall verfügbar ist
c_values = np.array(delta_k_entw) * np.array(delta_k_mess)
dynamic_C = _dynamic_C_from_data(delta_k_entw, delta_k_mess)
logging.info("dynamic_C (export) range: min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))

# =========================================
# csv Export
# =========================================

def exportiere_bildungswirkgefuege_csv(dateiname=None):
    """
    Exportiert alle berechneten Zeitreihen-Daten in eine CSV-Datei zur Weiterverarbeitung.
    """
    target_path = Path(dateiname) if dateiname else CSV_EXPORT_DIR / "tei_bildungswirkgefuege_datenbasis.csv"
    target_path.parent.mkdir(parents=True, exist_ok=True)
    # Helper: Padding für TEI-Spalten (32 → 33, führendes NaN/None)
    def _pad_to_quartale_range(seq, fill=np.nan):
        target = len(quartale_range)
        arr = list(seq)
        if len(arr) == target:
            return arr
        if len(arr) == target - 1:
            return [fill] + arr
        if len(arr) < target:
            return arr + [fill] * (target - len(arr))
        return arr[:target]

    export_df = pd.DataFrame({
        "Quartal": quartale_range,
        "Kompetenz_Mittelwert": mittelwerte_kompetenz,
        "Kompetenz_Streuung": stddev_kompetenz,
        "Kompetenz_Median": mediane_kompetenz,
        "Kompetenz_Steigung": mittlere_steigungen,
        "Kompetenzentwicklung": kompetenzentwicklung,
        "Neugier_Mittelwert": mittelwerte_neugier,
        "Motivation_Mittelwert": mittelwerte_motivation,
        "Differenz_Neugier_Motivation": diff_neugier_motivation,
        "Kumulierte_Differenz_Neugier_Motivation": kumulative_diff_neugier_motivation,
        "Bereitschaft": bereitschaft + [None],  # hat eine Länge von quartale, ergänze mit None für Gleichstand
        "Bildungswirkfaktor": bildungswirkfaktoren_smooth,
        "Bildungswirkindikator": bildungswirkindikatoren_smooth,
        "Steigung_Bildungswirkfaktor": steigungen_bildungswirkfaktor_smooth,
        "Steigung_Bildungswirkindikator": steigungen_bildungswirkindikator_smooth,
        "Bildungswirkdynamik": bildungswirkdynamik_smooth,
        "Delta_K_entw": delta_k_entw,
        "Delta_K_mess": delta_k_mess,
        "Delta_K_mess_KTT": _pad_to_quartale_range(delta_k_mess_ktt, 0.0),
        "Delta_N": delta_n,
        "Delta_M_micro": delta_m_micro_series.tolist(),
        "Dynamic_C": dynamic_C.tolist() if hasattr(dynamic_C, "tolist") else dynamic_C,
        "Unschaerfe_Marge": unschaerfe_marge.tolist() if hasattr(unschaerfe_marge, "tolist") else unschaerfe_marge,
        "Unschaerfe_Erfuellt": unschaerfe_erfuellt.tolist() if hasattr(unschaerfe_erfuellt, "tolist") else unschaerfe_erfuellt,
        "BPS_Bio": mittelwerte_bio_status.tolist() if hasattr(mittelwerte_bio_status, "tolist") else mittelwerte_bio_status,
        "BPS_Psy": mittelwerte_psy_status.tolist() if hasattr(mittelwerte_psy_status, "tolist") else mittelwerte_psy_status,
        "BPS_Soz": mittelwerte_soz_status.tolist() if hasattr(mittelwerte_soz_status, "tolist") else mittelwerte_soz_status,
        "Archetyp_TEI": (_pad_to_quartale_range(trace, None) if 'trace' in globals() else [None]*len(quartale_range)),
        "Archetyp_TEI_Confidence": (_pad_to_quartale_range(list(np.array(trace_conf, dtype=float))) if 'trace_conf' in globals() else np.full(len(quartale_range), np.nan))
    })

    export_df.to_csv(target_path, index=False)
    print(f"✅ TEI-Bildungswirkgefüge-Daten exportiert nach: {target_path}")

# Exportiere zusätzlich die Simulationsparameter als CSV
def exportiere_parameter_csv(dateiname=None):
    import csv
    target_path = Path(dateiname) if dateiname else CSV_EXPORT_DIR / "tei_bildungswirkgefuege_parameter.csv"
    target_path.parent.mkdir(parents=True, exist_ok=True)
    # Versuche archetyp und paradigma zu bestimmen
    # archetyp: sollte dem aktuell simulierten Archetyp entsprechen
    # paradigma: sollte dem aktuell gewählten Ansatz entsprechen
    try:
        archetyp = selected_archetyp
    except Exception:
        archetyp = None
    try:
        paradigma = gewaehlter_ansatz
    except Exception:
        paradigma = None

    # Robuste Ermittlung der Startwerte und Metadaten
    archetyp = globals().get("selected_archetyp", archetyp)
    paradigma = globals().get("gewaehlter_ansatz", paradigma)

    start_kompetenz_val = globals().get("start_kompetenz", None)
    if start_kompetenz_val is None and 'kompetenzentwicklung' in globals() and len(kompetenzentwicklung) > 0:
        start_kompetenz_val = kompetenzentwicklung[0]

    start_neugier_val = globals().get("initial_neugier", None)
    if start_neugier_val is None and 'mittelwerte_neugier' in globals() and len(mittelwerte_neugier) > 0:
        start_neugier_val = float(mittelwerte_neugier[0])

    start_motivation_val = globals().get("initial_motivation", None)
    if start_motivation_val is None and 'mittelwerte_motivation' in globals() and len(mittelwerte_motivation) > 0:
        start_motivation_val = float(mittelwerte_motivation[0])

    # Hinweis: 'bereitschaft' beginnt ab Quartal 1; es gibt keinen expliziten Startwert für Quartal 0.
    start_bereitschaft_val = globals().get("initial_bereitschaft", None)
    if start_bereitschaft_val is None:
        start_bereitschaft_val = None

    parameter = {
        "gamma_0": globals().get("gamma_0", 0.1161),
        "alpha": globals().get("alpha", 0.1101),
        "A": globals().get("A", 0.0436),
        "c_crit": globals().get("c_crit", 1.5800),
        "start_kompetenz": (K0_est if K0_est is not None else start_kompetenz_val),
        "start_neugier": (N0_est if N0_est is not None else start_neugier_val),
        "start_motivation": start_motivation_val,
        "start_bereitschaft": start_bereitschaft_val,
        "archetyp": archetyp,
        "paradigma": paradigma,
        "quartale": globals().get("quartale", None),
        "bps_bio_start": globals().get("bio_startstatus", None),
        "bps_psy_start": globals().get("psy_startstatus", None),
        "bps_soz_start": globals().get("soz_startstatus", None),
        # Kalibrierung (Diagnostik)
        "K0_est": K0_est,
        "N0_est": N0_est,
        "ΔK_fit_r2": r2_dK,
        "bps_bio_mean": globals().get("bio_status_mean", None),
        "bps_psy_mean": globals().get("psy_status_mean", None),
        "bps_soz_mean": globals().get("soz_status_mean", None),
        "TEI_Archetyp_Start": globals().get("TEI_ARCH_START", None),
        "TEI_Archetyp_Modal": globals().get("TEI_ARCH_MODAL", None),
        "TEI_Archetyp_Ende": globals().get("TEI_ARCH_END", None),
        "TEI_Archetyp_Wechsel": globals().get("TEI_ARCH_WECHSEL", None),
        "TEI_Archetyp_Confidence_Mean": globals().get("TEI_ARCH_CONF_MEAN", None),
        # Unschärfe-Kennzahlen (nur Report)
        "Unschaerfe_Anteil_Erfuellt_%": globals().get("unschaerfe_anteil_erfuellt", unschaerfe_anteil_erfuellt),
        "Unschaerfe_Marge_Mean": globals().get("unschaerfe_marge_mean", unschaerfe_marge_mean),
        "Unschaerfe_Marge_Min": globals().get("unschaerfe_marge_min", unschaerfe_marge_min),
        "Unschaerfe_Marge_Max": globals().get("unschaerfe_marge_max", unschaerfe_marge_max)
    }
    with open(target_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["Parameter", "Wert"])
        for key, value in parameter.items():
            writer.writerow([key, value])
        # PE-Zusammenfassung: TEI-Profil bevorzugt
        _pe_for_params = globals().get("PE_CODES_VISUALS") or globals().get("pe_auswirkungen", {})
        if _pe_for_params:
            for key, value in sorted(_pe_for_params.items()):
                writer.writerow([f"PE - {key}", value])
        if "biosoziales_profil" in globals():
            for key, value in sorted(biosoziales_profil.items()):
                writer.writerow([f"BPS - {key}", value])
    print(f"✅ Simulationsparameter exportiert nach: {target_path}")

# Optional: Export am Ende der Simulation aktivieren
exportiere_bildungswirkgefuege_csv()
exportiere_parameter_csv()

# =========================================
# Visualisierungen
# =========================================

# -----------------------------------------
# Kompetenzniveau | Einflüsse persönlicher Ereignisse
# -----------------------------------------

colors = plotly_template.get_colors()
_style_base = plotly_template.get_plot_styles()


def ci_legend(**overrides):
    """Einheitliche Legendenkonfiguration (horizontale Ausrichtung, feste Breite)."""
    legend_colors = plotly_template.get_colors()
    base = dict(
        orientation='h',
        x=0.5,
        xanchor='center',
        y=-0.2,
        yanchor='top',
        bgcolor=legend_colors['background'],
        bordercolor=legend_colors['text'],
        borderwidth=0,
        font=dict(color=legend_colors['text']),
        itemwidth=90
    )
    base.update(overrides)
    return base
# Quelle für PE-Visualisierung: TEI-Profil (falls vorhanden), sonst Archetyp-PE
_pe_source = None
try:
    if 'PE_CODES_VISUALS' in globals() and PE_CODES_VISUALS:
        _pe_source = PE_CODES_VISUALS
except Exception:
    _pe_source = None
if _pe_source is None:
    _pe_source = pe_auswirkungen

data = pd.DataFrame(list(_pe_source.items()), columns=['Ereigniskategorie', 'Auswirkung'])
data = data.sort_values(by='Auswirkung', ascending=False)
ereignis_label_mapping = {
    "PFE": "Fehlschlag",
    "PLE": "Leistungseinbruch",
    "PFV": "Fortschritt",
    "PGV": "Großereignis",
    "PSE": "Stabilitätserfolg",
    "PEE": "Erfolg"
}

data['Label'] = data.apply(
    lambda row: f"{ereignis_label_mapping.get(row['Ereigniskategorie'], row['Ereigniskategorie'])}: {row['Auswirkung']:.2f}",
    axis=1
)

fig_einfluss = px.bar(
    data,
    x='Ereigniskategorie',
    y='Auswirkung',
    title=f'Kompetenzniveau | Einflüsse persönlicher Ereignisse ({gewaehlter_ansatz} | {selected_archetyp})',
    labels={'Ereigniskategorie': "Kategorie", 'Auswirkung': "Einfluss auf Kompetenzniveau"},
    color='Auswirkung',
    color_continuous_scale=[
        [0.0, colors['negativeHighlight']],
        [0.5, colors['accent']],
        [1.0, colors['positiveHighlight']]
    ],
    text='Label'
)

fig_einfluss.update_layout(
    **plotly_template.get_standard_layout(
        title=f'Kompetenzniveau | Einflüsse persönlicher Ereignisse ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title="Kategorie",
        y_title="Gewichtung"
    ),
    coloraxis_colorbar=dict(title="Gewichtung")
)

fig_einfluss.update_traces(texttemplate='%{text}', textposition='outside')


safe_fig_show(fig_einfluss)
export_figure(fig_einfluss, "einfluss-pe", export_fig_einfluss, export_fig_png)

# -----------------------------------------
# Kompetenzniveau | Nettowirkung persönlicher Ereignisse (Gewichtung × Vorzeichen)
# -----------------------------------------
vorzeichen_map = {"PFE": -1, "PLE": -1, "PGV": -1, "PFV": 1, "PSE": 1, "PEE": 1}

netto_data = data.copy()
netto_data["Nettowirkung"] = netto_data.apply(
    lambda row: row["Auswirkung"] * vorzeichen_map.get(row["Ereigniskategorie"], 0), axis=1
)
netto_data = netto_data.sort_values(by="Nettowirkung", ascending=False)

netto_data['Label'] = netto_data.apply(
    lambda row: f"{ereignis_label_mapping.get(row['Ereigniskategorie'], row['Ereigniskategorie'])}: {row['Nettowirkung']:.2f}",
    axis=1
)

fig_einfluss_netto = px.bar(
    netto_data,
    x='Ereigniskategorie',
    y='Nettowirkung',
    title=f'Kompetenzniveau | Nettowirkung persönlicher Ereignisse ({gewaehlter_ansatz} | {selected_archetyp})',
    labels={'Ereigniskategorie': "Kategorie", 'Nettowirkung': "Nettowirkung (Gewichtung × Vorzeichen)"},
    color='Nettowirkung',
    color_continuous_scale=[
        [0.0, colors['negativeHighlight']],
        [0.5, colors['accent']],
        [1.0, colors['positiveHighlight']]
    ],
    text='Label'
)

fig_einfluss_netto.update_layout(
    **plotly_template.get_standard_layout(
        title=f'Kompetenzniveau | Nettowirkung persönlicher Ereignisse ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title="Kategorie",
        y_title="Nettowirkung"
    ),
    coloraxis_colorbar=dict(title="Nettowirkung")
)

fig_einfluss_netto.update_traces(texttemplate='%{text}', textposition='outside')

safe_fig_show(fig_einfluss_netto)
export_figure(fig_einfluss_netto, "einfluss-pe-netto", export_fig_einfluss_netto, export_fig_png_einfluss_netto)

# -----------------------------------------
# Visualisierung des Verhältnisses
# -----------------------------------------

fig_verhaeltnis = go.Figure(data=[
    go.Bar(
        name='Korrelationskoeffizienten',
        x=verhaeltnis_df['Korrelationskoeffizient'],
        y=verhaeltnis_df['Anzahl'],
        marker_color=[
            plotly_template.get_colors()["positiveHighlight"],
            plotly_template.get_colors()["negativeHighlight"],
            plotly_template.get_colors()["accent"]
        ]
    )
])

fig_verhaeltnis.update_layout(**plotly_template.get_standard_layout(
    title=f'Bildungswirkgefüge | Δ Korrelationskoeffizienten zu Null ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title='Korrelationskoeffizient',
    y_title='Durchläufe'
))

# Interpretation basierend auf der Verteilung der Korrelationskoeffizienten
interpretation_text = ""
if positive_korrelationskoeffizienten > negative_korrelationskoeffizienten and positive_korrelationskoeffizienten > nahe_null_korrelationskoeffizienten:
    interpretation_text = "Mehrheitlich positive Korrelationen: Verbesserungen in der Messgenauigkeit könnten auch die Unsicherheit in der Kompetenzentwicklung reduzieren."
elif negative_korrelationskoeffizienten > positive_korrelationskoeffizienten and negative_korrelationskoeffizienten > nahe_null_korrelationskoeffizienten:
    interpretation_text = "Mehrheitlich negative Korrelationen: Eine Balance zwischen Messgenauigkeit und Entwicklungsflexibilität ist notwendig."
elif nahe_null_korrelationskoeffizienten > positive_korrelationskoeffizienten and nahe_null_korrelationskoeffizienten > negative_korrelationskoeffizienten:
    interpretation_text = "Korrelationskoeffizienten nahe Null: Die Unsicherheiten in der Messung und Entwicklung können unabhängig voneinander optimiert werden."

fig_verhaeltnis.add_annotation(
    x=0.5, y=-0.2, xref='paper', yref='paper',
    text=interpretation_text,
    showarrow=False,
    font=dict(color=plotly_template.get_colors()["text"])
)

safe_fig_show(fig_verhaeltnis)
export_figure(fig_verhaeltnis, "verhaeltnis", export_fig_verhaeltnis, export_fig_png)

# -----------------------------------------
# Visualisierung des Korrelationsverlaufs
# -----------------------------------------

delta_k_entw_arr = np.array(delta_k_entw, dtype=float)
delta_k_mess_arr = np.array((delta_k_mess_ktt if USE_KTT_FOR_MESS else delta_k_mess), dtype=float)
x_durchlaeufe = (time_x[: len(delta_k_entw_arr)] if 'time_x' in globals() else list(range(1, len(delta_k_entw_arr) + 1)))
rolling_corr = []
for i in range(1, len(delta_k_entw_arr) + 1):
    if i < 2 or np.std(delta_k_entw_arr[:i]) == 0 or np.std(delta_k_mess_arr[:i]) == 0:
        rolling_corr.append(np.nan)
        continue
    corr_value, _ = pearsonr(delta_k_entw_arr[:i], delta_k_mess_arr[:i])
    rolling_corr.append(corr_value)

fig_durchlaeufe = go.Figure()
fig_durchlaeufe.add_trace(go.Scatter(
    mode='lines+markers',
    x=x_durchlaeufe,
    y=rolling_corr,
    marker=dict(
        size=6,
        color=colors['primaryLine']
    ),
    name='Korrelationsverlauf'
))

fig_durchlaeufe.update_layout(**plotly_template.get_standard_layout(
    title=f'Bildungswirkgefüge | Korrelationsverlauf ΔK_entw vs ΔK_mess ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title='Quartal',
    y_title='Korrelationskoeffizient',
    x_range=[0, CONFIG_QUARTALE]
))

safe_fig_show(fig_durchlaeufe)
export_figure(fig_durchlaeufe, "durchlaeufe", export_fig_durchlaeufe, export_fig_png)

# -----------------------------------------
# Bildungswirkgefüge | Unschärferelation (ΔK_mess⋅ΔK_entw = C)
# -----------------------------------------

labels = ['Kompetenzentwicklung ΔK_entw', 'Kompetenzmessung ΔK_mess', 'Motivationsdynamik ΔM_micro']
values = [abs(delta_k_entw_mean), abs(delta_k_mess_mean), abs(delta_m_micro_mean)]

def render_competence_and_uncertainty():
    global fig3
    fig1 = go.Figure(data=[
        go.Bar(
            name='Unsicherheiten',
            x=labels,
            y=values,
            marker_color=[
                colors['primaryLine'],
                colors['secondaryLine'],
                colors['accent']
            ]
        )
    ])

    fig1.update_layout(**plotly_template.get_standard_layout(
        title=f'Bildungswirkgefüge | Unsicherheiten ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Kategorie',
        y_title='Wert'
    ))

    c_values = np.array(delta_k_entw) * np.array(delta_k_mess)
    dynamic_C = _dynamic_C_from_data(delta_k_entw, delta_k_mess)
    logging.info("dynamic_C range (data): min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))
    dynamic_C_scalar = float(np.nanmean(dynamic_C))

    print("🛈 Modellprüfung läuft – GPT-Interpretation wird vorbereitet…")
    print("✅ Power-Law-basierter dynamischer C-Wert berechnet.")
    print(f"Mittelwert von C: {dynamic_C_scalar:.5f}")

    erfuellt = unschaerfe_produkt >= dynamic_C_scalar

    categories_local = ['Produkt der Unsicherheiten ΔK_mess⋅ΔK_entw', 'Dynamischer Unsicherheitswert (C)']
    values_local = [unschaerfe_produkt, dynamic_C_scalar]

    fig2 = go.Figure(data=[
        go.Bar(
            name='Unschärfeprodukt',
            x=categories_local,
            y=values_local,
            marker_color=[
                plotly_template.get_colors()['positiveHighlight'] if erfuellt else plotly_template.get_colors()['accent'],
                plotly_template.get_colors()['accent'] if erfuellt else plotly_template.get_colors()['negativeHighlight']
            ]
        )
    ])

    fig2.update_layout(**plotly_template.get_standard_layout(
        title=f'Bildungswirkgefüge | Dynamische Unsicherheitsrelation ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Kategorie',
        y_title='Wert'
    ))

    fig3 = go.Figure()

    fig3.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=unschaerfe_produkt,
        delta={
            'reference': dynamic_C_scalar,
            'increasing': {'color': plotly_template.get_colors()['positiveHighlight']},
            'decreasing': {'color': plotly_template.get_colors()['negativeHighlight']}
        },
        gauge={
            'axis': {
                'range': [None, max(unschaerfe_produkt, dynamic_C_scalar) * 1.2],
                'tickcolor': plotly_template.get_colors()['text'],
                'tickfont': {'color': plotly_template.get_colors()['text']}
            },
            'steps': [
                {'range': [0, dynamic_C_scalar], 'color': plotly_template.get_colors()['negativeHighlight']},
                {'range': [dynamic_C_scalar, max(unschaerfe_produkt, dynamic_C_scalar) * 1.2],
                 'color': plotly_template.get_colors()['positiveHighlight']}
            ],
            'threshold': {
                'line': {'color': plotly_template.get_colors()['accent'], 'width': 4},
                'thickness': 0.75,
                'value': dynamic_C_scalar
            },
            'bar': {'color': plotly_template.get_colors()['positiveHighlight']}
        },
        title={
            'text': f"ΔK_mess⋅ΔK_entw ≥ C(γ) {'erfüllt' if erfuellt else 'unerfüllt'}<br>({gewaehlter_ansatz} | {selected_archetyp})",
            'font': {'color': plotly_template.get_colors()['text']}
        },
        number={'font': {'color': plotly_template.get_colors()['text']}}
    ))

    fig3.update_layout(
        template=None,
        plot_bgcolor=plotly_template.get_colors()['background'],
        paper_bgcolor=plotly_template.get_colors()['background'],
        font=dict(color=plotly_template.get_colors()['text'])
    )

    safe_fig_show(fig1)
    safe_fig_show(fig2)
    safe_fig_show(fig3)

    export_figure(fig1, "unsicherheiten", export_fig1_unsicherheiten, export_fig_png)
    export_figure(fig2, "unsicherheitsrelation", export_fig2_unsicherheitsrelation, export_fig_png)
    export_figure(fig3, "unsicherheitsrelation-check", export_fig3_unsicherheitsrelation, export_fig_png)

    return fig1, fig2, fig3

fig_unsicherheiten, fig_unsicherheitsrelation, fig3 = render_competence_and_uncertainty()

def render_neugier_und_motivation():
    global fig_neugier_motivation
    fig_neugier_motivation = go.Figure()

    fig_neugier_motivation.add_trace(go.Scatter(
        x=time_x,
        y=mittelwerte_motivation,
        mode='lines+markers',
        name='Motivation',
        line=ci_line("primary")
    ))

    fig_neugier_motivation.add_trace(go.Scatter(
        x=time_x,
        y=mittelwerte_neugier,
        mode='lines+markers',
        name='Neugier',
        line=ci_line("secondary")
    ))

    ymin = min(min(mittelwerte_neugier), min(mittelwerte_motivation))
    ymax = max(max(mittelwerte_neugier), max(mittelwerte_motivation))
    margin = (ymax - ymin) * 0.15

    fig_neugier_motivation.update_layout(**plotly_template.get_standard_layout(
        title=f'Entwicklung von Neugier und Motivation ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Zeit (Quartale)',
        y_title='Neugier / Motivation (0–10)',
        y_range=[ymin - margin, ymax + margin],
        x_range=[0, CONFIG_QUARTALE]
    ))

    safe_fig_show(fig_neugier_motivation)
    export_figure(fig_neugier_motivation, "entwicklung-neugier-motivation", export_fig_entwicklung_neugier_motivation, export_fig_png)

    return fig_neugier_motivation

fig_neugier_motivation = render_neugier_und_motivation()

def render_bps_status():
    global fig_bps_status
    if bps_status_df.empty:
        fig_bps_status = None
        return None
    fig_bps_status = go.Figure()
    fig_bps_status.add_trace(go.Scatter(
        x=bps_time_x,
        y=bps_status_df["Bio"],
        mode='lines+markers',
        name='Biologisch',
        line=ci_line("primary")
    ))
    fig_bps_status.add_trace(go.Scatter(
        x=bps_time_x,
        y=bps_status_df["Psy"],
        mode='lines+markers',
        name='Psychologisch',
        line=ci_line("secondary")
    ))
    fig_bps_status.add_trace(go.Scatter(
        x=bps_time_x,
        y=bps_status_df["Soz"],
        mode='lines+markers',
        name='Sozial',
        line=ci_line("accent")
    ))

    fig_bps_status.update_layout(**plotly_template.get_standard_layout(
        title=f'Biopsychosoziale Statusverläufe ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Zeit (Quartale)',
        y_title='Status (0–1)',
        y_range=[0, 1],
        x_range=[0, CONFIG_QUARTALE]
    ))

    safe_fig_show(fig_bps_status)
    export_figure(fig_bps_status, "bps-status", export_fig_bps_status, export_fig_png_bps_status)

    return fig_bps_status

fig_bps_status = render_bps_status()

# -----------------------------------------
# Korrelations- und Kopplungsanalysen
# -----------------------------------------

def rolling_pearson(x, y, window):
    result = []
    for i in range(len(x) - window + 1):
        x_slice = x[i:i+window]
        y_slice = y[i:i+window]
        if np.std(x_slice) == 0 or np.std(y_slice) == 0:
            result.append(np.nan)
        else:
            r, _ = pearsonr(x_slice, y_slice)
            result.append(r)
    return result

def compute_bps_rolling_corr(x_values, y_values, window):
    x_arr = np.asarray(x_values, dtype=float)
    y_arr = np.asarray(y_values, dtype=float)
    length = min(len(x_arr), len(y_arr))
    if length == 0:
        return np.array([]), np.array([])
    x_arr = x_arr[:length]
    y_arr = y_arr[:length]
    valid_mask = (~np.isnan(x_arr)) & (~np.isnan(y_arr))
    if np.count_nonzero(valid_mask) < window:
        return np.array([]), np.array([])
    x_valid = x_arr[valid_mask]
    y_valid = y_arr[valid_mask]
    corr_vals = np.array(rolling_pearson(x_valid, y_valid, window), dtype=float)
    corr_x = np.arange(length)[valid_mask][window - 1:]
    return corr_x, corr_vals

def render_bps_phaseportrait():
    if bps_status_df.empty:
        return
    bio_series = bps_status_df["Bio"].to_numpy(dtype=float)
    psy_series = bps_status_df["Psy"].to_numpy(dtype=float)
    soz_series = bps_status_df["Soz"].to_numpy(dtype=float)
    phase_quartale = bps_time_x
    fig_bps_phase = go.Figure()
    colors_phase = plotly_template.get_colors()
    styles_phase = plotly_template.get_plot_styles()
    base_marker_style = styles_phase.get('marker_primaryLine', {})
    marker_size = base_marker_style.get('size', 10)
    marker_line_width = base_marker_style.get('line', {}).get('width', 2)
    quartal_min, quartal_max = float(np.nanmin(phase_quartale)), float(np.nanmax(phase_quartale))
    quartal_span = quartal_max - quartal_min if quartal_max != quartal_min else 1.0
    normalized_quartale = (phase_quartale - quartal_min) / quartal_span
    phase_colorscale = [
        [0.0, colors_phase["primaryLine"]],
        [0.5, colors_phase["positiveHighlight"]],
        [1.0, colors_phase["negativeHighlight"]]
    ]
    fig_bps_phase.add_trace(go.Scatter3d(
        x=bio_series,
        y=psy_series,
        z=soz_series,
        mode='lines+markers',
        name='Trajektorie',
        line=dict(color=colors_phase['primaryLine'], width=4),
        marker=dict(
            size=marker_size,
            color=normalized_quartale,
            colorscale=phase_colorscale,
            symbol='circle',
            line=dict(color=colors_phase['white'], width=marker_line_width)
        )
    ))
    fig_bps_phase.add_trace(go.Scatter3d(
        x=[bio_series[0]],
        y=[psy_series[0]],
        z=[soz_series[0]],
        mode='markers',
        name='Start',
        marker=dict(
            size=marker_size * 1.3,
            color=colors_phase['accent'],
            symbol='diamond',
            line=dict(color=colors_phase['white'], width=marker_line_width)
        )
    ))
    fig_bps_phase.add_trace(go.Scatter3d(
        x=[bio_series[-1]],
        y=[psy_series[-1]],
        z=[soz_series[-1]],
        mode='markers',
        name='Ende',
        marker=dict(
            size=marker_size * 1.2,
            color=colors_phase['positiveHighlight'],
            symbol='circle',
            line=dict(color=colors_phase['white'], width=marker_line_width)
        )
    ))
    base_layout = plotly_template.get_standard_layout(
        title=f'Biopsychosoziales Phasenportrait ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='',
        y_title=''
    )
    if 'scene' in base_layout:
        base_layout.pop('scene', None)
    fig_bps_phase.update_layout(**base_layout)
    fig_bps_phase.update_layout(
        scene=dict(
            xaxis=dict(
                title=dict(text='Biologisch', font=dict(color=colors_phase['text'])),
                backgroundcolor=colors_phase['background'],
                gridcolor=colors_phase['text'],
                linecolor=colors_phase['text'],
                tickfont=dict(color=colors_phase['text']),
                zerolinecolor=colors_phase['text']
            ),
            yaxis=dict(
                title=dict(text='Psychologisch', font=dict(color=colors_phase['text'])),
                backgroundcolor=colors_phase['background'],
                gridcolor=colors_phase['text'],
                linecolor=colors_phase['text'],
                tickfont=dict(color=colors_phase['text']),
                zerolinecolor=colors_phase['text']
            ),
            zaxis=dict(
                title=dict(text='Sozial', font=dict(color=colors_phase['text'])),
                backgroundcolor=colors_phase['background'],
                gridcolor=colors_phase['text'],
                linecolor=colors_phase['text'],
                tickfont=dict(color=colors_phase['text']),
                zerolinecolor=colors_phase['text']
            ),
            bgcolor=colors_phase['background'],
            aspectmode='cube'
        ),
        legend=ci_legend()
    )
    safe_fig_show(fig_bps_phase)
    export_figure(fig_bps_phase, 'bps-phasenportrait', export_fig_bps_phase, export_fig_png_bps_phase)

def render_correlation_and_dynamics():
    rolling_window = 3
    rolling_corr = rolling_pearson(mittelwerte_neugier, mittelwerte_motivation, window=rolling_window)
    fig_rolling_corr = go.Figure()
    fig_rolling_corr.add_trace(go.Scatter(
        x=time_x[rolling_window-1:rolling_window-1+len(rolling_corr)],
        y=rolling_corr,
        mode='lines+markers',
        name='Rolling Pearson (3 Quartale)',
        line=ci_line('primary')
    ))
    fig_rolling_corr.update_layout(**plotly_template.get_standard_layout(
        title=f'Gleitende Korrelation Neugier–Motivation (3 Quartale) ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Zeit (Quartal)',
        y_title='Korrelationskoeffizient',
        x_range=[0, CONFIG_QUARTALE]
    ))
    safe_fig_show(fig_rolling_corr)
    export_figure(fig_rolling_corr, 'rolling-corr-neugier-motivation', export_fig_korrelationsdynamik_neugier_motivation, export_fig_png_korrelationsdynamik_neugier_motivation)
    bio_corr_x, bio_corr_vals = compute_bps_rolling_corr(
        bps_status_df["Bio"].to_numpy(dtype=float) if not bps_status_df.empty else [],
        mittelwerte_motivation,
        rolling_window
    )
    psy_corr_x, psy_corr_vals = compute_bps_rolling_corr(
        bps_status_df["Psy"].to_numpy(dtype=float) if not bps_status_df.empty else [],
        mittelwerte_neugier,
        rolling_window
    )
    soz_corr_x, soz_corr_vals = compute_bps_rolling_corr(
        bps_status_df["Soz"].to_numpy(dtype=float) if not bps_status_df.empty else [],
        mittelwerte_pe,
        rolling_window
    )
    if bio_corr_vals.size or psy_corr_vals.size or soz_corr_vals.size:
        fig_bps_corr = go.Figure()
        if bio_corr_vals.size:
            fig_bps_corr.add_trace(go.Scatter(
                x=bio_corr_x,
                y=bio_corr_vals,
                mode='lines+markers',
                name='Bio ↔ Motivation',
                line=ci_line('primary'),
                marker=dict(size=6)
            ))
        if psy_corr_vals.size:
            fig_bps_corr.add_trace(go.Scatter(
                x=psy_corr_x,
                y=psy_corr_vals,
                mode='lines+markers',
                name='Psy ↔ Neugier',
                line=ci_line('secondary'),
                marker=dict(size=6)
            ))
        if soz_corr_vals.size:
            fig_bps_corr.add_trace(go.Scatter(
                x=soz_corr_x,
                y=soz_corr_vals,
                mode='lines+markers',
                name='Soz ↔ PE',
                line=ci_line('accent'),
                marker=dict(size=6)
            ))
        fig_bps_corr.update_layout(**plotly_template.get_standard_layout(
            title=f'Rolling BPS-Korrelationen ({gewaehlter_ansatz} | {selected_archetyp})',
            x_title='Zeit (Quartale)',
            y_title='Korrelationskoeffizient',
            x_range=[0, CONFIG_QUARTALE]
        ))
        safe_fig_show(fig_bps_corr)
        export_figure(fig_bps_corr, 'bps-rolling-korrelationen', export_fig_bps_korrelationen, export_fig_png_bps_korrelationen)
    diff_norm = (diff_neugier_motivation - np.mean(diff_neugier_motivation)) / np.std(diff_neugier_motivation)
    lowess_smoothed = lowess(diff_norm, simulations_ergebnisse_pe.index, frac=0.3)
    fig_korr_dynamik = go.Figure()
    fig_korr_dynamik.add_trace(go.Scatter(
        x=time_x,
        y=diff_norm,
        mode='lines+markers',
        name='Normierte Differenz Neugier–Motivation',
        line=ci_line('primary')
    ))
    fig_korr_dynamik.add_trace(go.Scatter(
        x=time_x,
        y=diff_neugier_motivation,
        mode='lines',
        name='Rohdifferenz Neugier–Motivation',
        line=ci_line('secondary', dash='dash')
    ))
    fig_korr_dynamik.add_trace(go.Scatter(
        x=lowess_smoothed[:, 0],
        y=lowess_smoothed[:, 1],
        mode='lines',
        name='Trend (LOWESS)',
        line=ci_line('accent', dash='dot')
    ))
    fig_korr_dynamik.update_layout(**plotly_template.get_standard_layout(
        title=f'Korrelationsdynamik Neugier-Motivation ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Zeit (Quartal)',
        y_title='Differenz',
        x_range=[0, CONFIG_QUARTALE],
    ))
    safe_fig_show(fig_korr_dynamik)
    export_figure(fig_korr_dynamik, 'korrelationsdynamik-neugier-motivation', export_fig_korrelationsdynamik_neugier_motivation, export_fig_png_korrelationsdynamik_neugier_motivation)

render_correlation_and_dynamics()
render_bps_phaseportrait()
# -----------------------------------------
# Dreidimensionale Unsicherheitsrelation
# -----------------------------------------

# Arrays für Visualisierung vorbereiten
delta_k_mess_array = np.array((delta_k_mess_ktt if USE_KTT_FOR_MESS else delta_k_mess))
delta_k_entw_array = np.array(delta_k_entw)
delta_n_array = np.array(delta_n)

# Falls dynamic_C ein einzelner Wert ist, ersetze ihn durch eine Reihe
if isinstance(dynamic_C, (np.float64, float)):
    dynamic_C = np.full_like(delta_k_mess_array, dynamic_C, dtype=float)

# Skalierungsfaktor, um die Werte in den Bereich 0 bis 10 zu bringen
skalierungsfaktor = 10
delta_k_mess_skal = delta_k_mess_array * skalierungsfaktor
delta_k_entw_skal = delta_k_entw_array * skalierungsfaktor
delta_n_skal = delta_n_array * skalierungsfaktor
dynamic_C_skal = dynamic_C * skalierungsfaktor

# Erstelle den 2D-Plot
fig_dreidimensionale_unsicherheitsrelation = go.Figure()
linien_unsicherheiten = {
    "delta_k_mess": ci_line("primary", width=3),
    "delta_k_entw": ci_line("primary", width=3, dash="dashdot"),
    "delta_n": ci_line("secondary", width=3),
    "dynamic_c": ci_line("accent", width=4),
}

# Kurve für ΔK_mess
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=time_x,
    y=delta_k_mess_skal,
    mode='lines',
    name='Kompetenzmessunsicherheit (ΔK_mess)',
    line=linien_unsicherheiten["delta_k_mess"]
))

# Kurve für ΔK_entw
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=time_x,
    y=delta_k_entw_skal,
    mode='lines',
    name='Kompetenzentwicklungsunsicherheit (ΔK_entw)',
    line=linien_unsicherheiten["delta_k_entw"]
))

# Kurve für ΔN
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=time_x,
    y=delta_n_skal,
    mode='lines',
    name='Neugierunsicherheit (ΔN)',
    line=linien_unsicherheiten["delta_n"]
))

# Kurve für Dynamic-C
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=time_x,
    y=[dynamic_C_skal[0]] * len(simulations_ergebnisse_pe.index),  # Konstante Linie für C
    mode='lines',
    name='Dynamischer Unsicherheitswert C',
    line=linien_unsicherheiten["dynamic_c"]
))

# Layout-Einstellungen für die Visualisierung (CI-konform via plotly_template)
fig_dreidimensionale_unsicherheitsrelation.update_layout(**plotly_template.get_standard_layout(
    title=f'Bildungswirkgefüge | Dreidimensionale Unsicherheitsrelation (ΔK_mess⋅ΔK_entw⋅ΔN ≥ C) ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title='Zeit [Quartal]',
    y_title=f'Unsicherheitsniveau (Faktor {skalierungsfaktor})'
))

safe_fig_show(fig_dreidimensionale_unsicherheitsrelation)
export_figure(fig_dreidimensionale_unsicherheitsrelation, "dreidimensionale-unsicherheitsrelation", export_fig_dreidimensionale_unsicherheitsrelation, export_fig_png)

# Vergleichsplot: ΔK_mess (Residuen) vs. ΔK_mess_KTT
try:
    fig_mess_compare = go.Figure()
    fig_mess_compare.add_trace(go.Scatter(
        x=time_x,
        y=np.array(delta_k_mess, dtype=float),
        mode='lines+markers',
        name='ΔK_mess (Residuen)',
        line=ci_line('primary')
    ))
    fig_mess_compare.add_trace(go.Scatter(
        x=time_x,
        y=np.array(delta_k_mess_ktt, dtype=float),
        mode='lines+markers',
        name='ΔK_mess_KTT',
        line=ci_line('secondary', dash='dash')
    ))
    fig_mess_compare.update_layout(**plotly_template.get_standard_layout(
        title='Vergleich ΔK_mess: Residuen vs. KTT',
        x_title='Zeit [Quartal]', y_title='ΔK'
    ))
    safe_fig_show(fig_mess_compare)
    export_figure(fig_mess_compare, 'delta-k-mess-vergleich', export_fig_summary, export_fig_png)
except Exception as _ex:
    logging.warning('Messvergleich konnte nicht erstellt werden: %s', _ex)

# -----------------------------------------
# TEI-Kompetenzprofil
# -----------------------------------------

fig_mc = go.Figure()
for i, column in enumerate(simulations_ergebnisse_pe_clipped.columns):
    smoothed_data = smooth_curve(simulations_ergebnisse_pe_clipped[column].values, clip_max=10)
    smoothed_data_clipped = np.clip(smoothed_data, 0, 10)
    fig_mc.add_trace(go.Scatter(
        x=time_x,
        y=smoothed_data_clipped,
        mode='lines',
        name=f'TEI-Trajektorie {i + 1}',
        line=ci_line("primary")
    ))
fig_mc.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | TEI-Kompetenzprofil ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title='Zeit [Quartal]',
    y_title='Kompetenzniveau',
    x_range=[0, CONFIG_QUARTALE],
    y_range=[0, 10]
))
# Farbcodierte Archetypenmarkierungen auf die TEI-Trajektorie legen (Synthese, persistent)
try:
    y_vals = simulations_ergebnisse_pe["TEI_Kompetenz"].to_numpy(dtype=float)
    n = int(min(len(y_vals), len(trace)))
    if n > 0:
        cols = plotly_template.get_colors()
        # stabile Reihenfolge der Archetypen nach erstem Auftreten (für Legende)
        order = []
        for name in trace[:n]:
            if name not in order:
                order.append(name)
        # je Archetyp ein Marker-Trace (keine Duplikate, klare Legende)
        x_index = time_x[:n]
        for name in order:
            idx = [i for i in range(n) if trace[i] == name]
            if not idx:
                continue
            fig_mc.add_trace(go.Scatter(
                x=x_index[idx],
                y=y_vals[idx],
                mode='markers',
                name=f'Archetyp: {name}',
                marker=dict(
                    size=8,
                    color=archetype_color(name),
                    line=dict(color=cols.get('white', '#FFFFFF'), width=1)
                )
            ))
except Exception as _e:
    logging.warning("Archetypen-Markierungen konnten nicht hinzugefügt werden: %s", _e)
safe_fig_show(fig_mc)
export_figure(fig_mc, "tei-kompetenzprofil", export_fig_mc, export_fig_png)

# -----------------------------------------
# Statistik des Kompetenzkondensats
# -----------------------------------------

fig_summary = go.Figure()
fig_summary.add_trace(go.Scatter(
    x=time_x_list + time_x_list[::-1],
    y=(np.clip(mittelwerte_kompetenz + stddev_kompetenz, None, 10)).tolist() + (np.clip(mittelwerte_kompetenz - stddev_kompetenz, None, 10)).tolist()[::-1],
    fill='toself',
    fillcolor=plotly_template.get_colors()['brightArea'],
    line=dict(color=plotly_template.get_colors()['depthArea']),
    name='Streuung',
    hoverinfo='text',
    hovertext=[
        f"Quartal {x}, Streuung oben: {y:.2f}" if i < len(simulations_ergebnisse_pe.index) else f"Quartal {x}, Streuung unten: {y:.2f}"
        for i, (x, y) in enumerate(zip(
            simulations_ergebnisse_pe.index.tolist() * 2,
            (np.clip(mittelwerte_kompetenz + stddev_kompetenz, None, 10)).tolist() + (np.clip(mittelwerte_kompetenz - stddev_kompetenz, None, 10)).tolist()[::-1]
        ))
    ]
))
fig_summary.add_trace(go.Scatter(
    x=time_x,
    y=smooth_curve(mittelwerte_kompetenz, clip_max=10),
    mode='lines',
    name='Mittelwert',
    line=ci_line("primary"),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Mittelwert %{y:.2f}<extra></extra>"
))
fig_summary.add_trace(go.Scatter(
    x=time_x,
    y=smooth_curve(mediane_kompetenz, clip_max=10),
    mode='lines',
    name='Median',
    line=ci_line("secondary"),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Median %{y:.2f}<extra></extra>"
))
fig_summary.add_trace(go.Scatter(
    x=time_x,
    y=smooth_curve(mittlere_steigungen),
    mode='lines',
    name='Steigung',
    line=ci_line("accent", dash="dot"),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Steigung %{y:.2f}<extra></extra>"
))
fig_summary.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | Statistik des Kompetenzkondensats ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title="Quartal",
    y_title="Kompetenzniveau",
    x_range=[0, CONFIG_QUARTALE],
    y_range=[0, 10]
))
safe_fig_show(fig_summary)
export_figure(fig_summary, "summary", export_fig_summary, export_fig_png)

# -----------------------------------------
# Kumulative Verdichtung des Kompetenzkondensats
# -----------------------------------------

fig_kumulative_kompetenz = go.Figure()
fig_kumulative_kompetenz.add_trace(go.Scatter(
    x=time_axis_quartale[: len(_y_int)] if 'time_axis_quartale' in globals() else simulations_ergebnisse_pe.index,
    y=_y_int,
    fill='tozeroy',
    fillcolor=plotly_template.get_colors()['depthArea'],
    name='Kompetenz',
    line=ci_line("primary"),
    mode='lines'
))
fig_kumulative_kompetenz.update_layout(**plotly_template.get_standard_layout(
    title=(
        f'Kompetenzniveau | Fläche ∫K dt: {flaeche_unter_mittelwert:.2f} | '
        f'Mittel: {avg_kompetenz_niveau:.2f} | ΔK: {delta_k_total:.2f} '
        f'({gewaehlter_ansatz} | {selected_archetyp})'
    ),
    x_title="Zeit [Quartal]",
    y_title="Kompetenzniveau",
    x_range=[0, (float(time_axis_quartale[-1]) if 'time_axis_quartale' in globals() else quartale)],
    y_range=[0, 10]
))

safe_fig_show(fig_kumulative_kompetenz)
export_figure(fig_kumulative_kompetenz, "kumulative-kompetenz", export_fig_kumulative_kompetenz, export_fig_png)

# -----------------------------------------
# Kompetenzkondensat | Kumulativer Vergleich
# -----------------------------------------

fig_kumulativer_vergleich = go.Figure()

fig_kumulativer_vergleich.add_trace(go.Scatter(
    x=time_x,
    y=smooth_curve(bestes_ergebnis, clip_max=10),
    fill='tozeroy',
    name='Optimum',
    line=ci_line("positive"),
))

fig_kumulativer_vergleich.add_trace(go.Scatter(
    x=time_x,
    y=smooth_curve(schlechtestes_ergebnis, clip_max=10),
    fill='tozeroy',
    name='Minimum',
    line=ci_line("negative"),
))

fig_kumulativer_vergleich.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | Kumulativer Vergleich: Beste ({flaeche_unter_bestes:.2f}) vs. Schlechteste ({flaeche_unter_schlechtestes:.2f}) ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title="Zeit [Quartal]",
    y_title="Kompetenzniveau",
    x_range=[0, CONFIG_QUARTALE],
    y_range=[0, 10]
))

safe_fig_show(fig_kumulativer_vergleich)
export_figure(fig_kumulativer_vergleich, "kumulativer-vergleich", export_fig_kumulativer_vergleich, export_fig_png)

# -----------------------------------------
# Kompetenzkondensat | Histogramm, Dichte und Kernel-Dichte-Schätzung (KDE)
# -----------------------------------------

fig_histogram = go.Figure()

# Histogramm (normiert auf Wahrscheinlichkeit)
fig_histogram.add_trace(go.Histogram(
    x=data_histogramm,
    name="Histogramm",
    marker_color=plotly_template.get_colors()['brightArea'],
    opacity=0.3,
    histnorm='probability',
    yaxis='y1'
))

# KDE
fig_histogram.add_trace(go.Scatter(
    x=x_kde,
    y=y_kde,
    mode='lines',
    line=ci_line("primary"),
    name='KDE',
    yaxis='y2'
))

# Normalverteilung
fig_histogram.add_trace(go.Scatter(
    x=x_kde,
    y=y_norm,
    mode='lines',
    line=ci_line("secondary"),
    name='Dichte',
    yaxis='y2'
))

# Layout mit zwei y-Achsen
fig_histogram.update_layout(
    **plotly_template.get_standard_layout(
        title=f'Kompetenzkondensat | Histogramm, Dichte und Kernel-Dichte-Schätzung (KDE) ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Kompetenzniveau',
        y_title='Wahrscheinlichkeit (Histogramm)',
        yaxis2=dict(
            title='Wahrscheinlichkeitsdichte und KDE',
            overlaying='y',
            side='right',
            showgrid=False,
            showline=True
        ),
        x_range=[0, CONFIG_QUARTALE],
    )
)

safe_fig_show(fig_histogram)
export_figure(fig_histogram, "histogram_dualskala", export_fig_histogramm, export_fig_png)

# -----------------------------------------
# Kompetenzniveau | Verdichtung des Kompetenzkondensats
# -----------------------------------------

fig_kompetenzniveau = go.Figure()

fig_kompetenzniveau.add_trace(
    go.Scatter(
        x=time_x,
        y=kompetenzniveaus_df.mean(axis=1).clip(upper=10),
        mode='lines+markers',
        name='Kompetenzniveau',
        line=ci_line("primary")
    )
)

fig_kompetenzniveau.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | Verdichtung des Kompetenzkondensats ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title="Zeit [Quartal]",
    y_title="Kompetenzniveau",
    x_range=[0, CONFIG_QUARTALE],
    y_range=[0, 10]
))

safe_fig_show(fig_kompetenzniveau)
export_figure(fig_kompetenzniveau, "kompetenzniveau", export_fig_kompetenzniveau, export_fig_png)

# -----------------------------------------
# Clusteranalyse | Neugier-Motivation, Kompetenz, Unsicherheitsrelation
# -----------------------------------------

dynamic_C_arr = np.asarray(dynamic_C)
n = min(len(mittelwerte_neugier), len(kompetenzentwicklung), len(dynamic_C_arr))
if np.isscalar(dynamic_C) or np.ndim(dynamic_C_arr) == 0:
    dynamic_C_arr = np.full(n, dynamic_C_arr if not np.isscalar(dynamic_C_arr) else dynamic_C_arr)
else:
    dynamic_C_arr = dynamic_C_arr[:n]
features = np.array([
    [mittelwerte_neugier[i], kompetenzentwicklung[i], dynamic_C_arr[i]]
    for i in range(n)
])

# Skalierung zur Normierung im Bereich [0, 1]
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# KMeans-Clustering
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
labels = kmeans.fit_predict(features_scaled)
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)


def _describe_dimension(value, mean, std, title):
    """Gibt eine kurze Trendbeschreibung mit Pfeilnotation zurück."""
    threshold = max(std * 0.35, 0.05)
    if value >= mean + threshold:
        tag = "↑"
    elif value <= mean - threshold:
        tag = "↓"
    else:
        tag = "≈"
    return f"{title} {tag}"


feature_means = features.mean(axis=0)
feature_stds = features.std(axis=0) + 1e-6  # Schutz gegen 0
cluster_labels = {}
for idx, center in enumerate(cluster_centers):
    descriptors = [
        _describe_dimension(center[0], feature_means[0], feature_stds[0], "Neugier"),
        _describe_dimension(center[1], feature_means[1], feature_stds[1], "Kompetenz"),
        _describe_dimension(center[2], feature_means[2], feature_stds[2], "C")
    ]
    cluster_labels[idx] = " · ".join(descriptors)

# Silhouette-Score berechnen
silhouette_avg = silhouette_score(features_scaled, labels)
title = f'Clusteranalyse | Neugier – Kompetenz – Unsicherheitsrelation (Silhouette-Score: {silhouette_avg:.3f}) ({gewaehlter_ansatz} | {selected_archetyp})'

# 3D-Visualisierung
fig_clusters = go.Figure()

styles_cluster = plotly_template.get_plot_styles()
# Primär-/Sekundär-/Akzentfarben als Kernpalette für die Cluster
cluster_marker_styles = [
    ci_marker("primary", symbol='circle'),
    ci_marker("secondary", symbol='circle'),
    ci_marker("accent", symbol='circle'),
]

for cluster_id in range(n_clusters):
    cluster_points = features[labels == cluster_id]
    base_style = cluster_marker_styles[cluster_id] if cluster_id < len(cluster_marker_styles) else ci_marker("primary", symbol='circle')
    marker_style = {**base_style}  # nicht das Original-Dict mutieren
    marker_style['size'] = [8 + len(cluster_points) * (80 / len(features))] * len(cluster_points)
    marker_style['opacity'] = 0.85
    fig_clusters.add_trace(go.Scatter3d(
        x=cluster_points[:, 0],
        y=cluster_points[:, 1],
        z=cluster_points[:, 2],
        mode='markers',
        name=cluster_labels.get(cluster_id, f'Cluster {cluster_id + 1}'),
        marker=marker_style,
        hoverinfo='text',
        text=[
            f"Quartal {i}<br>Neugier: {features[i,0]:.2f}<br>Kompetenz: {features[i,1]:.2f}<br>C: {features[i,2]:.2f}<br>{cluster_labels.get(cluster_id, '')}"
            for i in np.where(labels == cluster_id)[0]
        ]
    ))

# Layout anwenden, CI-konform inklusive scene für 3D
fig_clusters.update_layout(
    title=title,
    scene=dict(
        xaxis=dict(
            title=dict(text='Neugier', font=dict(color=colors['text'])),
            color=colors['text'],
            backgroundcolor=colors['background'],
            gridcolor=colors['text'],
            linecolor=colors['text'],
            tickfont=dict(color=colors['text']),
            zerolinecolor=colors['text'],
            showspikes=True,
            spikethickness=1
        ),
        yaxis=dict(
            title=dict(text='Kompetenz', font=dict(color=colors['text'])),
            color=colors['text'],
            backgroundcolor=colors['background'],
            gridcolor=colors['text'],
            linecolor=colors['text'],
            tickfont=dict(color=colors['text']),
            zerolinecolor=colors['text'],
            showspikes=True,
            spikethickness=1
        ),
        zaxis=dict(
            title=dict(text='C-Wert', font=dict(color=colors['text'])),
            color=colors['text'],
            backgroundcolor=colors['background'],
            gridcolor=colors['text'],
            linecolor=colors['text'],
            tickfont=dict(color=colors['text']),
            zerolinecolor=colors['text'],
            showspikes=True,
            spikethickness=1
        ),
        bgcolor=colors['background']
    ),
    hovermode='closest',
    hoverlabel=dict(
        bgcolor=colors["background"],
        font=dict(color=colors["text"]),
        bordercolor=colors["text"]
    ),
    paper_bgcolor=colors['background'],
    plot_bgcolor=colors['background'],
    font=dict(color=colors['text'])
)

safe_fig_show(fig_clusters)
export_figure(fig_clusters, "clusteranalyse", export_fig_clusters, export_fig_png)

# -----------------------------------------
# Bildungswirkgefüge | ν und ι
# -----------------------------------------

# Visualisierung des Bildungswirkgefüges
fig_bildungswirkgefuege = go.Figure()

# Plot für Bildungswirkfaktoren (ν)
fig_bildungswirkgefuege.add_trace(go.Scatter(
    x=time_x,
    y=bildungswirkfaktoren_smooth,
    mode='lines+markers',
    name='ν (Bildungswirkfaktor)',
    line=ci_line("primary")
))

# Plot für Bildungswirkindikator (ι) auf sekundärer y-Achse
fig_bildungswirkgefuege.add_trace(go.Scatter(
    x=time_x,
    y=steigungen_bildungswirkfaktor_smooth,
    mode='lines+markers',
    name='ι (Bildungswirkindikator)',
    line=ci_line("secondary"),
    marker=dict(
        color=steigungen_bildungswirkfaktor_smooth,
        colorscale=[[0, colors['negativeHighlight']], [1, colors['positiveHighlight']]],
        size=6,
        showscale=False
    ),
    yaxis='y2'
))

# Wendepunkte für den Bildungswirkindikator plotten
for point in wendepunkte_bildungswirkindikator:
    if zweite_ableitung_bildungswirkindikator[point] > 0:
        color = colors['positiveHighlight']
        text = "Stabilisierungspunkt | Positiver Wendepunkt erreicht: Interventionen wirken, Interventionen stabilisieren (Strategie effektiv)"
        name = 'Stabilisation'
    else:
        color = colors['negativeHighlight']
        text = "Präventionspunkt | Negativer Wendepunkt erreicht: Präventive Interventionen notwendig, Risiko erkannt (Ursachenforschung notwendig)."
        name = 'Prävention'

    fig_bildungswirkgefuege.add_trace(go.Scatter(
        x=[time_x[point]],
        y=[steigungen_bildungswirkfaktor_smooth[point]],
        mode='markers',
        marker=dict(color=color, size=25),
        name=name,
        text=[text],
        hoverinfo='text',
        yaxis='y2'
    ))

# Minima und Maxima mit Empfehlungen
point_annotations = [
    (minima_bildungswirkfaktor, 'negativeHighlight', 'Intervention', "Interventionspunkt | Minimum erreicht: Interventionsbedarf zur Verhinderung eines erneuten Anstiegs."),
    (maxima_bildungswirkfaktor, 'positiveHighlight', 'Regeneration', "Regenerationspunkt | Maximum erreicht: Interventionen erfolgreich, Monitoring weiterhin erforderlich.")
]

for points, color, name, text in point_annotations:
    for point in points:
        fig_bildungswirkgefuege.add_trace(go.Scatter(
            x=[time_x[point]],
            y=[bildungswirkfaktoren_smooth[point]],
            mode='markers',
            marker=dict(color=colors[color], size=25),
            name=name,
            text=[text],
            hoverinfo='text'
        ))

layout = plotly_template.get_standard_layout(
    title=f'Bildungswirkgefüge | ν und ι ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title="Zeit [Quartal]",
    y_title="ν (Bildungswirkfaktor)",
    x_range=[0, CONFIG_QUARTALE],
    yaxis2=dict(
        title=dict(text="ι (Bildungswirkindikator)", font=dict(color=colors['text'])),
        tickfont=dict(color=colors['text']),
        linecolor=colors['text'],
        tickcolor=colors['text'],
        overlaying='y',
        side='right',
        showgrid=False,
        showline=True
    )
)

fig_bildungswirkgefuege.update_layout(**layout)

safe_fig_show(fig_bildungswirkgefuege)
export_figure(fig_bildungswirkgefuege, "bildungswirkgefuege", export_fig_bildungswirkgefuege, export_fig_png)

# -----------------------------------------
# Bildungsgefüge | Bildungswirkdynamik
# -----------------------------------------

fig_bildungswirkdynamik = go.Figure()

# Plot für kumulative Bildungswirkung
fig_bildungswirkdynamik.add_trace(
    go.Scatter(
        x=time_x,
        y=bildungswirkfaktoren_smooth,
        fill='tozeroy',
        name='ν dx',
        line=ci_line("primary"),
        fillcolor=colors['depthArea']
    )
)

# Wendepunkte plotten
for wendepunkt in wendepunkte_bildungswirkfaktor:
    if zweite_ableitung_bildungswirkfaktor[wendepunkt] > 0:
        wendepunkt_text = 'Stabilisierungspunkt | Positiver Wendepunkt erreicht: Interventionen wirken, Maßnahmen stabilisieren'
        marker_color = colors['brightArea']
        name = 'Stabilisation'
    else:
        wendepunkt_text = 'Präventionspunkt | Negativer Wendepunkt erreicht: Präventive Maßnahmen notwendig, Risiko erkannt.'
        marker_color = colors['depthArea']
        name = 'Prävention'

    fig_bildungswirkdynamik.add_trace(go.Scatter(
        x=[time_x[wendepunkt]],
        y=[bildungswirkfaktoren_smooth[wendepunkt]],
        mode='markers',
        name=name,
        marker=dict(color=marker_color, size=25),
        text=[wendepunkt_text],
        hoverinfo='text'
    ))

# Minima plotten
minimum_text = 'Interventionspunkt | Minimum erreicht: Interventionsbedarf zur Verhinderung eines erneuten Anstiegs.'
fig_bildungswirkdynamik.add_trace(go.Scatter(
    x=time_x[minima_bildungswirkfaktor],
    y=bildungswirkfaktoren_smooth[minima_bildungswirkfaktor],
    mode='markers',
    name='Intervention',
    marker=dict(color=colors['negativeHighlight'], size=25),
    text=[minimum_text for _ in minima_bildungswirkfaktor],
    hoverinfo='text'
))

# Maxima plotten
maximum_text = 'Regenerationspunkt | Maximum erreicht: Interventionen erfolgreich, Monitoring weiterhin erforderlich.'
fig_bildungswirkdynamik.add_trace(go.Scatter(
    x=time_x[maxima_bildungswirkfaktor],
    y=bildungswirkfaktoren_smooth[maxima_bildungswirkfaktor],
    mode='markers',
    name='Regeneration',
    marker=dict(color=colors['positiveHighlight'], size=25),
    text=[maximum_text for _ in maxima_bildungswirkfaktor],
    hoverinfo='text'
))

# Diagramm-Layout
fig_bildungswirkdynamik.update_layout(
    **plotly_template.get_standard_layout(
        title=f'Bildungswirkgefüge | Kumulative Bildungswirkdynamik (ν dx): {integral_bildungswirkfaktor:.2f} ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title="Zeit [Quartal]",
        y_title="Kumulative Bildungswirkung (ν dx)"
    )
)

safe_fig_show(fig_bildungswirkdynamik)
export_figure(fig_bildungswirkdynamik, "bildungswirkdynamik", export_bildungswirkdynamik, export_fig_png)

# -----------------------------------------
# Sankey-Diagramm (Flussdiagramm)
# -----------------------------------------

def _safe_abs(value):
    return abs(value) if isinstance(value, (int, float, np.floating)) else 0.0

def _allocate_flow(total_value, weight_candidates):
    """Verteile einen Gesamtwert proportional auf Zielkanten."""
    weights = [_safe_abs(w) for w in weight_candidates]
    if not weights:
        return []
    total_magnitude = sum(weights)
    if total_magnitude == 0:
        return [total_value / len(weights)] * len(weights) if len(weights) > 0 else []
    return [total_value * (w / total_magnitude) for w in weights]

def _hex_to_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f'rgba({r}, {g}, {b}, {alpha})'

# Labels für das Sankey-Diagramm
labels = [
    "Initiale Neugier", "Startkompetenz", "persönliche Ereignisse",
    "Veränderungen Neugier", "Veränderungen Motivation", "Bereitschaft",
    "Kompetenzniveau", "Kompetenzmessunsicherheit", "Kompetenzentwicklungsunsicherheit",
    "ν (Bildungswirkfaktor)", "ι (Bildungswirkindikator)"
]

# Grundgrößen für Flussberechnung
initial_neugier_value = max(initial_neugier, 0)
start_kompetenz_value = max(start_kompetenz, 0)
pe_wirkungen_sum = sum(pe_wirkungen)
veranderungen_neugier_sum = flatten_and_sum(veranderungen_neugier)
veranderungen_motivation_sum = flatten_and_sum(veranderungen_motivation)
bereitschaft_sum = sum(bereitschaft)

# Aufteilung der Flüsse von den Startknoten
initial_flows = _allocate_flow(initial_neugier_value, [veranderungen_neugier_sum, veranderungen_motivation_sum, bereitschaft_sum])
pe_flows = _allocate_flow(abs(pe_wirkungen_sum), [veranderungen_neugier_sum, veranderungen_motivation_sum, bereitschaft_sum])
pe_flows = [np.sign(pe_wirkungen_sum or 1) * f for f in pe_flows]

# Hilfsstruktur zum Sammeln der Kanten
edges = []

def _add_edge(src, tgt, signed_value):
    magnitude = _safe_abs(signed_value)
    if magnitude <= 1e-9:
        return
    edges.append((src, tgt, magnitude, signed_value))

# Eingangsflüsse
_add_edge(0, 3, initial_flows[0] if len(initial_flows) > 0 else 0)
_add_edge(0, 4, initial_flows[1] if len(initial_flows) > 1 else 0)
_add_edge(0, 5, initial_flows[2] if len(initial_flows) > 2 else 0)
_add_edge(1, 5, start_kompetenz_value)
_add_edge(2, 3, pe_flows[0] if len(pe_flows) > 0 else 0)
_add_edge(2, 4, pe_flows[1] if len(pe_flows) > 1 else 0)
_add_edge(2, 5, pe_flows[2] if len(pe_flows) > 2 else 0)

# Flüsse aus den Zwischenknoten (Summe der eingehenden Beträge weiterreichen)
def _total_inflow(target_node):
    return sum(edge[2] for edge in edges if edge[1] == target_node)

def _total_signed_inflow(target_node):
    return sum(edge[3] for edge in edges if edge[1] == target_node)

neugier_total = _total_inflow(3)
motivation_total = _total_inflow(4)
bereitschaft_total = _total_inflow(5)

_add_edge(3, 6, np.sign(_total_signed_inflow(3) or 1) * neugier_total)
_add_edge(4, 6, np.sign(_total_signed_inflow(4) or 1) * motivation_total)
_add_edge(5, 6, np.sign(_total_signed_inflow(5) or 1) * bereitschaft_total)

# Aufteilung der Kompetenz auf Mess- und Entwicklungsunsicherheit
kompetenz_total = _total_inflow(6)
delta_k_entw_weight = _safe_abs(np.nanmean(delta_k_entw))
delta_k_mess_weight = _safe_abs(np.nanmean(delta_k_mess))
unsicherheits_flows = _allocate_flow(kompetenz_total, [delta_k_entw_weight, delta_k_mess_weight])

_add_edge(6, 7, np.sign(np.nanmean(delta_k_entw) or 1) * (unsicherheits_flows[0] if len(unsicherheits_flows) > 0 else 0))
_add_edge(6, 8, np.sign(np.nanmean(delta_k_mess) or 1) * (unsicherheits_flows[1] if len(unsicherheits_flows) > 1 else 0))

# Bildungswirkfaktor aus beiden Unsicherheiten speisen
_add_edge(7, 9, np.sign(np.nanmean(delta_k_entw) or 1) * _total_inflow(7))
_add_edge(8, 9, np.sign(np.nanmean(delta_k_mess) or 1) * _total_inflow(8))

# Bildungswirkindikator erhält Gesamtfluss aus ν
nu_total = _total_inflow(9)
_add_edge(9, 10, np.sign(np.mean(bildungswirkindikator) or 1) * nu_total)

# Daten für Plotly vorbereiten
sources = [edge[0] for edge in edges]
targets = [edge[1] for edge in edges]
values = [edge[2] for edge in edges]
custom_values = [edge[3] for edge in edges]

# Knotenfarben
node_colors = [
    plotly_template.get_colors()["positiveHighlight"],  # Initiale Neugier
    plotly_template.get_colors()["background"],         # Startkompetenz
    plotly_template.get_colors()["accent"],             # Persönliche Ereignisse
    plotly_template.get_colors()["positiveHighlight"],  # Veränderungen Neugier
    plotly_template.get_colors()["negativeHighlight"],  # Veränderungen Motivation
    plotly_template.get_colors()["accent"],             # Bereitschaft
    plotly_template.get_colors()["background"],         # Kompetenzniveau
    plotly_template.get_colors()["depthArea"],          # Messunsicherheit
    plotly_template.get_colors()["brightArea"],         # Entwicklungsunsicherheit
    plotly_template.get_colors()["primaryLine"],        # ν
    plotly_template.get_colors()["secondaryLine"],      # ι
]

# Linkfarben abhängig vom Vorzeichen
positive_link_color = _hex_to_rgba(plotly_template.get_colors()["text"], 0.6)
negative_link_color = _hex_to_rgba(plotly_template.get_colors()["negativeHighlight"], 0.65)
link_colors = [positive_link_color if val >= 0 else negative_link_color for val in custom_values]

# Erstellen des Sankey-Diagramms
fig_flussdiagramm = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color=plotly_template.get_colors()["text"], width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors,
        customdata=custom_values,
        hovertemplate=(
            '<b>%{source.label}</b> → <b>%{target.label}</b><br />' +
            'Wert: %{customdata:.3f}<extra></extra>'
        )
    )
)])

fig_flussdiagramm.update_layout(
    title_text=f'Bildungswirkgefüge | Sankey-Diagramm: Einflüsse und Strömungen ({gewaehlter_ansatz} | {selected_archetyp})',
    font_size=10,
    plot_bgcolor=plotly_template.get_colors()["background"],
    paper_bgcolor=plotly_template.get_colors()["background"],
    font=dict(color=plotly_template.get_colors()["text"])
)

safe_fig_show(fig_flussdiagramm)
export_figure(fig_flussdiagramm, "flussdiagramm", export_fig_flussdiagramm, export_fig_png)

# ----------------------------------
# Ontologisch-systemische Trajektorie (basierend auf H)
# ----------------------------------

# Sicherstellen, dass ΔK_mess und ΔK_entw die korrekte Länge haben
schedule_length = len(relative_schedule)
if len(delta_k_mess) != schedule_length:
    delta_k_mess = np.resize(delta_k_mess, schedule_length)
if len(delta_k_entw) != schedule_length:
    delta_k_entw = np.resize(delta_k_entw, schedule_length)

# Berechne die Gesamtdauer und Zeitfaktor
total_days = sum([duration for _, duration in relative_schedule])
days_per_quarter = total_days / 12  # Quartaleinheit

# Interdependenzoperator H als komplexe Synthese aus ΔK_entw und ΔK_mess
def berechne_H_komplex(delta_k_entw_series, delta_k_mess_series):
    magnitude = np.sqrt((delta_k_entw_series**2 + delta_k_mess_series**2) / 2)
    richtung = np.arctan2(delta_k_entw_series, delta_k_mess_series)  # Richtung im ΔK_entw/ΔK_mess-Raum
    return magnitude * np.exp(1j * richtung)

H_komplex = berechne_H_komplex(np.array(delta_k_entw), np.array(delta_k_mess))

# Netzwerkgraf vorbereiten
G = nx.Graph()
sections = ["Einführung", "Ressourcen", "Aufgaben", "Ergebnissicherung", "Weiterführende Quellen", "Lounge", "Feedback", "Kursorganisation"]
fixed_radius = 0.5

# Knoten definieren
for i, (course_name, duration) in enumerate(relative_schedule):
    task_count = task_counts[i] if i < len(task_counts) else 10
    G.add_node(course_name, title=f"Handlungssituation {course_name.split('-')[-1]}",
               color=plotly_template.get_colors()['primaryLine'],
               info=f"Informationen zu {course_name}\nDauer: {duration} Tage")
    for section in sections:
        section_name = f"{course_name} - {section}"
        G.add_node(section_name, title=section, color=plotly_template.get_colors()['secondaryLine'], info=f"Details zu {section} in {course_name}")
        G.add_edge(course_name, section_name, title=f"{course_name} to {section}")

# Ontologisch-systemische Knotenpositionierung aus H
pos = {}
current_day = 0

# Extrahiere Real- und Imaginärteile (ΔK_mess und ΔK_entw) aller H_i
delta_K_all = [np.real(H_i) for H_i in H_komplex]
delta_E_all = [np.imag(H_i) for H_i in H_komplex]

# Min-Max-Normalisierung auf Bereich [0, 10]
def normalize(values):
    min_val = np.min(values)
    max_val = np.max(values)
    if max_val == min_val:
        return [5.0 for _ in values]  # Vermeide Division durch 0 – mittig platzieren
    return [10 * (v - min_val) / (max_val - min_val) for v in values]

x_values = normalize(delta_K_all)
y_values = normalize(delta_E_all)

# Z-Achse (Ordinalzeitachse) bleibt wie gehabt
pos = {}
current_day = 0

for i, (course_name, duration) in enumerate(relative_schedule):
    z = current_day / days_per_quarter  # Zeitstruktur
    x = x_values[i]
    y = y_values[i]
    pos[course_name] = (x, y, z)
    current_day += duration

    # Unterknoten wie bisher (geometrisch um Hauptknoten)
    indices = np.arange(0, len(sections), dtype=float) + 0.5
    phi = np.arccos(1 - 2 * indices / len(sections))
    theta = np.pi * (1 + 5**0.5) * indices
    x_sphere = x + fixed_radius * np.sin(phi) * np.cos(theta)
    y_sphere = y + fixed_radius * np.sin(phi) * np.sin(theta)
    z_sphere = z + fixed_radius * np.cos(phi)
    for j, section in enumerate(sections):
        section_name = f"{course_name} - {section}"
        pos[section_name] = (x_sphere[j], y_sphere[j], z_sphere[j])

# Knotengrößen
node_size = []
for node in G.nodes():
    if "Aufgaben" in node:
        course_name = node.split(" - ")[0]
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == course_name), -1)
        size = 10 + 0.5 * task_counts[course_index] if course_index >= 0 else 6
    elif node in [name for name, _ in relative_schedule]:
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == node), -1)
        size = 20 + 0.3 * relative_schedule[course_index][1] if course_index >= 0 else 20
    else:
        size = 6
    node_size.append(size)

# Hovertexte
node_hovertext = []
for node in G.nodes():
    if "Aufgaben" in node:
        course_name = node.split(" - ")[0]
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == course_name), -1)
        hover_info = f"{G.nodes[node]['title']}<br>Anzahl der Aufgaben: {task_counts[course_index]}"
    elif "-" not in node:
        course_index = next((i for i, (c_name, _) in enumerate(relative_schedule) if c_name == node), -1)
        duration = relative_schedule[course_index][1] if course_index >= 0 else 'N/A'
        hover_info = f"{G.nodes[node]['title']}<br>Dauer: {duration} Tage"
    else:
        hover_info = f"{G.nodes[node]['title']}<br>{G.nodes[node]['info']}"
    node_hovertext.append(hover_info)

# Knoten-Trace
node_trace = go.Scatter3d(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    z=[pos[node][2] for node in G.nodes()],
    mode='markers+text',
    marker=dict(size=node_size, color=[G.nodes[node]['color'] for node in G.nodes()]),
    text=[G.nodes[node]['title'] for node in G.nodes()],
    textfont=dict(color=[plotly_template.get_colors()['white'] if 'Handlungssituation' in G.nodes[node]['title'] else G.nodes[node]['color'] for node in G.nodes()]),
    hoverinfo='text',
    hovertext=node_hovertext,
    hoverlabel=dict(
        bgcolor=colors['background'],
        font=dict(color=colors['text'], size=16, family="Arial"),
        bordercolor=colors['text']
    ),
    textposition='top center',
    name='Handlungssituation'
)

# Kanten-Trace
edge_x, edge_y, edge_z = [], [], []
for edge in G.edges():
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

edge_trace = go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    mode='lines',
    line=dict(color=plotly_template.get_colors()['depthArea'], width=3),
    name='Aktivität/Material'
)

# Lernpfad
learning_path_nodes = [pos[course_name] for course_name, _ in relative_schedule if course_name in G.nodes()]
x_path, y_path, z_path = zip(*learning_path_nodes)
t = np.linspace(0, 1, len(x_path))
t_fine = np.linspace(0, 1, 200)
x_spline = interp1d(t, x_path, kind='cubic')(t_fine)
y_spline = interp1d(t, y_path, kind='cubic')(t_fine)
z_spline = interp1d(t, z_path, kind='cubic')(t_fine)

learning_path_trace = go.Scatter3d(
    x=x_spline, y=y_spline, z=z_spline,
    mode='lines',
    line=ci_line("accent", width=5),
    name='Interdependenzpfad'
)

# Visualisierung
colors = plotly_template.get_colors()
fig_trajektorie = go.Figure(data=[edge_trace, node_trace, learning_path_trace])
# Entferne die automatische Übergabe von 'scene' aus dem Standard-Layout
standard_layout = plotly_template.get_standard_layout(
    title=f'Bildungswirkgefüge | Ontologisch-systemische Trajektorie (basierend auf H) ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title=None,
    y_title=None
)
standard_layout.pop("scene", None)

fig_trajektorie.update_layout(**standard_layout)
fig_trajektorie.update_layout(
    scene=dict(
        xaxis=dict(
            title=dict(text='Re(H) ∼ ΔK', font=dict(color=colors["text"])),
            range=[0, 10],
            showbackground=True,
            backgroundcolor=colors["background"],
            gridcolor=colors["text"],
            linecolor=colors["text"],
            tickfont=dict(color=colors["text"]),
            zerolinecolor=colors["text"]
        ),
        yaxis=dict(
            title=dict(text='Im(H) ∼ ΔK_entw', font=dict(color=colors["text"])),
            range=[0, 10],
            showbackground=True,
            backgroundcolor=colors["background"],
            gridcolor=colors["text"],
            linecolor=colors["text"],
            tickfont=dict(color=colors["text"]),
            zerolinecolor=colors["text"]
        ),
        zaxis=dict(
            title=dict(text='Zeit (Quartale)', font=dict(color=colors["text"])),
            range=[0, 12],
            showbackground=True,
            backgroundcolor=colors["background"],
            gridcolor=colors["text"],
            linecolor=colors["text"],
            tickfont=dict(color=colors["text"]),
            zerolinecolor=colors["text"]
        ),
        aspectmode='cube'
    ),
    legend=ci_legend(),
    paper_bgcolor=colors["background"],
    plot_bgcolor=colors["background"],
    margin=dict(l=0, r=0, b=0, t=60),
    showlegend=True
)
safe_fig_show(fig_trajektorie)
export_figure(fig_trajektorie, "ontologisch-systemische-trajektorie", export_fig_trajektorie, export_fig_png)

# ----------------------------------
# Morphologische Kompetenzentwicklung
# ----------------------------------

# Skalierungsfaktor (visuell, nicht modellverändernd)
# Automatische Kalibrierung: skaliert die maximalen Radien (ΔK_mess, ΔK_entw)
# auf einen gewünschten Zielradius der 3D-Darstellung.
target_radius = 0.6
epsilon = 1e-6

# Ontologisch fundierte Ableitungen aus dem Interdependenzoperator H
delta_K_all = [np.real(H_i) for H_i in H_komplex]  # Projektion auf ΔK_mess
delta_E_all = [np.imag(H_i) + 1 for H_i in H_komplex]  # Projektion auf ΔK_entw (+1 als Restterm)

# Automatisch geeigneten Skalierungsfaktor bestimmen
try:
    _r_mess = np.nanmax(np.abs(np.asarray(delta_K_all, dtype=float))) if len(delta_K_all) else 0.0
    _r_entw = np.nanmax(np.abs(np.asarray(delta_E_all, dtype=float))) if len(delta_E_all) else 0.0
    max_r = float(max(_r_mess, _r_entw))
except Exception:
    max_r = 0.0
skalierungsfaktor = float(target_radius / max(epsilon, max_r)) if max_r > 0 else 1.0

delta_k_skal = np.array(delta_K_all, dtype=float) * skalierungsfaktor
delta_k_entw_skal = np.array(delta_E_all, dtype=float) * skalierungsfaktor

# Bildungswirkfaktor als Mittelachse
ν_3d_kompetenz = bildungswirkfaktoren_smooth

# Dynamische Interpolation
max_len = max(len(delta_k_skal), len(delta_k_entw_skal), len(ν_3d_kompetenz))

def dynamisch_interpolieren(array, ziel_len):
    if len(array) != ziel_len:
        spline = make_interp_spline(np.arange(len(array)), array, k=3)
        return spline(np.linspace(0, len(array) - 1, ziel_len))
    return array

delta_k_skal = dynamisch_interpolieren(delta_k_skal, max_len)
delta_k_entw_skal = dynamisch_interpolieren(delta_k_entw_skal, max_len)
ν_3d_kompetenz_interpoliert = dynamisch_interpolieren(ν_3d_kompetenz, max_len)

# Zeitachse (Z)
_len_z = len(ν_3d_kompetenz_interpoliert)
z_time = time_axis_quartale[:_len_z] if 'time_axis_quartale' in globals() else np.linspace(0, CONFIG_QUARTALE, _len_z)

# Radien (Abstand zur Mittelachse)
radius_k = np.abs(delta_k_skal - ν_3d_kompetenz_interpoliert)
radius_entw = np.abs(delta_k_entw_skal - ν_3d_kompetenz_interpoliert)

# Zirkuläre Interpolation
num_phi = 50
phi = np.linspace(0, 2 * np.pi, num_phi)

ν_3d_kompetenz_repeated = np.tile(ν_3d_kompetenz_interpoliert[:, np.newaxis], (1, num_phi))
radius_k_repeated = np.tile(radius_k[:, np.newaxis], (1, num_phi))
radius_entw_repeated = np.tile(radius_entw[:, np.newaxis], (1, num_phi))
phi_repeated = np.tile(phi, (max_len, 1))
z_repeated = np.tile(z_time[:, np.newaxis], (1, num_phi))

# Fläche: kognitive Unsicherheit
x_kogn = ν_3d_kompetenz_repeated + radius_k_repeated * np.cos(phi_repeated)
y_kogn = ν_3d_kompetenz_repeated + radius_k_repeated * np.sin(phi_repeated)

# Fläche: emotionale Unsicherheit
x_entw = ν_3d_kompetenz_repeated + radius_entw_repeated * np.cos(phi_repeated)
y_entw = ν_3d_kompetenz_repeated + radius_entw_repeated * np.sin(phi_repeated)

# Energetische Dichte aus H
H_energy = np.abs(H_komplex) ** 2
H_energy_interpol = dynamisch_interpolieren(H_energy, max_len)

# Normierung für die Farbkodierung und separate Radien-Skalierung für bessere Sichtbarkeit
_e_min = float(np.nanmin(H_energy_interpol)) if len(H_energy_interpol) else 0.0
_e_max = float(np.nanmax(H_energy_interpol)) if len(H_energy_interpol) else 1.0
_e_span = max(epsilon, _e_max - _e_min)
energy_norm = (np.asarray(H_energy_interpol, dtype=float) - _e_min) / _e_span

# Zielradius für die energetische Hülle (visuell)
energy_target_radius = 0.6
energy_radius = energy_norm * energy_target_radius

energy_repeated_color = np.tile(energy_norm[:, np.newaxis], (1, num_phi))
energy_repeated_radius = np.tile(energy_radius[:, np.newaxis], (1, num_phi))

x_energy = ν_3d_kompetenz_repeated + energy_repeated_radius * np.cos(phi_repeated)
y_energy = ν_3d_kompetenz_repeated + energy_repeated_radius * np.sin(phi_repeated)

# Visualisierung starten
fig_morphologische_kompetenzentwicklung = go.Figure()

# Messunsicherheit
fig_morphologische_kompetenzentwicklung.add_trace(go.Surface(
    x=x_kogn, y=y_kogn, z=z_repeated,
    surfacecolor=radius_k_repeated,
    colorscale=[[0, colors["brightArea"]], [1, colors["depthArea"]]],
    showscale=False,
    opacity=0.7,
    name="ΔK_mess"
))

# Entwicklungsunsicherheit
fig_morphologische_kompetenzentwicklung.add_trace(go.Surface(
    x=x_entw, y=y_entw, z=z_repeated,
    surfacecolor=radius_entw_repeated,
    colorscale=[[0, colors["brightArea"]], [1, colors["brightArea"]]],
    showscale=False,
    opacity=0.5,
    name="ΔK_entw+1"
))

# Definiere Schwellen für niedrig, optimal und hoch
H_min = np.percentile(H_energy, 20)
H_opt = np.percentile(H_energy, 50)
H_max = np.percentile(H_energy, 80)

# Farbverlauf für H-Energie: sanfter Übergang von negativ (rot) → optimal (grün) → überkomplex (orange)
colorscale_energy = [
    [0.0,  colors["negativeHighlight"]],   # Start: niedriges H (rot)
    [0.25, colors["negativeHighlight"]],
    [0.40, colors["positiveHighlight"]],   # sanfter Übergang
    [0.60, colors["positiveHighlight"]],   # Zentrum: optimal
    [0.75, colors["secondaryLine"]],       # Übergang zu überkomplex
    [1.0,  colors["secondaryLine"]]        # Ende: hohes H (orange)
]

# Energetische Dichte (|H|²)
fig_morphologische_kompetenzentwicklung.add_trace(go.Surface(
    x=x_energy, y=y_energy, z=z_repeated,
    surfacecolor=energy_repeated_color,
    colorscale=colorscale_energy,
    showscale=True,
    opacity=0.4,
    colorbar=dict(title='|H|² (normiert)', tickformat='.3f'),
    name="|H|²"
))

# Sichtbarmachung der Mittelachse (Bildungswirkfaktor)
fig_morphologische_kompetenzentwicklung.add_trace(go.Scatter3d(
    x=ν_3d_kompetenz_interpoliert,
    y=ν_3d_kompetenz_interpoliert,
    z=z_time,
    mode='lines',
    line=dict(color=colors["primaryLine"], width=4),  # Linienstärke hier anpassbar
    name='Bildungswirkfaktor (ν)',
    showlegend=True
))

# Volumenberechnung

volumen = 0
for i in range(len(delta_k_skal) - 1):
    flaeche_delta_k = 0.5 * (delta_k_skal[i] + delta_k_skal[i + 1])
    flaeche_delta_e = 0.5 * (delta_k_entw_skal[i] + delta_k_entw_skal[i + 1])
    hoehe = z_time[i + 1] - z_time[i]
    volumen += (flaeche_delta_k * flaeche_delta_e * hoehe)

volumen_gerundet = round(volumen, 2)


# CI‑konformes Layout aus dem zentralen Template holen (ohne xaxis/yaxis)
layout = plotly_template.get_standard_layout(
    title=f"Morphologische Kompetenzentwicklung (ontologisch & energetisch) – Gesamtvolumen: {volumen_gerundet} ({gewaehlter_ansatz} | {selected_archetyp})",
    x_title=None,
    y_title=None
)
# Automatisch gesetzte xaxis/yaxis entfernen
layout.pop("xaxis", None)
layout.pop("yaxis", None)
# 3D scene gemäß CI konfigurieren, alle "white" Werte durch zentrale CI-Farbe "text" ersetzen
layout["scene"] = dict(
    xaxis=dict(
        title=dict(text="Re(H) ∼ ΔK_mess", font=dict(color=colors["text"])),
        tickfont=dict(color=colors["text"]),
        backgroundcolor=colors["background"],
        gridcolor=colors["text"],
        linecolor=colors["text"],
        zerolinecolor=colors["text"]
    ),
    yaxis=dict(
        title=dict(text="Im(H) ∼ ΔK_entw+1", font=dict(color=colors["text"])),
        tickfont=dict(color=colors["text"]),
        backgroundcolor=colors["background"],
        gridcolor=colors["text"],
        linecolor=colors["text"],
        zerolinecolor=colors["text"]
    ),
    zaxis=dict(
        title=dict(text="Zeit [Quartale]", font=dict(color=colors["text"])),
        tickfont=dict(color=colors["text"]),
        backgroundcolor=colors["background"],
        gridcolor=colors["text"],
        linecolor=colors["text"],
        zerolinecolor=colors["text"]
    ),
    bgcolor=colors["background"],
    aspectratio=dict(x=1.0, y=1.0, z=1.2)
)
# Layout anwenden
fig_morphologische_kompetenzentwicklung.update_layout(**layout)

safe_fig_show(fig_morphologische_kompetenzentwicklung)
export_figure(fig_morphologische_kompetenzentwicklung, "morphologische-kompetenzentwicklung", export_fig_morphologische_kompetenzentwicklung, export_fig_png)

# -----------------------------------------
# Kombinierte Fibonacci-Spiralvisualisierung
# (mit Fibonacci-Raster, Ursprung, Übergangs-Cover & Export)
# -----------------------------------------

fibonacci_threshold = 0.2
"""
0.10 oder größer:   grob-tolerant -> mehr Marker, mehr falsch-positive Treffer
0.05                mittlere SensitivitÃ¤t (dein aktueller Stand)
0.01 oder kleiner:  sehr sensibel -> nur sehr prÃ¤zise Fibonacci-Annäherungen zählen
"""

# Sichere Verhältnisberechnung
def safe_ratio(a, b):
    try:
        return a / b if b != 0 else np.nan
    except:
        return np.nan

# Daten glätten und konvertieren
mittelwerte_kompetenz_smooth = np.array(smooth_curve(mittelwerte_kompetenz), dtype=float)
bildungswirkfaktoren_smooth = np.array(bildungswirkfaktoren_smooth, dtype=float)

# Normierung der Radien auf [0, 10]
norm_radius_nu = np.interp(bildungswirkfaktoren_smooth, (min(bildungswirkfaktoren_smooth), max(bildungswirkfaktoren_smooth)), (0, 10))
norm_radius_k = np.interp(mittelwerte_kompetenz_smooth, (min(mittelwerte_kompetenz_smooth), max(mittelwerte_kompetenz_smooth)), (0, 10))

# Spiralwinkel
theta = np.linspace(0, 4 * np.pi, len(norm_radius_nu))

# ν-Spirale: Koordinaten, Farben, Hovertexte, Markersizes (proportional)
x_nu, y_nu, farben_nu, hovertext_nu, size_nu = [], [], [], [], []
for i in range(len(norm_radius_nu)):
    r = norm_radius_nu[i]
    x_nu.append(r * np.cos(theta[i]))
    y_nu.append(r * np.sin(theta[i]))
    if i == 0:
        farben_nu.append(colors["negativeHighlight"])
        hovertext_nu.append("Quartal 0<br>Startpunkt")
        size_nu.append(6)
    else:
        ratio = safe_ratio(norm_radius_nu[i], norm_radius_nu[i - 1])
        delta = abs(ratio - 1.618)
        is_close = delta < fibonacci_threshold
        farben_nu.append(colors["positiveHighlight"] if is_close else colors["negativeHighlight"])
        hovertext_nu.append(f"Quartal {i}<br>Ratio: {ratio:.3f}<br>Δφ: {delta:.3f}<br>{'✓ Fibonacci-nah' if is_close else '✗ Abweichung'}")
        size = 6 + 10 * np.exp(-delta * 50)  # exponentiell skalierte Knotengröße
        size_nu.append(size)

# Kompetenz-Spirale: Koordinaten, Farben, Hovertexte, Markersizes (proportional)
x_k, y_k, farben_k, hovertext_k, size_k = [], [], [], [], []
for i in range(len(norm_radius_k)):
    r = norm_radius_k[i]
    x_k.append(r * np.cos(theta[i]))
    y_k.append(r * np.sin(theta[i]))
    if i == 0:
        farben_k.append(colors["negativeHighlight"])
        hovertext_k.append("Quartal 0<br>Startpunkt")
        size_k.append(6)
    else:
        ratio = safe_ratio(norm_radius_k[i], norm_radius_k[i - 1])
        delta = abs(ratio - 1.618)
        is_close = delta < fibonacci_threshold
        farben_k.append(colors["positiveHighlight"] if is_close else colors["negativeHighlight"])
        hovertext_k.append(f"Quartal {i}<br>Ratio: {ratio:.3f}<br>Δφ: {delta:.3f}<br>{'✓ Fibonacci-nah' if is_close else '✗ Abweichung'}")
        size = 6 + 10 * np.exp(-delta * 50)  # exponentiell skalierte Knotengröße
        size_k.append(size)

# Plot initialisieren
fig_fibonacci = go.Figure()

# Fibonacci-Kreise + Annotation
phi = 1.618
kreise_r = [1, phi, phi**2, phi**3, phi**4]
for idx, r in enumerate(kreise_r):
    kreis_x = [r * np.cos(t) for t in np.linspace(0, 2 * np.pi, 300)]
    kreis_y = [r * np.sin(t) for t in np.linspace(0, 2 * np.pi, 300)]
    fig_fibonacci.add_trace(go.Scatter(
        x=kreis_x, y=kreis_y, mode='lines',
        line=dict(color='rgba(255, 255, 255, 0.05)', width=1, dash='dot'),
        hoverinfo='skip', showlegend=False
    ))
    fig_fibonacci.add_annotation(
        x=r + 0.2, y=-0.3,
        text=f"φ^{idx}" if idx > 0 else "1",
        showarrow=False,
        font=dict(color=colors["white"], size=10),
        xanchor="left", yanchor="middle"
    )

# Ursprung markieren
fig_fibonacci.add_trace(go.Scatter(
    x=[0], y=[0],
    mode='markers+text',
    marker=dict(color="black", size=12, symbol='x'),
    text=["Ursprung"],
    textposition="bottom center",
    hoverinfo="skip", showlegend=False
))

# ν-Spirale
fig_fibonacci.add_trace(go.Scatter(
    x=x_nu, y=y_nu,
    mode='lines+markers',
    marker=dict(color=farben_nu, size=10),
    line=dict(color=colors["secondaryLine"], width=2, shape="spline"),
    name="ν-Spirale (Bildungswirkfaktor)",
    text=hovertext_nu,
    hoverinfo="text"
))

# Kompetenz-Spirale
fig_fibonacci.add_trace(go.Scatter(
    x=x_k, y=y_k,
    mode='lines+markers',
    marker=dict(color=farben_k, size=10),
    line=ci_line("primary", shape="spline"),
    name="Kompetenz-Spirale",
    text=hovertext_k,
    hoverinfo="text"
))

# CI-konformes Layout über das zentrale Template
# Standardlayout abrufen und CI-Legende danach setzen, um Konflikte zu vermeiden
fibonacci_layout = plotly_template.get_standard_layout(
    title=f"Fibonacci Analyse mit {fibonacci_threshold} ({gewaehlter_ansatz} | {selected_archetyp})",
    x_title="x (normiert)",
    y_title="y (normiert)",
    x_range=[-10, 10],
    y_range=[-10, 10]
)
fibonacci_layout.pop("legend", None)

fig_fibonacci.update_layout(
    **fibonacci_layout,
    showlegend=True,
    legend=ci_legend()
)
# Statische Achsenbereiche beibehalten
fig_fibonacci.update_xaxes(range=[-10, 10])
fig_fibonacci.update_yaxes(range=[-10, 10])

safe_fig_show(fig_fibonacci)
export_figure(fig_fibonacci, "fibonacci-analyse", export_fig_spiral_combined, export_fig_png)

# -----------------------------------------
# Dashboard mit Subplotts
# -----------------------------------------

# Dashboard erstellen
fig_dashboard = make_subplots(
    rows=4, cols=2,
    subplot_titles=(
        "Eingabewerte & Simulationseinstellungen",
    "Dynamische Unsicherheitsrelation",
    f"TEI-Kompetenzprofil ({len(relative_schedule)} Handlungssituationen)",
        f"Kumulative Kompetenz: {flaeche_unter_mittelwert:.2f}",
        "Bildungswirkfaktor und Bildungswirkindikator",
        "Entwicklung von Neugier und Motivation",
        "Histogramm, Dichte und KDE",
        "Sankey-Diagramm"
    ),
    specs=[
        [{"type": "table"}, {"type": "domain"}],
        [{"type": "scatter"}, {"type": "scatter"}],
        [{"type": "scatter"}, {"type": "scatter"}],
        [{"type": "scatter"}, {"type": "domain"}]
    ],
    vertical_spacing=0.12,
    horizontal_spacing=0.1
)
fig_dashboard.update_layout(plot_bgcolor=colors["background"], paper_bgcolor=colors["background"], font=dict(color=colors["text"]))

# =========================================
# Eingabeparameter als Tabelle visualisieren
parameter_data = [
    ["Quartale", quartale],
    ["Handlungssituationen (TEI)", len(relative_schedule)],
    ["Initiale Neugier", initial_neugier],
    ["Startkompetenz", start_kompetenz],
    ["Theme", theme],
    ["Ansatz", f"{ansatz_wahl} ({gewaehlter_ansatz})"],
    ["Archetyp", selected_archetyp],
    ["Bereitschafts_Std", bereitschafts_std],
    *[(f"PE – {k}", f"{v:.2f}") for k, v in pe_auswirkungen.items()]
]

fig_parameter_tabelle = go.Figure(data=[
    go.Table(
        header=dict(
            values=["Eingabeparameter", "Wert"],
            fill_color=colors["brightArea"],
            font=dict(color=colors["text"])
        ),
        cells=dict(
            values=list(zip(*parameter_data)),
            fill_color=colors["background"],
            font=dict(color=colors["text"])
        )
    )
])

fig_parameter_tabelle.update_layout(
    title=f"Eingabewerte & Simulationseinstellungen ({gewaehlter_ansatz} | {selected_archetyp})",
    paper_bgcolor=colors["background"],
    plot_bgcolor=colors["background"],    font=dict(color=colors["text"])
)

# Visualisierungen dem Dashboard hinzufügen
visuals = [
    fig_parameter_tabelle,
    fig3,
    fig_mc,
    fig_kumulative_kompetenz,
    fig_bildungswirkgefuege,
    fig_neugier_motivation,
    fig_histogram,
    fig_flussdiagramm
]

for i, fig in enumerate(visuals, start=1):
    for trace in fig.data:
        fig_dashboard.add_trace(trace, row=(i - 1) // 2 + 1, col=(i - 1) % 2 + 1)

fig_dashboard.update_layout(
    title=f'Dashboard: Bildungswirkgefüge vom {formatted_time} ({gewaehlter_ansatz} | {selected_archetyp})',
    autosize=True,
    height=None,
    width=None,
    showlegend=False,
    legend_title_font=dict(color=colors['text']),
    legend=ci_legend(y=-0.15, yanchor='top'),
    title_font=dict(size=18),
    font=dict(size=12, color=colors['text']),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background']
)

# CI-konforme Achsenanpassung
for i in range(1, 9):
    fig_dashboard.update_xaxes(
        title_text="Zeit [Quartal]",
        linecolor=colors['text'],
        tickcolor=colors['text'],
        row=(i - 1) // 2 + 1,
        col=(i - 1) % 2 + 1
    )
    fig_dashboard.update_yaxes(
        title_text="Kompetenzniveau",
        linecolor=colors['text'],
        tickcolor=colors['text'],
        row=(i - 1) // 2 + 1,
        col=(i - 1) % 2 + 1
    )

safe_fig_show(fig_dashboard)
export_figure(fig_dashboard, "dashboard", export_fig_dashboard, export_fig_png)

# Ende der Visualisierungen
# =========================================

# Modellprüfung nach der Simulation, gesteuert über Config
from config_bildungswirkgefuege import modellpruefung_aktiv

if modellpruefung_aktiv:
    import os as _os
    # TEI-Kontext für die Modellprüfung setzen, damit der Report unter 08_* landet
    _os.environ.setdefault("BILDWIRK_CONTEXT", "TEI")
    try:
        _os.environ.setdefault("BILDWIRK_TEI_REPORT_DIR", str(TEI_EXPORT_ROOT))
    except Exception:
        pass
    import modellpruefung
    report_path, gpt_used = modellpruefung.fuehre_modellpruefung_durch()
    if gpt_used:
        print("✅ Modellprüfung nach Simulation inkl. GPT-Interpretation durchgeführt.")
    else:
        print("ℹ️ Modellprüfung nach Simulation ohne GPT-Interpretation abgeschlossen.")
    print(f"📄 Bericht gespeichert unter: {report_path}")
else:
    print("ℹ️ Modellprüfung ist deaktiviert (config).")
