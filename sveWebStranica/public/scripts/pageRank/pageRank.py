import networkx as nx
import matplotlib.pyplot as plt

def parse_input_from_file(file_path):
    """Parse input text from a file to create a directed graph."""
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            node, neighbors = line.strip().split(";")
            neighbors = neighbors.split(",") if neighbors else []
            for neighbor in neighbors:
                G.add_edge(node.strip(), neighbor.strip())
    return G

def unos(g):
    GRAF = nx.DiGraph()
    for node, neighbors in g.items():
        for neighbor in neighbors:
            GRAF.add_edge(node, neighbor)
    return GRAF

def draw_graph(G, node_scores=None, title="Graph Visualization", pos=None, brSlika=0):
    """Draw the graph with optional node coloring based on scores."""
    plt.figure(figsize=((2 + len(G) // 10) * 5, (2.2 + len(G) // 10) * 3))

    pos = pos or nx.spring_layout(G, seed=42)

    if node_scores:
        scores = [node_scores[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=scores, cmap=plt.cm.Blues, node_size=500, font_size=10, font_weight="bold")
        sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(scores), vmax=max(scores)))
        sm.set_array([])
        plt.colorbar(sm, label="PageRank", ax=plt.gca())
    else:
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_weight="bold")

    plt.title(title, fontsize=16)
    plt.savefig(f'public/slike/slika{brSlika}.png')
    plt.close()

def visualize_pagerank_steps(G, alpha=0.85, max_iter=100, tol=1.0e-6, step_interval=5, brSlika=0):
    """Visualize the iterative steps of the PageRank algorithm with reduced visualizations."""
    pos = nx.spring_layout(G, seed=42)
    scores = {node: 1 / G.number_of_nodes() for node in G.nodes()}  # Initialize scores

    step_titles = []  # To store titles for each step

    for iteration in range(max_iter):
        new_scores = {node: (1 - alpha) / G.number_of_nodes() for node in G.nodes()}
        for node in G:
            for neighbor in G[node]:
                new_scores[neighbor] += alpha * (scores[node] / G.out_degree(node, weight=None))

        # Check for convergence
        diff = sum(abs(new_scores[n] - scores[n]) for n in G.nodes())
        scores = new_scores

        # Add title logic for steps
        if iteration == 0:
            title = "POČETAK"
        elif diff < tol or iteration == max_iter - 1:
            title = "KRAJ"
        else:
            title = f"KORAK: {iteration + 1}"

        # Visualize and save graph
        if iteration % step_interval == 0 or diff < tol:
            draw_graph(G, node_scores=scores, title=title, pos=pos, brSlika=brSlika)
            brSlika += 1

        if diff < tol:
            print(f"Converged after {iteration + 1} iterations.")
            break

    return brSlika

def calculate_and_visualize_pagerank(G, brSlika=0):
    """Calculate PageRank and visualize the graph with scores."""
    pagerank_scores = nx.pagerank(G)
    print("PageRank Scores:")
    for node, score in pagerank_scores.items():
        print(f"{node}: {score:.4f}")

    draw_graph(G, node_scores=pagerank_scores, title="PageRank Visualization", brSlika=brSlika)

'''
if __name__ == "__main__":
    # File path for graph data
    file_path = "graph2.txt"

    # Parse input and create graph
    G = parse_input_from_file(file_path)

    # Visualize initial graph
    draw_graph(G, title="Initial Graph")

    # Visualize PageRank steps
    visualize_pagerank_steps(G, step_interval=5)

    # Calculate and visualize final PageRank
    calculate_and_visualize_pagerank(G)
'''