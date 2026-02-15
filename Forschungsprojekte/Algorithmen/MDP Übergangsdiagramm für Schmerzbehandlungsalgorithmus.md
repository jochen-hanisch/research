![[file-MWdZuFXMl6lx567pMMh5RtTy]]


## Python-Code

```python
import matplotlib.pyplot as plt
import networkx as nx

# Define the Markov Decision Process (MDP) states and transitions
states = [
    "Schmerzevaluation",
    "Medikationsentscheidung Esketamin",
    "Medikationsentscheidung Fentanyl",
    "Weitere Diagnostik",
    "Reevaluation",
    "Ende"
]

edges = [
    ("Schmerzevaluation", "Medikationsentscheidung Esketamin"),
    ("Schmerzevaluation", "Ende"),
    ("Medikationsentscheidung Esketamin", "Reevaluation"),
    ("Medikationsentscheidung Fentanyl", "Reevaluation"),
    ("Reevaluation", "Medikationsentscheidung Esketamin"),
    ("Reevaluation", "Medikationsentscheidung Fentanyl"),
    ("Reevaluation", "Weitere Diagnostik"),
    ("Reevaluation", "Ende"),
    ("Weitere Diagnostik", "Reevaluation")
]

# Create directed graph
G = nx.DiGraph()
G.add_nodes_from(states)
G.add_edges_from(edges)

# Position nodes for better visualization
pos = {
    "Schmerzevaluation": (0, 1),
    "Medikationsentscheidung Esketamin": (-1, 0),
    "Medikationsentscheidung Fentanyl": (1, 0),
    "Weitere Diagnostik": (2, 0),
    "Reevaluation": (0, -1),
    "Ende": (0, -2)
}

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=4000, node_color='skyblue', font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
plt.title('MDP Übergangsdiagramm für Schmerzbehandlungsalgorithmus')
plt.show()
```
