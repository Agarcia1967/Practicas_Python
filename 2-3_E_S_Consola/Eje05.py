# Ejercicio 5.- 
# Hacer un programa en Python que pida por teclado una distancia en metros  
# e imprimir esa distancia en 
#   pulgadas, 
#   pies, 
#   yardas... 
# Buscar los factores de conversión en  la red.
# 
metros=float(input('Distancia en metros a convertir:'))
# Una forma basica seria usando un print para cada caso
#
# print(f"{metros} metros son {metros*39.37008} pulgadas")
# print(f"{metros} metros son {metros*3.2808} pies")
# print(f"{metros} metros son {metros*1.09} yardas")
#
# como todas ellas son iguales, vamos a usar una función


def convierte(distancia_metros, factor_conversion, nombre_unidad):
    print(f"{distancia_metros} metros son {distancia_metros*factor_conversion} {nombre_unidad}")
    return


#
# Ahora llamamos a la función con los parametros que necesita y obtenemos el resultado.
#

convierte(metros,39.37008,"pulgadas")
convierte(metros,3.28008,"pies")
convierte(metros,1.09,"yardas")
convierte(metros,0.00062137, "millas") 
# Puedes poner mas ...

convierte(metros,0.001, "km") 



