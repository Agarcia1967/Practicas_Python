x=[[1,2,3],[4,5,6]]
for fila in range(0,len(x)): #Bucle que atraviesa todas las filas
    for col in range(0,len(x[0])):#Bucle que atraviesa todas las columnas
        x[fila] [col]=x[fila] [col]**2
print(x)
