def notas(a):

    if a<5:
        return "Suspenso"
    elif 5<a and a<7:
        return "Aprobado"
    elif 7<a and a<9:
        return "Notable"
    elif 9<a and a <10:
        return "Sobresaliente"
    elif a==10:
        return "Matricula de honor"

a=round(float(input("Introduce la nota: ")))
nota=notas(a)
print(nota)
