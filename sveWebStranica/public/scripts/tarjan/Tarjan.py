from read import unosTar

#aut = index
#hub = lowlink
#iz = djeca cvora

def TarjanRek(cvor, graf, index, stog):
    graf.get(cvor).aut = index
    graf.get(cvor).hub = index
    index = index + 1
    stog.append(cvor)

    for jedan in graf.get(cvor).iz:

        if graf.get(jedan).aut == -1:
            index = TarjanRek(jedan, graf, index, stog)
            graf.get(cvor).hub = min(graf.get(cvor).hub, graf.get(jedan).hub)
        
        elif jedan in stog:
            graf.get(cvor).hub = min(graf.get(cvor).hub, graf.get(jedan).aut)


    if graf.get(cvor).hub == graf.get(cvor).aut:
        jedan = stog.pop()
        graf.get(jedan).hub = graf.get(cvor).aut
        
        while jedan != cvor:
            jedan = stog.pop()
            graf.get(jedan).hub = graf.get(cvor).aut

    return index


def TarjanAlg(adresa):
    rj = unosTar(adresa)
    index = 0
    stog = []
    
    for vrh in rj.keys():
        if rj.get(vrh).aut == -1:
            index = TarjanRek(vrh, rj, index, stog)
    
    return rj



#TarjanAlg("C:\\Users\domin\OneDrive\Desktop\graf.txt")
