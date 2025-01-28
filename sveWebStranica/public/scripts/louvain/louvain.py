import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain
import numpy as np

def unos(g):
    GRAF = nx.DiGraph()
    for node, neighbors in g.items():
        for neighbor in neighbors:
            GRAF.add_edge(node, neighbor)
    return GRAF

def draw_graph(G, communities=None, title="Graph Visualization", pos=None, brSlika=0, korak=0):
    """Draw the graph with optional community coloring."""
    plt.figure(figsize=((2 + len(G)//10)*5, (2.2 + len(G)//10)*3))
    pos = pos or nx.spring_layout(G, seed=42, k=0.15 / np.sqrt(len(G)))
    
     # Dodaj oznaku trenutnog koraka
    plt.title(f"{title}\nKorak: {korak}", fontsize=14)
    

    if communities:
        colors = [communities[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.Set3, node_size=500, font_size=10, font_weight="bold")
    else:
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_weight="bold")
    
    # Sačuvaj sliku
    plt.savefig(f'public/slike/slika{brSlika}.png')
    plt.close()

def louvain_algorithm_steps(G):
    """Apply Louvain algorithm step by step and visualize each step."""
    pos = nx.spring_layout(G, seed=42)

    # 1. korak: Svaki je čvor svoja zajednica
    initial_partition = {node: i for i, node in enumerate(G.nodes())}
    draw_graph(G, initial_partition, title="Prva podjela: svaki čvor je svoja zajednica", pos=pos, brSlika=1, korak=1)

    # Louvain Metoda: Optimiziranje modularnosti
    partition = community_louvain.best_partition(G.to_undirected(), resolution=1.0)
    draw_graph(G, partition, title="Početna Louvain particija", pos=pos, brSlika=2, korak=2)

    modularity = community_louvain.modularity(partition, G.to_undirected())
    print(f"Initial modularity: {modularity:.4f}")

    # Iterate and refine
    for i in range(3):  # Simulating multiple steps
        partition = community_louvain.best_partition(G.to_undirected(), resolution=1.0)
        modularity = community_louvain.modularity(partition, G.to_undirected())
        print(f"Step {i+3} modularity: {modularity:.4f}")
        draw_graph(G, partition, title=f"modularnost: {modularity:.4f}", pos=pos, brSlika=(3+i), korak=(3+i))

    print("Final partition:", partition)
    return partition
