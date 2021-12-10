#ALUMNO APROBADO O SUSPENSO
nom=input("Nombre: ") #NOMBRE DEL ALUMNO
nota1=float(input("Nota 1: ")) #PRIMERA NOTA
nota2=float(input("Nota 2: ")) #SEGUNDA NOTA
media= (nota1+nota2)/2
if media>=5 and media<7:
    print("Aprobado")
elif media>=7:
    print("Notable")

elif 9 <= media <= 10:
    print("Sobresaliente")
else :
    # %s -> strings/cadenas de texto o booleanos
    # %.3 -> floats con 3 decimales
    # %d -> enteros
    print("Suspenso con nota final %.2f y notas parciales %.2f y %.2f" %(media, nota1 , nota2))
