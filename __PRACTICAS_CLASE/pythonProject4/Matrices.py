#
#  Programa que utiliza bucles anidados 
#  en una matriz dada eleva todos los elementos al cuadrado
#  Para ello recorre todas las filas 
#             y para cada fila todas las columnas
#
x=[[1,2,3],[4,5,6]]
for fila in range(0,len(x)): #Bucle que atraviesa todas las filas
    #for col in range(0,len(x[0])):#Bucle que atraviesa todas las columnas  
    for col in range(0,len(x[col])):#Bucle que atraviesa todas las columnas  
        x[fila] [col]=x[fila] [col]**2
print(x)
