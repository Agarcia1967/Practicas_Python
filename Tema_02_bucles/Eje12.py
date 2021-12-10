# Ejercicio 12
# Dado un número natural n, 
# escribe un algoritmo para determinar si éste es o no primo 
# (el 1 no es un número primo).

n=int(input("Introduzca un N (mayor o igual a 0):"))
if (n<0):
    print("El numero debe ser positivo")
    quit()

# El caso de n<2 no son primos
if (n<2):
    esPrimo=False
else:
    esPrimo=True

# Calculamos los divisores entre 2 y n-1. Recordar que range NO tomael valor de n
for idx in range(2,n):
    esPrimo = esPrimo and not(n % idx == 0)

if (esPrimo):
    print(f"{n} es Primo")
else: 
    print(f"{n} NO es Primo")