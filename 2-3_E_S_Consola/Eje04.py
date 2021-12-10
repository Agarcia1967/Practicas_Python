# Ejercicio 4.- 
# Hacer un programa en Python que pida al usuario los coeficientes de una  ecuación de segundo grado 
# y saque por pantalla las dos soluciones, suponiendo que  existan. 

# Vamos a usar la libreria math para la raiz cuadrada, sino se puede user pow() o el operador **
import math

print('Vamos a resolver ecuaciones de segundo grado en fucnción de sus coeficientes:')
A = float(input('Dime el coeficiente A:'))
B = float(input('Dime el coeficiente B:'))
C = float(input('Dime el coeficiente C:'))

# Las condiciones son que A<>0 y que B^2 >= 4*A*C para que la raiz exista

print(f"Ecuacion: {A}*x^2+{B}*x+{C}=0 ")
if (A==0):
    print("No tiene soliciones A es 0")
    # Usamos quit() para salir del programa 
    quit() 
if (B*B<4*A*C):
    print("No tiene soluciones B^2-4*A*C<0")
    # usamos quit() para salir del programa
    quit()
# Se puede usar raiz=pow(B*B-4*A*C,0.5) o tambien raiz=(B*B-4*A*C)**(0.5)
raiz=math.sqrt(B*B-4*A*C)
# raiz=pow(B*B-4*A*C,0.5)
# raiz=(B*B-4*A*C)**(0.5)

sol1 = (-B + raiz)/(2*A)
sol2 = (-B - raiz)/(2*A)

print(f"Solucion 1={sol1}")
print(f"Solucion 2={sol2}")
