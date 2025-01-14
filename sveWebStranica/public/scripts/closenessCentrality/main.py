import Closeness as viz, sys, json

GRAF = viz.unos(json.loads(sys.argv[1]))
viz.vizualiziraj_graf(GRAF)