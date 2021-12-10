# Ejercicio 5.- 
# Dado un número natural n, 
# escribe un programa para calcular la parte entera de la raíz cuadrada de n 
# y muestre en resultado en la forma:
# La parte entera de la raíz cuadrada de 38 es: 6

# Como quiere hacerlo con bucles usaremos una aproximacion n*(n+1)< numero

n=int(input("Introduzca un numero entero:"))
if (n<0):
    quit()
idx=1
while (idx*(idx+1) < n): 
    idx +=1
print (f"La parte entera de la raíz cuadrada de {n} es: {idx}")

# Se podria usar esta otra aproximacion 
# -peor ya que idx cuando acaba no contiene la raiz sino el siguiente-
# Ademas no funciona para n=1 SINO cambiamos el valor inicial de idx=2

idx=2
while (idx*idx < n): 
    idx +=1
print (f"La parte entera de la raíz cuadrada de {n} es: {idx-1}")