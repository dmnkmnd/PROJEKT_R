from read import unos
from math import log10 

def algAA(lokacija, cvor1, cvor2):
    rj=unos(lokacija)
    if(cvor1 in rj.get(cvor2).u or cvor1 in rj.get(cvor2).iz or cvor2 in rj.get(cvor1).u or cvor2 in rj.get(cvor1).iz ):
        return "Već su povezani stoga predikacja nema smisla!"
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

        suma = round(suma, 4)
        return suma, zajedno

#print (algAA("C:\\Users\domin\OneDrive\Desktop\graf.txt", "C", "D"))