from puntoGPS import puntoGPS
from typing import List
import gpxpy
import gpxpy.gpx

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

def cargaFicheroXML(fichero:str)->List[puntoGPS]:
    result=[]
    gpx_file = open(fichero, 'r')

    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # print(f'Point at ({point.latitude},{point.longitude}) -> {point.elevation} {point.time}')
                pto=f'{point.latitude},{point.longitude},{point.elevation},{point.time.__format__("%Y-%m-%dT%H:%M:%SZ")}'
                # print (point.time.__format__('%Y-%m-%dT%H:%M:%SZ'))
                result.append(puntoGPS(pto))
    return result