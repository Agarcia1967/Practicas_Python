# Ejercicio 1.- 
# Define una función que retorne el factorial de un número entero no negativo
def factorial(numero : int):
    result: int = 1
    for i in range(1,numero+1):
        result = result * i
    return result

    
# dado y escribe un programa que solicite un número entero no negativo 
entrada: int =int(input("numero positivo para calcular su factorial:"))
# y muestre en  pantalla éste y su factorial.
if (entrada > 0):
    print("El factorial de ", entrada, " es : ", factorial(entrada))
