# =========================================
# Import
# -----------------------------------------

import os
import sys
from pathlib import Path

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

# PNG-Exportordner (übersteuerbar via Umgebungsvariable `BILDWIRK_PNG_DIR`)
PNG_DIR_ENV = os.environ.get("BILDWIRK_PNG_DIR")
if PNG_DIR_ENV:
    PNG_EXPORT_DIR = Path(PNG_DIR_ENV)
else:
    # Default: Bilder nicht in den Report-Ordner schreiben, sondern ins Projektverzeichnis (user-agnostisch via HOME)
    PNG_EXPORT_DIR = (
        Path.home()
        / "Documents"
        / "Allgemein beruflich"
        / "Research"
        / "Forschungsprojekte"
        / "Systemische Kompetenzentwicklung für High Responsibility Teams"
    )
PNG_EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# HTML-Exportordner (übersteuerbar via Umgebungsvariable `BILDWIRK_HTML_DIR`)
HTML_DIR_ENV = os.environ.get("BILDWIRK_HTML_DIR")
if HTML_DIR_ENV:
    HTML_EXPORT_DIR = Path(HTML_DIR_ENV)
else:
    HTML_EXPORT_DIR = EXPORT_ROOT / "html"
HTML_EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# Optionales Remote-Ziel für `scp` (z. B. user@host:/path). Wenn nicht gesetzt, bleiben HTML lokal.
REMOTE_SCP_DEST = os.environ.get("BILDWIRK_REMOTE_SCP_DEST")

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
from scipy.integrate import solve_ivp
from scipy.stats import gaussian_kde, norm, pearsonr
from statsmodels.nonparametric.smoothers_lowess import lowess
from math import pi
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
    simulations_durchlaeufe,
    initial_neugier,
    start_kompetenz,
    export_fig_visual,
    export_fig_png,
    theme,
    ansatz_wahl,
    selected_archetyp,
)

# Logging-Konfiguration
log_dir = EXPORT_ROOT
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

# Strukturierte Konsolenausgabe der gewählten Parameter
"""Strukturierte Konsolenausgabe der gewählten Parameter erfolgt, sobald
die Archetypdaten (inkl. BPS) vorliegen, damit alles zusammenhängend
ausgegeben wird."""

from archetypen import archetypen, hole_archetyp, motivation_params_for, map_report_pe_to_internal

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

# Erweiterte Exportfunktion für Plotly-Figuren (HTML und PNG)
def export_figure(fig, name, export_flag_html, export_flag_png):
    filename_part = f"{gewaehlter_ansatz} {selected_archetyp}"
    safe_filename = slugify(f"{name}_{filename_part}")

    if export_flag_html:
        export_path_html = HTML_EXPORT_DIR / f"{safe_filename}.html"
        fig.write_html(str(export_path_html), full_html=True, include_plotlyjs="cdn")
        if REMOTE_SCP_DEST:
            try:
                subprocess.run(["scp", str(export_path_html), REMOTE_SCP_DEST], check=True)
                print(f"✅ HTML-Datei '{export_path_html}' erfolgreich übertragen.")
                try:
                    export_path_html.unlink(missing_ok=True)
                    print(f"🗑️ Lokale HTML-Datei '{export_path_html}' wurde gelöscht.")
                except OSError:
                    pass
            except subprocess.CalledProcessError as e:
                print("❌ Fehler beim HTML-Übertragen:")
                print(e.stderr)
        else:
            print(f"✅ HTML-Datei lokal gespeichert: '{export_path_html}'")

    if export_flag_png:
        export_path_png = PNG_EXPORT_DIR / f"{safe_filename}.png"
        try:
            fig.write_image(str(export_path_png), width=1200, height=800, scale=2)
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

archetyp_daten = hole_archetyp(selected_archetyp)

if archetyp_daten:
    # Rückgabe der Daten statt direkte Ausgabe im Terminal
    bereitschafts_std = archetyp_daten["Bereitschafts_Std"]
    pe_auswirkungen = archetyp_daten.get("PE", {})
    # Optional: Falls Berichts-Kategorien vorhanden sind, auf interne Treiber mappen
    if "PE_report" in archetyp_daten and isinstance(archetyp_daten["PE_report"], dict):
        mapped = map_report_pe_to_internal(archetyp_daten["PE_report"])
        # Mapped Werte mit vorhandenen PE zusammenführen (gemappt dominiert)
        pe_auswirkungen = {**pe_auswirkungen, **{k: float(v) for k, v in mapped.items()}}
    default_biosoziales_profil = {"bio": 0.5, "psy": 0.5, "soz": 0.5}
    biosoziales_profil = {**default_biosoziales_profil, **archetyp_daten.get("biosozial", {})}
    bio_startstatus = float(np.clip(biosoziales_profil["bio"], 0.0, 1.0))
    psy_startstatus = float(np.clip(biosoziales_profil["psy"], 0.0, 1.0))
    soz_startstatus = float(np.clip(biosoziales_profil["soz"], 0.0, 1.0))

    # Strukturierte Konsolenausgabe (zusammengeführt inkl. BPS)
    print("🧩 Simulation mit folgenden Parametern gestartet:")
    print(f"  📊 Quartale: {quartale}")
    print(f"  🔁 Simulationsdurchläufe: {simulations_durchlaeufe}")
    print(f"  🧠 Initiale Neugier: {initial_neugier}")
    print(f"  🎯 Startkompetenz: {start_kompetenz}")
    print(f"  🎨 Theme: {plotly_template.get_theme()}")
    print(f"  🧭 Ansatzwahl: {ansatz_wahl} ({ansatz_namen.get(ansatz_wahl, 'Unbekannt')})")
    print(f"  🧬 Gewählter Archetyp: {selected_archetyp}")
    print(
        "  🧱 BPS-Profil: "
        f"Bio {bio_startstatus:.2f} | Psy {psy_startstatus:.2f} | Soz {soz_startstatus:.2f}"
    )
    # Effektive Motivationsparameter aus Archetyp + PE ableiten
    _mot = motivation_params_for(selected_archetyp, pe_auswirkungen)
    alpha_c = _mot["alpha_c"]
    alpha_dm = _mot["alpha_dm"]
    alpha_dk = _mot["alpha_dk"]
    alpha_pe = _mot["alpha_pe"]
    alpha_n = _mot["alpha_n"]
    eta_motivation = _mot["eta_motivation"]
    C_opt = _mot["C_opt"]
    sigma_C = _mot["sigma_C"]

    # Die Werte könnten in einer Variablen behalten oder später für die Darstellung genutzt werden
else:
    msg = f"Konfiguration fehlerhaft: Archetyp '{selected_archetyp}' ist nicht definiert."
    logging.error(msg)
    raise ValueError(msg)

# -----------------------------------------
# Relativer Zeitplan in Tagen
# -----------------------------------------

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

# -----------------------------------------
# Aufgaben pro Handlungssituation (Gesamt 484)
# -----------------------------------------

task_counts = [
    6, 16, 28, 37, 31, 14, 47, 36, 11, 25, 12, 18, 15, 18, 24, 26,
    24, 36, 20, 28, 29, 15, 5, 6, 17, 19, 11, 22, 9, 61, 55, 13, 54, 60
]

# -----------------------------------------
# Berechnung der Lehr-Lern-Ansätze
# -----------------------------------------

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

# Phasenlogik: Anteil der Quartale für Anpassung / Verfestigung / Wachstum
# (orientiert an typischen Verläufen der jeweiligen Paradigmen)
ansatz_phasen_grenzen = {
    1: (0.20, 0.45, 0.70),  # Instruktional – frühe Steuerung, klare Konsolidierung
    2: (0.25, 0.55, 0.80),  # Kognitivistisch – längere Verfestigung/Schemaarbeit
    3: (0.15, 0.40, 0.65),  # Behavioristisch – schnelle Anpassung, frühe Automatisierung
    4: (0.30, 0.55, 0.85),  # Humanistisch – Selbstreflexion, spätes Wachstum
    5: (0.25, 0.50, 0.80),  # Konstruktivistisch – Exploration/iteratives Verfestigen
    6: (0.30, 0.60, 0.85),  # Soziokulturell – längere gemeinschaftliche Konsolidierung
    7: (0.35, 0.65, 0.90),  # Systemisch – spätes manifestes Wachstum
}

