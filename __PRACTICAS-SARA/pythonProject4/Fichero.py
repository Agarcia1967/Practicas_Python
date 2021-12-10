#Abrir el fichero para escrubur: "w"
f= open("Prueba","w")
f.write("linea 1\nLines 2\nLinea3")
f.close()

#Abrir el fichero para escribir al final: "a"
f=open("Prueba", "a")
f.write("\nLinea4")
f.close()

#Abrir el fichero para leer: "r"
f=open("Prueba", "r")
l=f.readlines()
print(l)
print(len(l),len(l[0])) #Numero de filas del fichero//Numero de caracteres de la lista
f.close()

#Abrir el fichero para leer: "r"
f=open("Prueba", "r")
linea1=f.readline()
print(linea1)
linea2=f.readline()
print(linea2)
linea3=f.readline()
print(linea3)
f.close()
