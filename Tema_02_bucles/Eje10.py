# Ejercicio 10.- 
# Dados dos números enteros n (n≥0) y a (a>0) 
# encontrar, si existe, el menor entero x del intervalo [0, n] 
# para el que se cumpla lo siguiente: 
# la diferencia entre las sumas de los valores enteros de los intervalos [n-x, n] y [0, x] coincide con a.

# Definimos una funcion que nos calcule la suma de un intervalo (a<b)
def sumaIntervalo(a,b):
    suma=0
    for x in range(a,b+1):
        suma += x
    return suma


n=int(input("Introduzca un N (mayor o igual a 0):"))
if (n<0):
    print("El numero debe ser positivo")
    quit()

a=int(input("Introduzca un A (mayor que 0):"))
if (a<1):
    print("El numero debe ser mayor que cero")
    quit()

for idx in range(n):
    primerIntervalo=sumaIntervalo(n-idx,n)
    segundoIntervalo=sumaIntervalo(0,idx)
    diferencia=primerIntervalo-segundoIntervalo
    # print(f'{idx} {primerIntervalo}-{segundoIntervalo}={diferencia}  {a}')
    if (diferencia == a):
        print(f'Encontrado x={idx} donde suma[',n-idx,',',n,f']-suma[0,{idx}]={a}')
