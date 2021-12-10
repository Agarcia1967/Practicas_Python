# Ejercicio 7. 
# Escribe un programa que tome dos enteros 
# y sume todos los enteros que se encuentran entre el menor y el mayor de ellos 
# (ambos inclusive).

suma=0
a=int(input("Dame el numero a:"))
b=int(input("Dame el numero b:"))
if (a>b):
    tmp=a
    a=b
    b=tmp
for idx in range(a,b+1):
    suma +=idx

print("La suma desde %d hasta %d es igual a %d " %(a,b,suma))