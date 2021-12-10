# Ejercicio 18. 
# Escribe un programa que lea el fichero “data.txt” 
# y calcule la media de todos los números. 
# El resultado debe ser 491,95.

f=open('data.txt')
datos=f.readlines()
f.close
suma=0.0
for i in range(len(datos)):
    datos[i]=float(datos[i])
    suma+=datos[i]
media=suma/len(datos)
print('La media es %6.3f' %(media))