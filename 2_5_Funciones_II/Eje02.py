# Ejercicio 2.- 
# Define una función que retorne la suma de todos los divisores propios positivos de un número dado, 
# sin incluirse él mismo. 
# Utiliza ésta para escribir un programa que solicite por teclado un número entero positivo mayor que uno 
# y muestre en la pantalla si éste es o no perfecto.
# Nota. Un número entero positivo es perfecto cuando es igual a la suma de todos sus divisores propios positivos
# El 28 es perfecto

# Definimos una funcion que nos dice si un numero es divisible por un divisor dado
def divisible(numero:int,divisor:int): return (numero % divisor == 0)


def sumaDivisores(numero:int):
    suma:int=0
    for i in range(1,numero):
        if divisible(numero,i):
            suma=suma+i
    return suma


entrada=int(input("Dime un numero:"))

if (sumaDivisores(entrada)==entrada):
    print(entrada," es perfecto")
else:
    print(entrada," NO es perfecto")