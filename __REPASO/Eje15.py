# Ejercicio 15. 
# Escribe un programa que recibe dos listas 
# y modifica la primera para eliminar todos los ceros que tenga 
# y añadirle todos los elementos de la segunda que no contenga ya.

def join(l1:list, l2:list)->list:
    # Vamos a eliminar los cero
    # for item in l1:
    #    if (item==0):
    #        l1.remove(item)
    while (0 in l1):
        l1.remove(0)
    # Ahora recorremos l2 para actualizaar l1 con los que no tenga
    for item in l2:
        # Buscamos cada elemento de l2 en l1 y sino esta lo añadimos
        if (not item in l1):
            l1.append(item)
    return l1

def test(lista1:list,lista2:list):
    print('Lista 1   ;',lista1)
    print('Lista 2   ;',lista2)
    join(lista1,lista2)
    print('Lista join:', lista1)
    print()


test([1,2,3,0,4,0,5,6],[1,2,3])
# Al estar 0 en l2, en la join saldra
test([1,2,3,0,4,0,5,6],[7,8,0])
test([],[])
test([1,2,3,4],[5,6,7])
test([],[1,2,3,4,5,6,7])
test([1,2,3,4,5,6,7],[])
test([0,0,0,4,0,0,0],[1])