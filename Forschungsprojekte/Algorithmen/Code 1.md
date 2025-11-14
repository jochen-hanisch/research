```python

import numpy as np

# Anzahl der Zustände
n_states = 21  # 20 Anweisungen + 1 Endzustand
n_actions = 3  # Ausführen, Überspringen, Test beenden

# Übergangswahrscheinlichkeiten
P = np.zeros((n_states, n_actions, n_states))
# Belohnungsfunktion
R = np.zeros((n_states, n_actions))

# Beispielfüllung der Matrizen P und R
for s in range(n_states - 1):
    P[s, 0, s + 1] = 1  # Aktion ausführen führt zum nächsten Zustand
    P[s, 1, s + 1] = 1  # Zum nächsten Zustand übergehen
    P[s, 2, n_states - 1] = 1  # Test beenden führt zum Endzustand
    R[s, 0] = 1  # Belohnung für das Ausführen einer Aktion
    R[s, 1] = -1  # Kosten für das Überspringen
    R[s, 2] = -10  # Hohe Kosten für das vorzeitige Beenden

# Implementierung der Value Iteration
V = np.zeros(n_states)
gamma = 0.95  # Diskontierungsfaktor
threshold = 1e-4  # Konvergenzschwelle
while True:
    V_prev = V.copy()
    for s in range(n_states):
        V[s] = max([sum(P[s, a, s_prime] * (R[s, a] + gamma * V_prev[s_prime])
                        for s_prime in range(n_states)) for a in range(n_actions)])
    if np.max(np.abs(V - V_prev)) < threshold:
        break

# Ausgabe der optimalen Politik
policy = np.zeros(n_states, dtype=int)
for s in range(n_states):
    policy[s] = np.argmax([sum(P[s, a, s_prime] * (R[s, a] + gamma * V[s_prime])
                               for s_prime in range(n_states)) for a in range(n_actions)])

print("Optimale Politik:", policy)
```
