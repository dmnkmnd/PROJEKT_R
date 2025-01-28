import networkx as nx;

def procitaj_graf(g):
    GRAF = nx.DiGraph()
    for node, neighbors in g.items():
        for neighbor in neighbors:
            GRAF.add_edge(node, neighbor)
    for i in GRAF.nodes:
        GRAF.nodes[i]["description"] = '∞'
    return GRAF