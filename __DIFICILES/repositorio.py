from puntoGPS import puntoGPS
from typing import List

# Devuelve una lista de puntoGPS
def cargaFichero(fichero:str)->List[puntoGPS]:
    """
    carga un fichero de puntos definido en fichero
    Devuelve una lista de puntoGPS
    """
    f=open(fichero,"r")
    tmp=f.readlines()
    f.close()
    result=[]
    for linea in tmp:
        result.append(puntoGPS(linea))
    return result

