# 🧭 Systemische Beobachtung: z.B. Notfallteam

## 🧩 Teamstruktur (normiert auf Skala 0–1)

| Dimension                     | Beschreibung                                                                 | Wert |
|------------------------------|------------------------------------------------------------------------------|------|
| **Strukturelle Kopplung (x)** | Klarheit und Verbindlichkeit der Rollenverteilung im Team                   |      |
| **Kommunikationsdichte (y)** | Interaktionshäufigkeit und -intensität (z. B. pro Minute, verbal/nonverbal) |      |
| **Entwicklungspotenzial (z)**| Offenheit für Lernen, Reflexion und situative Weiterentwicklung              |      |

---

## 👥 Einzelperspektiven (optional)

| Teammitglied | Rollenklärung x | Interaktion y | Entwicklung z |
|--------------|------------------|----------------|----------------|
| A            |                  |                |                |
| B            |                  |                |                |
| C            |                  |                |                |

---

## 🧠 Beobachtungsnotizen

### ✴ Auffällige Dynamiken oder Muster
- …

### ⚖ Stabilitäts- oder Destabilisierungsphasen
- …

### 🔄 Emergenz-Phänomene (Selbstorganisation, plötzliche Umstrukturierung o. Ä.)
- …

---

## 🧮 Datenexport (für Modellinput)

```python
x = np.array([/* x-Werte */])
y = np.array([/* y-Werte */])
z = np.array([/* z-Werte */])
```
## 📌 Quelle / Kontext

- **📍 Einsatz / Simulation**: `___________________________`
- **📅 Datum / Uhrzeit**: `___________________________`
- **🧑‍💼 Beobachter/in**: `___________________________`
- **📝 Methode**: `Beobachtung / Interview / Nachbesprechung / Logdaten`

## 📊 Datenerhebung

### 🎯 Ziel der Erhebung
Erfassung systemisch relevanter Zustände in einem Notfallteam zur Modellierung von:
- struktureller Kopplung \( x \)
- Kommunikationsdichte \( y \)
- Entwicklungspotenzial \( z \)

### 🧾 Erhebungsart
- [ ] Strukturierte Beobachtung
- [ ] Interviewbasierte Selbsteinschätzung
- [ ] Fremdeinschätzung durch Beobachter/in
- [ ] Logdaten / Sensorsysteme
- [ ] Kombination / Mixed Methods

### 🔁 Erhebungszeitpunkte
- [ ] einmalig (z. B. retrospektiv)
- [ ] mehrfach (z. B. Einsatzphasen, Schichten)
- [ ] kontinuierlich (Monitoring)

### 👥 Beobachtungseinheiten
- [ ] Teamaggregat (1 Datensatz für das gesamte Team)
- [ ] Pro Teammitglied (individuelle Einschätzungen)
- [ ] Pro Phase / Ereignisabschnitt

### 📐 Skalierung der Variablen
Alle Skalen werden **im Feld auf einer Skala von 0 bis 10 erhoben**  
→ **Im Modell werden die Werte durch `10` geteilt**, um eine Normierung auf \([0.0 – 1.0]\) zu erreichen.

| Variable | Beschreibung | Skala im Feld | Modellwert |
|----------|--------------|----------------|-------------|
| \( x \)  | Strukturelle Kopplung (Formalisierung, Rollenklarheit) | 0–10 | \( x_{\text{norm}} = x/10 \) |
| \( y \)  | Kommunikationsdichte (Häufigkeit, Fluss, Redundanz) | 0–10 | \( y_{\text{norm}} = y/10 \) |
| \( z \)  | Entwicklungspotenzial (Lern-, Reflexions- oder Anpassungsfähigkeit) | 0–10 | \( z_{\text{norm}} = z/10 \) |

---

> 🧠 **Hinweis**: Diese Anpassung erlaubt eine intuitivere Einschätzung im Feld (z. B. durch Skalenanker), während das Modell weiterhin auf normierten Werten basiert.

