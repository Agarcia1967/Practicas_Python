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


# Esta funcion OBLIGA a que el valor sea positivo, sino sigue preguntando
def getPositivo(texto:str):
    entrada:int=-1
    while (entrada<0):
        entrada=int(input(texto))
    return entrada


print("Introduzca los valores POSITVOS ;")
b=getPositivo("Introduzca valor de b:")
c=getPositivo("Introduzca valor de c:")
d=getPositivo("Introduzca valor de d:")
k=getPositivo("Introduzca elemento de la serie a calcular(k):")
a:int=f_a(k,b,c,d)
print(F"a[{k}]={a}")