n=0 #Variable que recoge los numeros del usuario (n=0 para que entre en el bucle)
media=0 #Variable que recoge la suma de los números
cuenta=0 #Variable que cuenta cuántos números llegan
while n>=0: #Cuando n<0, paramos
    n=float(input("Dame un número: "))
    if n>=0:
        media=media+n #Sumamos el último número recibido
        cuenta=cuenta+1 #Contamos el último número recibido
media=media/cuenta #Media final (Fuera del bucle)
print(media)
