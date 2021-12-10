#TIPOS DE ERRORES
#Área de un triángulo
b=float(input("Base:")) #Base del triángulo
a=float(input("Altura: ")) #Altura del triángulo
area = a*b/2 #Área del triángulo
pront(area) #ERROR EN SINTAXIS

#Área de un triángulo
b=float(input("Base:")) #Base del triángulo
a=float(input("Altura: ")) #Altura del triángulo
area = a*b/0 #Área del triángulo #ERROR EN TIEMPO DE EJECUCIÓN
print(area)

#Área de un triángulo
b=float(input("Base:")) #Base del triángulo
a=float(input("Altura: ")) #Altura del triángulo
area = a*b/3 #Área del triángulo #ERROR SEMÁNTICO
print(area)
