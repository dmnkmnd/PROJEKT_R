import louvain as viz, sys, json
GRAF = viz.unos(json.loads(sys.argv[1]))
viz.draw_graph(GRAF, title="Initial Graph", brSlika=1)
viz.louvain_algorithm_steps(GRAF)