a=float(input("Introduce un valor para a: "))
b=float(input("Introduce un valor para b: "))
solucion= -b/a
if a!=0 and b!=0:
    print("La solución es :",solucion)
elif a==0:
    print("No tiene solución")
elif b==0:
    print("La solucion es 0")
