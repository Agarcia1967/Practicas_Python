# Ejercicio 3.- 
# Escribir un programa que lea del teclado número a número. 
# La lectura de números termina con un número negativo. 
# El programa debe mostrar la media aritmética de los números introducidos.

suma=0
cantidad=0
while True:
    numero=int(input("Introduzca un numero (negoativo para acabar):"))
    if (numero < 0):
        break
    cantidad += 1
    suma += numero
    
if ( cantidad > 0 ):
    print("media=", suma / cantidad)
else:
    print("no hay datos para calcular la media")
