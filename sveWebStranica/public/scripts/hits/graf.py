class GrafHA:
    def __init__(self, u, iz, aut, hub):
        self.u = u
        self.iz = iz
        self.aut = aut
        self.hub = hub

    def __str__(self):
        return f"({self.u}, {self.iz}, {self.aut}, {self.hub})"



def podPar (unos):
    ispis = []
    
    for prvi in unos:
        for drugi in unos.get(prvi).iz:
            ispis.append((prvi, drugi))

    return ispis  

def podAuto (unos):
    ispis = []
    
    for prvi in unos:
        ispis.append(unos.get(prvi).aut)

    return ispis 

def podHub (unos):
    ispis = []
    
    for prvi in unos:
        ispis.append(unos.get(prvi).hub)

    return ispis 

def podSusjedi (svi, povezani, cvor1, cvor2):
    ispis = []

    for prvi in svi:
        if prvi in povezani:
            ispis.append(1)
        elif (prvi == cvor1 or prvi == cvor2):
            ispis.append(2)
        else:
            ispis.append(0)
    
    return ispis

def podGrupe( graf):
    prijelaz = {}
    ispis = []
    index = 1

    for prvi in graf:
        if graf.get(prvi).hub in prijelaz:
            ispis.append(prijelaz.get(graf.get(prvi).hub))
        else:
            prijelaz.update({graf.get(prvi).hub: index})
            ispis.append(index)
            index = index + 1

    return ispis


