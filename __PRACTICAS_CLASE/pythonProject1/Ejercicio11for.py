n=int(input("Dame un número: "))
for i in range (1, n):
    resto=n%i
    if resto==0:
        print("Los divisores de",n ,"son",i)
