import matplotlib.pyplot as plt, networkx as nx, numpy as np, random, os
from vrh import Vrh

seed = 0
boje = ['green', 'orange', 'purple', 'pink', 'cyan', 'yellow', 'brown', 'magenta', 'lime', 'lightblue']

def vizualizirajPocetniGraf(GRAF, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    plt.figure(figsize=((2+len(GRAF)//10)*5,(2.2+len(GRAF)//10)*3)) 
    plt.title('POČETAK', fontsize=16, pad=20)
    nx.draw(GRAF, pos, with_labels=True, node_color='blue', edge_color='black', node_size=500, font_size=15, font_color="black")
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()


def vizualizirajZavrsniGraf(GRAF, vrhovi, B, udaljenost, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    if(udaljenost != -1):
        bridovi = GRAF.edges()
        najkraciPutevi = dobavi_najkrace_puteve(vrhovi, B)
        j = 0
        for i in najkraciPutevi:
            plt.figure(figsize=((2+len(GRAF)//10)*5,(2.2+len(GRAF)//10)*3))
            plt.title('KRAJ (put ' + str(j+1) + ' / '  + str(len(najkraciPutevi)) + '), udaljenost: ' + str(udaljenost), fontsize=16, pad=20)
            nx.draw(GRAF, pos, with_labels=True, node_color='grey', edge_color='red', node_size=500, font_size=15, font_color="black", edgelist=[])
            nx.draw_networkx_edges(GRAF, pos, edgelist=list(set(bridovi) - set(i)), edge_color='black', width=1.5)
            nx.draw_networkx_edges(GRAF, pos, edgelist=i, edge_color=boje[j % len(boje)], width=2.5)
            j += 1
            plt.savefig('public/slike/slika' + str(brSlika) + '.png')
            brSlika += 1
            plt.close()
    else:
        plt.figure(figsize=((2+len(GRAF)//10)*5,(2.2+len(GRAF)//10)*3)) 
        plt.title('KRAJ (nedostižan čvor)', fontsize=16, pad=20)
        zeleni = []
        for i in vrhovi:
            zeleni.append(i.naziv)
        nx.draw(GRAF, pos, with_labels=True, node_color='blue', edge_color='black', node_size=500, font_size=15, font_color="black")
        nx.draw_networkx_nodes(GRAF, pos, nodelist=zeleni, node_color='green', node_size=500)
        nx.draw_networkx_nodes(GRAF, pos, nodelist=list(set(GRAF.nodes()) - set(zeleni)), node_color='red', node_size=500)
        plt.savefig('public/slike/slika' + str(brSlika) + '.png')
        plt.close()
    

def dobavi_najkrace_puteve(vrhovi, zavrsniCvor):
    najkraciPutevi = set()
    def dobaviPut(put, cvor):
        for i in vrhovi:
            if i.naziv == cvor:
                if not i.prethodnik:
                    najkraciPutevi.add(tuple(put))
                    return
                for prethodnik in i.prethodnik:
                    dobaviPut(put + [(prethodnik, cvor)], prethodnik)
    dobaviPut([], zavrsniCvor)
    return najkraciPutevi

def vizualizirajGraf(GRAF, cvor, posjeceni, bridoviSad, korak, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    plt.figure(figsize=((2+len(GRAF)//10)*5,(2.2+len(GRAF)//10)*3)) 
    plt.title('korak: ' + str(korak), fontsize=16, pad=20)
    bridovi = list(set(GRAF.edges()) - set(bridoviSad))
    nx.draw(GRAF, pos, with_labels=True, node_color='blue', edge_color='black', node_size=500, font_size=15, font_color="black", edgelist=bridovi)
    nx.draw_networkx_edges(GRAF, pos, edgelist=bridoviSad, edge_color='red')
    for u, v in bridoviSad:
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        plt.text(x, y, "1", fontsize=10, ha="center", va="center", color="black")
    posjeceniList = []
    for i in posjeceni:
        posjeceniList.append(i.naziv)
    nx.draw_networkx_nodes(GRAF, pos, nodelist=posjeceniList, node_color='grey', node_size=500)
    nx.draw_networkx_nodes(GRAF, pos, nodelist=[cvor], node_color='green', node_size=500)
    for node, (x, y) in pos.items():
        description = GRAF.nodes[node].get("description", "")
        plt.text(x, y + 0.025, description, fontsize=12, ha="center", va="bottom", color="red")
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()