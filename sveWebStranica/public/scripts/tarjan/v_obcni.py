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
    plt.figure(figsize=(8, 6))  # Size of the window in inches
    pos = nx.spring_layout(G, k=0.8, scale=0.5)  # Layout for node positions

    nx.draw_networkx_nodes(G, pos, node_size=300)
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True, arrowsize=10)  # Increase arrowsize

    plt.axis('off')
    plt.savefig(lokSlika, format="PNG")  # Spremanje slike kao PNG
    plt.close() 
    

if __name__ == "__main__":
    input_data = sys.stdin.read()
    dataJSON = json.loads(input_data)  
    save_path = sys.argv[1]  
    v_AA(dataJSON, save_path)