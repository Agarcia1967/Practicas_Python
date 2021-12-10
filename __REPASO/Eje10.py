# Ejercicio 10. Escribe una función que, para tres números dados, devuelve la media de los tres. 
# Comprueba su funcionamiento con un programa que utilice la función.

def media(a:int,b:int,c:int)->float: return (a+b+c)/3

a=10
b=20
c=43

print('La media de %d %d y %d es %6.3f' %(a,b,c,media(a,b,c)))

a=30
b=100
c=31
m=media(a,b,c)

print('La media de %d %d y %d es %6.3f' %(a,b,c,media(a,b,c)))

print ('Llamada con valores %6.3f' %(media(10,30,120)))