# Ejercicio 6.- 
# Define una función para que dados dos números enteros positivos, el segundo en el rango [2, 16], 
# retorne una cadena de caracteres con los dígitos correspondientes al primer número expresado en la base del segundo. 
# En el caso de que la base sea mayor que 10, se utilizarán también como dígitos los caracteres alfabéticos 
# necesarios por orden y comenzando por la letra ‘A’. 
# Existen funciones predefinidas en Python que pueden serte de utilidad. ¡Búscalas y utilízalas!
# Escribe un programa que solicite por teclado un número entero no negativo 
# y muestre éste en pantalla en las bases: 2, 8, 10 y 16. 

# Para realizar un cambio de base se procede de la siguiente manera:
# 
# Si el ",numero," es menor que la base se calcula el simbolo que le corresponde (0..9,A..F)
# En caso contrario se calcula el nuevo numero y se añade el simbolo que representa la base
def toStr(n:int,base:int):
    convertString: str = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]


# Esta funcion OBLIGA a que el valor sea positivo, sino sigue preguntando
def getPositivo(texto:str):
    entrada:int=-1
    while (entrada<0):
        entrada=int(input(texto))
    return entrada


numero=getPositivo("Dame un numero entero positivo:")
print("El ",numero," en base 16 es:",toStr(numero,16))
print("El ",numero," en base 10 es:",toStr(numero,10))
print("El ",numero," en base  8 es:",toStr(numero,8))
print("El ",numero," en base  2 es:",toStr(numero,2))