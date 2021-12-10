# Ejercicio 9. 
# Escribe un programa que, para un n dado, 
# calcule el porcentaje de enteros menores que n que tienen más de 5 divisores 
# y muestre cuáles son.

# Cero no sirve porque sino al calcular el % nos daria division por cero
n=-1
while (n<0):
  n=int(input("Introduce un valor para n (mayor que cero):"))

encontrados=0
for idx in range(n):
    # Para cada iteracion tengo que calcular cuantos divisores tiene idx
    # Y los divisores de un numero estan entre 1 y el mismo (idx)
    divisores=0
    # El rango de los divisores es entre 1 y n ¡¡¡¡OJO AL RANGE!!!!!
    for idy in range(1,idx+1):
        if (idx % idy ==0):
            # es divisor
            divisores+=1
    # Cuando llegue aqui, en divisores tendre la cantidad de divisores que hay para el valor idx
    # Si es mayor que cinco, tengo que imprimir el numero idx y anotar que tengo uno mas para luego
    # calcular el porcentaje
    if (divisores>=5):
        print(idx,end=" ")
        encontrados+=1
porcentaje=encontrados/n
print("\nEl porcentaje encontrado es del %3.2f (%d sonbre %d) " %(porcentaje,encontrados,n))