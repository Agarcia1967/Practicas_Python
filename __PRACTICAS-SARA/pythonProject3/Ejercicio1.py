def numeros(): #Funcion que pide tres numeros mayores de 10 y hace su media
    a=0
    while a<10:
        a=float(input("Introduce un valor mayor de 10: "))
    b=0
    while b<10:
        b=float(input("Introduce un valor mayor de 10: "))
    c=0
    while c<10:
        c=float(input("Introduce un valor mayor de 10: "))
    x=(a+b+c)/3
    return x

sol=numeros()
print(sol)

#Otra manera de hacerlo

def funcion():
    n1=float(input("Dame un numero: "))
    cont=0
    suma=0
    while cont==3:
        n1=float(input("Tiene que ser mayor que 10: "))
        if n1>10:
            cont=cont+1
            suma=suma+n1
    media=suma/cont
    return media
