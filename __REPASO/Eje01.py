# Ejercicio 1. 
# Escribe un programa que pida al usuario dos enteros a y b, calcule π**π y π**π 
# y devuelva el mensaje: βLa mayor potencia que se puede conseguir de [a] y [b] es β¦β.
# Utiliza una sola funciΓ³n print

a=int(input("Dame un valor para a:"))
b=int(input("Dame un valor para b:"))
ab=a**b
ba=b**a
if (ab>ba):
    mayor=ab
else:
    mayor=ba
print(f"La mayor potencia que se puede conseguir con {a} y {b} es {mayor}")