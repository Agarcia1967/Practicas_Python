# Ejercicio 2 
# Escribir un programa que solicite un número entero n mientras que éste no sea positivo y 
# que muestre el dato proporcionado.

entrada=int(input("Introduzca un numero:"))
while (entrada<0):
    entrada=int(input("Introduzca un numero:"))
print(entrada)


# Alternativa
entrada = -1
while True:
    # La primera vez no cumplira la condicion y seguira pidiendo la entrada
    if (entrada>=0):
        break
    entrada=int(input("Introduzca un numero:"))
print(entrada)

