# Ejercicio 17. 
# Escribe un programa que lea el fichero “data.txt” disponible en el Campus Virtual 
# y cuente cuántos números de dos cifras y de tres hay en total.

# un numero es 2 cifras si su len como string es 2
# idem para 3

f=open('data.txt')
datos=f.readlines()
f.close()

# Ahora datos ya es una lista

condos=0
contres=0
for i in datos:
    if len(i) == 2:
        condos += 1
    if len(i) == 3:
        contres += 1
print('%d numeros con dos digitos \n%d con tres digitos' %(condos,contres))