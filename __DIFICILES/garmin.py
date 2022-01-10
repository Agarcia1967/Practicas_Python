# Ejercicio
# https://es.wikiloc.com/rutas-mountain-bike/101-peregrinos-2019-35798838
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


from datetime import datetime
from puntoGPS import puntoGPS
# from funcaux import datetime_to_float
from repositorio import *
from servicios import *
from puntoAgregado import *



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

def test_createGPS():
    assert (1==1)

puntos=cargaFichero('101.csv')
puntos=procesaPuntos(puntos)

repo=RepositorioAgregado()
repo.fromPtos(puntos)

print ("%s" %(repo.toStr()))

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
print("Sube: %8.2f\nBaja: %8.2f\n" %(incs,incb))
