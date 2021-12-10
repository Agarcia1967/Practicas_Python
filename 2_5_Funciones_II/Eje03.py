# Ejercicio 3.- 
# Utilizando la función definida en el ejercicio anterior, escribe un programa 
# que muestre en pantalla la secuencia de números perfectos comprendidos entre 2 y un 
# número entero positivo umbral que se solicitará por teclado.
# Salida esperada para umbral = 10000 -> 6 28 496 8128

def divisible(numero:int,divisor:int): return (numero % divisor == 0)


def sumaDivisores(numero):
    suma:int=0
    for i in range(1,numero):
        if divisible(numero,i):
            suma=suma+i
    return suma


umbral:int=int(input("Dime un Umbral:"))

for idx in range(1,umbral+1):
    if (sumaDivisores(idx)==idx):
        print(idx," es perfecto")
