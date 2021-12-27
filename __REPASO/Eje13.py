# Ejercicio 13. 
# Escribe un programa que tome una lista 
# y cambie cada número de la lista por su triple.

def triplica(lista: list)->list:
    for i in range(len(lista)):
        lista[i]*=3
    return lista

# En este caso vamos a devolver una nueva lista con los valores calcuados
def triplica2(lista:list)->list:
    nuevalista=[]
    for ele in lista:
        nuevalista.append( ele * 3 )
    return nuevalista

def test(l:list):
    print('Antes de triplicar  :',l)
    print('Despues de triplicar:',triplica2(l))
    

lista=[2,4,5,6]
test(lista)
test([])
test([1,4,30,50,1200])