# Definiere den gewählten Ansatz basierend auf der Auswahl
try:
    gewaehlter_ansatz = ansatz_namen[ansatz_wahl]
except KeyError:
    msg = f"Konfiguration fehlerhaft: Ansatzwahl '{ansatz_wahl}' ist nicht definiert."
    logging.error(msg)
    raise ValueError(msg)

# Dämpfungsfaktor festlegen
daempfungs_faktor = 0.1  # 10% der ursprünglichen Bereitschaftssteigerung

# Definiere die Verteilung der Phasen basierend auf dem Paradigma
anpassung_anteil, verfestigung_anteil, wachstum_anteil = ansatz_phasen_grenzen.get(
    ansatz_wahl,
    (0.25, 0.50, 0.75)
)

# Simulation Setup
t_span = (0, simulations_durchlaeufe)
t_eval = np.linspace(t_span[0], t_span[1], 300)

# Berechnung basierend auf dem gewählten Ansatz

# ----------------------------------------------
# 1 Instruktionaler Ansatz mit Berücksichtigung von PE und Neugier
# ----------------------------------------------
if ansatz_wahl == 1:  # Instruktional
    def learning_rate(t, I, E, pe_mod, neugier):
        return E * I * (1 + 0.1 * pe_mod) * (1 + neugier)

    def dLdt(t, L, I, E, pe_auswirkungen, neugier):
        pe_mod = random.choice(list(pe_auswirkungen.values()))
        r = learning_rate(t, I, E, pe_mod, neugier)
        return r * (1 - L)

    args = (0.9, 0.8, pe_auswirkungen, initial_neugier)

# ----------------------------------------------
# 2 Kognitivistischer Ansatz mit persönlichen Ereignissen und Neugier
# ----------------------------------------------
elif ansatz_wahl == 2:  # Kognitivistisch
    def learning_rate(t, E, S, M_kognitiv, alpha, beta, gamma, pe_mod, neugier):
        return (alpha * E + beta * S + gamma * M_kognitiv) * (1 + pe_mod) * (1 + neugier)

    def dLdt(t, L, E, S, M_kognitiv, alpha, beta, gamma, pe_auswirkungen, neugier):
        pe_mod = random.choice(list(pe_auswirkungen.values()))
        r = learning_rate(t, E, S, M_kognitiv, alpha, beta, gamma, pe_mod, neugier)
        return r * (1 - L)

    args = (0.7, 0.6, 0.5, 0.4, 0.3, 0.3, pe_auswirkungen, initial_neugier)

# ----------------------------------------------
# 3 Behavioristischer Ansatz mit persönlichen Ereignissen
# ----------------------------------------------
elif ansatz_wahl == 3:  # Behavioristisch
    def learning_rate(t, B, R, C, S, pe_mod):
        S_mod = S * (1 + pe_mod)  # Verstärkungsstärke durch PE beeinflusst
        return S_mod * (C - B)

    def dLdt(t, L, B, R, C, S, pe_auswirkungen):
        pe_mod = random.choice(list(pe_auswirkungen.values()))
        r = learning_rate(t, B, R, C, S, pe_mod)
        return r * (1 - L)

    args = (0.3, 0.8, 1.0, 0.9, pe_auswirkungen)

# ----------------------------------------------
# 4 Humanistischer Ansatz mit persönlichen Ereignissen und Neugier
# ----------------------------------------------
elif ansatz_wahl == 4:  # Humanistisch
    def learning_rate(t, E, K, S, w_E, w_K, w_S, pe_auswirkungen, neugier):
        E += 0.1 * (pe_auswirkungen['PFE'] - pe_auswirkungen['PSE'])
        K += 0.1 * (pe_auswirkungen['PLE'] - pe_auswirkungen['PFV'])
        S += 0.1 * (pe_auswirkungen['PGV'] - pe_auswirkungen['PEE'])
        return (w_E * E + w_K * K + w_S * S) * (1 + neugier)

    def dLdt(t, L, E, K, S, w_E, w_K, w_S, pe_auswirkungen, neugier):
        r = learning_rate(t, E, K, S, w_E, w_K, w_S, pe_auswirkungen, neugier)
        return r * (1 - L)

    args = (0.7, 0.6, 0.5, 0.4, 0.3, 0.3, pe_auswirkungen, initial_neugier)

# ----------------------------------------------
# 5 Konstruktivistischer Ansatz mit persönlichen Ereignissen und Neugier
# ----------------------------------------------
elif ansatz_wahl == 5:  # Konstruktivistisch
    def learning_rate(t, E, I, R, alpha, beta, gamma, pe_mod, neugier):
        E = E * (1 + pe_mod)
        I = I * (1 + pe_mod)
        R = R * (1 + pe_mod)
        return (alpha * E + beta * I + gamma * R) * (1 + neugier)

    def dLdt(t, L, E, I, R, alpha, beta, gamma, pe_auswirkungen, neugier):
        pe_mod = random.choice(list(pe_auswirkungen.values()))
        r = learning_rate(t, E, I, R, alpha, beta, gamma, pe_mod, neugier)
        return r * (1 - L)

    args = (0.8, 0.7, 0.6, 0.5, 0.3, 0.2, pe_auswirkungen, initial_neugier)

# ----------------------------------------------
# 6 Soziokultureller Ansatz mit persönlichen Ereignissen und Neugier
# ----------------------------------------------
elif ansatz_wahl == 6:  # Soziokulturell
    def learning_rate(t, S, ZPD, C, alpha, pe_mod, neugier):
        S = S * (1 + pe_mod)
        C = C * (1 + pe_mod)
        ZPD_max = 1.0
        return alpha * S * (ZPD / ZPD_max) * (1 + C) * (1 + neugier)

    def dLdt(t, L, S, ZPD, C, alpha, pe_auswirkungen, neugier):
        pe_mod = random.choice(list(pe_auswirkungen.values()))
        r = learning_rate(t, S, ZPD, C, alpha, pe_mod, neugier)
        return r * (1 - L)

    args = (0.8, 0.7, 0.6, 0.05, pe_auswirkungen, initial_neugier)

# ----------------------------------------------
# 7 Systemischer Ansatz mit persönlichen Ereignissen und Neugier
# ----------------------------------------------
elif ansatz_wahl == 7:  # Systemisch
    def learning_rate(t, C, M, k, pe_mod, neugier):
        """Berechnet die Lernrate unter Berücksichtigung systemischer Dynamiken."""
        C = C * (1 + pe_mod)  # PE-Einfluss auf kognitive Unsicherheit
        M = M * (1 + pe_mod)  # PE-Einfluss auf Motivation
        dynamischer_faktor = np.sin(t / 10) + np.cos(t / 20)  # Langfristige Schwankungen
        return k * C * M * dynamischer_faktor * (1 + neugier)

    def dLdt(t, L, C, M, k, pe_auswirkungen, neugier):
        """Differentialgleichung zur Simulation der Kompetenzentwicklung."""
        pe_mod = random.choice(list(pe_auswirkungen.values()))  # Zufällige PE-Auswirkung
        r = learning_rate(t, C, M, k, pe_mod, neugier)
        return r * (1 - L)  # Systemische Selbstbegrenzung der Kompetenzentwicklung

    # Initiale Parameter: C = Kognitive Unsicherheit, M = Motivation, k = Skalierungsfaktor
    args = (0.8, initial_neugier, 0.1, pe_auswirkungen, initial_neugier)

# ==========================================================
# Simulation starten und Berechnungen durchführen
# ==========================================================
sol = solve_ivp(dLdt, t_span, [start_kompetenz], args=args, t_eval=t_eval, method='RK45')

