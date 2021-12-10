# Ejercicio 1.- 
# Hacer un programa en Python que haga lo siguiente:
# o Lea por teclado el nombre y dos notas de un alumno.
# o  Calcule la nota media.
# o Guarde en una variable el valor booleano “verdadero” si la nota media es mayor
# o  igual que 5 y “falso” en caso contrario
nombre=input('¿Cuál es tu nombre?:')
# Leemos el valor,como una cadena, para que se interprete como numero lo forzamos con int(). 
# Suponemos que las notas son numeros enteros, sino usar la funcion float() en vez de int()
nota1=int(input('Dime la primera nota:'))
nota2=int(input('Dime la segunda nota:'))
media=(nota1+nota2)/2
# Las palabras True y False deben ir con la primera en mayuscula, sino no será valido
if (media >=5):
     aprobado= True 
else: 
    aprobado= False
# Esto no es necesario, solo para comprobar los resultados
print(f"Nombre:{nombre} Nota1:{nota1} Nota2:{nota2} Media:{media} Aprobado:{aprobado} ")
