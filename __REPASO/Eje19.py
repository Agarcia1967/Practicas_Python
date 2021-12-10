# Ejercicio 19. 
# Escribe un programa que lea el fichero “LigaJ16” 
# y calcule: 
# el porcentaje de partidos que ganó el equipo local (el primero), 
# el porcentaje de empates y de victorias de equipos visitantes (el segundo).

def escribeporcentaje(txt:str, cuantos: int, total: int): print ('%s : %5.2f por 100' %(txt,cuantos/total*100))

f=open('LigaJ16.txt')
datos=f.readlines()
f.close()

# Cada linea de datos tiene la siguiente forma:
# Atletico 1-2 Mallorca
# Real Sociedad 0-2 Real Madrid
# Vamos a usar la funcion split para dividir
ganalocal=0
ganavisitante=0
empate=0
for item in datos:
    linea=item.split('-')
    # Ahora linea es una lista con dos item
    # ['Granada 2', '1 Alaves\n']
    # ['Sevilla 1', '0 Villarreal\n']
    # Vamos a aplicar split ahora a cada uno de los item de la linea
    local=linea[0].split(' ')
    visitante=linea[1].split(' ')
    # Ahora en el ULTIMO item de la lista de local tenemos el resultado
    # y en el PRIMERO de la lista de visitante tenemos el resultado de visitante
    goleslocal=int(local[-1])
    golesvisitante=int(visitante[0])
    # Ahora ya tenemos los goles de cada uno, calculemos lo que nos piden
    if (goleslocal>golesvisitante):
        ganalocal=ganalocal+1
    elif (goleslocal==golesvisitante):
        empate=empate+1
    else:
        ganavisitante=ganavisitante + 1

escribeporcentaje('Visitantes ganaron en',ganavisitante,len(datos))
escribeporcentaje('Locales    ganaron en',ganalocal,len(datos))
escribeporcentaje('Los empates fueron   ',empate,len(datos))