import matplotlib.pyplot as plt, networkx as nx, numpy as np, random

seed = 0
boje = ['lightblue', 'green', 'orange', 'purple', 'pink', 'cyan', 'yellow', 'brown', 'magenta', 'lime']

def vizualizirajPocetniGraf(GRAF, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    plt.figure(figsize=(12, 12))
    plt.title('POČETAK', fontsize=16, pad=20)
    nx.draw(GRAF, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=500, font_size=15, font_color="black")
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()

def vizualizirajZavrsniGraf(GRAF, povezaniPodgrafovi, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    plt.figure(figsize=(12, 12))
    plt.title('KRAJ', fontsize=16, pad=20)
    bridovi = GRAF.edges()
    nx.draw(GRAF, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=500, font_size=15, font_color="black", edgelist=[])
    j = 0
    for i in povezaniPodgrafovi:
        bridovi = list(set(bridovi) - set(i.edges()))
        nx.draw_networkx_nodes(GRAF, pos, nodelist=i.nodes(), node_color=boje[j % len(boje)], node_size=500)
        nx.draw_networkx_edges(GRAF, pos, edgelist=i.edges(), edge_color=boje[j % len(boje)])
        j += 1
    nx.draw_networkx_edges(GRAF, pos, edgelist=bridovi, edge_color='black')
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()

def vizualizirajGraf(GRAF, povezaniPodgrafovi, maxBridovi, l, preskok, jeZadnji, brSlika):
    random.seed(seed)
    np.random.seed(seed)
    pos = nx.spring_layout(GRAF, k=0.1, seed=42)
    plt.figure(figsize=(12, 12))
    if(l % preskok == 0 and jeZadnji == False):
        plt.title('broj zajednica: ' + str(l), fontsize=16, pad=20)
    else:
        plt.title('broj zajednica: ' + str(l) + ' (POSLJEDNJI KORAK)', fontsize=16, pad=20)
    bridovi = list(set(GRAF.edges()) - set(maxBridovi))
    nx.draw(GRAF, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=500, font_size=15, font_color="black", edgelist=[])
    j = 0
    for i in povezaniPodgrafovi:
        bridovi = list(set(bridovi) - set(i.edges()))
        nx.draw_networkx_nodes(GRAF, pos, nodelist=i.nodes(), node_color=boje[j % len(boje)], node_size=500)
        bezMaxBridovi = list(set(i.edges()) - set(maxBridovi))
        nx.draw_networkx_edges(GRAF, pos, edgelist=bezMaxBridovi, edge_color=boje[j % len(boje)])
        j += 1
    nx.draw_networkx_edges(GRAF, pos, edgelist=bridovi, edge_color='black')
    nx.draw_networkx_edges(GRAF, pos, edgelist=maxBridovi, edge_color='red')
    plt.savefig('public/slike/slika' + str(brSlika) + '.png')
    plt.close()