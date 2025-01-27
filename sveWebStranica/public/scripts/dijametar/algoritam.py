import vizualizacija as viz, networkx as nx, sys

def dijametar_alg(GRAF):
    strogoPovezani = 1
    dijametar = 0

    if nx.is_strongly_connected(GRAF):
        strogoPovezani = 1
        dijametar = nx.diameter(GRAF)
        putevi = []
        sviParoviPuteva = dict(nx.all_pairs_shortest_path_length(GRAF))
        for u, udaljenosti in sviParoviPuteva.items():
            for v, udaljenost in udaljenosti.items():
                if udaljenost == dijametar:
                    sviPutevi = list(nx.all_shortest_paths(GRAF, source=u, target=v))
                    for put in sviPutevi:
                        if len(put) - 1 == dijametar:
                            putevi.append(put)
    else:
        strogoPovezani = 0
        najvecaSPKomponenta = max(nx.strongly_connected_components(GRAF), key=len)
        podgraf = GRAF.subgraph(najvecaSPKomponenta)
        dijametar = nx.diameter(podgraf)
        putevi = []
        sviParoviPuteva = dict(nx.all_pairs_shortest_path_length(podgraf))
        for u, udaljenosti in sviParoviPuteva.items():
            for v, udaljenost in udaljenosti.items():
                if udaljenost == dijametar:
                    sviPutevi = list(nx.all_shortest_paths(podgraf, source=u, target=v))
                    for put in sviPutevi:
                        if len(put) - 1 == dijametar:
                            putevi.append(put)

    viz.vizualizirajGraf(GRAF, putevi, dijametar)

    return strogoPovezani