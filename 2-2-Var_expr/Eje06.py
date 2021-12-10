# Ejercicio 6.- Año Bisiesto 
# Crea una variable anyo entera y asígnale el valor 2011. 
# Crea otra variable llamada  bisiesto y asígnale una expresión lógica 
# que sirva para determinar si el año almacenado en la variable anyo corresponde a un año bisiesto o no.  
# Un año es bisiesto de acuerdo con la siguiente definición: 
# “Un año es bisiesto si 
#       * es divisible entre 4, 
#       * excepto el último de cada siglo (aquel divisible por 100), 
#       * salvo que sea divisible por 400.” 
# Ejemplos: años bisiestos (2000, 2012, 2024), no bisiestos (2011, 2013, 2100)  

year = 2011

divisiblecuatro = (year % 4 == 0)
divisiblecien = (year % 100 == 0)
divisiblecuatrocientos = (year % 400 == 0)

bisiesto = divisiblecuatro and divisiblecien and divisiblecuatrocientos

print(f"{year} es bisiesto? {bisiesto}")


## Usando una funciones

# Esta funcion nos dice si un numero es divisible por un factor (resto cero)
def esdivisible(numero,factor): return (numero % factor ==0) 


# Esta función nos devuelve True/False si un año es bisiesto. Ver descripcion.
def esbisiesto(year): return esdivisible(year,4) and esdivisible(year,100) and esdivisible(year,400)


# Esta función nos calcula si un año es o no bisiesto
def CalculaBisiesto(year):
    if (esbisiesto(year)):
        print (f"{year} es bisiesto")
    else:
        print (f"{year} NO es bisiesto")


# Ahora simplemente llamamos a la función que realiza el trabajo de calcular e imprimir los resultados
CalculaBisiesto(2011)
CalculaBisiesto(2000)
CalculaBisiesto(1900)
CalculaBisiesto(2012)
CalculaBisiesto(2024)