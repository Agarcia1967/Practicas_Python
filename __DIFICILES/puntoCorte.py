from funcaux import hms
from datetime import datetime
from puntoGPS import puntoGPS
from typing import List

class puntoCorte( ):
    """Representa un punto de corte sobre la serie de puntos"""
    ini : int = 0 # Indice del punto donde comienza el corte
    fin : int = 0 # Indice del punto donde acaba el corte
    accDist : float = 0 # acumulado distancia desde origen
    accSubida : float = 0 # acumulado de subida
    accBajada : float = 0 # acumulado de bajada 
    accDt: int =0 # Acumulado de tiempo

    def __init__(self,ini,fin,d,s,b,t):
        """
        Constructor de la clase, crea un puntoCORTE
        """
        # entrada:
        self.ini = ini
        self.fin = fin
        self.accDist = d
        self.accSubida = s
        self.accBajada = b
        self.accDt = t

    # @staticmethod
    # def calcula_Corte(puntos:List[puntoGPS])->List[puntoCorte]:
    #    lista = []
    #    return lista

    def toStr(self)->str:
        return("(%4d,%4d) distancia=%4.1f Sube=%8.1f Baja=%5.1f t=%dsg" 
        %(self.ini,self.fin,self.accDist,self.accSubida,self.accBajada,self.accDt))

