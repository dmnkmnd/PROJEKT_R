import vizualizacija as viz, networkx as nx
from networkx.algorithms.community import girvan_newman

maxBridovi = []

def brid_za_uklanjanje(GRAF, povezaniPodgrafovi):
    maxVr = -1
    maxBrid = 0
    bridoviBC = nx.edge_betweenness_centrality(GRAF)
    for key, value in bridoviBC.items():
        if(value > maxVr):
            maxVr = value
            maxBrid = key
    maxBridovi.append(maxBrid)
    return maxBrid

def girvan_newman_alg(GRAF, brojZajednica, preskok):
    brSlika = 1
    viz.vizualizirajPocetniGraf(GRAF, brSlika)
    brSlika += 1
    povezaniPodgrafovi = [GRAF.subgraph(c).copy() for c in nx.strongly_connected_components(GRAF)]
    k = 1
    l = len(povezaniPodgrafovi)
    if(l > k):
        if(l % preskok == 0):
            viz.vizualizirajGraf(GRAF, povezaniPodgrafovi, maxBridovi, l, preskok, 0, brSlika)
            brSlika += 1
            maxBridovi.clear()
        k = l
    while(l < brojZajednica):
        GRAF.remove_edge(*brid_za_uklanjanje(GRAF, povezaniPodgrafovi))
        povezaniPodgrafovi = [GRAF.subgraph(c).copy() for c in nx.strongly_connected_components(GRAF)]
        l = len(povezaniPodgrafovi)
        if(l > k):
            if(l % preskok == 0):
                jeZadnji = l == brojZajednica
                viz.vizualizirajGraf(GRAF, povezaniPodgrafovi, maxBridovi, l, preskok, jeZadnji, brSlika)
                brSlika += 1
                maxBridovi.clear()
            k = l
    if(l % preskok != 0):
        viz.vizualizirajGraf(GRAF, povezaniPodgrafovi, maxBridovi, l, preskok, True, brSlika)
        brSlika += 1
        maxBridovi.clear()
    viz.vizualizirajZavrsniGraf(GRAF, povezaniPodgrafovi, brSlika)
    return