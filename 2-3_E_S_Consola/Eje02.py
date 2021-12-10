# Ejercicio 2.- Añadir al programa del Ejercicio 1 las sentencias necesarias para realizar la
# salida de datos por pantalla de la forma siguiente:
# La nota media de Juan es 3.25 (o el valor que corresponda)
# Aprueba la asignatura: False (o el valor que corresponda
nombre=input('¿Cuál es tu nombre?:')
# Leemos el valor,como una cadena, para que se interprete como numero lo forzamos con int()
# Suponemos que las notas son numeros enteros, sino usar la funcion float() en vez de int()
nota1=int(input('Dime la primera nota:'))
nota2=int(input('Dime la segunda nota:'))
media=(nota1+nota2)/2
# Las palabras True y False deben ir con la primera en mayuscula, sino no será valido
if (media >=5):
     aprobado= True 
else: 
    aprobado= False
print(f"La nota media de {nombre} es {media}")
print(f"Aprueba la asignatura: {aprobado}")