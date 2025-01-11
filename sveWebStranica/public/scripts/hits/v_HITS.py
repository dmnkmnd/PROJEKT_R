from HITS import algHits
from read import unos
from graf import * 

import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
import numpy as np

def graf_HITS (link, iteracija):
    if(iteracija == 0):
        graf = unos(link)

    else:
        graf = algHits(link, iteracija)
    
    
    # vizualizacija
    G = nx.DiGraph()  
    G.add_nodes_from(list(graf.keys()))
    G.add_edges_from(podPar(graf))

    # veličina čvorova = autoriteti
    node_sizes = podAuto(graf)
    node_sizes = [a * 6000 + 200 for a in node_sizes]

    # intenizet boje = hubovi
    values = podHub(graf)
    values = [a*1.5 + 0.04 for a in values]
    cmap = cm.get_cmap('Blues')  
    node_colors = [cmap(value) for value in values]  

    # Crtaj graf
    plt.figure(figsize=(8, 6))
    nx.spring_layout(G, k=0.8, scale=0.6)
    nx.draw( 
        G,
        with_labels=True,
        font_weight='bold',
        node_size=node_sizes,
        node_color=node_colors,  # Boje iz kolormapa
        edge_color='green'
    )
    plt.show()

graf_HITS("C:\\Users\domin\OneDrive\Desktop\graf.txt", 100)
