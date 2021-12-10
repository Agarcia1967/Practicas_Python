# Ejercicio 1
# Escribir un programa que lea del teclado carácter a carácter. 
# La lectura de caracteres se termina con “.”
# El programa debe mostrar el número de veces que se ha introducido el carácter "a".

caracter=''
contador=0
while True:
    if (caracter=='.'):
        break
    entrada=input("Introduzca un caracter(. para acaba)")
    # Asumimos que ha introducido algo, sino fallara
    caracter=entrada[0]
    if (caracter=='a'):
        contador = contador +1
print(f"El numero de caracteres a es {contador}")

# Alternativa a la version anterior.

def leeCaracter():
    entrada=input("Introduzca un caracter(. para acaba)")
    # Asumimos que ha introducido algo, sino fallará
    return entrada[0]


caracter=leeCaracter()
contador=0
while (caracter!=','):
    if (caracter=='a'):
        contador=contador+1
    caracter=leeCaracter()
print(f"El numero de caracteres a es {contador}")
