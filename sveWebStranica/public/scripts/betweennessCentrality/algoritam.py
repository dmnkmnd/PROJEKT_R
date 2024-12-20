import vizualizacija as viz, networkx as nx, sys

def betw_cen_alg(GRAF):
    brSlika = 1
    betwCvorovi = nx.betweenness_centrality(GRAF, normalized=True)
    viz.vizualizirajGraf(GRAF, betwCvorovi, brSlika)