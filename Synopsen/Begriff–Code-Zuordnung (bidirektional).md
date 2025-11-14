
# 1. Von Begriffen zu Codes

## [[Elementaroperationen]]
**Beschreibung:**  
Grundlegende rekursive Operationen eines Systems: $Feedback$, $Reflexion$, $Re\text{-}Entry$.

**Verwendet in:**  
- Simulation der Systemdynamik entlang der Zeitachsen:
  - $feedback = 5 + 2 \cdot \sin(...) + \text{noise}$
  - $reflection = 5 + 2 \cdot \cos(...) + \text{noise}$
  - $re\_entry[i] = \alpha \cdot re\_entry[i - 1] + \ldots$

---

## [[Elementarraum]]

**Beschreibung:**  
Ontologischer Möglichkeitsraum, in dem sich rekursive Systemdynamiken auf Basis der [[Elementaroperationen]] entfalten.

**Verwendet in:**  
- 3D-Trajektorien mit Plotly: $f(t)$, $r(t)$, $e(t)$  
- Volumenberechnung durch Konvexhülle: $V_{\text{auto}} = \text{ConvexHull}(f, r, e)$  
- Darstellung der dynamischen Raumstruktur ohne epistemische Bewertung

---

## [[Systemintelligenz]]
**Beschreibung:**  
Emergente Strukturleistung eines Systems – sichtbar als temporär kohärente Dynamik in einem rekursiven Raum.

**Verwendet in:**  
- Berechnung als Produkt normierter Achsen:  
  $$V(t) = \hat{f}(t) \cdot \hat{r}(t) \cdot \hat{e}(t)$$  
- Visualisierung als Farbcodierung entlang der Zeitachse

---

## [[Systemische Stabilitätsfunktion]]
**Beschreibung:**  
Formale Messung der strukturellen Kohärenz eines Systems durch Vergleich mit einer normierten Fibonacci-Folge.

**Verwendet in:**  
- Stabilitätsprüfung:  
  $$S(c) = \max \left\{ n \in \mathbb{N} \mid \operatorname{corr}(|V_k|, \hat{F}_k) \geq \tau \right\}$$  
- Visualisierung des Stabilitätsverlaufs $S_n(c)$ als Farbverlauf in der Trajektorie

---

## [[Interdependenzoperator]]
**Beschreibung:**  
Mathematischer Operator $H$, der $Feedback$, $Reflexion$ und $Re\text{-}Entry$ zu einer strukturellen Einheit verknüpft.

**Verwendet in:**  
- Konzeptionelle Grundlage für $V(t)$ und $S(c)$  
- Formalisiert die wechselseitige Bedingtheit aller drei [[Elementaroperationen]]

---

# 2. Von Codes zu Begriffen

## Simulation rekursiver Achsen

Verwendeter Code:
- $feedback = 5 + 2 \cdot \sin(...) + \text{noise}$
- $reflection = 5 + 2 \cdot \cos(...) + \text{noise}$
- $re\_entry[i] = \alpha \cdot re\_entry[i - 1] + \ldots$

**Verknüpfte Begriffe:**  
[[Elementaroperationen]], [[Elementarraum]], [[Interdependenzoperator]]

---

## Bildung der [[Systemintelligenz]]

Verwendeter Code:
- $$V(t) = \hat{f}(t) \cdot \hat{r}(t) \cdot \hat{e}(t)$$

**Verknüpfte Begriffe:**  
[[Systemintelligenz]], [[Elementaroperationen]], [[Interdependenzoperator]]

---

## Berechnung der [[Systemische Stabilitätsfunktion]]

Verwendeter Code:
- $corr = \operatorname{corr}(V_k, \hat{F}_k)$  
- Stabilitätsbedingung:  
  $$S(c) = \max \left\{ n \in \mathbb{N} \mid \operatorname{corr}(|V_k|, \hat{F}_k) \geq \tau \right\}$$

**Verknüpfte Begriffe:**  
[[Systemische Stabilitätsfunktion]], [[Systemintelligenz]], [[Elementarraum]]

---

## Visualisierung der Raumstruktur im [[Elementarraum]]

Verwendeter Code:
- Plotly 3D: $x = f(t)$, $y = r(t)$, $z = e(t)$  
- Einfärbung der Trajektorie durch Zeit oder $S_n(c)$

**Verknüpfte Begriffe:**  
[[Elementarraum]], [[Systemintelligenz]]

---

## Volumenberechnung als Maß für [[Autopoiese]]

Verwendeter Code:
- $V = \text{ConvexHull}(f, r, e)$

**Verknüpfte Begriffe:**  
[[Autopoiese]], [[Elementarraum]], [[Systemintelligenz]]

---

## Frequenzanalyse zur [[Entwicklungsdynamik]]

Verwendeter Code:
- Fourier-Transformationen:  
  $\text{FFT}(f(t))$, $\text{FFT}(r(t))$, $\text{FFT}(e(t))$

**Verknüpfte Begriffe:**  
[[Emergenz]], [[Entwicklungsdynamik]], [[Rhythmische Stabilität]]