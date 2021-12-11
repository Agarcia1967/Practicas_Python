# Ejercicio 9.- 
#Define la función fibonacci(n) para que retorne el enésimo elemento de 
# la sucesión de Fibonacci. Esta sucesión, se obtiene de la forma siguiente:
# 𝑓𝑖𝑏𝑜𝑛𝑎𝑐𝑐𝑖(𝑛) = 
#            1 si 𝑛 = 0
#            1 si 𝑛 = 1
#            𝑓𝑖𝑏𝑜𝑛𝑎𝑐𝑐𝑖(𝑛 − 1) + 𝑓𝑖𝑏𝑜𝑛𝑎𝑐𝑐𝑖(𝑛 − 2) si 𝑛 > 1
# Escribe un programa que solicite por teclado un número entero no negativo y muestre en 
# pantalla el término correspondiente de la sucesión de Fibonacci.
# Resultado esperado para n = 9 -> 55

def fiobonacci(n:int):
    if n<2:
        return 1
    else:
        return fiobonacci(n-1) + fiobonacci(n-2)


# Otra forma mas pegada a la definicion que nos da el enunciado
def fio2(n:int):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else: 
        fio2(n-1) + fio2(n-2)

# Usamos la funcion que hemos escrito anteriormente 
from getPositivo import getIntPositivo


n=getIntPositivo("Introduce un numero para calcular Fiobonacci:")
f=fiobonacci(n)
print(f"fiobonacci({n})={f}")