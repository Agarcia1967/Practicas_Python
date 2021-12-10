# Ejercicio 4.- Operadores Relacionales y Lógicos 
# 1. Define dos variables enteras, a y b, y asígnales dos valores cualesquiera. 
a=10
b=40
# Ahora asigna a una variable llamada c una expresión lógica que compruebe si 
# “a está comprendida entre 5 y 30 (ambos inclusive) y b es un número par”. 
c = (a>=5 and a<=30)  and (b % 2 ==0)
# Para saber si un número es múltiplo de otro (en este caso múltiplo de dos, o lo  que es lo mismo par) 
# debes comprobar si el resto al dividir ambos números es  cero.
#  Asigna diferentes pares de valores a las variables a y b y comprueba que la  expresión escrita es correcta.  
print(f"c={c}")
# 2. Obtén el tipo de c usando type
print(f"type(c)={type(c)}")  
# 3. Asigna a otra variable d la expresión contraria, es decir, aplicando las leyes de  De Morgan (Tema 1) que 
# “a no está en comprendida entre 5 y 30 o b no es par”. 
# Hazlo de dos formas, primero usando el operador de negación (not) con la  expresión del apartado 1, 
d1 = (not c)
# y luego escribiendo la expresión indicada en este  apartado. 
d2 = (a<5 or a>30) and (b % 2 ==1)
# Cambia los valores de a y b y comprueba en cada caso que las expresiones de asignación de c y d producen siempre valores opuestos. 
print(f"d1={d1}")
print(f"d2={d2}")

def test(a,b):
    c = (a>=5 and a<=30)  and (b % 2 ==0)
    d1 = not (c)
    d2 = (a<5 or a>30) and (b % 2 ==1) 
    print(f"test({a},{b}) a={a} b={b} c={c} typeof(c)={type(c)} d1={d1} d2={d2}")
    return


test(10,40)
test(10,21)
test(1,2)
test(100,200)
test(0,0)
test(-10,3)