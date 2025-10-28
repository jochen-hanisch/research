---
author: Jochen Hanisch-Johannsen
title: Bildungswirkfaktor
Repository:
created: 2024-09-30
updated: []
publish: false
tags:
  - Research
  - Begriff
  - Definition
  - Dissertation
  - "#Bildungswirkfaktor"
  - "#Kompetenzentwicklung"
  - "#Wirkung"
  - "#Lernprozess"
  - "#Forschung"
published:
project: Wirkgefüge im digitalen Bildungsraum
type:
  - Wissenschaftliche Notiz
---

# 1 Definition

Der Bildungswirkfaktor ($\nu$) ist eine spezifische Variante des allgemeinen [[Wirkfaktor|Wirkfaktors]], die zur Messung der Stärke und Richtung der [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung]] in Bildungsprozessen dient. Er bewertet die Effizienz und Effektivität des Lernens, indem er die Geschwindigkeit und den Umfang der Kompetenzentwicklung unter Berücksichtigung interner und externer Einflüsse quantifiziert. Der Bildungswirkfaktor basiert auf der Steigung der Kompetenzentwicklungskurve und stellt dar, in welchem Ausmaß die Kompetenzentwicklung im zeitlichen Verlauf erfolgt.

Im Kontext der [[Wirkung]] repräsentiert der Bildungswirkfaktor die Intensität und Qualität von Veränderungen im System, die durch Bildungsprozesse initiiert werden. Die Wirkung beschreibt die systemische Veränderung, die durch den Bildungswirkfaktor verursacht wird und sich im Gesamtergebnis des Systems manifestiert. Der Bildungswirkfaktor bietet somit eine Grundlage für die quantitative Beschreibung der Wirkung in einem Bildungsumfeld. Ein stabiler Bildungswirkfaktor weist auf eine kontrollierte Entwicklung hin, während starke Schwankungen auf instabile und schwer vorhersehbare Lernprozesse hindeuten.

# 2 Herleitung

## 2.1 Mathematische Herleitung

Der Bildungswirkfaktor $\nu$ ist mathematisch als zeitliche Ableitung der Kompetenzentwicklung $K(t)$ definiert:

$$
\nu = \frac{dK}{dt} \tag{1}
$$

Diese Formel beschreibt die Änderungsrate des Kompetenzniveaus $K$ über die Zeit $t$. Die Steigung der Kompetenzentwicklungskurve verdeutlicht die Dynamik des Lernprozesses im betrachteten Zeitraum. Ein positiver Wert signalisiert eine zunehmende Kompetenz (positive Wirkung), während ein negativer Wert Kompetenzverluste (negative Wirkung) anzeigt.

## 2.2 Standardisierte Änderungsrate

Alternativ kann die Stärke der Bildungseffekte auch durch die Veränderung pro Zeiteinheit $\Delta t$ ausgedrückt werden:

$$
\nu = \frac{\Delta K(t)}{\Delta t} \tag{2}
$$

Hierbei steht $\Delta K(t) = K(t+\Delta t) - K(t)$ für die beobachtbare Änderung des Kompetenzniveaus und $\Delta t$ für das betrachtete Zeitintervall. Diese Formel wird verwendet, um kurzfristige Änderungen im Kompetenzniveau zu berechnen und kurzfristige Fluktuationen im Lernprozess darzustellen. Die diskrete Änderung $\Delta K(t)$ ist von den im weiteren Verlauf verwendeten Unsicherheiten $\Delta K_{mess}$ und $\Delta K_{entw}$ zu unterscheiden.

## 2.3 Mathematische Interpretation und Kurvendiskussion

Der Bildungswirkfaktor wird durch die Steigung der Kompetenzentwicklungskurve dargestellt:

$$
\nu = \frac{dK}{dt} \tag{3}
$$

Die Struktur der $\nu$-Kurve ist entscheidend für die Interpretation der Lernprozesse. Wendepunkte zeigen Übergänge zwischen stabilen und instabilen Phasen an, während Minima und Maxima auf extrem instabile Zustände oder Regenerationsphasen hinweisen. Eine stabile $\nu$-Kurve ohne starke Fluktuationen zeigt, dass die Kompetenzentwicklung in einem kontrollierten und vorhersehbaren Bereich verläuft. Je mehr Extremwerte oder Wendepunkte in der $\nu$-Kurve vorhanden sind, desto stärker sind die Unsicherheiten und desto instabiler sind die Lernprozesse ausgeprägt.

