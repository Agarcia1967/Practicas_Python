# Ejercicio 2.- Conversión de Temperaturas 
# En el intérprete de Python o en un fichero en el editor escribe el siguiente código.  
# Crea una variable, llamada C, para guardar un valor de una temperatura en grados  Celsius. 
# Inicialmente debe tomar el valor 30. 
c=30
# Ahora crea otra variable llamada F y  asígnale el valor de convertir a grados Fahrenheit la temperatura en grados Celsius 
# que contiene C. 
# 
# Para pasar de grados Celsius a Fahrenheit debes escribir la expresión  siguiente: 
# °C a °F: Multiplica por 9, divide entre 5, después suma 32 
f=c*9/5+32
# Trata de escribirlo mediante una única expresión. 
# El resultado debe ser 86
print(f"{c} grados Celsius son {f} grados Farenheit") 
# Ahora, haz la conversión contraria. 
# Asigna a la variable F el valor 77 y calcula en C la temperatura en grados Celsius: 
f=77
# °F a °C: Resta 32, después multiplica por 5, después divide entre 9 
c=(f-32)*5/9
# Debes tener en cuenta la precedencia de los operadores para poder obtener el  resultado correcto, 25 grados centígrados. 
print(f"{f} grados Farenheit son {c} grados Celsius") 
# Por último, en lugar de usar valores enteros, asigna valores reales a las variables C y  F 
# y comprueba que las expresiones de conversión siguen funcionando. 
# Lo podemos hacer con funciones ...

def farenheit(celsius):
  return 32+celsius*9/5


def celsius(farenheit):
    return (farenheit-32)*5/9


print(f"30 Celsius son {farenheit(30)} Farenheit")
print(f"77 farenheit son {celsius(77)} celsius")

print(f"0 Celsius son {farenheit(0)} Farenheit")
print(f"0 farenheit son {celsius(0)} celsius")

print(f"100 farenheit son {celsius(100)} celsius")
print(f"100 Celsius son {farenheit(100)} Farenheit")