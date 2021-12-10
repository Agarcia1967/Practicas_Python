# Ejercicio 14. 
# Escribe una función que reciba una lista de números 
# y devuelva 
#      True si la multiplicación de los números menores que 5 de la lista 
#              es mayor que la suma de los números mayores o iguales que 5, 
#    y False en otro caso. 
# Comprueba su funcionamiento con un programa que utilice la función.

def funcion(lista: list)->bool:
    suma=0
    producto=1
    for i in lista:
        if (i<5):
            producto *= i
        else:
            suma += i
    if (producto>suma):
        return True
    return False

def test(listatest:list): print('Lista: ',listatest,' Cumple criterio',funcion(listatest))

test([1,2,5])
test([1,2,4,5])
test([])
test([1,2,4,5,100])
