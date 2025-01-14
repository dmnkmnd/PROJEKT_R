import v_HITS as viz, sys, json
json = json.loads(sys.argv[1])
iteracija = int(sys.argv[2])
viz.graf_HITS(json, iteracija)