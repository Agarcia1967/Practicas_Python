# Ejercicio 9.- 
#Define la funciΓ³n fibonacci(n) para que retorne el enΓ©simo elemento de 
# la sucesiΓ³n de Fibonacci. Esta sucesiΓ³n, se obtiene de la forma siguiente:
# πππππππππ(π) = 
#            1 si π = 0
#            1 si π = 1
#            πππππππππ(π β 1) + πππππππππ(π β 2) si π > 1
# Escribe un programa que solicite por teclado un nΓΊmero entero no negativo y muestre en 
# pantalla el tΓ©rmino correspondiente de la sucesiΓ³n de Fibonacci.
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