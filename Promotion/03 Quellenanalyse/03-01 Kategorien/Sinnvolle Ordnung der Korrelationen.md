

Die Korrelationen sollten in einer logischen Reihenfolge angeordnet sein, die die Beziehungen zwischen den Variablen nach Relevanz, Komplexität oder Hierarchie strukturiert.

#### **Begründung der Ordnung**

1. Beginne mit einfachen Paarungen zwischen **Hauptvariablen**, um eine klare Grundlage zu schaffen (z. B. Suchbegriffe und Kategorien).
2. Steigere die Komplexität, indem **interne Korrelationen** (innerhalb einer Gruppe) und **übergreifende Beziehungen**betrachtet werden.
3. Platziere **intern-hierarchische Beziehungen** (z. B. Forschungsunterfragen und Indizes) nach der Analyse übergeordneter Konzepte.
4. Schließe mit internen Konsistenzen innerhalb einer Kategorie ab, um die Datenqualität und Redundanzen zu prüfen.

---

### Optimierte und geordnete Korrelationen

1. **Suchbegriffe → Kategorien**  
    Verknüpft Keywords mit Konzepten, um ihre Beziehung zu den Hauptkategorien zu analysieren. Dies ist der grundlegendste Vergleich.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, tags_to_search_processed, categories_processed,                                  'Korrelation zwischen Suchbegriffen und Kategorien',                                  'Suchbegriffe', 'Kategorien')`
    
2. **Forschungsunterfragen → Kategorien**  
    Zeigt, wie die Forschungsfragen mit den Kategorien zusammenhängen – ein direkter Bezug zur inhaltlichen Struktur.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, research_questions_processed, categories_processed,                                  'Korrelation zwischen Forschungsunterfragen und Kategorien',                                  'Forschungsunterfragen', 'Kategorien')`
    
3. **Forschungsunterfragen → Suchbegriffe**  
    Überprüft die semantische Verbindung zwischen spezifischen Forschungsfragen und Keywords.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, research_questions_processed, tags_to_search_processed,                                  'Korrelation zwischen Forschungsunterfragen und Suchbegriffen',                                  'Forschungsunterfragen', 'Suchbegriffe')`
    
4. **Indizes → Kategorien**  
    Verbindet Indizes (z. B. thematische Schwerpunkte oder numerische Skalen) mit Kategorien, um die Übereinstimmung zwischen analytischen Konzepten und theoretischen Gruppen zu untersuchen.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, index_terms_processed, categories_processed,                                  'Korrelation zwischen Indizes und Kategorien',                                  'Indizes', 'Kategorien')`
    
5. **Indizes → Suchbegriffe**  
    Untersucht, welche Keywords in spezifischen Indizes erscheinen und wie sie miteinander verknüpft sind.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, index_terms_processed, tags_to_search_processed,                                  'Korrelation zwischen Indizes und Suchbegriffen',                                  'Indizes', 'Suchbegriffe')`
    
6. **Forschungsunterfragen → Indizes**  
    Stellt dar, wie Forschungsfragen durch analytische Indizes gestützt werden können.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, research_questions_processed, index_terms_processed,                                  'Korrelation zwischen Forschungsunterfragen und Indizes',                                  'Forschungsunterfragen', 'Indizes')`
    
7. **Forschungsunterfragen → Forschungsunterfragen**  
    Überprüft die Kohärenz und Redundanz zwischen den Forschungsfragen.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, research_questions_processed, research_questions_processed,                                  'Korrelation zwischen Forschungsunterfragen',                                  'Forschungsunterfragen', 'Forschungsunterfragen')`
    
8. **Suchbegriffe → Suchbegriffe**  
    Identifiziert semantische Beziehungen oder mögliche Synonyme innerhalb der Keywords.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, tags_to_search_processed, tags_to_search_processed,                                  'Korrelation zwischen Suchbegriffen',                                  'Suchbegriffe', 'Suchbegriffe')`
    
9. **Kategorien → Kategorien**  
    Zeigt die Beziehungen oder Überschneidungen zwischen den theoretischen Kategorien.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, categories_processed, categories_processed,                                  'Korrelation zwischen Kategorien',                                  'Kategorien', 'Kategorien')`
    
10. **Indizes → Indizes**  
    Prüft, ob Indizes einander beeinflussen oder sich überschneiden.
    
    python
    
    Code kopieren
    
    `visualize_bivariate_correlation(df, index_terms_processed, index_terms_processed,                                  'Korrelation zwischen Indizes',                                  'Indizes', 'Indizes')`
    

---

### **Erklärung der Reihenfolge**

1. **Schritt 1-3:** Starte mit den direkten Beziehungen zwischen Keywords, Kategorien und Forschungsfragen, da sie die Hauptstruktur des Modells bilden.
2. **Schritt 4-6:** Analysiere, wie Indizes mit den bisherigen Variablen interagieren, um die analytischen Aspekte zu integrieren.
3. **Schritt 7-10:** Führe interne Analysen durch, um Konsistenz, Kohärenz und mögliche Redundanzen zu identifizieren.

Diese Reihenfolge ermöglicht eine klare Struktur, beginnend mit grundlegenden Verknüpfungen, gefolgt von komplexeren Beziehungen und abschließend internen Prüfungen.