# EJERCICIO 1. LEER UNA LISTA DE NÚMEROS DE UN FICHERO 
# Descarga el fichero llamado datos.txt. 
# Observa que este fichero se compone de una serie de líneas, en  cada una de las cuales hay un número entero. 
# Escribe una función que reciba como parámetro el nombre del fichero 
# y devuelva como resultado una  lista con los números leídos del fichero. 
# Aplica la función sum() de python sobre esta lista para averiguar la  suma de todos los datos que has leído
# 1. Debe salirte 49195.

def leeFichero(nombre): 
    f=open(nombre)
    datos=f.readlines()
    f.close()
    # Aqui tenemos en datos una lista de STRING que debemos convertir en lista de INT
    # Para ello la vamos a recorrer (datos) y convertimos cada elemento en un entero que AÑADIMOS (append)
    # Devolvemos la lista resultado, que es la transformacion de la anterior
    resultado = []
    for linea in datos:
        resultado.append(int(linea.rstrip()))
    return resultado


numeros=leeFichero('datos.txt')
# Ahora aplicamos la funcion sum() a la lista de enteros que nos devuelve el leeFichero
print(sum(numeros))