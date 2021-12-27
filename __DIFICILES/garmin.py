# Ejercicio
# Dado un fichero CSV sin cabeceras, que contiene las coordenadas GPS x,y,z ademas de una marca de tiempo 
# se pide:
#    Leer el fichero
#    Calcular para cada toma 
#        la distancia con la anterior 
#        la altura con el anterior 
#        la altura ganada desde el principio 
#        la altura perdida desde el principio
#        la velocidad media hasta ese punto (respecto al inicio)
#        
# 

import math
from datetime import datetime

def hms(time:int)->str:
    h : int = time // 3600
    m : int = (time -  h * 3600) // 60
    s : int = (time - h * 3600 - m * 60)
    return "%02d:%02d:%02d"%(h,m,s)

def datetime_to_float(d):
    epoch = d.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def convert_float(s:str)->float:
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
    dt : datetime 
    incDt: float =1 # Diferencial de segundos
    accDt: float =0 # Acumulado de tiempo

    def __init__(self,entrada:str):
        # entrada:
        # 42.556836241856217,-6.593071678653359,547.79998779296875,2017-04-29T11:11:08Z
        lat,lon,alt,time = entrada.strip().split(',')
        # Convertimos a radianes 
        self.lon =  ( convert_float( lon.strip() ) )
        self.lat =  ( convert_float( lat.strip() ) )
        self.altura =  convert_float( alt.strip() )
        self.dt = datetime.strptime(time.strip(),'%Y-%m-%dT%H:%M:%SZ')

    def toStr(self)->str:
        return("lt=%8.5f ln=%8.5f h=%5.1f d=%6.2f dh=%4.1f aDt=%8.1f ahs=%5.1f ahb=%5.1f h=%s (%2.0f)" 
        %(self.lat,self.lon,self.altura,self.distancia,self.incAltura,self.accDist,self.accSubida,self.accBajada,hms(self.accDt),self.incDt))

def haversine(p1: puntoGPS, p2: puntoGPS)->float:
    """
    Calcula la distancia de entre dos puntos GPS (en radianes lat y lon)
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

# Devuelve una lista de puntoGPS
def cargaFichero(fichero:str)->list:
    f=open(fichero,"r")
    tmp=f.readlines()
    f.close()
    result=[]
    for linea in tmp:
        result.append(puntoGPS(linea))
    return result

# Procesa el array de puntos para calcular los datos agregados
def procesaPuntos(datos:list)->list:
    for idxpto in range(1,len(datos)): # len(datos)
        datos[idxpto].incDt = datetime_to_float(datos[idxpto].dt)-datetime_to_float(datos[idxpto-1].dt)
        datos[idxpto].accDt = datos[idxpto-1].accDt+datos[idxpto].incDt
        datos[idxpto].distancia = haversine(datos[idxpto],datos[idxpto-1])
#        if datos[idxpto].distancia < 0:
#            print("error")
#            quit()
        datos[idxpto].accDist = datos[idxpto-1].accDist+datos[idxpto].distancia
        datos[idxpto].incAltura = datos[idxpto].altura - datos[idxpto-1].altura
        if (datos[idxpto].incAltura>=0):
            datos[idxpto].accSubida = datos[idxpto-1].accSubida + datos[idxpto].incAltura
            datos[idxpto].accBajada = datos[idxpto-1].accBajada 
        else:
            datos[idxpto].accBajada = datos[idxpto-1].accBajada - datos[idxpto].incAltura
            datos[idxpto].accSubida = datos[idxpto-1].accSubida 
        
         # print("%5d: %s" %(idxpto+1,datos[idxpto].toStr()))
    return datos


# x= puntoGPS('42.556836241856217,-6.593071678653359,547.79998779296875,2017-04-29T11:11:08Z')
# x= puntoGPS('42.556782681494951,-6.597870988771319,543.5999755859375, 2017-04-29T11:12:00Z')

# a= puntoGPS('42.5553340371698,  -6.60053928382694,522.799987792968,2017-04-29T06:29:36Z')
# b= puntoGPS('42.5553339533507,  -6.60053920000792,523,             2017-04-29T06:29:36Z')
# 
# c= puntoGPS('42.5553705822676,  -6.6005502641201,  522.400024414062,2017-04-29T06:29:36Z')
# d= puntoGPS('42.5554321054369,  -6.60058563575148, 522.200012207031,2017-04-29T06:29:36Z') 
# 
# x= puntoGPS('42.5555393099784,  -6.60067381337285, 522.400024414062,2017-04-29T06:29:36Z')
# x= puntoGPS('42.5555767770856,  -6.60079929046332, 522.200012207031,2017-04-29T06:29:36Z')
# x= puntoGPS('42.5556378811597,  -6.60108259879052, 522,             2017-04-29T06:29:36Z')


# a= puntoGPS('42.555333953350782,-6.600539200007916,523,2017-04-29T06:29:36Z')
# b= puntoGPS('42.555370582267642,-6.600550264120102,522.4000244140625,2017-04-29T06:30:10Z')
# c= puntoGPS('42.555432105436921,-6.600585635751486,522.20001220703125,2017-04-29T06:30:12Z')
# d= puntoGPS('42.555539309978485,-6.60067381337285,522.4000244140625,2017-04-29T06:30:15Z')

# print("%8.4f metros %8.4f metros" %(haversine(a,b),haversine2(a,b)))
# print("%8.4f metros %8.4f metros" %(haversine(b,c),haversine2(b,c)))
# print("%8.4f metros %8.4f metros" %(haversine(c,d),haversine2(c,d)))

# quit()
puntos=cargaFichero('101.csv')

procesaPuntos(puntos)

desde=float(input("Desde punto km:"))
hasta=float(input("Hasta punto km:"))

incs: float = 0
incb: float = 0
for idxpto in range(1,len(puntos)):
    if (puntos[idxpto].accDist<desde*1000) or (puntos[idxpto].accDist>hasta*1000):
        continue;
    if (puntos[idxpto].incAltura>0):
        incs += puntos[idxpto].incAltura
    else:
        incb += puntos[idxpto].incAltura
    # print("%5d: %s" %(idxpto+1,puntos[idxpto].toStr()))
print("Sube: %8.2f\nBaja: %8.f" %(incs,incb))

