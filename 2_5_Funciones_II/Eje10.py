# Ejercicio 10.- 
# Utilizando la función fibonacci(n) que se define en el ejercicio previo, 
# escribe un programa que solicite por teclado un número entero m no negativo y muestre 
# en pantalla la sucesión que resulta de sumar los k primeros números de la sucesión de 
# Fibonacci, con k = 0, 1, 2,…, m.
# Resultado esperado para m = 10 -> 1 2 4 7 12 20 33 54 88 143 232


def fiobonacci(n:int):
    if n<2:
        return 1
    else:
        return fiobonacci(n-1) + fiobonacci(n-2)

# Usamos la funcion que hemos escrito anteriormente 
from getPositivo import getIntPositivo

n=getIntPositivo("Introduce un numero para calcular la suma de los terminos de Fiobonacci:")
suma:int=0
for idx in range(0,n+1):
    f=fiobonacci(idx)
    suma = suma + f
    print(f"fiobonacci({idx})={f} suma={suma}")