from funcaux import datetime_to_float
from puntoGPS import puntoGPS, haversine

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
    result=procesaPuntos(result)
    return result

# Procesa el array de puntos para calcular los datos agregados
def procesaPuntos(puntos:list)->list:
    """
    Procesa una lista de puntos calculando toods los valores de la clase PuntoGPS apartir de lat, lon, altura y hora
    """
    for idxpto in range(1,len(puntos)): # len(puntos)
        puntos[idxpto].incDt = datetime_to_float(puntos[idxpto].dt)-datetime_to_float(puntos[idxpto-1].dt)
        puntos[idxpto].accDt = puntos[idxpto-1].accDt+puntos[idxpto].incDt
        puntos[idxpto].distancia = haversine(puntos[idxpto],puntos[idxpto-1])
#        if puntos[idxpto].distancia < 0:
#            print("error")
#            quit()
        puntos[idxpto].accDist = puntos[idxpto-1].accDist+puntos[idxpto].distancia
        puntos[idxpto].incAltura = puntos[idxpto].altura - puntos[idxpto-1].altura
        if (puntos[idxpto].incAltura>=0):
            puntos[idxpto].accSubida = puntos[idxpto-1].accSubida + puntos[idxpto].incAltura
            puntos[idxpto].accBajada = puntos[idxpto-1].accBajada 
        else:
            puntos[idxpto].accBajada = puntos[idxpto-1].accBajada - puntos[idxpto].incAltura
            puntos[idxpto].accSubida = puntos[idxpto-1].accSubida 
        
         # print("%5d: %s" %(idxpto+1,puntos[idxpto].toStr()))
    return puntos
