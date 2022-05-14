
from funcaux import datetime_to_float
from puntoGPS import puntoGPS, haversine
from typing import List

# Procesa el array de puntos para calcular los datos agregados
def procesaPuntos(puntos:List[puntoGPS])->List[puntoGPS]:
    """
    Procesa una lista de puntos calculando todos los valores de la clase PuntoGPS apartir de lat, lon, altura y hora
    Se hace una REDUCCION de aquellos puntos que esten a menos de 30 metros
    """
    TmpPuntos = []
    TmpPuntos.append(puntos[0])
    for idxpto in range(1,len(puntos)): # len(puntos)
        puntos[idxpto].incDt = datetime_to_float(puntos[idxpto].dt)-datetime_to_float(puntos[idxpto-1].dt)
        puntos[idxpto].accDt = puntos[idxpto-1].accDt+puntos[idxpto].incDt
        puntos[idxpto].distancia = haversine(puntos[idxpto],puntos[idxpto-1])
        if (puntos[idxpto].distancia >= 30 ):
            TmpPuntos.append(puntos[idxpto])
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
            
        if (puntos[idxpto].distancia>0):
            puntos[idxpto].tpcvar = puntos[idxpto].incAltura / puntos[idxpto].distancia * 100
        
        # print("%5d: %s" %(idxpto+1,puntos[idxpto].toStr()) )
    print("%5d puntos %5d tmpPuntos" %(len(puntos), len(TmpPuntos)))
    if ( len(TmpPuntos) < len(puntos) ):
        puntos= procesaPuntos(TmpPuntos)
    return puntos

    def calcula_porcentajes(ptos:List[puntoGPS])->List[puntoGPS]:
        tabla: list = []
        return tabla
    # calcula tendencias y cortes
    # Vamos a procesar los puntos para calcular los cambios de tendencia ascenso/descenso
    # Haremos los cortes cuando cambie la tendencia
    def calcula_cortes(puntos:list)->list:
        return 
