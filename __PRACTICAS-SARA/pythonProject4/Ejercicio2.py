def ej2(fichero):
    f=open(fichero, "r")
    l=f.readlines()
    f.close()
    longitud=len(l)
    return longitud

l=ej2("alumnos.txt")
print(l)

def coincide_apellido(linea,ap):
    lista=linea.split(",")
    return ap in lista[0]

f=open("alumnos.txt", "r")
l=f.readlines()
f.close()
c=0
for linea in l:
    if coincide_apellido(linea,"Fernandez"):
       c=c+1

print(c/len(l)*100)





