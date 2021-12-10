# Ejercicio 5.- Datos Representados en Cadenas 
# 1. Crea dos variables: 
#       base que contenga el valor entero 9 y altura el valor 5.
base = 9
altura = 5
# Supuesto que ambas variables representan mediante enteros la base y la altura,  respectivamente, de un triángulo, 
# calcular en otra variable llamada area, que  debe ser de tipo str, el texto que representa el área del triángulo. 
# El resultado debería ser la cadena ’22.5’. Debes usar una única expresión.
area = str( ( base * altura )  / 2 )
# 2. Crea una variable llamada mensaje que sea igual a la concatenación del texto  
mensaje = 'El area del triangulo es igual a ' + area 
# “El area del triangulo es igual a” y el valor de la variable area. 
print (mensaje)
# 3. Ahora al revés. 
# Cambia el valor de las variables base y altura de forma que ahora guarden las cadenas ‘5’ y ‘7’ respectivamente. 
base='5'
altura='7'

# Después calcula en la  variable area, que ahora debe ser de tipo float, el área de dicho triángulo. 
## Debemos de covertir el tipo de string a float para proceder al calculo
area= float(base)*float(altura)/2
# El  resultado debe ser 17.5. 
# Actualiza el valor de la variable mensaje. ¿Debes  cambiar algo en la expresión usada anteriormente? 
## Ahora area es un float, necesito convertirlo a string para añadirlo al mensaje
mesaje = 'El area del triangulo es igual a ' + str(area)
print(mensaje)
