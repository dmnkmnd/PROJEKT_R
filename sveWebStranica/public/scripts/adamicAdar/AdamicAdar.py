from read import unos
from math import log10 

def algAA(rj, cvor1, cvor2):
    if(cvor1 in rj.get(cvor2).u or cvor1 in rj.get(cvor2).iz or cvor2 in rj.get(cvor1).u or cvor2 in rj.get(cvor1).iz ):
        #Već su povezani stoga predikacja nema smisla!
        return "CVOROVI POVEZANI", [], rj
    else:
        zajedno = []
        suma =0.0
        
        for one in rj.get(cvor1).u:
            if(((one in rj.get(cvor2).u) or (one in rj.get(cvor2).iz)) and one not in zajedno):
                zajedno.append(one)

        for one in rj.get(cvor1).iz:
            if(((one in rj.get(cvor2).u) or (one in rj.get(cvor2).iz)) and one not in zajedno):
                zajedno.append(one)

        for one in zajedno:
            suma = suma + 1.0 / log10(len(set(rj.get(one).u).union(rj.get(one).iz)))
            rj.get(one).aut = 1 + 1.0 / log10(len(set(rj.get(one).u).union(rj.get(one).iz)))
            

        suma = round(suma, 4)
        return suma, zajedno, rj

#print (algAA("C:\\Users\domin\OneDrive\Desktop\graf.txt", "E", "F"))