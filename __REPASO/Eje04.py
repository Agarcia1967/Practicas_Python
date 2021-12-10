# Ejercicio 4. 
# Escribe un programa que muestre la siguiente pregunta: “¿En qué provincia está Gijón?”. 
# A continuación, en distintas líneas, muestra 
# “a) Asturias”, “b) Cantabria”, “c) Sevilla”. 
# Pide al usuario una opción e infórmale de si ha acertado la respuesta.

import sys

print("¿En qué provincia está Gijón?")
print("a) Asturias\nb) Cantabria\nc) Sevilla\n")
# respuesta=input("¿Cual es tu opción?")
print("¿Cual es tu opción?")
respuesta=sys.stdin.read(1)
if (respuesta=="a"):
    print("Has acertado")
else:
    print("Has fallado")