# Phasenaufteilung und Berechnungen
n = len(sol.y[0])
phasen_anteile = [int(n * anpassung_anteil), int(n * verfestigung_anteil), int(n * wachstum_anteil), n]

bereitschafts_steigerung_phase = {
    'Anpassung': daempfungs_faktor * sol.y[0][:phasen_anteile[0]].mean(),
    'Verfestigung': daempfungs_faktor * sol.y[0][phasen_anteile[0]:phasen_anteile[1]].mean(),
    'Wachstum': daempfungs_faktor * sol.y[0][phasen_anteile[1]:phasen_anteile[2]].mean(),
    'Plateau': daempfungs_faktor * sol.y[0][phasen_anteile[2]:phasen_anteile[3]].mean()
}

# ==============================================

# C ist jetzt der dynamische Unsicherheitswert
def _calculate_dynamic_C_core(delta_k_entw, delta_k_mess):
    r, _ = pearsonr(delta_k_entw, delta_k_mess)
    if np.std(delta_k_entw) == 0 or np.std(delta_k_mess) == 0:
        logging.warning(
            "Pearson-Korrelation nicht berechenbar (Varianz=0). "
            "delta_k_entw=%s, delta_k_mess=%s",
            delta_k_entw,
            delta_k_mess
        )
        return np.nan
    return abs(r) * (np.std(delta_k_entw) * np.std(delta_k_mess))


def calculate_dynamic_C(
    delta_k_entw=None,
    delta_k_mess=None,
    *,
    delta_e=None,
    delta_k=None
):
    """
    Berechnet den dynamischen Kopplungswert C zwischen Entwicklungs- und Messunsicherheit.

    Frühere Aufrufe mit delta_e / delta_k werden weiterhin akzeptiert, lösen jedoch
    eine Deprecation-Warnung aus.
    """
    if delta_k_entw is None and delta_e is not None:
        warnings.warn(
            "Parameter 'delta_e' ist veraltet. Verwende 'delta_k_entw'.",
            DeprecationWarning,
            stacklevel=2
        )
        delta_k_entw = delta_e
    if delta_k_mess is None and delta_k is not None:
        warnings.warn(
            "Parameter 'delta_k' ist veraltet. Verwende 'delta_k_mess'.",
            DeprecationWarning,
            stacklevel=2
        )
        delta_k_mess = delta_k

    if delta_k_entw is None or delta_k_mess is None:
        raise ValueError("Es müssen sowohl 'delta_k_entw' als auch 'delta_k_mess' übergeben werden.")

    delta_k_entw = np.asarray(delta_k_entw)
    delta_k_mess = np.asarray(delta_k_mess)
    return _calculate_dynamic_C_core(delta_k_entw, delta_k_mess)

# Funktion zur Fluktuation eines Parameters innerhalb eines bestimmten Bereichs
def fluctuate_parameter(param, fluctuation_range=0.01):
    return param * (1 + np.random.normal(0, fluctuation_range))

# Anpassung der Bereitschaftssteigerung für jede Phase
for key in bereitschafts_steigerung_phase.keys():
    bereitschafts_steigerung_phase[key] = fluctuate_parameter(bereitschafts_steigerung_phase[key])

# Anpassung der PE-Auswirkungen
for key in pe_auswirkungen.keys():
    pe_auswirkungen[key] = fluctuate_parameter(pe_auswirkungen[key])

# Definition verschiedener Verteilungsfunktionen
def weibull_distribution(scale, shape, size):
    return np.random.weibull(shape, size) * scale

def normal_distribution(mean, std, size):
    return np.random.normal(mean, std, size)

def beta_distribution(alpha, beta, size):
    return np.random.beta(alpha, beta, size)

def poisson_distribution(lam, size):
    return np.random.poisson(lam, size)

# Berechnung der Kompetenzentwicklung mit der Weibull-Verteilung
def weibull_kompetenzentwicklung(scale, shape, current_level):
    improvement = np.random.weibull(shape) * scale
    new_competence_level = current_level + improvement
    return new_competence_level

# Überprüfung auf unerwartete Ereignisse
def check_for_unexpected_events(lam):
    return np.random.poisson(lam)

# Aktualisierung der Motivation mit Fluktuation
def update_motivation(current_motivation):
    fluctuation = np.random.normal(0, 0.1)
    new_motivation = max(0, min(10, current_motivation + fluctuation))
    return new_motivation

# Definition eines persönlichen Ereignisses und dessen Auswirkungen
def persoenliches_ereignis(pe_profil=None):
    kategorien = ['PFE', 'PLE', 'PFV', 'PGV', 'PSE', 'PEE']
    if pe_profil:
        rohw = np.array([abs(float(pe_profil.get(k, 0.0))) for k in kategorien], dtype=float)
        if np.allclose(rohw.sum(), 0.0):
            probs = np.full(len(kategorien), 1 / len(kategorien))
        else:
            probs = rohw / rohw.sum()
    else:
        probs = np.array([0.125, 0.0833, 0.2083, 0.125, 0.4167, 0.0417], dtype=float)
    ereignis_typ = np.random.choice(kategorien, p=probs)
    impacts = {
        'PFE': np.random.normal(-0.2, 0.1),
        'PLE': np.random.normal(-0.3, 0.2),
        'PFV': np.random.normal(0.2, 0.1),
        'PGV': np.random.normal(-0.4, 0.2),
        'PSE': np.random.normal(0.1, 0.05),
        'PEE': np.random.normal(0.3, 0.1)
    }
    basis = impacts[ereignis_typ]
    gewicht = float(pe_profil.get(ereignis_typ, 0.0)) if pe_profil else 0.0
    skala = 1.0 + abs(gewicht)
    return ereignis_typ, basis * skala

# Klasse zur Darstellung eines Lernenden mit verschiedenen Attributen
class Lernender:
    def __init__(
        self,
        motivation,
        vorwissen,
        emotionales_wohlbefinden,
        soziale_interaktion,
        kognitive_faehigkeiten,
        biosozial=None
    ):
        self.motivation = motivation
        self.vorwissen = vorwissen
        self.emotionales_wohlbefinden = emotionales_wohlbefinden
        self.soziale_interaktion = soziale_interaktion
        self.kognitive_faehigkeiten = kognitive_faehigkeiten
        default_bps = {"bio": 0.5, "psy": 0.5, "soz": 0.5}
        profile = {**default_bps, **(biosozial or {})}
        self.biologischer_status = float(np.clip(profile["bio"], 0.0, 1.0))
        self.psychologischer_status = float(np.clip(profile["psy"], 0.0, 1.0))
        self.sozialer_status = float(np.clip(profile["soz"], 0.0, 1.0))

    def update_motivation(self, delta):
        self.motivation = max(0, min(10, self.motivation + delta))

    def update_curiosity(self, delta):
        self.vorwissen = max(0, min(10, self.vorwissen + delta))

    def update_bps(self, pe_wirkung, delta_k=0.0, delta_m=0.0):
        """
        Aktualisiert die biopsychosozialen Statuswerte basierend auf PE-Einflüssen
        und aktuellen Entwicklungs-/Motivationsschwankungen.
        """
        pe_effect = float(np.clip(pe_wirkung, -1.0, 1.0))
        stress = float(np.clip(abs(delta_k) + abs(delta_m), 0.0, 2.0))
        self.biologischer_status = float(
            np.clip(self.biologischer_status + 0.03 * pe_effect - 0.02 * stress, 0.0, 1.0)
        )
        self.psychologischer_status = float(
            np.clip(self.psychologischer_status + 0.05 * pe_effect - 0.01 * abs(delta_m), 0.0, 1.0)
        )
        self.sozialer_status = float(
            np.clip(self.sozialer_status + 0.04 * pe_effect, 0.0, 1.0)
        )

    def get_bps_profile(self):
        return {
            "bio": self.biologischer_status,
            "psy": self.psychologischer_status,
            "soz": self.sozialer_status
        }

