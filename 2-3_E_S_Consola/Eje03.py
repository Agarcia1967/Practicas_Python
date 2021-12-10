# Ejercicio 3.- Hacer un programa que lea por teclado el radio de un círculo y calcule el  área del mismo. 
# El resultado debe tener una forma similar a esta: 
# El área de un círculo de radio 4.0 es 50.2656 

# Usamos float para leer un numero real (con o sin decimales). Si usas int y pones decimales no funciona
# Definimos la constante PI en una varible. No es imprescindible, pero mejora la lectura del código.

pi = i = 3.1416

radio = float(input("Radio del circulo:"))

area= 2*pi*radio*radio
print(f"El área de un circulo de radio {radio} es {area}")

# o mejor aun lo podemos hacer con una función que devuelva el valor del area:

def area_circulo(radio_circulo):
  return 2*pi*radio_circulo*radio_circulo


area2=area_circulo(radio)
print(f"El área de un circulo de radio {radio} es {area2}")
