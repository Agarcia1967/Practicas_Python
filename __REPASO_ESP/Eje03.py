# Ejercicio 3. 
# ∑ K(1,infinito) 1/k es una serie divergente: la suma tiende a infinito. 
# Compruébalo con una función que reciba un número 
# y calcule cuántos términos de la serie hay que sumar para superar dicho número. 
# Comprueba su funcionamiento con un programa que utilice la función. 
# Por ejemplo, la salida para 5 debe ser: 
# Para superar el 5 es necesario sumar 83 términos de la serie.

def calculatermino(limite:int)->int:
    suma:float=0
    idx=1
    while (suma < limite):
        suma += 1/idx
        idx+=1
    return idx-1

def test(n): print("Para superar el %d hacen falta %d terminos" %(n,calculatermino(n)))

test(1)
test(5)
test(10)
test(15)