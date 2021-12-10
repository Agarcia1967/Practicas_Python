# Ejercicio 6.- 
# Dados dos enteros a≥0 y b>0, 
# escribe un programa que calcule el cociente y el resto de su división entera 
# utilizando para ello el método de restas sucesivas y mostrar el resultado en la forma:
# Cociente: 17 // 3 = 5
# Resto: 17 % 3 = 2

dividendo=int(input("Introduzca un numero entero:"))
if (dividendo<0):
    print("El dividendo debe ser positivo")
    quit()
divisor=int(input("Introduzca un numero entero:"))
if (divisor<=0):
    print("El divisor debe ser mayor que cero")
    quit()
cociente=0
resto=dividendo
while (resto>divisor):
    cociente +=1
    resto-=divisor

print(f"Cociente: {dividendo} / {divisor} = {cociente}")
print(f"Resto   : {dividendo} % {divisor} = {resto}")