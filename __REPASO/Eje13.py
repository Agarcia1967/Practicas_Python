# Ejercicio 13. 
# Escribe un programa que tome una lista 
# y cambie cada número de la lista por su triple.

def triplica(lista: list)->list:
    for i in range(len(lista)):
        lista[i]*=3
    return lista

def test(l:list):
    print('Antes de triplicar  :',l)
    triplica(l)
    print('Despues de triplicar:',l)

lista=[2,4,5,6]
test(lista)
test([])
test([1,4,30,50,1200])