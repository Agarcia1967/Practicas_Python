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

    def toStr(self)->str:
        return("[%7.2f,%7.2f] d=%8.2f ahs=%6.1f ahb=%6.1f h=%s" 
        %(self.min,self.max,self.accDist,self.accSubida,self.accBajada,hms(self.accDt)))

class RepositorioAgregado():
    """Representa un repositorio de agregados"""
    repo : List[puntoAgregado] = []

    def __init__(self):
        # print("Creando rangos")
        self.create(-100,-50)
        self.create(-50,-40)
        self.create(-40,-30)
        self.create(-30,-20)
        self.create(-20,-10)        
        self.create(-10,-5)        
        self.create(-5,0)
        self.create(0,2)
        self.create(2,6)
        self.create(6,10)
        self.create(10,15)
        self.create(15,20)        
        self.create(20,25)
        self.create(25,30)
        self.create(30,40)        
        self.create(40,100)
        return

    def create(self,min: float, max:float):
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

    def toStr(self)->str:
        result = ''
        for p in self.repo:
            result += '\n' + p.toStr()
        return result