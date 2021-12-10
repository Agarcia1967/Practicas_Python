# Ejercicio 7.- 
# Sea linea(ch, n) una función que retorna una cadena de n caracteres ch, 
# cuya definición se da al final del enunciado, se pide:
# 1. Definir una función cuadrado(ch, n) para un carácter ch y un entero positivo 
# n dados, que retorne una cadena de caracteres que cumpla lo siguiente: impresa 
# en pantalla debe dar lugar a un cuadrado relleno con caracteres ch de n líneas. 
# Dado que en la pantalla la separación entre líneas es, aproximadamente, el doble que 
# entre dos caracteres consecutivos de una misma línea, para no desvirtuar en exceso 
# el cuadrado el número de caracteres por línea deberá ser el doble de éstas.
def cuadrado(ch:str,n:int):
    result:str=''
    # Se podria usar ch[0] por si en la entrada pusieran mas de un caracter
    # Esto es un REFINAMIENTO ...
    ch=ch[0]
    for lineas in range(n):
        for columnas in range(2*n):
            result= result + ch
        result = result + '\n'
    return result


# 2. Utilizando la función definida anteriormente, escribe un programa que solicite por 
# teclado un número entero positivo y un carácter y muestre en pantalla un cuadrado 
# relleno en la forma ya indicada.
#
from getPositivo import getIntPositivo

ch=input("Introduce un caracter:")
n=getIntPositivo("Introduce el numero de filas:")
print(cuadrado(ch,n))

