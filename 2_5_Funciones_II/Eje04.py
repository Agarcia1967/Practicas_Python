# Ejercicio 4
# Define una función, es_primo, que retorne 
#      cierto si un número entero dado es primo 
#      falso en caso contrario. 
# En la definición, se considerará que el número 1 no es primo.
# Escribe un programa que de forma repetitiva solicite por teclado un número entero mayor 
# que cero y muestre en pantalla si es o no primo, en la forma: El número 100 no es primo.
# El programa deberá finalizar cuando el dato que se introduzca por teclado no cumpla el 
# requisito de ser un entero mayor que cero.

# Empezamos con una funcion que nos diga si un numero es divisible de manera entera (resto cero)
def divisible(numero:int,divisor:int): return ( numero % divisor == 0 )


# Para ser primo no debe tener ningun divisor salvo la unidad y el mismo
# La varible primo empieza suponiendo que lo es, 
# y si encuentra algun divisor sera false (al usar la funcion and en cada iteracion)
def primo(numero:int):
    # El cero y el uno NO son primos
    primo:bool
    if (numero<2):
        return False
    # Empezamos suponiendo que es primo
    primo=True
    for idx in range (2,numero):
        primo = primo and not(divisible(numero, idx))
        # Este if lo que hace es cuando encuentra un divisor sale del bucle
        # En cuanto tenga un divisor ya no tiene sentido seguir buscando.
        # Esto es una optimizacion AVANZADA del algoritmo
        if not(primo):
            break
    return primo


 # print(primo(1))
 # print(primo(2))
 # print(primo(20))
 # print(primo(13))

# Vamos repetir todo HASTA que se cumpla la condicion (entrada sea cero o negativo)
while (True):
    entrada = int(input("Introduzca un numero (0 para salir):"))
    if (entrada<1):
        break;
    if (primo(entrada)):
       print(f"El numero {entrada} es primo")
    else:
        print(f"El numero {entrada} NO es primo")