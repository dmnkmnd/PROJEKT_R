from AdamicAdar import algAA
from read import unos
from graf import * 

import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
import numpy as np


def v_AA (graf, cvorA, cvorB):
    G = nx.Graph()  

    cvorovi = list(graf.keys())
    cvorovi.sort()

    G.add_nodes_from(cvorovi)
    bridi = podPar(graf)
    bridi.append((cvorA,cvorB))
    G.add_edges_from(bridi)

    vriVeza, clan, graf = algAA(graf, cvorA, cvorB)


    values = podSusjedi(cvorovi, clan, cvorA, cvorB)
    values = [a*0.32 + 0.08 for a in values]
    cmap = cm.get_cmap('Oranges')  
    node_colors = [cmap(value) for value in values]  

    doprinos = podAuto(graf)
    doprinos = [a - 1 for a in doprinos]

    # Crtanje 
    plt.figure(figsize=(8, 6)) # veličina u inčima prozora
    pos = nx.spring_layout(G, k=0.8, scale=0.5)  # Layout za pozicije čvorova

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_labels(G, pos, font_weight='bold')

    orgBr = [(p, d) for p, d in G.edges if (p, d) != (cvorA, cvorB)]
    nx.draw_networkx_edges(G, pos, edgelist=orgBr, edge_color='black')

    nx.draw_networkx_edges(G, pos, edgelist=[(cvorA, cvorB)], edge_color='red', style='dashed')
    edge_labels = {(cvorA, cvorB): vriVeza}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    doprinos_labels = {node: f"{doprinos[i]:.2f}" for i, node in enumerate(G.nodes)}
    shifted_pos = {node: (x, y - 0.07) for node, (x, y) in pos.items()}  # Pomak za ispis ispod
    nx.draw_networkx_labels(G, shifted_pos, labels=doprinos_labels, font_color='blue', font_size=10)

    plt.savefig('public/slike/slika2.png')
    plt.close()