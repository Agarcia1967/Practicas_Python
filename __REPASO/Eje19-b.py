# Ejercicio 19. 
# Escribe un programa que lea el fichero “LigaJ16” 
# y calcule: 
#       el porcentaje de partidos que ganó el equipo local (el primero), 
#       el porcentaje de empates  
#       el porcentaje de victorias de equipos visitantes (el segundo).
#       el total y media de goles locales
#       el total y media de goles visitantes

# En este caso vamos a utilizar la lectura del fichero linea a linea
# Python no tiene una funcion EOF()  (end of file) como tal, sino que se detecta
# Para detectar el EOF cuando lea una linea que sea False habre llegado

# Para IMPRIMIR los resultados, necesitamos 
#      un texto, 
#      cuantos
#      total 
# para poder calcular el porcentaje = cuantos/total
def escribeporcentaje(txt:str, cuantos: int, total: int):
    # Si total fuese cero no tendria sentido calcular nada
    if (total>0): 
       print ('%s : %5.2f por 100' %(txt,cuantos/total*100))
    else:
        print('%s : NO HAY DATOS')

# Para IMPRIMIR los resultados, necesitamos 
#      un texto, 
#      cuantosgoles
#      total de partidos(=lineas de fichero)
# para poder calcular el porcentaje = cuantos/total
def escribemedia(txt:str, cuantos: int, total: int):
    # Si total fuese cero no tendria sentido calcular nada
    if (total>0): 
       print ('%s : %d goles con una media por partido %4.2f goles' %(txt,cuantos,cuantos/total))
    else:
        print('%s : NO HAY DATOS')

# Inicializamos los contadores y varibles de acumulacion
ganalocal=0
ganavisitante=0
empate=0 
numeroLineas=0
totalgolesvisitante=0
totalgoleslocales=0
f=open('LigaJ16.txt','r')

# Usaremos un bucle "infinito" del que saldremos con un break cuando detectemos el fin de fichero
while True:
    # Leemos una linea de cada vez
    lineaFichero = f.readline()
    # Vamos a detectar el EOF, Cuando ocurra esto salimos del bucle while usando break
    if not (lineaFichero):
        break
    # Si llegamos a este punto, es que hemos leido una linea. Procesemosla
    numeroLineas=numeroLineas + 1
    # Cada linea de datos tiene la siguiente forma:
    #      Atletico 1-2 Mallorca
    #      Real Sociedad 0-2 Real Madrid
    # Vamos a usar la funcion split para dividir en dos la cadena, usando el - como separador
    linea=lineaFichero.split('-')
    # Ahora linea es una lista con dos items
    # Ejemplo:
    #       ['Granada FC 2', '1 Alaves\n']
    #       ['Sevilla 1', '0 Villarreal\n']

    # Vamos a aplicar split ahora a cada uno de los elementos de la linea para "romper" el string en partes
    # Cada parte contendrá un string, y en concreto los datos del resultado.
    local=linea[0].split(' ')
    visitante=linea[1].split(' ')
    # Ahora :
    #      el ULTIMO  item de la lista de local     tenemos el resultado de local
    #      el PRIMERO item de la lista de visitante tenemos el resultado de visitante
    # Ejemplo:
    #       local = ['Granada','FC', '2']   !FIJATE QUE TIENE TRES ITEMS!
    #       visitante=   ['1', 'Alaves\n']  !EN ESTE CASO SOLO DOS!
    # Tener en cuenta que hay nombres compuestos, luego el local esta en el ULTIMO 
    # no necesariamente en el segundo item de la lista

    # Vamos a convertir el string en un entero para poder procesarlos
    # El resultado de local esta el ultimo, usanos -1
    goleslocal=int(local[-1])  
    golesvisitante=int(visitante[0])
    # Tenemos los goles de cada uno en una variable INT, calculemos lo que nos piden
    totalgolesvisitante += golesvisitante
    totalgoleslocales += goleslocal    
    # print('local %d-%d visitantes  (%d,%d)' %(goleslocal,golesvisitante,totalgoleslocales,totalgolesvisitante))
    if (goleslocal>golesvisitante):
        ganalocal=ganalocal+1
    elif (goleslocal==golesvisitante):
        empate=empate+1
    else:
        ganavisitante=ganavisitante + 1
# Hay que cerrar el fichero
f.close()

# Vamos a imprimir los resultados
escribeporcentaje('Visitantes ganaron en',ganavisitante,numeroLineas)
escribeporcentaje('Locales    ganaron en',ganalocal,numeroLineas)
escribeporcentaje('Empates              ',empate,numeroLineas)

escribemedia('LOCALES   ',totalgoleslocales,numeroLineas)
escribemedia('VISITANTES',totalgolesvisitante,numeroLineas)