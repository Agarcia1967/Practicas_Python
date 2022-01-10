from funcaux import hms
from datetime import datetime
import math

def convert_float(s:str)->float:
    """
    Convierte un string a float controlando el error, si existe prosigue con valor 0 
    """
    try:
        f = float(s)
    except ValueError:
        f = float()
    return f

class puntoGPS():
    """Representa un punto de GPS por sus coordenadas y time de captura"""
    lon : float = 0
    lat : float = 0
    altura : float = 0
    distancia  : float = 0 # distancia al siguiente punto
    incAltura  : float = 0 # diferencial de altura con siguiente
    accDist : float = 0 # acumulado distancia desde origen
    accSubida : float = 0 # acumulado de subida
    accBajada : float = 0 # acumulado de bajada
    tpcvar : float = 0 # tanto por ciento de variacion respecto al punto anterior
    dt : datetime 
    incDt: float =1 # Diferencial de segundos
    accDt: float =0 # Acumulado de tiempo

    def __init__(self,entrada:str):
        """
        Constructor de la clase, crea un puntoGPS a partir de un string que espera con un formato determinado
        ejemplo: 42.556836241856217,-6.593071678653359,547.79998779296875,2017-04-29T11:11:08Z
        """
        # entrada:
        # 42.556836241856217,-6.593071678653359,547.79998779296875,2017-04-29T11:11:08Z
        lat,lon,alt,time = entrada.strip().split(',')
        # Convertimos a radianes 
        self.lon =  ( convert_float( lon.strip() ) )
        self.lat =  ( convert_float( lat.strip() ) )
        self.altura =  convert_float( alt.strip() )
        self.dt = datetime.strptime(time.strip(),'%Y-%m-%dT%H:%M:%SZ')

    def toStr(self)->str:
        return("(%8.5f,%8.5f,%6.1f,d=%6.2f h=%4.1f) aDt=%8.1f ahs=%5.1f ahb=%5.1f h=%s (%2.0f) pc=%4.1f" 
        %(self.lat,self.lon,self.altura,self.distancia,self.incAltura,self.accDist,self.accSubida,self.accBajada,hms(self.accDt),self.incDt,self.tpcvar))

def haversine(p1: puntoGPS, p2: puntoGPS)->float:
    """
    Calcula la distancia de entre dos puntos GPS (en radianes lat y lon) por la formula de haversine
    """
    # convert decimal degrees to radians 
    # haversine formula 
    dlon:float = math.radians(p2.lon) - math.radians(p1.lon)
    dlat:float = math.radians(p2.lat) - math.radians(p1.lat)
    a:float = math.sin(dlat/2)**2 + math.cos(math.radians(p1.lat)) * math.cos(math.radians(p2.lat)) * math.sin(dlon/2)**2
    c:float = 2 * math.asin(math.sqrt(a)) 
    # Radius of earth in kilometers is 6372,8 kms
    mts: float = 6372800 * c
    return mts
