# Ejercicio 7.- 
# Escribe un programa que lea por teclado enteros positivos número a número 
# y proporcione 
#       el mayor de ellos 
#       y la posición en la que éste se introdujo. 
# La lectura de números terminará si se introduce el valor 0.
# Ejemplo de salida para la entrada: 100 25 36 596 3 15 0
# El mayor número es 596 y se proporcionó en la posición 4

posicion=-1
mayor=-1
idx=0
numero=1
while (numero!=0):
    numero=int(input("Introduzca un numero (cero para acabar):"))
    if (numero>0):
        idx+=1
        if (numero>mayor):
            mayor=numero
            posicion=idx

if (posicion>0):
    print(f"El mayor numero es {mayor} y se proporcionó en la posición {posicion}")
else:
    print("No hay datos")