# Simulation der Motivation und Neugier eines Lernenden über mehrere Monate und Durchläufe
def simulate_motivation_neugier_modified(lernender, monate, durchlaeufe, pe_matrix):
    """
    Simulation der Motivation und Neugier eines Lernenden über mehrere Quartale und Durchläufe.
    Neugier und Motivation werden durch PE-Ereignisse sowie biopsychosoziale Statuswerte moduliert.
    """
    np.random.seed(42)
    alle_neugier_verlaeufe = []
    alle_motivations_verlaeufe = []
    alle_messunsicherheit_verlaeufe = []
    alle_mikro_m_verlaeufe = []
    alle_bio_verlaeufe = []
    alle_psy_verlaeufe = []
    alle_soz_verlaeufe = []

    startzustand = {
        "motivation": lernender.motivation,
        "vorwissen": lernender.vorwissen,
        "emotionales_wohlbefinden": lernender.emotionales_wohlbefinden,
        "soziale_interaktion": lernender.soziale_interaktion,
        "kognitive_faehigkeiten": lernender.kognitive_faehigkeiten,
        "bps": lernender.get_bps_profile()
    }

    for i in range(durchlaeufe):
        pe_verlauf = pe_matrix[:, i]
        lernender.motivation = startzustand["motivation"]
        lernender.vorwissen = startzustand["vorwissen"]
        lernender.emotionales_wohlbefinden = startzustand["emotionales_wohlbefinden"]
        lernender.soziale_interaktion = startzustand["soziale_interaktion"]
        lernender.kognitive_faehigkeiten = startzustand["kognitive_faehigkeiten"]
        lernender.biologischer_status = startzustand["bps"]["bio"]
        lernender.psychologischer_status = startzustand["bps"]["psy"]
        lernender.sozialer_status = startzustand["bps"]["soz"]
        c = lernender.vorwissen
        motivation = lernender.motivation
        c_history = [c]
        m_history = [motivation]
        mess_unsicherheit_history = []
        mikro_m_history = []
        bio_history = [lernender.biologischer_status]
        psy_history = [lernender.psychologischer_status]
        soz_history = [lernender.sozialer_status]

        # Historie für adaptive Schätzung von C_opt/sigma_C
        C_dyn_hist = []

        for t in range(monate):
            # Ersetze PE-Wirkung durch Verlauf aus pe_verlauf
            pe_wirkung = pe_verlauf[t] if t < len(pe_verlauf) else 0
            _, pe_mikro = persoenliches_ereignis(pe_auswirkungen)
            pe_wirkung = 0.5 * pe_wirkung + 0.5 * pe_mikro
            # Einflussgrößen aus dem Systemverlauf ableiten
            delta_m_micro = 0 if len(m_history) < 2 else m_history[-1] - m_history[-2]
            delta_k_entw = 0 if len(c_history) < 2 else c_history[-1] - c_history[-2]
            if len(c_history) >= 3:
                prev_window = c_history[-3:-1]
            elif len(c_history) >= 2:
                prev_window = c_history[:-1]
            else:
                prev_window = []
            if prev_window:
                k_hat = float(np.mean(prev_window))
                delta_k_mess_local = abs(c_history[-1] - k_hat)
            else:
                delta_k_mess_local = 0.0

            lernender.update_bps(pe_wirkung, delta_k_entw, delta_m_micro)
            bio_factor = 0.5 + lernender.biologischer_status
            psy_factor = 0.5 + lernender.psychologischer_status
            soz_factor = 0.5 + lernender.sozialer_status

            # Neugier- und Motivationsdynamik theoriegeleitet
            motivation = lernender.motivation
            c = lernender.vorwissen  # Vorwissen/Neugierlevel (0..10)

            # Dynamische Unsicherheit C_dyn (lokal) für Curiosity gemäß Optimalbereich
            C_dyn = 0.0
            if abs(delta_k_entw) > 0 and abs(delta_k_mess_local) > 0:
                C_dyn = calculate_dynamic_C(
                    [delta_k_entw, delta_k_entw + 1e-4],
                    [delta_k_mess_local, delta_k_mess_local + 1e-4]
                )
            C_dyn_hist.append(float(C_dyn))
            # Adaptive Schätzung von C_opt/sigma_C, falls nicht in Config gesetzt
            if C_opt is None:
                C_opt_eff = (np.nanmedian(C_dyn_hist[-5:])
                             if len(C_dyn_hist) >= 3 else float(C_dyn))
            else:
                C_opt_eff = float(C_opt)
            if sigma_C is None:
                sigma_eff = np.nanstd(C_dyn_hist[-5:]) if len(C_dyn_hist) >= 3 else abs(float(C_dyn))
                sigma_eff = float(sigma_eff) if sigma_eff and sigma_eff > 1e-6 else 1.0
            else:
                sigma_eff = float(sigma_C) if sigma_C > 1e-6 else 1.0

            curiosity_gain = np.exp(-((float(C_dyn) - C_opt_eff) / sigma_eff) ** 2)

            # Neugier (c) aktualisieren – abhängig von Entwicklungs-/Mikro-Dynamik
            delta_c = (0.5 * delta_k_entw + 0.5 * delta_m_micro) * soz_factor
            if delta_k_entw * delta_k_mess_local >= C_dyn:
                delta_c += 0.1 * psy_factor
            delta_c += 0.05 * (psy_factor - 1.0)
            lernender.update_curiosity(delta_c)
            c = lernender.vorwissen

            # Beiträge als normierte Funktionen
            f_c = np.sqrt(max(c, 0.0) / 10.0)
            f_dm = np.tanh(delta_m_micro)
            f_dk = np.tanh(delta_k_entw)
            pe_moduliert = pe_wirkung * soz_factor
            f_pe = np.tanh(pe_moduliert)

            deltaM = (
                alpha_c * f_c +
                alpha_dm * f_dm +
                alpha_dk * f_dk +
                alpha_pe * f_pe +
                alpha_n * curiosity_gain
            )
            # Logistische Begrenzung auf Skala 0..10
            delta_motivation = float(eta_motivation * deltaM * motivation * (1.0 - motivation / 10.0))

            lernender.update_motivation(delta_motivation)
            c_history.append(lernender.vorwissen)
            m_history.append(lernender.motivation)
            mess_unsicherheit_history.append(delta_k_mess_local)
            mikro_m_history.append(delta_m_micro)
            bio_history.append(lernender.biologischer_status)
            psy_history.append(lernender.psychologischer_status)
            soz_history.append(lernender.sozialer_status)

        alle_neugier_verlaeufe.append(c_history)
        alle_motivations_verlaeufe.append(m_history)
        alle_messunsicherheit_verlaeufe.append(mess_unsicherheit_history)
        alle_mikro_m_verlaeufe.append(mikro_m_history)
        alle_bio_verlaeufe.append(bio_history)
        alle_psy_verlaeufe.append(psy_history)
        alle_soz_verlaeufe.append(soz_history)

    return (
        alle_neugier_verlaeufe,
        alle_motivations_verlaeufe,
        alle_messunsicherheit_verlaeufe,
        alle_mikro_m_verlaeufe,
        alle_bio_verlaeufe,
        alle_psy_verlaeufe,
        alle_soz_verlaeufe
    )

# Anpassung der Bereitschaft je nach Phase
def anpassung_der_bereitschaft(aktuelles_quartal):
    phase = bereitschafts_steigerung_phase
    if aktuelles_quartal <= 4:
        return fluctuate_parameter(phase['Anpassung'])
    elif 5 <= aktuelles_quartal <= 6:
        return fluctuate_parameter(phase['Verfestigung'])
    elif 7 <= aktuelles_quartal <= 10:
        return fluctuate_parameter(phase['Wachstum'])
    else:
        return fluctuate_parameter(phase['Plateau'])

