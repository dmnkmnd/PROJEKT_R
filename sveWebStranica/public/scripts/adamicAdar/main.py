import read as cit, v_AA as viz, sys, json
GRAF = cit.unos(json.loads(sys.argv[1]))
cvorA = sys.argv[2]
cvorB = sys.argv[3]
viz.v_AA(GRAF, cvorA, cvorB)