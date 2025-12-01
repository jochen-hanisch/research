```python

import numpy as np

# Beispielhafte Definitionen (stark vereinfacht)
states = np.arange(7)  # NRS 4-10, Schmerz kontrolliert als Zustand 7
actions = np.array([0, 1, 2, 3])  # Esketamin, Fentanyl, Anpassen, Diagnostik
P = np.zeros((len(states), len(actions), len(states)))  # Übergangsmatrix
R = np.zeros((len(states), len(actions)))  # Belohnungsmatrix

# Beispielhafte Füllung von P und R mit fiktiven Daten

# Value Iteration
V = np.zeros(len(states))
gamma = 0.99
threshold = 0.01
while True:
    delta = 0
    for s in range(len(states)):
        v = V[s]
        V[s] = max(sum(P[s, a, s_prime] * (R[s, a] + gamma * V[s_prime]) for s_prime in range(len(states))) for a in actions)
        delta = max(delta, abs(v - V[s]))
    if delta < threshold:
        break

# Optimale Politik berechnen
policy = np.zeros(len(states), dtype=int)
for s in range(len(states)):
    policy[s] = np.argmax([sum(P[s, a, s_prime] * (R[s, a] + gamma * V[s_prime]) for s_prime in range(len(states))) for a in actions])

print("Optimale Politik:", policy)
```

