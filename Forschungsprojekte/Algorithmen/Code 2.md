```python

import matplotlib.pyplot as plt
import networkx as nx

def draw_mdp():
    # Erstelle einen gerichteten Graphen
    G = nx.DiGraph()

    # Zustände und Aktionen hinzufügen
    states = range(1, 22)  # Zustände 1 bis 21 (20 Anweisungen + 1 Endzustand)
    actions = ["Aktion ausführen", "Überspringen", "Test beenden"]
    
    # Übergänge hinzufügen (vereinfacht für das Beispiel)
    for s in states[:-1]:
        G.add_edge(s, s+1, action="Aktion ausführen")
        G.add_edge(s, 21, action="Test beenden")

    # Endzustand ohne ausgehende Übergänge
    pos = nx.spring_layout(G, seed=42)  # Layout für die Knoten

    # Knoten und Kanten zeichnen
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=9, font_weight='bold')
    edge_labels = {(u, v): d['action'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Plot anzeigen
    plt.title("MDP-Übergangsdiagramm für Test T2")
    plt.show()

draw_mdp()

```
