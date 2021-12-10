# Ejercicio 5 
# Define una función para obtener el término enésimo de la sucesión de números enteros definida como:
# 𝑎𝑘 = 
#     𝑏 si 𝑘 = 0
#     𝑐 ∙ 𝑎𝑘−1 + 𝑑 si 𝑘 > 0, con 𝑘 = 1, 2, 3, …
# A continuación, escribe un programa que solicite por teclado los valores enteros de los 
# parámetros b (primer elemento de la sucesión), c y d, así como el número entero no 
# negativo del término (k) a calcular y, utilizando la función definida, muestre en pantalla 
# el valor de dicho término

# Es una funcion recursiva, ya que se llama a si misma en la definion.

def f_a(k:int,b:int,c:int,d:int):
    if ( k == 0 ):
        return b
    else:
        return c*f_a(k-1,b,c,d)+d

# Usamos la funcion que hemos escrito anteriormente 
from getPositivo import getIntPositivo

print("Introduzca los valores POSITVOS ;")
b=getIntPositivo("Introduzca valor de b:")
c=getIntPositivo("Introduzca valor de c:")
d=getIntPositivo("Introduzca valor de d:")
k=getIntPositivo("Introduzca elemento de la serie a calcular(k):")
a:int=f_a(k,b,c,d)
print(F"a[{k}]={a}")