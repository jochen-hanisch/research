
1. **Beschreibung des Stimulus**  
    Dieser Bildschirm zeigt eine Filter‑ und Kachelübersicht, mit der Lernende Inhalte nach Status (“H‑RS‑xx”) und weiteren Tags (nfs, pal, bz, rh, rs, emb, h‑nfs) auswählen können. Oben befindet sich ein Freitext‑Suchfeld „Nach Titel filtern…“ sowie darunter Tag‑Buttons; „h‑rs“ ist aktiv markiert. Darunter werden zwölf Inhaltselemente als Kacheln dargestellt – jeweils ein Vorschaubild, Titel („Status 9: zur freien Verfügung“, „Status 1: einsatzbereit über Funk“ etc.) und Tag‑Icons. Aufgabe im LMS: Nutzer:innen können gezielt Module aus ihrem Lernpfad herausfiltern und so ihren Plan personalisieren.
    
2. **Analyse der Heatmap**
    
    - **Hotspots**
        
        - Suchfeld „Nach Titel filtern…“ (oben links)
            
        - Der rote Tag‑Button „h‑rs“
            
        - Erste Kachel (Status 9) mit kontrastreichem Vorschaubild
            
        - Die Titel der ersten drei Kacheln
            
    - **Unterrepräsentierte Zonen**
        
        - Andere Tag‑Buttons (nfs, pal, bz, rh, rs, emb, h‑nfs)
            
        - Untere Kacheln (Status 8 und 0)
            
        - Tag‑Icons unterhalb der Kacheltitel
            
        - Weißraum zwischen Suchfeld und Kacheln
            
    - **Erste Hypothesen**  
        Intensive Farben (Rot des aktiven Tags, knallige Vorschaubilder) fungieren als starke Aufmerksamkeitsanker. Periphere Tags und weiter unten positionierte Karten werden kaum beachtet.
        
3. **Analyse der Viewmap**
    
    - **Dominante Blickpfade**
        
        1. Einstieg im Suchfeld, kurzer Return zum Tag‑Bereich
            
        2. Fixation auf den aktiven „h‑rs“-Tag
            
        3. Horizontale Line‑Scan der ersten Kachelreihe (Status 9 → 1 → 2 → 3)
            
        4. Abstieg zur zweiten Reihe mit kurzer Inspektion von Status 4 und 5
            
        5. Abschließend kaum Blick auf die unterste Reihe (Status 8 und 0)
            
    - **Orientierungsmuster**  
        Linear‑explorativ: Top‑Down‑Scannen der UI‑Controls, dann sequentielles Abarbeiten der Kacheln.
        
    - **Kognitive Interpretation**  
        Nutzer:innen verifizieren zuerst den Filterkontext (aktiver Tag), prüfen dann die prominentesten Angebote (oberste, farbkräftige Vorschaubilder) und selektieren daraus ihre nächste Lerneinheit.
        
4. **Analyse der Fog‑View**
    
    - **Systematisch nicht wahrgenommene Bereiche**
        
        - Filter‑Tags außer „h‑rs“
            
        - Tag‑Icons unterhalb der Kacheltitel
            
        - Untere Kacheln (Status 6, 7, 8, 0)
            
        - Leerraum und UI‑Trennlinien
            
    - **Mögliche Ursachen**
        
        - Gleichförmige, wenig kontrastierte Gestaltung sekundärer Tags und Icons
            
        - Kacheln in weiter unten liegenden Reihen außerhalb des primären Sichtfensters
            
        - Weißraum unterbricht den visuellen Fluss und lässt Interaktionsmöglichkeiten „verschwinden“
            
    - **Hypothesen**  
        Lernende fokussieren nur die top‑positionierten, farbintensiven Elemente und übersehen alternative Personalisierungsoptionen.
        
5. **Ableitung technisch‑gestalterischer Wirkmechanismen**
    
    - **Farb‑ und Kontraststeuerung**  
        Der aktive rote Tag‑Button und farbintensive Vorschaubilder ziehen den Blick stark an (Gestaltprinzip Figur‑Grund).
        
    - **Taxonomische Filter‑Icons**  
        Rund gestaltete Tag‑Buttons signalisieren Gruppierung, allerdings fehlt eine gleiche Betonung für alle Tags, was deren Nutzung limitiert.
        
    - **Kachel‑Grid‑Layout**  
        Klare Rasterstruktur erleichtert das sequentielle Scanning, erzeugt aber eine Hierarchie nach Position (oben > unten).
        
    - **Proximity und Weißraum**  
        Zu großer Abstand zwischen Filter‑Controls und Kacheln schwächt die wahrgenommene Verbindung von Filter und Ergebnissen.
        
6. **Zuordnung zur Forschungsunterfrage FU4b**  
    Die Taxonomie‑Filter und Grid‑Darstellung steuern systemisch‑konstruktivistisch das Personalisierungsverhalten: durch Farb‑ und Positionshierarchien wird festgelegt, welche Lerninhalte als relevant erscheinen. Nutzende bleiben bei den prominent bei Filter „h‑rs“ gruppierten und top‑gezeigten Kacheln, während weniger hervorgehobene Module unentdeckt bleiben. Damit beeinflusst die technische Gestaltung direkt, wie Gesundheitsberufe ihre Lernpfade selektiv anpassen und welche Inhalte sie vertiefen.
    
7. **Fazit**  
    Die Kombination aus aktivem Tag‑Button und farbintensiven Vorschaubildern bietet schnelle Personalisierungsanker. Gleichzeitig gehen sekundäre Tags und weiter unten positionierte Inhalte verloren. Zur Optimierung empfehle ich:
    
    - Einheitliche Kontrastverstärkung aller Tag‑Buttons, ggf. Hover‑Effekte
        
    - Reduzierung des Weißraums zwischen Filter und Grid, um inhaltliche Verbindung sichtbarer zu machen
        
    - Alternative Layout-Varianten (z. B. Lazy‑Load oder Paginierung) für untere Kacheln
        
    - Visuelle Gruppierungen (Rahmen, Schatten) für alle Filter‑Resultate, um eine gleichmäßige Aufmerksamkeit zu gewährleisten und individuelle Lernbedürfnisse systemisch‑konstruktivistisch umfassend zu unterstützen.