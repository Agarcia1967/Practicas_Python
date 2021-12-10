# Ejercicio 1.- Conceptos Básicos sobre Variables 
# En el intérprete de Python crea una variable llamada a y guardar en ella el valor 3.  
a = 3
# Ahora crea una segunda variable b y asígnale la expresión a + 5. 
b=a+5
# 1. Si se evalúa o se imprime b, ¿cuál será su valor? 
print(f"b={b}")
# 2. Modifica el contenido de a asignándole el valor 7. Después de esa asignación,  ¿cuánto vale b? ¿Por qué? 
a=7
print(f"a={a} b={b}")

# 3. Dados los valores asignados y las operaciones hechas, ¿de qué tipo son a y b? 
print(f"type(a)={type(a)}")
print(f"type(b)={type(b)}")
# 4. Asigna ahora a la variable a el valor 5.0 y actualiza el contenido de b  realizando de nuevo la asignación b = a + 5. 
a=5
b=a+5
# ¿Cuánto vale b ahora? ¿De qué  tipo es? 
print(f"b={b} {type(b)}")
# 5 . Si escribimos en el intérprete la expresión b = b + 1,
#  ¿estamos comprobando  si b es igual a b + 1? ¿Qué logramos al ejecutarla?  
print(f"Esta incrementando b en uno, no comprobando (deberia llevar doble igual para comprobar)")
# 6. Asigna a la variable a la cadena “Hola ” y la variable b la cadena “Mundo”. 
a="Hola"
b="Mundo" 
# ¿De qué tipo son ahora las variables? ¿Con qué función puedes saber su tipo?  
print(f"type(a)={type(a)}")
print(f"type(b)={type(b)}")
# ¿Qué resultado se produciría al ejecutar la expresión a + b? 
print(f"a={a}")
print(f"b={b}")
print(f"a+b={a+b}")