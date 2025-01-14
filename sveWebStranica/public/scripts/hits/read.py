from graf import GrafHA
import json

def unos (dataJSON):
    
    rj = {}
    
    for key, values in dataJSON.items():
        rj.update({
            key: 
            GrafHA(
                [],
                values, 
                1.0, 
                1.0
                ) 
            })
    
    for cvor in rj:
        for one in rj.get(cvor).iz:
            rj.get(one).u.append(cvor)
            

    return rj



def unosTar (file):
    try:
        dataJSON = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Neispravan JSON format: {e}")
    
    rj = {}
    
    for key, values in dataJSON.items():
        rj.update({
            key: 
            GrafHA(
                [],
                values, 
                -1, 
                -1
            ) 
            })
    return rj

#unos("C:\\Users\domin\OneDrive\Desktop\graf.txt")