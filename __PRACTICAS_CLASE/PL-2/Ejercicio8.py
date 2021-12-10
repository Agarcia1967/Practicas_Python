a=float(input("Introduce un año: "))
m=int(input("Introduce un mes del año:"))
if a%4==0 and a%100!=0:
    print("El año es bisiesto")
elif a%400==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("El mes tiene 31 dias")
elif m==4 or m==6 or m==9 or m==11:
    print("El mes tiene 30 días")
elif m==2 and ((a%4==0 and a%100!=0) or (a%400==0)):
    print("El mes tiene 29 días")
elif m==2 and ((a%4!=0 and a%100==0) or (a%400!=0)):
    print("El mes tiene 28 días")
