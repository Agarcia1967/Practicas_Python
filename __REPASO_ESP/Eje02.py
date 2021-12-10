# Ejercicio 2. Escribe una función que reciba un número n 
# y devuelva ∑(k=1,𝑛)=k**2 
# y  𝑘=1y𝑛(𝑛+1)(2𝑛+1)/6. 
# Comprueba que ambos valores son iguales con un programa que utilice la función

def sumatorio(n): 
    suma =0
    for k in range(1,n+1):
        suma = suma + k**2
    return suma

def producto(n): return n*(n+1)*(2*n+1)/6

def comprobacion(n:int)-> bool: return (sumatorio(n)-producto(n) == 0)

def test(n:int): 
    a= sumatorio(n)
    b= producto(n)
    print("%d -> %d %d %d" %(n, a,b,a-b), comprobacion(n))

test(2)
test(3)
test(4)
test(100)