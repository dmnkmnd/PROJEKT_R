import vizualizacija as viz, networkx as nx, sys
from vrh import Vrh

def dijkstra_alg(GRAF, pocCvor, zavrsCvor, preskok):
    brSlika = 1
    viz.vizualizirajPocetniGraf(GRAF, brSlika)
    brSlika += 1
    posjeceni = []
    neposjeceni = []
    for v in GRAF.nodes:
        if v == pocCvor:
            GRAF.nodes[v]["description"] = '0'
            continue
        else:
            neposjeceni.append(Vrh(v, sys.maxsize, []))
    trVrh = Vrh(pocCvor, 0, [])
    posjeceni.append(Vrh(trVrh.naziv, trVrh.vr, trVrh.prethodnik))
    tez = 1
    korak = 1
    for i in range (len(GRAF.nodes) - 1):
        bridovi = []
        for v in neposjeceni:
            if (GRAF.has_edge(trVrh.naziv, v.naziv) and trVrh.vr + tez <= v.vr):
                v.vr = trVrh.vr + tez
                bridovi.append((trVrh.naziv, v.naziv))
                v.prethodnik.append(trVrh.naziv)
                GRAF.nodes[v.naziv]["description"] = str(v.vr)
        if korak % preskok == 0:
            viz.vizualizirajGraf(GRAF, trVrh.naziv, posjeceni, bridovi, korak, brSlika)
            brSlika += 1
        minVr = sys.maxsize
        for v in neposjeceni:
            if v.vr < minVr:
                minVrh = v
                minVr = v.vr
        posjeceni.append(Vrh(minVrh.naziv, minVrh.vr, minVrh.prethodnik))
        for v in neposjeceni:
            if v.naziv == minVrh.naziv and v.vr == minVrh.vr:
                neposjeceni.remove(v)
                break
        trVrh.naziv = minVrh.naziv
        trVrh.vr = minVrh.vr
        trVrh.prethodnik = minVrh.prethodnik
        korak += 1
    udaljenost = -1 #ako udaljenost ostane u -1 A -> B je nedostizno
    for v in posjeceni:
        if v.naziv == zavrsCvor:
            udaljenost = v.vr
            break
    viz.vizualizirajZavrsniGraf(GRAF, posjeceni, zavrsCvor, udaljenost, brSlika)
    return udaljenost