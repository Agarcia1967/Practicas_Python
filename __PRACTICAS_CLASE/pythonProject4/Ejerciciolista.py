def sum_pot1(l, n):
    s=0
    for item in l:
        s=s+item**n
    return s

def sum_pot2(l,n):
    # El array empieza vacio, sin elementos
    x=[]
    for item in l:
        # Fijate que para añadir elementos al array usa append, porque son elementos NUEVOS no creados todavia
        x.append(item**n)
    # devolvemos la suma
    return sum (x)



print(sum_pot1([5,11,9],2))
print(sum_pot2([5,11,9],2))

# La sum_pot1 es redundante ya que se puede escribir como un caso de la segunda
# def sum_pot1(1,n): return sum_pot2(l,n)
# LA DIFERENCIA estriba que pot1 "gasta" menos memoria, ya que solo almacena la suma de las potencias
# mientras que pot2 "almacena" todos los valores al cuadrado en una lista y luego los suma.
# Si la lista tuviese MILLONES de valores, el segundo necesitaria MUCHA mas memoria, 
# mientras que pot1 se conforme solo con la necesaria para almacenar la varibale de la suma