# Berechnung der Motivation je nach Quartal, inkl. PE-Einflüsse
def motivation(aktuelles_quartal, pe_auswirkungen):
    # Basis-Motivation durch Quartalsschocks
    if aktuelles_quartal == 8:
        basis = -0.3
    elif aktuelles_quartal == 12:
        basis = 0.4
    else:
        basis = 0

    # PE-Effekte dynamisch einbeziehen
    pe_wert = gesamtauswirkung_pe(pe_auswirkungen)

    # Gesamtmotivation = Basis + Anteil PE + Fluktuation
    return fluctuate_parameter(basis + 0.2 * pe_wert)

# Berechnung der Neugier je nach Quartal und Startkompetenz
def neugier(aktuelles_quartal, start_kompetenz):
    if aktuelles_quartal <= 6:
        return fluctuate_parameter(initial_neugier * 0.1)
    return fluctuate_parameter(-initial_neugier * 0.1)

# Berechnung der gesamten PE-Auswirkungen
# Negative Ereignisse (PFE, PLE) wirken subtraktiv, positive (PFV, PGV, PSE, PEE) additiv
def gesamtauswirkung_pe(pe_auswirkungen):
    # Zufallsfaktoren pro Schlüssel
    zufallsfaktoren = {k: np.random.uniform(0.8, 1.2) for k in pe_auswirkungen}

    # Negative Effekte: PFE, PLE
    negativ = (
        pe_auswirkungen.get('PFE', 0) * zufallsfaktoren.get('PFE', 1) +
        pe_auswirkungen.get('PLE', 0) * zufallsfaktoren.get('PLE', 1)
    )
    # Positive Effekte: PFV, PGV, PSE, PEE
    positiv = (
        pe_auswirkungen.get('PFV', 0) * zufallsfaktoren.get('PFV', 1) +
        pe_auswirkungen.get('PGV', 0) * zufallsfaktoren.get('PGV', 1) +
        pe_auswirkungen.get('PSE', 0) * zufallsfaktoren.get('PSE', 1) +
        pe_auswirkungen.get('PEE', 0) * zufallsfaktoren.get('PEE', 1)
    )
    # Ergebnis: Positive minus Negative
    return positiv - negativ

# Extreme finden
def identify_extrema_and_inflection_points(data):
    maxima, _ = find_peaks(data)
    minima, _ = find_peaks(-data)
    derivative = np.gradient(data)
    inflection_points, _ = find_peaks(np.abs(np.gradient(derivative)))
    return maxima, minima, inflection_points