## 2.4 Systemische Verknüpfung

Der Bildungswirkfaktor steht in direktem Zusammenhang mit der [[Allgemein beruflich/Research/Bildungswissenschaft/Wirkung|systemischen Wirkung]] sowie mit zwei äußeren Unsicherheiten: der Unsicherheit in der Kompetenzmessung ($\Delta K_{mess}$) und der Unsicherheit in der [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung|Kompetenzentwicklung]] ($\Delta K_{entw}$). Diese Größen werden in der Simulation über eine Unschärferelation nach dem Schema

$$
\Delta K_{mess} \cdot \Delta K_{entw} \ge C(\gamma)
$$

gebunden, wobei $C(\gamma)$ eine **Kopplungs-/Balancegrenze** des Systems markiert. Auf der psychischen Ebene wirken zusätzlich die semantische Kognitionsunsicherheit ($\Delta C_{kog}$), die affektive Varianz ($\Delta E$) und die explorative Neugierunsicherheit ($\Delta N$), deren Kopplung durch

$$
\Delta C_{kog} \cdot \Delta E \cdot \Delta N \ge C(\gamma)
$$

begrenzt ist. Der Bildungswirkfaktor vermittelt zwischen diesen Beobachtungsräumen: Diskrete Versionierungen stabilisieren kurzfristig $\Delta K_{entw}$, erhöhen jedoch $\Delta K_{mess}$ und modulieren damit indirekt $\Delta N$.

Wichtig ist die **Trennung der Begriffe**:

- Der **Bildungswirkfaktor** ist die **Dynamik der Kompetenzentwicklung** und bleibt definiert als
  $$
  \nu = \frac{dK}{dt} \quad (\text{bzw. diskret } \nu \approx \tfrac{\Delta K(t)}{\Delta t}).
  $$
- Die **Kopplungsstärke** zwischen Entwicklungs- und Messunsicherheit fassen wir als separates Maß ([[Kopplungshypothese]]).
  $$
  \Xi := \Delta K_{mess} \cdot \Delta K_{entw}.
  $$
  $\Xi$ ist **nicht** identisch mit $\nu$ und **nicht** mit $C(\gamma)$; es kann $C(\gamma)$ über- oder unterschreiten, während $C(\gamma)$ die **untere Schranke** der Kopplung darstellt.

Hohe Werte deuten auf stark gekoppelte Unsicherheiten hin (potenziell instabilere Prozesse), niedrige Werte auf entkoppelte oder gut gedämpfte Unsicherheiten. Robuste Lernprozesse liegen vor, wenn  moderat und stabil verläuft und  sich nahe an  bewegt, ohne dass eine Gleichsetzung erforderlich ist.

Diese Lesart ist zugleich eine Konkretisierung der [[Kopplungshypothese]], die annimmt, dass Bildungswirkungen nicht monokausal erklärbar sind, sondern aus der dynamischen Verschränkung multipler Faktoren hervorgehen. Empirische Befunde aus Visible Learning (Hattie, 2024) lassen sich in diesem Rahmen als Belege für Kopplung deuten. Dort zeigen sich hohe Effektstärken insbesondere dann, wenn Faktoren wie Feedback, Klarheit und Lehrer-Schüler-Beziehung nicht isoliert, sondern in ihrer Wechselwirkung betrachtet werden. Die Simulation operationalisiert diesen Zusammenhang mathematisch über $\Xi = \Delta K_{mess} \cdot \Delta K_{entw}$ und zeigt, dass robuste Kompetenzentwicklung an eine balancierte Kopplung gebunden ist.

### 2.4.1 Bedürfnisdimensionen als Stellgrößen

