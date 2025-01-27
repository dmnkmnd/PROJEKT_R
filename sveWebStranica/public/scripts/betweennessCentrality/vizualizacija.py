import matplotlib.pyplot as plt, networkx as nx, numpy as np, random, matplotlib.cm as cm

seed = 0

def vizualizirajGraf(GRAF, betwCvorovi, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    plt.figure(figsize=((2+len(GRAF)//10)*5,(2.2+len(GRAF)//10)*3))
    velicine_cvorova = [85 + 4500 * betwCvorovi[c] for c in GRAF.nodes()]
    norm = plt.Normalize(vmin=min(betwCvorovi.values()), vmax=max(betwCvorovi.values()))
    boje = [cm.Blues(norm(betwCvorovi[c])) for c in GRAF.nodes()]
    plt.title('BETWEENNESS CENTRALITY', fontsize=15)
    nx.draw(GRAF, pos, with_labels=True, node_color=boje, edge_color='black', edgecolors='black', node_size=velicine_cvorova, font_size=10, font_color="black")
    sm = plt.cm.ScalarMappable(cmap=cm.Blues, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, label="betweenness cenrality vrijednosti u čvoru")
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()