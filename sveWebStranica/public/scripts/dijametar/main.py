import citanje_grafa as cit, algoritam as alg, vizualizacija as viz, sys, json

GRAF = cit.procitaj_graf(json.loads(sys.argv[1]))
rez = alg.dijametar_alg(GRAF)
izlaz = { "dijametar": rez[0], "strogoPovezani": rez[1] }
print(json.dumps(izlaz))