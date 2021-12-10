# Ejercicio 2. 
# Escribe un programa que implemente el siguiente juego. 
# Se pide al  usuario el nombre de dos jugadores 
# y ambos intentan adivinar el radio que debe tener una circunferencia para que su área sea 31,51.
# El programa calcula la distancia a la que se han quedado ambos jugadores y 
# devuelve, en distintas líneas, los mensajes “[Nombre 1] ha errado por [distancia 1]” y
# “[nombre 2] ha errado por [distancia 2]”. Las distancias se mostrarán con dos 
# decimales. Utiliza una sola función print.

PI = 3.1416

def error(radio): return 31.51-PI-radio**2

def msg(nombre,err): return "El jugador %s ha errado por %.2f" %(nombre,err)

j1=input("Nombre jugador 1")
r1=float(input("Radio de jugador 1"))

j2=input("Nombre jugador 2")
r2=float(input("Radio de jugador 2"))

salida: str = msg(j1,error(r1)) + '\n' + msg(j2,error(r2))

print("%s\n%s" %(salida))