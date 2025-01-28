import matplotlib.pyplot as plt, networkx as nx, numpy as np, random, os

seed = 0

def vizualizirajGraf(GRAF, putevi, udaljenost):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    bridovi = GRAF.edges()
    brSlika = 1
    for i in putevi:
        putViz = [(i[j], i[j+1]) for j in range(len(i) - 1)]
        plt.figure(figsize=((2+len(GRAF)//10)*5,(2.2+len(GRAF)//10)*3)) 
        plt.title('put (' + str(brSlika) + ' / '  + str(len(putevi)) + '), udaljenost: ' + str(udaljenost), fontsize=16, pad=20)
        nx.draw(GRAF, pos, with_labels=True, node_color='grey', edge_color='red', node_size=500, font_size=15, font_color="black", edgelist=[])
        nx.draw_networkx_edges(GRAF, pos, edgelist=list(set(bridovi) - set(putViz)), edge_color='black', width=1.5)
        nx.draw_networkx_edges(GRAF, pos, edgelist=putViz, edge_color='orange', width=2.5)
        plt.savefig('public/slike/slika' + str(brSlika) + '.png')
        brSlika += 1
        plt.close()