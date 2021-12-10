def ej1(fichero):
    f=open(fichero, "r")
    l=f.readlines()
    f.close()
    for pos in range(0, len(l)):
        l[pos]=int(l[pos])
    return l

lista=ej1("datos.txt")
print(sum(lista))
