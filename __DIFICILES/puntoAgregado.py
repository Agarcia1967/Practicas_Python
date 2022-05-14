from funcaux import hms
from array import *
from typing import List
from puntoGPS import puntoGPS

class puntoAgregado():
    """Representa un punto de AGREGADO POR PENDIENTE"""
    min : float = -100
    max : float = 100
    accDist : float = 0 # acumulado distancia desde origen
    accSubida : float = 0 # acumulado de subida
    accBajada : float = 0 # acumulado de bajada
    accDt: float =0 # Acumulado de tiempo

    def __init__(self,min:float,max:float):
        """
        Constructor de la clase
        Inicializa un rango de agregados
        """
        self.min = min
        self.max = max

    def __str__(self)->str:
        return("[%7.2f,%7.2f] d=%8.2f ahs=%6.1f ahb=%6.1f h=%s" 
        %(self.min,self.max,self.accDist,self.accSubida,self.accBajada,hms(self.accDt)))

    def toStr(self)->str:
        return self.__str__()

class RepositorioAgregado():
    """Representa un repositorio de agregados"""
    repo : List[puntoAgregado] = []

    def __init__(self):
        # print("Creando rangos")
        self.createRango(-30,-100)
        self.createRango(-15,-30)
        self.createRango(-10,-15)
        self.createRango(-5,-10)        
        self.createRango(-5,-1)
        self.createRango(-1,1)
        self.createRango(1,5)
        self.createRango(5,10)
        self.createRango(10,15)
        self.createRango(15,30)
        self.createRango(30,100)
        # self.createRango(15,20)        
        # self.createRango(20,25)
        # self.createRango(25,30)
        # self.createRango(30,40)        
        # self.createRango(40,100)
        return

    def createRango(self,min: float, max:float):
        if (min>max):
            tmp=min
            min=max
            max=tmp
        self.repo.append( puntoAgregado(min,max) )

    def add(self,pdte: float,altura:float, distancia: float, segundos: float):
        # min : float = -100
        # max : float = 100
        # accDist : float = 0 # acumulado distancia desde origen
        # accSubida : float = 0 # acumulado de subida
        # accBajada : float = 0 # acumulado de bajada
        # accDt: float
        for p in self.repo:
            if (pdte>=p.min and pdte<=p.max):
                p.accDist += distancia
                p.accDt += segundos
                if (pdte>0):
                    p.accSubida += altura
                else:
                    p.accBajada += altura
                return
        # print("Algo va mal")

    def fromPtos(self, ptos:List[puntoGPS]):
        for p in ptos:
            self.add(p.tpcvar,p.incAltura,p.distancia,p.incDt)
        return

    def __str__(self)->str:
        result = ''
        for p in self.repo:
            result += '\n' + p.toStr()
        return result
        

    def toStr(self)->str:
        return self.__str__()