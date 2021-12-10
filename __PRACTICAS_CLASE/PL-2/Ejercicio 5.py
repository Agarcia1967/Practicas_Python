n= int(input("Introduce un número: "))

print("a) el cuadrado del número")
print("b) el cubo del número")
print("c) el doble del número")

o= input("Escoge una opción: ")

if o=="a":
    x=n**2
    print("El cuadrado del número es:" x)
elif o=="b":
    y=n**3
    print("El cubo del número es:", y)
elif o=="c":
    z=2*n
    print("El doble del número es:", z)
else:
    print("Opción incorrecta")
