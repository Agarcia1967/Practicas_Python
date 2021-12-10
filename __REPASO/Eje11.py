9# Ejercicio 11. 
# Escribe una función que reciba dos nombres 
#     devuelva el más corto de ellos 
#     o, en caso de ser igual de largos, el primero. 
# 
# Comprueba su funcionamiento con un programa que utilice la función.

def nombre(n1:str, n2:str)->str:
    if (len(n1)>len(n2)):
        return n2
    else:
        # Sino es mayor n1 que n2 entonces es menor o igual,
        # luego en ambos casos devuelvo n1
        return n1

# Vamos a usar otra "función" para hacer el test
def test(n1:str, n2:str): print ('nombre("%s","%s")="%s"' %(n1, n2, nombre(n1,n2)))

# Ahora hacemos el test
test('Pepe','Juan')
test('Pepe','Juan Luis')
test('Pepe Luis','Juan')
test('Pepe','')
test('','Juan')
test('124 345','3453453453')
        
    