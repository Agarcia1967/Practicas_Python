from puntoGPS import puntoGPS

# Devuelve una lista de puntoGPS
def cargaFichero(fichero:str)->list:
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