# Hilfsfunktion zur Summation von Listen von Listen
def flatten_and_sum(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return sum(flat_list)

# Konsolidierte Glättungsfunktion für Kurven
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
    data = np.asarray(data)

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

# =========================================
# Zeit & Indexvorbereitung
# -----------------------------------------

# Aktuelles Datum und Uhrzeit erhalten
current_time = datetime.datetime.now()

# Formatieren des Datums und der Uhrzeit für den Titel
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Spaltennamen für DataFrames
quartale_columns = [f'Quartal_{i}' for i in range(0, quartale + 1)]
durchlauf_columns = [f'Durchlauf_{i}' for i in range(simulations_durchlaeufe)]

# Für Standardabweichungen bei Einzel-Durchläufen ddof=0 verwenden, sonst klassisch ddof=1
std_ddof = 1 if simulations_durchlaeufe > 1 else 0

# =========================================
# Initialisierung der Simulation
# -----------------------------------------

# Initialisierung der DataFrames zur Speicherung der Simulationsergebnisse und Bereitschaftssteigerungen
simulations_ergebnisse_pe = pd.DataFrame(index=range(0, quartale + 1), columns=durchlauf_columns)
bereitschaftssteigerungen = pd.DataFrame(index=range(0, simulations_durchlaeufe + 1), columns=quartale_columns)
kompetenzniveaus_df = pd.DataFrame(index=range(0, quartale + 1), columns=[f'Durchlauf_{i}' for i in range(simulations_durchlaeufe)])
neugier_entwicklung_df = pd.DataFrame(index=range(0, quartale + 1), columns=[f'Durchlauf_{i}' for i in range(simulations_durchlaeufe)])

# Initialisierung der Liste für die Aufzeichnung von PE-Auswirkungen
pe_auswirkungen_list = []

# =========================================
# Durchführung der Simulation
# -----------------------------------------


# Hilfsfunktion zur Berechnung der initialen Motivation (gewichtete Summe von Kompetenz, Neugier und PE)
def berechne_initiale_motivation(kompetenz, neugier, pe):
    return 0.4 * kompetenz + 0.4 * neugier + 0.2 * pe

# Simulation der Kompetenzentwicklung für jeden Durchlauf
for durchlauf in range(simulations_durchlaeufe):
    kompetenzentwicklung = np.full(quartale + 1, start_kompetenz)
    neugierentwicklung = np.full(quartale + 1, initial_neugier)
    pe_auswirkungen_temp = []

    # Beginn der Schleife bei Quartal 0
    for quartal in range(0, quartale + 1):
        if quartal == 0:
            # Quartal 0 ist der Startpunkt, daher keine Veränderungen
            kompetenzniveaus_df.at[quartal, f'Durchlauf_{durchlauf}'] = start_kompetenz
            neugier_entwicklung_df.at[quartal, f'Durchlauf_{durchlauf}'] = initial_neugier
            simulations_ergebnisse_pe.at[quartal, f'Durchlauf_{durchlauf}'] = start_kompetenz
            pe_auswirkungen_temp.append(0)  # Keine PE-Auswirkungen im Startquartal
            # Initiale Motivation berechnen (deterministisch)
            archetyp_pe = np.mean(list(pe_auswirkungen.values()))
            initial_motivation = berechne_initiale_motivation(start_kompetenz, initial_neugier, archetyp_pe)
            # Initiale Bereitschaft berechnen: Phase + Motivation + Zufall
            initial_bereitschaft = np.random.normal(
                anpassung_der_bereitschaft(0) + initial_motivation,
                bereitschafts_std
            )
            bereitschaftssteigerungen.at[durchlauf, f'Quartal_{quartal}'] = initial_bereitschaft
        else:
            # Berechnung der Steigerung der Bereitschaft, Motivation und Neugier sowie der gesamten PE-Auswirkungen
            steigerung = anpassung_der_bereitschaft(quartal)
            motivation_wert = motivation(quartal, pe_auswirkungen)
            neugier_wert = neugier(quartal, start_kompetenz)
            aggregierte_pe = gesamtauswirkung_pe(pe_auswirkungen)
            ereignis_typ, pe_mikro = persoenliches_ereignis(pe_auswirkungen)
            pe_auswirkung = 0.5 * aggregierte_pe + 0.5 * pe_mikro

            # Berechnung der neuen Bereitschaft und Anpassung der Kompetenzentwicklung
            bereitschaft = np.random.normal(steigerung + motivation_wert + neugier_wert + pe_auswirkung, bereitschafts_std)
            neue_kompetenz = np.clip(kompetenzentwicklung[quartal - 1] + bereitschaft, 1, 10)
            neue_neugier = max(0, min(10, neugierentwicklung[quartal - 1] + np.random.normal(0, 0.1)))

            # Speichern der neuen Werte
            kompetenzentwicklung[quartal] = neue_kompetenz
            neugierentwicklung[quartal] = neue_neugier
            kompetenzniveaus_df.at[quartal, f'Durchlauf_{durchlauf}'] = neue_kompetenz
            neugier_entwicklung_df.at[quartal, f'Durchlauf_{durchlauf}'] = neue_neugier
            bereitschaftssteigerungen.at[durchlauf, f'Quartal_{quartal}'] = bereitschaft
            pe_auswirkungen_temp.append(pe_auswirkung)

    pe_auswirkungen_list.append(pe_auswirkungen_temp)
    simulations_ergebnisse_pe.iloc[:, durchlauf] = kompetenzentwicklung

# =========================================
# Post-Processing & Ableitungen
# -----------------------------------------

# Sicherstellen, dass alle Kompetenzniveaus auf maximal 10 beschränkt sind
simulations_ergebnisse_pe_clipped = simulations_ergebnisse_pe.clip(upper=10)

# Index zurücksetzen, falls der Startindex nicht 0 ist
if simulations_ergebnisse_pe_clipped.index[0] > 0:
    simulations_ergebnisse_pe_clipped.reset_index(drop=True, inplace=True)

# Wenn Quartal 0 inbegriffen ist, passen Sie die Spaltenberechnung entsprechend an
pe_auswirkungen_df = pd.DataFrame(pe_auswirkungen_list, columns=range(0, quartale + 1)).T

# Konvertierung der Datentypen falls notwendig
bereitschaftssteigerungen = bereitschaftssteigerungen.infer_objects(copy=False)
pe_auswirkungen_df = pe_auswirkungen_df.infer_objects(copy=False)

# Berechnung der Mittelwerte für Bereitschaft und PE-Auswirkungen
mittelwerte_bereitschaft = bereitschaftssteigerungen.mean(axis=0)
mittelwerte_pe = pe_auswirkungen_df.mean(axis=1)

# Berechnung der Median- und Mittelwerte sowie der Standardabweichung für die beschränkten Kompetenzwerte
mediane_kompetenz = simulations_ergebnisse_pe_clipped.median(axis=1)
mittelwerte_kompetenz = simulations_ergebnisse_pe_clipped.mean(axis=1)
stddev_kompetenz = simulations_ergebnisse_pe_clipped.std(axis=1, ddof=std_ddof).clip(upper=10)

# Berechnung der Unsicherheitsprodukte
delta_bereitschaft = bereitschafts_std

# Berechnung der PE-Wirkungen für alle Durchläufe
pe_wirkungen = [gesamtauswirkung_pe(pe_auswirkungen) for _ in range(simulations_durchlaeufe)]

# Simulation der Änderungen von Neugier und Motivation
(
    veranderungen_neugier,
    veranderungen_motivation,
    messunsicherheiten_lauf,
    mikro_motivation_lauf,
    bio_status_lauf,
    psy_status_lauf,
    soz_status_lauf
) = simulate_motivation_neugier_modified(
    Lernender(
        initial_neugier,
        start_kompetenz,
        0,
        0,
        0,
        biosozial=biosoziales_profil
    ),
    quartale,
    simulations_durchlaeufe,
    pe_auswirkungen_df.to_numpy()
)

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
bio_status_mean = round(float(np.nanmean(mittelwerte_bio_status)), 3)
psy_status_mean = round(float(np.nanmean(mittelwerte_psy_status)), 3)
soz_status_mean = round(float(np.nanmean(mittelwerte_soz_status)), 3)
logging.info(
    "BPS mean status: bio=%s, psy=%s, soz=%s",
    bio_status_mean,
    psy_status_mean,
    soz_status_mean
)

# Berechnung der Bereitschaft für jedes Quartal
bereitschaft = [anpassung_der_bereitschaft(quartal) for quartal in range(1, quartale + 1)]

# Umwandlung der Kompetenzentwicklung in eine Liste
kompetenzentwicklung = simulations_ergebnisse_pe.mean(axis=1).tolist()

# Berechnung von ΔK_mess (Messunsicherheit) und ΔK_entw (Entwicklungsunsicherheit)
delta_k_mess = simulations_ergebnisse_pe.std(axis=1, ddof=std_ddof).tolist()
delta_k_entw = (
    simulations_ergebnisse_pe.mean(axis=1)
    - simulations_ergebnisse_pe.mean(axis=1).shift(1).fillna(0)
).infer_objects().tolist()

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
# Systemindikatoren & Dynamik
# -----------------------------------------

# Berechnung des Bildungswirkfaktors und relevanter Werte
bildungswirkfaktoren = delta_bereitschaft * simulations_ergebnisse_pe.std(axis=1, ddof=std_ddof)

# Logging für dynamic_C (vor Berechnung)
# Stelle sicher, dass dynamic_C definiert ist, bevor darauf zugegriffen wird
if 'dynamic_C' in locals():
    c_values = np.array(delta_k_entw) * np.array(delta_k_mess)
    dynamic_C = gamma(c_values)
    logging.info("dynamic_C (init) range: min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))
else:
    c_values = np.array(delta_k_entw) * np.array(delta_k_mess)
    dynamic_C = gamma(c_values)
    logging.info("dynamic_C (init) range: min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))

# Glättung der Bildungswirkfaktoren
bildungswirkfaktoren_smooth = smooth_curve(bildungswirkfaktoren, clip_max=10)

# Berechnung der ersten Ableitung der geglätteten Bildungswirkfaktoren
steigungen_bildungswirkfaktor = np.gradient(bildungswirkfaktoren_smooth)

# Glättung der Steigungen
steigungen_bildungswirkfaktor_smooth = smooth_curve(steigungen_bildungswirkfaktor, clip_max=10)

# Berechnung des Integrals des Bildungswirkfaktors
integral_bildungswirkfaktor = np.trapezoid(bildungswirkfaktoren, dx=1)

# Berechnung der Wendepunkte, Minima und Maxima für den Bildungswirkindikator (ι)
erste_ableitung_bildungswirkfaktor = steigungen_bildungswirkfaktor_smooth
zweite_ableitung_bildungswirkfaktor = np.gradient(steigungen_bildungswirkfaktor_smooth)

wendepunkte_bildungswirkfaktor = np.where(np.diff(np.sign(zweite_ableitung_bildungswirkfaktor)))[0]
maxima_bildungswirkfaktor, _ = find_peaks(bildungswirkfaktoren_smooth)
minima_bildungswirkfaktor, _ = find_peaks(-bildungswirkfaktoren_smooth)

# Berechnung des Bildungswirkindikators als die Ableitung des Bildungswirkfaktors
bildungswirkindikator = np.gradient(bildungswirkfaktoren)
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
flaeche_unter_mittelwert = np.trapezoid(smooth_curve(mittelwerte, clip_max=10), dx=1)
quartale_range = np.arange(0, quartale + 1)

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

if simulations_durchlaeufe > 1:
    korrelations_matrix_bereitschaft = np.corrcoef(bereitschafts_matrix.T)
    korrelations_matrix_pe = np.corrcoef(pe_matrix.T)
else:
    korrelations_matrix_bereitschaft = np.array([[1.0]])
    korrelations_matrix_pe = np.array([[1.0]])

# Berechnung der minimalen und maximalen Werte für die Farbskala
zmin_bereitschaft = np.nanmin(korrelations_matrix_bereitschaft)
zmax_bereitschaft = np.nanmax(korrelations_matrix_bereitschaft)
zmin_pe = np.nanmin(korrelations_matrix_pe)
zmax_pe = np.nanmax(korrelations_matrix_pe)

# Berechnung der Korrelationskoeffizienten für jeden Durchlauf (Placeholder für Visualisierung)
if simulations_durchlaeufe > 1:
    korrelationskoeffizienten_durchlaeufe = [
        pearsonr(np.random.randn(100), np.random.randn(100))[0] for _ in range(simulations_durchlaeufe)
    ]
else:
    korrelationskoeffizienten_durchlaeufe = [np.nan]

# Daten für das Streudiagramm
durchlauf_df = pd.DataFrame({
    'Durchlauf': range(1, simulations_durchlaeufe + 1),
    'Korrelationskoeffizient': korrelationskoeffizienten_durchlaeufe
})

# Berechnung der Korrelationskoeffizienten für ΔK_entw und ΔK_mess
if np.std(delta_k_entw) == 0 or np.std(delta_k_mess) == 0:
    basis_korrelation = np.nan
else:
    basis_korrelation = pearsonr(delta_k_entw, delta_k_mess)[0]
korrelationskoeffizienten = [basis_korrelation] * max(simulations_durchlaeufe, 1)

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
delta_n = np.nanstd(veranderungen_neugier, axis=0, ddof=std_ddof).tolist()
if len(delta_n) < len(quartale_range):
    delta_n = [np.nan] * (len(quartale_range) - len(delta_n)) + delta_n

# Berechne dynamic_C, damit es überall verfügbar ist
c_values = np.array(delta_k_entw) * np.array(delta_k_mess)
dynamic_C = gamma(c_values)
logging.info("dynamic_C (init) range: min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))

# =========================================
# csv Export
# =========================================

def exportiere_bildungswirkgefuege_csv(dateiname=None):
    """
    Exportiert alle berechneten Zeitreihen-Daten in eine CSV-Datei zur Weiterverarbeitung.
    """
    target_path = Path(dateiname) if dateiname else EXPORT_ROOT / "bildungswirkgefuege_datenbasis.csv"
    target_path.parent.mkdir(parents=True, exist_ok=True)
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
        "Delta_N": delta_n,
        "Delta_M_micro": delta_m_micro_series.tolist(),
        "Dynamic_C": dynamic_C.tolist() if hasattr(dynamic_C, "tolist") else dynamic_C,
        "BPS_Bio": mittelwerte_bio_status.tolist() if hasattr(mittelwerte_bio_status, "tolist") else mittelwerte_bio_status,
        "BPS_Psy": mittelwerte_psy_status.tolist() if hasattr(mittelwerte_psy_status, "tolist") else mittelwerte_psy_status,
        "BPS_Soz": mittelwerte_soz_status.tolist() if hasattr(mittelwerte_soz_status, "tolist") else mittelwerte_soz_status
    })

    export_df.to_csv(target_path, index=False)
    print(f"✅ Vollständige Bildungswirkgefüge-Daten exportiert nach: {target_path}")

# Exportiere zusätzlich die Simulationsparameter als CSV
def exportiere_parameter_csv(dateiname=None):
    import csv
    target_path = Path(dateiname) if dateiname else EXPORT_ROOT / "bildungswirkgefuege_parameter.csv"
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
        "start_kompetenz": start_kompetenz_val,
        "start_neugier": start_neugier_val,
        "start_motivation": start_motivation_val,
        "start_bereitschaft": start_bereitschaft_val,
        "archetyp": archetyp,
        "paradigma": paradigma,
        "quartale": globals().get("quartale", None),
        "simulations_durchlaeufe": globals().get("simulations_durchlaeufe", None),
        "bps_bio_start": globals().get("bio_startstatus", None),
        "bps_psy_start": globals().get("psy_startstatus", None),
        "bps_soz_start": globals().get("soz_startstatus", None),
        "bps_bio_mean": globals().get("bio_status_mean", None),
        "bps_psy_mean": globals().get("psy_status_mean", None),
        "bps_soz_mean": globals().get("soz_status_mean", None)
    }
    with open(target_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["Parameter", "Wert"])
        for key, value in parameter.items():
            writer.writerow([key, value])
        if "pe_auswirkungen" in globals():
            for key, value in sorted(pe_auswirkungen.items()):
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

_LINE_ROLES = {
    "primary": "linie_primaryLine",
    "secondary": "linie_secondaryLine",
    "accent": "linie_accent",
    "positive": "linie_positiveHighlight",
    "negative": "linie_negativeHighlight",
}
_MARKER_ROLES = {
    "primary": "marker_primaryLine",
    "secondary": "marker_secondaryLine",
    "accent": "marker_accent",
    "positive": "marker_positiveHighlight",
    "negative": "marker_negativeHighlight",
}


def ci_line(role, **overrides):
    """Liefert eine Linie entsprechend der CI-Rolle."""
    key = _LINE_ROLES.get(role)
    if key is None:
        raise KeyError(f"Unbekannte CI-Linienrolle: {role}")
    style = deepcopy(_style_base[key])
    style.update(overrides)
    return style


def ci_marker(role, **overrides):
    """Liefert Marker-Styles passend zur CI-Rolle."""
    key = _MARKER_ROLES.get(role)
    if key is None:
        raise KeyError(f"Unbekannte CI-Markerrolle: {role}")
    style = deepcopy(_style_base[key])
    style.update(overrides)
    return style


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
data = pd.DataFrame(list(pe_auswirkungen.items()), columns=['Ereigniskategorie', 'Auswirkung'])
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
# Visualisierung der einzelnen Durchläufe als Streudiagramm
# -----------------------------------------

# Daten für die Durchläufe
x_durchlaeufe = list(range(1, simulations_durchlaeufe + 1))
y_durchlaeufe = [pearsonr(np.random.randn(100), np.random.randn(100))[0] for _ in range(simulations_durchlaeufe)]

fig_durchlaeufe = go.Figure()

# Aura-Trace (weiße, halbtransparente große Punkte hinterlegt)
# Aura entfernt, da mit neuem Magenta zu starker Kontrast auf dunklem Hintergrund
# fig_durchlaeufe.add_trace(go.Scatter(
#     mode='markers',
#     x=x_durchlaeufe,
#     y=y_durchlaeufe,
#     marker=dict(
#         size=12,
#         color="rgba(255,255,255,0.4)"
#     ),
#     showlegend=False,
#     hoverinfo="skip"
# ))

# Eigentliche Durchlaufpunkte
fig_durchlaeufe.add_trace(go.Scatter(
    mode='markers',
    x=x_durchlaeufe,
    y=y_durchlaeufe,
    marker=dict(
        size=6,
        color=colors['primaryLine']
    ),
    name='Durchläufe'
))

fig_durchlaeufe.update_layout(**plotly_template.get_standard_layout(
    title=f'Bildungswirkgefüge | Korrelationskoeffizienten ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title='Durchlauf',
    y_title='Korrelationskoeffizient'
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
    dynamic_C = gamma(c_values)
    logging.info("dynamic_C range: min=%s, max=%s", np.nanmin(dynamic_C), np.nanmax(dynamic_C))
    dynamic_C_scalar = dynamic_C.mean()

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
        x=simulations_ergebnisse_pe.index,
        y=mittelwerte_motivation,
        mode='lines+markers',
        name='Motivation',
        line=ci_line("primary")
    ))

    fig_neugier_motivation.add_trace(go.Scatter(
        x=simulations_ergebnisse_pe.index,
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
        x_range=[0, quartale]
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
        x=bps_status_df.index,
        y=bps_status_df["Bio"],
        mode='lines+markers',
        name='Biologisch',
        line=ci_line("primary")
    ))
    fig_bps_status.add_trace(go.Scatter(
        x=bps_status_df.index,
        y=bps_status_df["Psy"],
        mode='lines+markers',
        name='Psychologisch',
        line=ci_line("secondary")
    ))
    fig_bps_status.add_trace(go.Scatter(
        x=bps_status_df.index,
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
        x_range=[0, quartale]
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
    phase_quartale = bps_status_df.index.to_numpy(dtype=float)
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
        x=simulations_ergebnisse_pe.index[rolling_window-1:rolling_window-1+len(rolling_corr)],
        y=rolling_corr,
        mode='lines+markers',
        name='Rolling Pearson (3 Quartale)',
        line=ci_line('primary')
    ))
    fig_rolling_corr.update_layout(**plotly_template.get_standard_layout(
        title=f'Gleitende Korrelation Neugier–Motivation (3 Quartale) ({gewaehlter_ansatz} | {selected_archetyp})',
        x_title='Zeit (Quartal)',
        y_title='Korrelationskoeffizient',
        x_range=[0, quartale]
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
            x_range=[0, quartale]
        ))
        safe_fig_show(fig_bps_corr)
        export_figure(fig_bps_corr, 'bps-rolling-korrelationen', export_fig_bps_korrelationen, export_fig_png_bps_korrelationen)
    diff_norm = (diff_neugier_motivation - np.mean(diff_neugier_motivation)) / np.std(diff_neugier_motivation)
    lowess_smoothed = lowess(diff_norm, simulations_ergebnisse_pe.index, frac=0.3)
    fig_korr_dynamik = go.Figure()
    fig_korr_dynamik.add_trace(go.Scatter(
        x=simulations_ergebnisse_pe.index,
        y=diff_norm,
        mode='lines+markers',
        name='Normierte Differenz Neugier–Motivation',
        line=ci_line('primary')
    ))
    fig_korr_dynamik.add_trace(go.Scatter(
        x=simulations_ergebnisse_pe.index,
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
        x_range=[0, quartale],
    ))
    safe_fig_show(fig_korr_dynamik)
    export_figure(fig_korr_dynamik, 'korrelationsdynamik-neugier-motivation', export_fig_korrelationsdynamik_neugier_motivation, export_fig_png_korrelationsdynamik_neugier_motivation)

render_correlation_and_dynamics()
render_bps_phaseportrait()
# -----------------------------------------
# Dreidimensionale Unsicherheitsrelation
# -----------------------------------------

# Arrays für Visualisierung vorbereiten
delta_k_mess_array = np.array(delta_k_mess)
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
    x=simulations_ergebnisse_pe.index,
    y=delta_k_mess_skal,
    mode='lines',
    name='Kompetenzmessunsicherheit (ΔK_mess)',
    line=linien_unsicherheiten["delta_k_mess"]
))

