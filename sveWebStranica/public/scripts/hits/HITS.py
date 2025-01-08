from read import unos
from math import sqrt

def algHits(lokacija, iter):
    rj=unos(lokacija)

    for i in range(iter):
        uk_aut = 0.0
        uk_hub = 0.0
        hubovi = []
        autori = []

        for cvor in rj:
            n_aut = 0.0
            n_hub = 0.0

            #autoritet
            for rod in rj.get(cvor).u:
                n_aut = n_aut + rj.get(rod).hub
            autori.append(n_aut)

            #hub
            for dje in rj.get(cvor).iz:
                n_hub = n_hub + rj.get(dje).aut
            hubovi.append(n_hub)

        # promjena
        uk_aut = sqrt(sum(a * a for a in autori))
        uk_hub = sqrt(sum(h * h for h in hubovi))
        autori = [a / uk_aut for a in autori]
        hubovi = [h / uk_hub for h in hubovi]

        sum_autori = sum(autori)
        sum_hubovi = sum(hubovi)
        autori = [a / sum_autori for a in autori]
        hubovi = [h / sum_hubovi for h in hubovi]

        j=0
        for cvor in rj:
            rj.get(cvor).aut=autori[j] 
            rj.get(cvor).hub=hubovi[j] 
            j=j+1
    
    return rj
    


algHits("C:\\Users\domin\OneDrive\Desktop\graf.txt", 3)

