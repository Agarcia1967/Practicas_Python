# Ejercicio 5. 
# Escribe un programa que, para dos números dados, 
# devuelva “Sí” sólo si uno de los números es par y el otro impar, 
# y “No” en cualquier otro caso. 
# Además, si se ha devuelto “Sí”, se debe informar de cuál de los números es el par y cuál el impar; 
# y si se devuelve “No”, se debe informar si ambos son pares o ambos impares

def esPar(n): return (n %2 ==0)


a = int(input("Dame el primer numero:"))
b = int(input("Dame el segundo numero:"))

if (esPar(a) and not esPar(b)) or (esPar(b) and not esPar(a)):
   print("SI")
   if (esPar(a)):
       print ("%d es par %d es impar" %(a,b))
   else:
        print ("%d es par %d es impar" %(b,a))
else:
    print("NO")
    if (esPar(a)):
        print ("ambos pares")
    else:
        print("Ambos impares")