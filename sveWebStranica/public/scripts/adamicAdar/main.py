import read as cit, v_obcni as pocetniGraf, v_AA as viz, sys, json
GRAF = cit.unos(json.loads(sys.argv[1]))
cvorA = sys.argv[2]
cvorB = sys.argv[3]
pocetniGraf.v_AA(GRAF)
viz.v_AA(GRAF, cvorA, cvorB)