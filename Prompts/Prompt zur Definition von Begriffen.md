---
author: Jochen Hanisch-Johannsen
title: Prompt Begriffsbestimmung
Repository: 
created: 2024-10-29
updated: []
publish: false
tags: []
published: 
project: []
type:
  - Prompt-Notiz
---
# 1 Beschreibung des Prompts

Dieser Prompt ist darauf ausgelegt, eine detaillierte, wissenschaftlich fundierte Definition und Beschreibung eines spezifischen Begriffs zu generieren. Er soll relevante wissenschaftliche Quellen durchsehen und die Informationen gezielt extrahieren, analysieren und in strukturierter Form darstellen. Ziel ist es, präzise Definitionen und Kontexte für den Begriff anzubieten, die sich in wissenschaftliche Arbeiten integrieren lassen.

# 2 Prompt-Formulierung

> "Bitte analysiere und definiere den Begriff **[Begriff]** umfassend. Suche nach relevanten wissenschaftlichen Quellen, die den Begriff beschreiben, und erläutere den Begriff im Kontext dieser Literatur. Achte darauf, alle verwendeten Quellen mit korrekter Zitation aufzuführen. Strukturierte die Antwort in einer hierarchischen Überschriftenstruktur und gebe die Ausgabe in **Obsidian Markdown** wieder. Verwende korrekte Markdown-Formatierung für alle Überschriften und Unterpunkte."

# 3 Parameter & Anpassungen

- **Modelleingabe**: GPT-4
- **Parameter**:
  - Temperatur: 0.3 (für eine präzisere und sachliche Antwort)
  - Länge: Max. 750 Tokens
  - Frequenzbestrafung: 0.4 (um Redundanzen zu vermeiden)
- **Sprache**: Deutsch
- **Besondere Anweisungen**: Strukturierung der Antwort in Absätzen und Überschriften (Obsidian-kompatibel), klare Definition und Beispiele für den Begriff, Zitation wissenschaftlicher Literatur, keine Umgangssprache.

# 4 Beispiele & Ergebnisse

## 4.1 Beispiel 1
- **Eingabe**: "Definiere den Begriff *Systemisches Lernen* und nenne relevante Literatur."  
- **Ausgabe**: 
  - "## Systemisches Lernen  
    Systemisches Lernen beschreibt eine ganzheitliche Lernmethode, die Beziehungen und Wechselwirkungen innerhalb eines Systems berücksichtigt (vgl. Luhmann, 2000). Es wird häufig in der Erwachsenenbildung und bei der Arbeit mit High Responsibility Teams angewendet..."

## 4.2 Beispiel 2
- **Eingabe**: "Erläutere den Begriff *Autopoiesis* und zitiere wissenschaftliche Quellen."  
- **Ausgabe**:
  - "## Autopoiesis  
    Der Begriff 'Autopoiesis' beschreibt die Selbsterschaffung und -erhaltung lebender Systeme durch eigene Prozesse und Strukturen (Maturana & Varela, 1972)..."

# 5 Anwendungsbereiche & Limitationen

- **Anwendungsbereiche**: Wissenschaftliche Definitionen, Begriffsanalysen für akademische Arbeiten, Begriffsklärungen in Bildung, Beratung und Gesundheitswesen.
- **Limitationen**: Bei sehr komplexen, interdisziplinären Begriffen ist möglicherweise eine engere Eingrenzung des Kontextes nötig. Wenn spezifische, selten zitierte Fachliteratur notwendig ist, kann die Datenverfügbarkeit eingeschränkt sein.

# 6 Weiterführende Anpassungen

- Mögliche Erweiterung: Hinzufügen von spezifischen Unterthemen, die beim Begriff von Interesse sind (z.B. historische Entwicklung, Anwendungsbereiche, Diskussion relevanter Kontroversen).
- Weitere Beispiele: Ergänzen zusätzlicher akademischer Anwendungsbeispiele.
- Tieferes Quellenverzeichnis: Verzeichnis ergänzender Literatur hinzufügen, die dem Begriff Relevanz verleiht.

# 7 Fazit

**Stärken**: Geeignet für präzise, akademische Begriffsdefinitionen und fördert eine strukturierte Erläuterung mit wissenschaftlicher Zitation.  
**Schwächen**: Höhere Abstraktion und enge Kontexte erfordern engere Anweisungen, um alle relevanten Aspekte des Begriffs abzudecken.