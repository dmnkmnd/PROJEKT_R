import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # Za mapiranje boja

# Funkcija za učitavanje grafa iz json-a
def unos(g):
    GRAF = nx.DiGraph()
    for node, neighbors in g.items():
        for neighbor in neighbors:
            GRAF.add_edge(node, neighbor)
    return GRAF

# Funkcija za vizualizaciju grafa s centralitetom bliskosti
def vizualiziraj_graf(graf):
    # Izračunavanje centraliteta bliskosti za svaki čvor
    centralitet_bliskosti = nx.closeness_centrality(graf)

    # Postavljanje veličina čvorova s uravnoteženim faktorom skaliranja
    velicine_cvorova = [85 + 4500 * centralitet_bliskosti[cvor] for cvor in graf.nodes()]

    # Mapiranje boja tako da veći centralitet ima tamniju nijansu crvene
    norm = plt.Normalize(vmin=min(centralitet_bliskosti.values()), vmax=max(centralitet_bliskosti.values()))
    boje = [cm.Reds(norm(centralitet_bliskosti[cvor])) for cvor in graf.nodes()]

    # Prikaz grafa
    fig, ax = plt.subplots(figsize=(14, 14))  # Stvaranje figure i osi
    pozicija = nx.spring_layout(graf, seed=42)  # Pozicioniranje čvorova

    # Crtanje grafa s usmjerenim bridovima (strelice)
    nx.draw_networkx(
        graf, pozicija,
        node_size=velicine_cvorova,
        node_color=boje,
        with_labels=True,  # Prikaz imena čvorova
        labels={cvor: cvor for cvor in graf.nodes()},  # Prikazuje samo ime čvora
        edge_color='gray',
        font_size=10,  # Povećan font za čitljivost
        arrows=True,  # Prikaz strelica za usmjereni graf
        ax=ax  # Povezivanje s trenutnom osi
    )

    # Prikaz grafa s ljestvicom boja za vrijednosti centraliteta
    sm = plt.cm.ScalarMappable(cmap=cm.Reds, norm=norm)
    sm.set_array([])

    # Dodavanje ljestvice boja na trenutnu os
    cbar = fig.colorbar(sm, ax=ax, orientation="vertical")
    cbar.set_label("Centralitet bliskosti")  # Legenda boja

    plt.title("Vizualizacija usmjerenog grafa s centralitetom bliskosti")
    plt.savefig('public/slike/slika1.png')
    plt.close()

'''
# Učitavanje grafa iz datoteke
ime_datoteke = "graph2.txt"  # Promijenite naziv datoteke po potrebi
graf = ucitaj_graf_iz_datoteke(ime_datoteke)

# Vizualizacija grafa
vizualiziraj_graf(graf)
'''