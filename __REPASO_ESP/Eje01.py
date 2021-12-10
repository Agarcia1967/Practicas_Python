# Ejercicio 1. 
# Escribe una función que pida números al usuario hasta recibir tres mayores que 10. 
# Devuelve la media de esos tres. Comprueba su funcionamiento con un programa que utilice la función.

def pidenumero()->float :
    cuantos=0
    suma =0
    while (cuantos<3):
        numero=0
        while (numero< 10):
            numero = float(input("Dame un numero"))
        suma = suma + numero
        cuantos=cuantos+1
    return suma / cuantos

print("%f es la media" %(pidenumero()))