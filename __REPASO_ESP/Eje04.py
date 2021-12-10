# Ejercicio 4. 
# Escribe una función que compruebe si un número dado es primo 
# (únicamente divisible entre 1 y sí mismo) o no (True/False). 
# Utilízala en un programaque muestre, para un número n dado, 
# todos los números primos menores que n separados por comas.

def esDivisible(n,divisor): return ( n % divisor == 0 )

def esPrimo(n:int)->bool:
    # Los divisores estan ente 2 y n-1
    if (n<2): return False
    primo=True
    for divisor in range(2,n):
        primo = primo and not esDivisible(n,divisor)
        # Aqui se podria poner una condicion, para que en cuanto encuentre un divisor 
        # no siga mirando ya que no será primo
        # 
    return primo

def escribePrimosMenores(n:int):
    for idx in range(1,n):
        if (esPrimo(idx)):
            print(idx,end=',')
    print()

n=0
while (n<1):
 n=int(input("Dame un numero (mayor que cero):"))

escribePrimosMenores(n)
