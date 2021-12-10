# Ejercicio 8. 
# Escribe un programa pida al usuario un entero n hasta que sea mayor que 0, 
# y muestre en pantalla los términos de la sucesión de Fibonacci 
# que sean menores que n separados por espacios y, en otra línea, la suma de ellos.
# La sucesión de Fibonacci empieza con 0 y 1, y a partir del tercer elemento, 
# cada uno es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21…

def fibionnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibionnaci(n-1) + fibionnaci(n-2)

n=-1
suma=0
while (n<0):
    n=int(input("Introduzca un valor para n:"))
    idx=0
    termino=0
    while (termino<n):
    # for idx in range(n)
        termino = fibionnaci(idx)
        if (termino<n):
            suma+=termino
            idx+=1
            # Para imprimir en la misma linea se usa en parametro end de la funcion print
            print("%d " %(termino), end='')
    print("\nSuma de la serie: %d" %(suma))



# Version iterativa (sin recursion)
# EN CADA ITERACION tenemos que tener almacenados los dos ultimos terminos calculados
# Para esto usamos p1 y p2, para almacenar los ultimos valores calculados.
# Ademas, para las iteraciones DESPUES de la segunda, los valores de p1 y p2 se actualizan
# de forma que p1 pasa a tomar el valor de p2 y p2 toma el valor calculado en termino (suma de los dos anteriores)

n=-1
suma=0
p1=0
p2=1
while (n<0):
    n=int(input("Introduzca un valor para n:"))
    termino=0
    idx=0
    while (termino<n):
        suma+=termino
        if (idx==0):
            termino=0
        elif (idx==1):
            termino=1
        else:
            termino=p1+p2
            p1=p2
            p2=termino
        # Para imprimir en la misma linea se usa en parametro end de la funcion print
        if (termino<n):
            print("%d " %(termino), end='')
        idx+=1
    print("\nSuma de la serie: %d" %(suma))
