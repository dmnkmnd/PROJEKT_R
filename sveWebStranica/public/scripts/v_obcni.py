from read import unos
from graf import * 

import matplotlib.pyplot as plt
import networkx as nx
import sys
import json


def v_AA(file, lokSlika):
    graf = unos(file)
    G = nx.DiGraph()  # Use DiGraph for directed graph

    cvorovi = list(graf.keys())
    cvorovi.sort()

    G.add_nodes_from(cvorovi)
    G.add_edges_from(podPar(graf))

    # Drawing
    plt.figure(figsize=((2+len(graf)//10)*5,(2.2+len(graf)//10)*3))
    pos = nx.spring_layout(G, k=0.8, scale=0.5)  

    nx.draw_networkx_nodes(G, pos, node_size=300)
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True, arrowsize=10)  

    plt.axis('off')
    plt.savefig(lokSlika, format="PNG")  # Spremanje slike kao PNG
    plt.close() 
    

if __name__ == "__main__":
    input_data = sys.stdin.read()
    dataJSON = json.loads(input_data)  
    save_path = sys.argv[1]  
    v_AA(dataJSON, save_path)