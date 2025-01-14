import pageRank as viz, sys, json
# Parse input and create graph
G = viz.unos(json.loads(sys.argv[1]))
koraci = int(sys.argv[2])
brSlika=1
# Visualize initial graph
viz.draw_graph(G, title="Initial Graph", brSlika=brSlika)
brSlika += 1
# Visualize PageRank steps
brSlika = viz.visualize_pagerank_steps(G, step_interval=koraci, brSlika=brSlika)
# Calculate and visualize final PageRank
viz.calculate_and_visualize_pagerank(G, brSlika=brSlika)