Die in [[Kopplungshypothese#1 Definition]] beschriebenen Bedürfniscluster liefern konkrete Stellhebel, um $\nu$, $\Delta K_{mess}$, $\Delta K_{entw}$ sowie $\Delta C_{kog}$, $\Delta E$ und $\Delta N$ zu beeinflussen. Aus den dort ausgewiesenen Pfaden folgt:

- **Bindung** und **Selbstwerterhalt** dämpfen $\Delta K_{entw}$, indem sie Entwicklungsunsicherheit reduzieren und somit die Glättung von $\nu$ unterstützen ([[Kopplungshypothese#2.4 Bedürfnisdimensionen nach Young und Roediger]]).
- **Kontrolle nach außen** wirkt über klare Kommunikations- und Bewertungsstrukturen auf $\Delta K_{mess}$ ein und stabilisiert dadurch die Beobachtung von Kompetenzzuwächsen ([[Kopplungshypothese#2.2 Netzwerkstrukturen in Bildungssystemen]]).
- **Emotionale Sicherheit** und **Selbstregulation** reduzieren $\Delta E$ und halten das psychische System anschlussfähig.
- **Kontrolle nach innen** und **Vermeidung von Unlust** werden in [[Kopplungshypothese#2.6 Integration der empirischen Daten zu Kopplungspotentialen]] als Transformationspfad von Neugier zu Motivation ausgewiesen; dieser Pfad stabilisiert $\nu$ und moduliert $\Delta N$ sowie $\Delta C_{kog}$.

Der Bildungswirkfaktor fungiert damit als Messspiegel dieser bedürfnisorientierten Kopplungen:

>Veränderungen in den Bedürfnisclustern schlagen sich unmittelbar in den Größen $\nu$, $\Delta K_{mess}$, $\Delta K_{entw}$ sowie $\Delta C_{kog}$, $\Delta E$ und $\Delta N$ nieder. Interventionen lassen sich so bidirektional planen, d.h. über bedürfnisbasierte Architekturen (theoretischer Rahmen in [[Kopplungshypothese]]) und über die hier dargestellten messbaren Wirkungsindikatoren.

## 2.5 Bezug zum allgemeinen Wirkfaktor

Im Gegensatz zum allgemeinen [[Wirkfaktor]], der in verschiedenen Kontexten zur Beschreibung von Einflüssen auf ein System verwendet wird, ist der Bildungswirkfaktor eine spezialisierte Form, die auf den Bildungsprozess angewandt wird. Während der Wirkfaktor allgemein als treibender Mechanismus fungiert, beschreibt der Bildungswirkfaktor konkret die Änderungen in Lern- und Kompetenzentwicklungsprozessen. Er ist daher ein Subtyp des Wirkfaktors, der die spezifischen Merkmale und Einflussgrößen im Bildungssystem berücksichtigt.

## 2.6 Ableitungen, Herleitungen und prüfbare Konsequenzen

### 2.6.1 Mathematische Klarstellung

- **Dynamik (Bildungswirkfaktor):** $\nu = \frac{dK}{dt}$ bzw. zeitdiskret $\nu \approx \frac{\Delta K(t)}{\Delta t}$.  
- **Äußere Unschärfegrenze:** $\Delta K_{mess} \cdot \Delta K_{entw} \ge C(\gamma)$ (mit $C(\gamma)$ als Kopplungs-/Balanceparameter).  
- **Innere Unschärfegrenze:** $\Delta C_{kog} \cdot \Delta E \cdot \Delta N \ge C(\gamma)$ (psychisches Kopplungsfeld).  
- **Kein Gleichheitszwang:** $C(\gamma)$ ist **nicht** identisch mit den Produkten; es markiert die **untere Schranke / Systemgrenze**, gegen die sich Prozesse annähern können.  
- **Kopplungsmaß:** $\Xi = \Delta K_{mess} \cdot \Delta K_{entw}$ (separat von $\nu$ und $C(\gamma)$).

### 2.6.2 Didaktische Folgerungen

1. **Neugier → Motivation** als Transformationskette: Steuert primär $\nu$; bricht diese Kette, steigen $\Delta N$, $\Delta E$ und $\Delta C_{kog}$.  
2. **Prüfungsdesign:** Mehr summative Tests ohne formative Einbettung → ↑$\Delta K_{mess}$, ggf. ↑$\Delta E$ → geringere Robustheit.  
3. **Bindung und Feedbackkultur:** Wirken dämpfend auf $\Delta K_{entw}$ und $\Delta E$ und stabilisieren $ \nu $.  
4. **Ziel:** **Robuste Kopplung** = moderate, stabile $\nu$, Produkte $\Delta K_{mess} \cdot \Delta K_{entw}$ nahe $C(\gamma)$ sowie kontrollierte innere Produkte $\Delta C_{kog} \cdot \Delta E \cdot \Delta N$.

### 2.6.3 Minimaler Rechenweg (Pseudocode / Python-Skizze)

```python
import numpy as np

def bildungswirkfaktor(K, t):
    # zentrale Differenzen (vereinfacht)
    dKdt = np.gradient(K, t)
    return dKdt  # ν(t)

def kopplungscheck(deltaK_mess, deltaK_entw, c_gamma):
    return (deltaK_mess * deltaK_entw) >= c_gamma  # Bool pro Zeitschritt

def innere_kopplung(deltaC_kog, deltaE, deltaN, c_gamma):
    return (deltaC_kog * deltaE * deltaN) >= c_gamma

def extrema(v):
    # Wendepunkte/Extrema der ν-Kurve (einfacher Ansatz)
    dv = np.gradient(v)
    zc = np.where(np.diff(np.sign(dv)) != 0)[0]  # Nullstellenwechsel
    return zc  # Indizes potentieller Wendepunkte
```

**Anwendung:**

- $\nu(t)$ glätten (z. B. Savitzky–Golay) → Extrempunkte detektieren → **Instabilitätsfenster** markieren.  
- Gleichzeitig $\Delta K_{mess}$, $\Delta K_{entw}$ sowie $\Delta C_{kog}$, $\Delta E$, $\Delta N$ überwachen → **Kopplungsverletzungen** (wenn die Produkte deutlich kleiner oder größer als $C(\gamma)$ werden) frühzeitig erkennen.

### 2.6.4 Strukturelle Kopplung als Folge der Kopplungshypothese

Die im Projekt verwendete Unschärferelation verbindet **Messunsicherheit** ($\Delta K_{mess}$) und **Entwicklungsunsicherheit** ($\Delta K_{entw}$) über eine **Kopplungsgrenze** $C(\gamma)$. Der Bildungswirkfaktor $\nu = \frac{dK}{dt}$ vermittelt die Dynamik der Kompetenzentwicklung. Im Sinne einer **strukturellen Kopplung** fungiert $C(\gamma)$ als Balancewert zwischen (a) psychologischen Grundbedürfnissen (Roediger, 2015) und (b) pädagogisch-didaktischer Architektur (dein Simulationsmodell). Die Kopplung ist dann gut, wenn $\Delta K_{mess} \cdot \Delta K_{entw}$ nahe an $C(\gamma)$ liegt (nicht notwendig gleich), und $\nu$ dabei stabil (ohne starke Extreme) verläuft.

Die über die Modellprüfungen aggregierten Korrelationen fungieren als empirische Indikatoren der Kopplung. Hohe Zusammenhänge zwischen $\nu$, $\Delta K_{mess}$, $\Delta K_{entw}$ sowie den intrapsychischen Unsicherheiten $\Delta C_{kog}$, $\Delta E$ und $\Delta N$ stützen die [[Kopplungshypothese]], da sie zeigen, dass sich strukturelle Kopplung nicht nur theoretisch postulieren, sondern auch empirisch im Datenraum beobachten lässt. Damit erweitert sich der Bildungswirkfaktor um eine empirische Dimension. Korrelationen zwischen diesen Größen dienen als Beobachtungsgrößen, die die [[Kopplungshypothese]] stützen und eine Brücke zwischen Simulation und empirischen Befunden (Hattie, 2024) schlagen.

**A) Mathematische Kopplung**

```mermaid
flowchart TD
  subgraph PSY[Psychologische Ebene – Grundbedürfnisse Roediger]
    BIND[Bindung]
    EXT[Kontrolle außen]
    INT[Kontrolle innen]
    SW[Selbstwert]
    LUST[Lust/Unlust-Balance]
  end

  subgraph SIM[Didaktisch-simulative Ebene]
    dK_entw_down["↓ ΔK_{entw} (Entwicklungsunsicherheit)"]
    dK_mess_down["↓ ΔK_{mess} (Messunsicherheit)"]
    dE_down["↓ ΔE (emotionale Varianz)"]
    dCog_down["↓ ΔC_{kog} (Kognitionsunsicherheit)"]
    MOTIV["Neugier → Motivation"]
    dN_mod["ΔN (Neugierunsicherheit)"]
    NU["ν = dK/dt"]
    XI["Ξ = ΔK_{mess} · ΔK_{entw}"]
    CG["C(γ) – Kopplungsgrenze"]
    WIRK[Systemische Wirkung]
  end

  %% Kopplungslogik
  dK_entw_down --> XI
  dK_mess_down --> XI
  XI -->|≥| CG

  %% Dynamikpfad
  MOTIV --> NU --> WIRK

  %% Grundbedürfnisse
  BIND --> dK_entw_down
  SW --> dK_entw_down
  EXT --> dK_mess_down
  INT --> MOTIV
  LUST --> MOTIV

  %% Intrapsychische Dämpfung
  BIND --> dE_down
  SW --> dE_down
  MOTIV --> dN_mod
  dE_down -.-> MOTIV
  dCog_down -.-> MOTIV
```

**B) Prozessdidaktische Kette**

```mermaid
flowchart TD
  BIND[Bindung] --> dK_entw_down["↓ ΔK_{entw}"]
  SW[Selbstwert] --> dK_entw_down
  EXT[Kontrolle außen] --> dK_mess_down["↓ ΔK_{mess}"]
  INT[Kontrolle innen] --> MOTIV["Neugier → Motivation"]
  LUST[Lust/Unlust] --> MOTIV
  EMPATH[Emotionale Unterstützung] --> dE_down["↓ ΔE"]
  KOG[Didaktische Klarheit] --> dCog_down["↓ ΔC_{kog}"]
  REFLEX[Explorationsräume] --> dN_mod["ΔN"]

  dK_entw_down --> MOTIV
  dK_mess_down --> MOTIV
  dE_down -.-> MOTIV
  dCog_down -.-> MOTIV
  MOTIV --> NU["ν = dK/dt"] --> WIRK[Systemische Wirkung]
  MOTIV --> dN_mod

  XI["Ξ = ΔK_{mess} · ΔK_{entw}"] -. Kontext .- CG["C(γ) – Kopplungsgrenze"]
```

**Interpretation:**

- **Bindung** und **Selbstwert** stabilisieren Lernverläufe ⇒ senken $\Delta K_{entw}$ und dämpfen $\Delta E$.  
- **Externe Kontrolle** (klare Kriterien, transparente Prüfungen) reduziert $\Delta K_{mess}$ und macht Entwicklungsfortschritte beobachtbar.  
- **Emotionale Unterstützung** und **didaktische Klarheit** mindern $\Delta E$ bzw. $\Delta C_{kog}$ und halten Motivationspfade offen.  
- **Interne Kontrolle** (Selbststeuerung) transformiert **Neugier → Motivation**, moduliert $\Delta N$ und stabilisiert $\nu$.  
- $C(\gamma)$ ist kein Produkt, sondern eine **Systemgrenze / Balancemarke**: Entfernen sich $\Delta K_{mess} \cdot \Delta K_{entw}$ stark von $C(\gamma)$ oder werden die inneren Produkte zu groß, ist die Kopplung gestört. Nähe zu $C(\gamma)$ bei moderatem $\nu$ kennzeichnet **robuste Lernprozesse**.

# 3 Folgerungen

- **Stabilität der Lernprozesse**:  
   Ein niedriger und stabiler Bildungswirkfaktor $\nu$ zeigt an, dass die Kompetenzentwicklung in einem stabilen Bereich verläuft und die Lernprozesse nicht durch externe Störungen oder hohe Messunsicherheiten beeinflusst werden.
- **Instabile Phasen**:  
   Ein hoher oder stark schwankender Bildungswirkfaktor deutet auf instabile Lernphasen hin, die durch externe Faktoren wie persönliche Ereignisse oder methodische Schwächen ausgelöst werden können.
- **Verbindung zur Wirkung**:  
   Der Bildungswirkfaktor beeinflusst direkt die beobachtbare [[Wirkung]] innerhalb des Bildungssystems. Positive Werte verstärken die gewünschte Wirkung, während negative Werte hemmend wirken. Die Unsicherheitskopplung und deren Ausmaß bestimmen, wie stark der Bildungswirkfaktor die resultierende Wirkung im System verändert.
- **Systemische Relevanz**:  
   Da der Bildungswirkfaktor als spezialisierter [[Wirkfaktor]] fungiert, interagiert er mit anderen Einflussgrößen im System, wie z. B. Lernbereitschaft oder Lernumgebung. Dadurch wird die tatsächliche Wirkung immer im Kontext mehrerer Faktoren generiert.

## 4 Kopplungsperspektive mit der Kopplungshypothese

Die bedürfnisbasierte [[Kopplungshypothese]] definiert Bildungswirksamkeit als Ergebnis wiederholbarer Anschlusschancen zwischen psychischen und sozialen Systemen (Luhmann, 1997). Der Bildungswirkfaktor liefert hierzu das dynamische Gegenstück: Über $\nu$, $\Delta K_{mess}$, $\Delta K_{entw}$ sowie $\Delta C_{kog}$, $\Delta E$ und $\Delta N$ wird sichtbar, ob die in der Hypothese skizzierten Bedürfnisse – Bindung, externe und interne Kontrolle, Selbstwerterhalt sowie Vermeidung von Unlust – tatsächlich stabil adressiert werden (Young & Roediger, 2011). Flache Steigungen und geringe Unsicherheitsprodukte deuten auf gelingende Kopplung hin, während sprunghafte Verläufe unmittelbar vor Augen führen, wo strukturelle Brücken auszudünnen beginnen.

Die metaanalytischen Befunde bei Hattie (2024) stützen diese Lesart, weil hohe Effektstärken dort auftreten, wo Interventionen sowohl psychische als auch soziale Voraussetzungen bedienen. Wird etwa formative Evaluation mit vertrauensvollen Kommunikationsmustern kombiniert, sinkt $\Delta K_{mess}$, $\Delta K_{entw}$ nähert sich stabilen Fenstern, $\Delta E$ wird gedämpft und $\nu$ bleibt steuerbar. Der Bildungswirkfaktor fungiert in diesem Setting als Frühwarnsignal: Liegen gemessene Verläufe dauerhaft oberhalb der Kopplungsgrenze $C(\gamma)$ oder zeigen starke Extremwerte, empfiehlt sich eine Rückkopplung an die Bedürfnisarchitektur der [[Kopplungshypothese#2 Herleitung]].

Damit entsteht eine iterierbare Steuerungsschleife. Bedürfnisorientierte Interventionen werden über die Kopplungshypothese geplant, die Messgrößen des Bildungswirkfaktors validieren deren Wirkung und führen bei Abweichungen gezielt zurück zu den Stellgrößen Bindung, Kontrolle oder Selbstwert. Die beiden Notizen bilden so ein integriertes Arbeitsinstrument, das theoretische Brücken, empirische Indizien und datenbasierte Diagnostik zusammenführt (Hattie, 2024; Luhmann, 1997; Young & Roediger, 2011).

# 7 Zusammenfassung

Der Bildungswirkfaktor $(\nu)$ beschreibt die Stärke der Bildungsprozesse in Bezug auf die [[Allgemein beruflich/Research/Bildungswissenschaft/Kompetenzentwicklung]]. Er wird durch die zeitliche Ableitung des Kompetenzniveaus berechnet und gibt die Änderungsrate der Kompetenzentwicklung wieder. Ein stabiler $\nu$-Wert zeigt eine kontrollierte Entwicklung, während instabile oder stark schwankende Werte auf Unsicherheiten und instabile Lernprozesse hinweisen. Die Kopplung der äußeren Unsicherheiten $\Delta K_{mess}$ und $\Delta K_{entw}$ sowie der inneren Variablen $\Delta C_{kog}$, $\Delta E$ und $\Delta N$ markiert dabei die Grenzen, innerhalb derer Bildung wirksam bleibt. Der Bildungswirkfaktor ist eine spezialisierte Form des allgemeinen [[Wirkfaktor]], da er gezielt die dynamischen Prozesse innerhalb eines Bildungskontextes abbildet und die resultierende [[Allgemein beruflich/Research/Bildungswissenschaft/Wirkung]] im System beschreibt.

# Quelle(n)

- Angulo, R. E., & Palacios, D. H. (2024). *Negative Wahrscheinlichkeiten und ihre Anwendung in biologischen und sozialen Systemen*. Springer.
- Arnold, R. (2014). *Systemische Pädagogik: Grundlagen und Anwendungen*. Schneider Verlag Hohengehren.
- Luhmann, N. (1997). *Die Gesellschaft der Gesellschaft*. Suhrkamp.
- Roediger, E. (2015). *Schematherapie: Ein praxisorientiertes Handbuch*. Beltz.
- Wittchen, H.-U., & Hoyer, J. (2011). *Handbuch der Verhaltenstherapie*. Springer.
- Hattie, J. (2024). *Visible learning 2.0* (S. Wernke & K. Zierer, Übers.). Schneider Verlag Hohengehren GmbH.
- Young, J. E., & Roediger, E. (2011). *Schematherapie: Ein praxisorientiertes Handbuch*. Junfermann.
