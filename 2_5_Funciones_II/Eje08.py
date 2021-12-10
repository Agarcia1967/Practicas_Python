# Ejercicio 8.- Basándose en la definición de funciones similares a las utilizadas en el 
# ejercicio previo, escribe ahora un programa que solicite por teclado un número entero 
# positivo y un carácter y muestre en la pantalla únicamente el contorno del cuadrado con
# el carácter dado. El número proporcionado determina el número de líneas del cuadrado y 
# el número de caracteres por línea será el doble de éstas.
# Resultado esperado para print contorno_cuadrado("*", 3):
# ******
# *    *
# ******

# En este caso cambia la funcion de generacion del cuadrado, que para la primera y ultima fila seran diferentes

def cuadrado(ch:str,n:int):
    result:str=''
    # Se podria usar ch[0] por si en la entrada pusieran mas de un caracter
    # Esto es un REFINAMIENTO ...
    ch=ch[0]
    # Vamos ha hacerlo de manera muy basica, en tres bloques, primera fila, ultima fila y el resto.
    # Primera fila
    for columnas in range(2*n):
        result=result+ch
    result=result+'\n'
    # filas 2 hasta n-1
    for lineas in range(2,n-1):
        result=result+ch
        for columnas in range(2,2*n-1):
            result= result + ' '
        result = result + ' '+ch+'\n'
    # ultima fila solo en caso de tener mas de dos filas ...
    if (n>1):
        for columnas in range(2*n):
            result=result+ch
        result=result+'\n'
    return result

    
# Esta funcion OBLIGA a que el valor sea positivo, sino sigue preguntando
def getPositivo(texto:str):
    entrada:int=-1
    while (entrada<0):
        entrada=int(input(texto))
    return entrada


ch=input("Introduce un caracter:")
n=getPositivo("Introduce el numero de filas:")
print(cuadrado(ch,n))

