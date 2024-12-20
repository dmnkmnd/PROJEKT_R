import citanje_grafa as cit, algoritam as alg, vizualizacija as viz, sys, json

GRAF = cit.procitaj_graf(json.loads(sys.argv[1]))
brZajednica = int(sys.argv[2])
preskok = int(sys.argv[3])
alg.girvan_newman_alg(GRAF, brZajednica, preskok)