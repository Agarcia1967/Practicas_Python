# Ejercicio 12. 
# Escribe una función que reciba un número 
# y devuelva 
#     la suma de todos los múltiplos de 2 menores que ese número 
#     y de todos los múltiplos de 3 menores que ese número. 
# Comprueba su funcionamiento con un programa que utilice la función.

# función que devuelve si un numero es multiplo de otro (divisible por divisor con resto cero)
def multiplo(numero: int, divisor:int)-> bool: return ( numero % 2 == 0 )

def funcion(numero:int)->int:
    suma=0
    for idx in range(numero):
        # Hecho asi solo suma el valor una vez cuando sea divisible por ambos
        # Si quisieramos hacer para los divisibles por 2 y tambien cuando lo sea por 3
        # podriamos poner dos if seguidos (al mismo nivel)
        # if multiplo(idx,2): suma ´+= idx 
        # if multiplo(idx,3): suma ´+= idx
        if multiplo(idx,2) or multiplo(idx,3):
            suma += idx
    return suma

def test(n:int): print("test funcion(%d)=%d" %(n, funcion(n)))

# print("test con valor 10 : %d" %(funcion(10)))
# print("test con valor 2  : %d" %(funcion(2)))
# print("test con valor 3  : %d" %(funcion(3)))
# print("test con valor 6  : %d" %(funcion(6)))

test(10)
test(2)
test(3)
test(6)
test(100)