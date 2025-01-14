import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain

def unos(g):
    GRAF = nx.DiGraph()
    for node, neighbors in g.items():
        for neighbor in neighbors:
            GRAF.add_edge(node, neighbor)
    return GRAF

def draw_graph(G, communities=None, title="Graph Visualization", pos=None, brSlika=0):
    """Draw the graph with optional community coloring."""
    plt.figure(figsize=(8, 6))
    pos = pos or nx.spring_layout(G, seed=42)
    
    if communities:
        colors = [communities[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.Set3, node_size=500, font_size=10, font_weight="bold")
    else:
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_weight="bold")
    
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()

def louvain_algorithm_steps(G):
    """Apply Louvain algorithm step by step and visualize each step."""
    pos = nx.spring_layout(G, seed=42)

    # Step 1: Initial partitioning (each node is its own community)
    initial_partition = {node: i for i, node in enumerate(G.nodes())}
    draw_graph(G, initial_partition, title="Initial Partition: Each Node in Its Own Community", pos=pos, brSlika=2)

    # Louvain Method: Optimize modularity
    partition = community_louvain.best_partition(G.to_undirected(), resolution=1.0)
    draw_graph(G, partition, title="Initial Louvain Partition", pos=pos, brSlika=3)

    modularity = community_louvain.modularity(partition, G.to_undirected())
    print(f"Initial modularity: {modularity:.4f}")

    # Iterate and refine
    for i in range(1, 4):  # Simulating multiple steps
        partition = community_louvain.best_partition(G.to_undirected(), resolution=1.0)
        modularity = community_louvain.modularity(partition, G.to_undirected())
        print(f"Step {i} modularity: {modularity:.4f}")
        draw_graph(G, partition, title=f"Step {i}: Louvain Partition", pos=pos, brSlika=(2+i))

    print("Final partition:", partition)
    return partition