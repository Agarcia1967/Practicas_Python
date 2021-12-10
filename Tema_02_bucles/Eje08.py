# Ejercicio 8.- 
# Dado un número entero n0, escribe un programa que imprima sus cifras de la menos a la más significativa.
# Ejemplo de salida del programa para la entrada: 7249:
# Las cifras del número 7249 de la menos a la más significativa son: 9 4 2 7

# Para hacer esto se divide sucesivamente el numero por 10 y se imprime el resto.


numero=int(input("Introduzca un numero (cero para acabar):"))
if (numero<0):
    print("El numero debe ser positivo")
    quit()
cifras=''
temporal=numero
while temporal > 0 :
    resto = temporal % 10
    cifras=cifras + ' ' + str(resto)
    temporal = int(temporal / 10)

print(f"Las cifras del número {numero} de la menos a la más significativa son: {cifras}")