# Kurve für ΔK_entw
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=delta_k_entw_skal,
    mode='lines',
    name='Kompetenzentwicklungsunsicherheit (ΔK_entw)',
    line=linien_unsicherheiten["delta_k_entw"]
))

# Kurve für ΔN
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=delta_n_skal,
    mode='lines',
    name='Neugierunsicherheit (ΔN)',
    line=linien_unsicherheiten["delta_n"]
))

# Kurve für Dynamic-C
fig_dreidimensionale_unsicherheitsrelation.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
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

# -----------------------------------------
# monte-carlo-simulation
# -----------------------------------------

fig_mc = go.Figure()
for i, column in enumerate(simulations_ergebnisse_pe_clipped.columns):
    smoothed_data = smooth_curve(simulations_ergebnisse_pe_clipped[column].values, clip_max=10)
    smoothed_data_clipped = np.clip(smoothed_data, 0, 10)
    fig_mc.add_trace(go.Scatter(
        x=simulations_ergebnisse_pe.index,
        y=smoothed_data_clipped,
        mode='lines',
        name=f'Durchlauf {i + 1}',
        line=ci_line("primary")
    ))
fig_mc.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | Monte Carlo-Simulation ({simulations_durchlaeufe} Durchläufe) ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title='Zeit [Quartal]',
    y_title='Kompetenzniveau',
    x_range=[0, quartale],
    y_range=[0, 10]
))
safe_fig_show(fig_mc)
export_figure(fig_mc, "monte-carlo-simulation", export_fig_mc, export_fig_png)

