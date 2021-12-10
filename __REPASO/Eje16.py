# Ejercicio 16. 
# Escribe un programa que implemente el siguiente juego. 
# Primero, se pide al usuario el número de jugadores. 
# Después, se les pide que adivinen tu altura exacta. 
# El programa devuelve 
# una lista con la distancia a la que se ha quedado cada uno 
# e informa de qué jugador ha ganado al ser el que se ha quedado más cerca.

mialtura=168

n=int(input("¿Cuantos jugadores hay?"))

estimaciones=[]
for idx in range(n):
    print ('Jugador %d ¿Que altura estimas que tengo?:' %(idx  ))
    alturaestimada=int(input())
    estimaciones.append(alturaestimada)
# Ahora tengo la lista con todas las alturas
# Vamos a calcular las diferencias 
# Ahora tengo que encontrar el minimo en valor absoluto, ese sera el posganador
posganador=0
for idx in range(len(estimaciones)):
    estimaciones[idx]=abs(mialtura-estimaciones[idx])
    print('El jugador %d ha quedado a %f de acertar' %(idx,estimaciones[idx]))
    if (estimaciones[idx]<estimaciones[posganador]):
        posganador=idx
print('El ganador ha sido %d con un error de %f' %(posganador,estimaciones[posganador]))

