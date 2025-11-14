```python
import matplotlib.pyplot as plt
import networkx as nx

def draw_colored_mdp_t1():
    # Erstelle einen gerichteten Graphen für Test T1
    G = nx.DiGraph()

    # Zustände und Aktionen hinzufügen
    states = range(1, 22)  # Zustände 1 bis 21 (20 Anweisungen + 1 Endzustand)
    
    # Übergänge hinzufügen (vereinfacht für das Beispiel)
    for s in states[:-1]:
        G.add_edge(s, s+1, action="Aktion ausführen", color='black')
        if s == 20:  # Spezifisch für Test T1, wo Anweisung 20 zu einer zyklischen Schleife führen kann
            G.add_edge(s, 1, action="Zyklus starten", color='red')  # Zyklischer Übergang farblich hervorheben
        G.add_edge(s, 21, action="Test beenden", color='black')

    # Endzustand ohne ausgehende Übergänge
    pos = nx.spring_layout(G, seed=42)  # Layout für die Knoten

    # Knoten und Kanten zeichnen
    edges = G.edges(data=True)
    colors = [data['color'] for _, _, data in edges]
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=9, font_weight='bold', edge_color=colors)
    edge_labels = {(u, v): d['action'] for u, v, d in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Plot anzeigen
    plt.title("MDP-Übergangsdiagramm für Test T1 mit farblichem Highlight")
    plt.show()

# Rufe die Funktion auf, um das Diagramm zu zeichnen
draw_colored_mdp_t1()
```