# -----------------------------------------
# Statistik des Kompetenzkondensats
# -----------------------------------------

fig_summary = go.Figure()
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index.tolist() + simulations_ergebnisse_pe.index.tolist()[::-1],
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
    x=simulations_ergebnisse_pe.index,
    y=smooth_curve(mittelwerte_kompetenz, clip_max=10),
    mode='lines',
    name='Mittelwert',
    line=ci_line("primary"),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Mittelwert %{y:.2f}<extra></extra>"
))
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=smooth_curve(mediane_kompetenz, clip_max=10),
    mode='lines',
    name='Median',
    line=ci_line("secondary"),
    hoverinfo='text',
    hovertemplate="Quartal %{x}: Median %{y:.2f}<extra></extra>"
))
fig_summary.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
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
    x_range=[0, quartale],
    y_range=[0, 10]
))
safe_fig_show(fig_summary)
export_figure(fig_summary, "summary", export_fig_summary, export_fig_png)

# -----------------------------------------
# Kumulative Verdichtung des Kompetenzkondensats
# -----------------------------------------

fig_kumulative_kompetenz = go.Figure()
fig_kumulative_kompetenz.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=smooth_curve(mittelwerte, clip_max=10),
    fill='tozeroy',
    fillcolor=plotly_template.get_colors()['depthArea'],
    name='Kompetenz',
    line=ci_line("primary"),
    mode='lines'
))
fig_kumulative_kompetenz.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | Kumulative Verdichtung: {flaeche_unter_mittelwert:.2f} ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title="Zeit [Quartal]",
    y_title="Kompetenzniveau",
    x_range=[0, quartale],
    y_range=[0, 10]
))

safe_fig_show(fig_kumulative_kompetenz)
export_figure(fig_kumulative_kompetenz, "kumulative-kompetenz", export_fig_kumulative_kompetenz, export_fig_png)

# -----------------------------------------
# Kompetenzkondensat | Kumulativer Vergleich
# -----------------------------------------

fig_kumulativer_vergleich = go.Figure()

fig_kumulativer_vergleich.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=smooth_curve(bestes_ergebnis, clip_max=10),
    fill='tozeroy',
    name='Optimum',
    line=ci_line("positive"),
))

fig_kumulativer_vergleich.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
    y=smooth_curve(schlechtestes_ergebnis, clip_max=10),
    fill='tozeroy',
    name='Minimum',
    line=ci_line("negative"),
))

fig_kumulativer_vergleich.update_layout(**plotly_template.get_standard_layout(
    title=f'Kompetenzniveau | Kumulativer Vergleich: Beste ({flaeche_unter_bestes:.2f}) vs. Schlechteste ({flaeche_unter_schlechtestes:.2f}) ({gewaehlter_ansatz} | {selected_archetyp})',
    x_title="Zeit [Quartal]",
    y_title="Kompetenzniveau",
    x_range=[0, quartale],
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
        x_range=[0, quartale],
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
        x=simulations_ergebnisse_pe.index,
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
    x_range=[0, quartale],
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
    x=simulations_ergebnisse_pe.index,
    y=bildungswirkfaktoren_smooth,
    mode='lines+markers',
    name='ν (Bildungswirkfaktor)',
    line=ci_line("primary")
))

# Plot für Bildungswirkindikator (ι) auf sekundärer y-Achse
fig_bildungswirkgefuege.add_trace(go.Scatter(
    x=simulations_ergebnisse_pe.index,
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
        x=[simulations_ergebnisse_pe.index[point]],
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
            x=[simulations_ergebnisse_pe.index[point]],
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
    x_range=[0, quartale],
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
        x=simulations_ergebnisse_pe.index,
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
        x=[simulations_ergebnisse_pe.index[wendepunkt]],  # Verwenden Sie den Index direkt
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
    x=simulations_ergebnisse_pe.index[minima_bildungswirkfaktor],
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
    x=simulations_ergebnisse_pe.index[maxima_bildungswirkfaktor],
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
z_time = np.linspace(0, quartale, len(ν_3d_kompetenz_interpoliert))

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
energy_repeated = np.tile(H_energy[:, np.newaxis], (1, num_phi))
x_energy = ν_3d_kompetenz_repeated + energy_repeated * np.cos(phi_repeated)
y_energy = ν_3d_kompetenz_repeated + energy_repeated * np.sin(phi_repeated)

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
    surfacecolor=energy_repeated,
    colorscale=colorscale_energy,
    showscale=True,
    opacity=0.4,
    colorbar=dict(title='|H|²'),
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

# Glättungsfunktion
def smooth_curve(data, window=3):
    return np.convolve(data, np.ones(window) / window, mode='same')

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
    x_range=[-quartale, quartale],
    y_range=[-quartale, quartale]
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
        f"Monte Carlo Simulation ({simulations_durchlaeufe} Durchläufe)",
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
    ["Simulationsdurchläufe", simulations_durchlaeufe],
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
    import modellpruefung
    report_path, gpt_used = modellpruefung.fuehre_modellpruefung_durch()
    if gpt_used:
        print("✅ Modellprüfung nach Simulation inkl. GPT-Interpretation durchgeführt.")
    else:
        print("ℹ️ Modellprüfung nach Simulation ohne GPT-Interpretation abgeschlossen.")
    print(f"📄 Bericht gespeichert unter: {report_path}")
else:
    print("ℹ️ Modellprüfung ist deaktiviert (config).")
