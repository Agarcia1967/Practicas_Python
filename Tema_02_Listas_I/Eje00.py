# Pruebas iniciales (30 min)
# Usando el intérprete python, crea dos listas llamadas lista1 y lista2. La primera lista contiene tres datos 
# que son: 5, 8 y 10. La segunda contiene cinco datos que son 3, 2, 9, 12, y 4.
lista1=[5,8,10]
lista2=[3,2,9,12,4]
# Tambien se pueden definir explicitamente, Fijate que ahora la lista va entre parentesis.
lista1=list((5,8,10))
lista2=list((3,2,9,12,4))

print("lista1:",lista1)
print("lista2:",lista2)
# 1.1 Operaciones básicas
# 1. Usa len() para averiguar la longitud de cada lista
print("longuitud de lista1:",len(lista1))
print("longuitud de lista2:",len(lista2))
# 2. Usa el operador + para concatenarlas, y averigua la longitud del resultado
lista3 = lista1 + lista2
print ("Longuitud de concatenar lista1 y lista2:",len(lista3))
# 3. Encuentra el número mayor de ambas listas (es el 12). 
# Puedes hacerlo, 
#      bien encontrando primero el máximo de la lista lista1, 
#      después el máximo de la lista lista2 
#      y finalmente el máximo de ambos máximos, 
# o bien encontrando el máximo de la concatenación. 
maxList1 = max(lista1)
maxList2 = max(lista2)
maximo = max(maxList1,maxList2)
print ("Maximo de las listas:",maximo)
maximo = max(lista3)
print ("Maximo de lista3:",maximo)
# Prueba ambos enfoques
# 1.2 Acceso a los elementos de la lista
# 4. Escribe una expresión que te de la suma del primer elemento de cada lista (debe sumar el 5 con el 3 y producir 8)
print("Suma de primeros componentes:",lista1[0]+lista2[0])
# 5. Escribe una expresión que sume el último elemento de cada lista. (10+4)
# Para acceder al ultimo podemos usar el indice -1 o bien usar la funcion len(lista)-1 ya que las listas van de 0..N-1
print("Ultimo valor de lista1:",lista1[-1])
print("Ultimo valor de lista2:",lista2[-1])
print("Suma de ultimos elementos de la lista:",lista1[-1]+lista2[-1])
# 6. Escribe una asignación que sustituya el 8 de la lista lista1 por un cero, comprueba que el elemento ha cambiado
lista1[1]=0
print("lista1 sin 8:",lista1)
# 1.3 Asignación de listas
# 7. Ejecuta la asignación lista3=lista2, y vuelca lista3 para comprobar que contiene los valores 3,2,9,12 y 4
lista3=lista2
print("lista3 ahora igual a lista2:",lista3)
# 8. Modifica lista3, de modo que su primer elemento valga 7. 
lista3[0]=7
# Vuélcala para comprobar que así es
print("lista3=",lista3)
# 9. Vuelca ahora lista2. 
# Verás que su primer elemento también ha cambiado. 
# Esto se debe a que, a partir de la asignación lista3=lista2 ambas variables se refieren a la misma lista. 
print("lista2=",lista2)
# 1.4 Recorrido de listas con bucles
# 10. Escribe un bucle que imprima cada elemento de lista1
print("Vamos a imprimir lista1 elemento a elemento:",lista1)
for ele in lista1:
    print(ele)
print("Vamos a imprimir lista1 elemento a elemento pero por su indice:",lista1)
for idx in range(len(lista1)):
    print(lista1[idx])
        
# 11. Escribe un bucle que imprima lista2 “al revés” (comenzando por el último y terminando por el primero)
print("Vamos a imprimir lista1 al reves:",lista1)
for idx in reversed(range(len(lista1))):
    print(lista1[idx])
# 12. Escribe un bucle que calcule la suma de lista2 y compáralo con lo que sale haciendo sum(lista2)
suma=0
for ele in lista2:
    suma=suma + ele
print("suma de lista2:",suma)
print("Suma de lista2 con sum(lista2)",sum(lista2))