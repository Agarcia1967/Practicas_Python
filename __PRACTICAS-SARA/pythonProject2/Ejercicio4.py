def aynobisiesto ():
    if (a%4==0 and a%100!=0) and (a%4==0 and a%400!=0):
        print("Verdadero")
    else:
        print("Falso")

a=float(input("Introduce un número positivo: "))
bisiesto=aynobisiesto()
print(bisiesto)
