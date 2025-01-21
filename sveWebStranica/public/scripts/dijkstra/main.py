import citanje_grafa as cit, algoritam as alg, vizualizacija as viz, sys, json

GRAF = cit.procitaj_graf(json.loads(sys.argv[1]))
cvorA = sys.argv[2]
cvorB = sys.argv[3]
preskok = int(sys.argv[4])
rez = alg.dijkstra_alg(GRAF, cvorA, cvorB, preskok)
print(rez)