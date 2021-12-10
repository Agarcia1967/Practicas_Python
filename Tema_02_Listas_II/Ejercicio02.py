# EJERCICIO 2. 
# ANALIZAR DATOS EN UN FICHERO 
# Descarga el fichero llamado alumnos.txt. 
# Contiene un listado de todos los alumnos matriculados en la  asignatura “Fundamentos de Informática” 
# en la EPI-Gijón, en el curso 2011-2012, pero por motivos de  privacidad de los datos se han intercambiado 
# aleatoriamente los apellidos y los nombres entre los alumnos.  
# Si das un vistazo al fichero, abriéndolo con el notepad++, verás que contiene un alumno por línea,  
# figurando en primer lugar el apellido y después, separado por coma, el nombre. 
# Realiza los ejercicios siguientes sobre los datos de este fichero. 
# • Escribe código python para determinar el número total de alumnos 
f=open('alumnos.txt')
alumnos=f.readlines()
f.close()
print('Numero de alumnos:',len(alumnos))
# • Escribe una función que reciba dos parámetros: 
#          una línea leída del fichero y 
#          un apellido de  persona, 
# y la función debe retornar “True” si cualquiera de los dos apellidos de la persona  coinciden con el apellido dado. 
# Por ejemplo: 
# >>> coincide_apellido("Lopez Alvarez, Andres", "Lopez") 
# True 
# >>> coincide_apellido("Lopez Alvarez, Andres", "Suarez") 
# False 
# >>> coincide_apellido("Lopez Alvarez, Andres", "Andres") 
# False
def coincide_apellido(linea, muestra): 
    resultado = muestra in alumnos[linea]
    print("Buscando ",muestra," en ", alumnos[linea].rstrip(), " con el resultado ",resultado)
    return resultado


print(coincide_apellido(0,"Calvo"))
print(coincide_apellido(15,"Ortega"))

# • Usando la función anterior, determina qué porcentaje de alumnos tiene “Fernandez” como  alguno de sus dos apellidos (debe salirte el 15,256%) 
cuantos=0
for idx in range(len(alumnos)):
    if (coincide_apellido(idx,"Fernandez")):
        cuantos=cuantos+1
porcentaje = cuantos / len(alumnos) * 100
print(porcentaje) 
# • Escribe una función que reciba como parámetro una línea del fichero 
# y retorne un entero que  indique cuántas palabras tiene el nombre.
#  Por ejemplo: 
# >>> palabras_en_nombre("Lopez Alvarez, Andres") 
# 1 
# >>> palabras_en_nombre("Suarez Fernandez, Jose Luis") 
# 2 
# >>> palabras_en_nombre("de Marichalar y Borbon, Felipe Juan Froilan de Todos los  Santos") 
# 7
def palabras_en_nombre(idx): 
    linea=alumnos[idx].split(",")
    nombre=linea[1].rstrip()
    result=len(nombre.split())
   # print(f"{nombre} tiene {result} palabras")
    return result


print(palabras_en_nombre(0))
print(palabras_en_nombre(1))
print(palabras_en_nombre(2))
# • Usando la función anterior, 
# escribe un programa que cuente cuántos alumnos tienen nombre  simple (1 palabra), cuántos de 2 palabras, etc. 
# Puedes usar una lista para cada posible número de  palabras, 
# de modo que numero_palabras[1] por ejemplo almacene cuántos tienen nombre simple,  
# numero_palabras[2] cuántos tienen 2 palabras, etc.. 
# Puedes asumir que no habrá nadie con más de 7 palabras 
# y por tanto darle a la lista un tamaño prefijado de 8 elementos 
# (ya que el elemento  [0], aunque no lo usaremos, está ahí) 

# !Cuidado! Si no te funciona ¿has tenido en cuenta que los elementos de la lista han de ser de tipo int?
# Tu programa comenzaría poniendo 8 ceros en esa lista, 
numero_palabras = []
for idx in range(8):
    numero_palabras.append(0)
# para después ir leyendo líneas del fichero 

for idx in range(len(alumnos)):
# y para cada una de ellas llamar a palabras_en_nombre() que le dirá que ese alumno tiene X  palabras en su nombre, 
    np = palabras_en_nombre(idx)
# y seguidamente incrementarás numero_palabras[X] para contar que hay  un alumno más con X palabras en su nombre. 
    numero_palabras[np] = numero_palabras[np] + 1
# Al final imprimes la lista numero_palabras (o si prefieres, solo los elementos con valor distinto  de cero). 

for idx in range(8):
    if (numero_palabras[idx]>0):
        print("Hay ",numero_palabras[idx]," nombres con ", idx, " palabras de longitud")
# Debe salirte que hay 
# Hay  225  nombres con  1  palabras de longitud
# Hay  10  nombres con  2  palabras de longitud
# Hay  4  nombres con  3  palabras de longitud
# Hay  2  nombres con  5  palabras de longitud
# Hay  1  nombres con  7  palabras de longitud 



