# Ejercicio 4.- 
#  un programa que lea del teclado número a número. La lectura de números termina con un número negativo. 
# El programa debe mostrar 
#         la media aritmética de los números pares leídos 
#       y la media aritmética de los números impares leídos

sumapares=0
cantidadpares=0

sumaimpares=0
cantidadimpares=0
while True:
    numero=int(input("Introduzca un numero (negoativo para acabar):"))
    if (numero < 0):
        break
    if ( numero % 2 == 0 ):
        cantidadpares += 1
        sumapares += numero
    else:
        cantidadimpares += 1
        sumaimpares += numero

    
if ( cantidadpares > 0 ):
    print("media Pares=", sumapares / cantidadpares)
else:
    print("no hay datos para calcular la media de los pares")


if ( cantidadimpares > 0 ):
    print("media Impares=", sumaimpares / cantidadimpares)
else:
    print("no hay datos para calcular la media de los pares")