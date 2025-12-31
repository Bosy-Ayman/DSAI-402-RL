import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

transition = [
    [0.25, 0.35, 0.4, 0],
    [0.55, 0, 0, 0.45],
    [0, 0.20, 0.60, 0.2],
    [0.30, 0.30, 0.2, 0.2],
]

G = nx.MultiDiGraph()
G.add_nodes_from([1, 2, 3, 4])
for idx_out in range(len(transition)):
    for idx_to in range(len(transition[idx_out])):
        G.add_edge(idx_out + 1, idx_to + 1, weight=transition[idx_out][idx_out])

fig, ax = plt.subplots(figsize=(17, 10))


pos = nx.spring_layout(G, seed=42)  # layout for visualization
print(pos)
# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color="lightblue")
nx.draw_networkx_labels(
    G,
    pos,
    font_size=12,
    font_weight="bold",
)


# Draw edges
edges = [e for e in G.edges(data=True) if e[2]["weight"] > 0]
nx.draw_networkx_edges(
    G, pos, arrowstyle="-|>", arrowsize=20, edge_color="gray", edgelist=edges
)

# Draw edge labels (probabilities)
edge_labels = {(u, v): f"{d['weight']*100:.0f}%" for u, v, d in edges}
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=10,
    # bbox=dict(alpha=0.5),
)

plt.title("Cities Question")
plt.savefig("nodes.jpg")
print("Graph is saved as image nodes.jpg")

transition = np.array(transition)
numberOfTransitions = 3
for i in range(numberOfTransitions):
    transition = transition @ transition

print(f"after {numberOfTransitions} Transitions")
idx = 1
for i in transition:
    print(f"{idx} &", end=" ")
    for j in i:
        print(f"{j*100:.5f}", end=" & ")
    print("\\\\")
    idx += 1
