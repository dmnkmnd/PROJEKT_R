from Tarjan import TarjanAlg
from read import unos
from graf import * 

import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
import numpy as np

def v_Tar (jsonGRAF):
    graf = TarjanAlg(jsonGRAF)

    # vizualizacija
    G = nx.DiGraph()  
    G.add_nodes_from(list(graf.keys()))
    G.add_edges_from(podPar(graf))

    grupe = podGrupe(graf)
    print(grupe)
    uzorakBoje = plt.cm.get_cmap('viridis', max(grupe) + 1 ) 

    boje = [uzorakBoje(one) for one in grupe] 
    plt.figure(figsize=((2+len(graf)//10)*5,(2.2+len(graf)//10)*3))
    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_color=boje, edge_color="black", font_weight='bold')
    plt.savefig('public/slike/slika1.png')
    plt.close()

#v_Tar("C:\\Users\domin\OneDrive\Desktop\graf.txt")