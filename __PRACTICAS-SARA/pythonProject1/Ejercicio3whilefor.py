m=int(input("Numero de filas: "))
n=int(input("Numero de columnas: "))
for i in range(1,m+1): #Bucle que atraviesa las filas
    for j in range (1,n+1): #Bucle que atraviesa las columnas
        if j<n: #Antes del último elemento de la fila, separamos con estacio
            print("A%d%d" %(i,j), end=" ") #Estamos en el elemento i j de la matriz
        else: #Cuando lleguemos al último de la fila (j=n), cambiamos de lines con \n
            print("A%d%d" % (i,j),end="\n")

#OTRA FORMA
m=int(input("Numero de filas: "))
n=int(input("Numero de columnas: "))
for i in range(1,m+1): #Bucle que atraviesa las filas
    for j in range (1,n+1): #Bucle que atraviesa las columnas
         print("A%d%d" %(i,j), end=" ") #Estamos en el elemento i j de la matriz
         if j==n: #Cuando lleguemos al último de la fila (j=n), cambiamos de linea con \n
             print(end="\n")
