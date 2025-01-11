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

def draw_graph(G, node_scores=None, title="Graph Visualization", pos=None):
    """Draw the graph with optional node coloring based on scores."""
    plt.figure(figsize=(8, 6))
    pos = pos or nx.spring_layout(G, seed=42)

    if node_scores:
        scores = [node_scores[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=scores, cmap=plt.cm.Blues, node_size=500, font_size=10, font_weight="bold")
        sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(scores), vmax=max(scores)))
        sm.set_array([])
        plt.colorbar(sm, label="PageRank", ax=plt.gca())
    else:
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_weight="bold")

    plt.title(title)
    plt.show()

def visualize_pagerank_steps(G, alpha=0.85, max_iter=100, tol=1.0e-6, step_interval=5):
    """Visualize the iterative steps of the PageRank algorithm with reduced visualizations."""
    pos = nx.spring_layout(G, seed=42)
    scores = {node: 1 / G.number_of_nodes() for node in G.nodes()}  # Initialize scores

    for iteration in range(max_iter):
        new_scores = {node: (1 - alpha) / G.number_of_nodes() for node in G.nodes()}
        for node in G:
            for neighbor in G[node]:
                new_scores[neighbor] += alpha * (scores[node] / G.out_degree(node, weight=None))

        # Convergence check
        diff = sum(abs(new_scores[n] - scores[n]) for n in G.nodes())
        scores = new_scores

        # Visualize every `step_interval` steps
        if iteration % step_interval == 0 or diff < tol:
            draw_graph(G, node_scores=scores, title=f"PageRank Step {iteration + 1}", pos=pos)

        if diff < tol:
            print(f"Converged after {iteration + 1} iterations.")
            break

def calculate_and_visualize_pagerank(G):
    """Calculate PageRank and visualize the graph with scores."""
    pagerank_scores = nx.pagerank(G)
    print("PageRank Scores:")
    for node, score in pagerank_scores.items():
        print(f"{node}: {score:.4f}")

    draw_graph(G, node_scores=pagerank_scores, title="PageRank Visualization")

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

