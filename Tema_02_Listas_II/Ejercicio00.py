# Listas II 
#  Pruebas iniciales (20 min) 
# Usando el intérprete python, 
#   crea una variable llamada texto que contenga “Esto es una prueba”,
texto = 'Esto es una prueba' 
#   y otra  llamada fecha que contenga la cadena “16/10/2000”. 
fecha = '16/10/2000'
# 1.1 Operaciones básicas sobre cadenas 
# 1. Usa len() para averiguar la longitud del texto 
print(f'len({texto})={len(texto)}')
# 2. Usa el operador + para concatenar las dos variables (fecha y texto), 
#          con un guión  separándolas y guarda el resultado en la variable resultado. 
# Al final, debe contener: “16/10/2000  – Esto es una prueba” 
resultado = fecha + '-' + texto
print(f"resultado={resultado}")
# 3. Usa el operador in para averiguar si el texto contiene la palabra “prueba” o la palabra “esto”  (con la “e” minúscula) 
print("Test de palabara prueba en resultado=","prueba" in resultado)
print("Test de palabra esto en resultado   =","esto" in resultado)
# 4. Ejecuta texto.split() y observa la lista que resulta.
print (resultado.split()) 
# ¿Qué hace split()? 
print ("split devuelve una lista de string usando como separador el caracter pasado como parametro")
# Prueba  texto.split(“e”) ¿qué significa el parámetro que pasas a split()? 
print ("resultado.split(e)=",resultado.split("e")) 
# 5. Usa split() sobre fecha para separar su contenido en tres variables dia, mes y anyo. 
print("Fecha separada=",fecha.split("/"))
# 6. Usa help(str.replace) para averiguar cosas sobre el método replace que puedes usar sobre una cadena. 

# Úsalo sobre la variable texto para cambiar “es” por “era”. 

print("Cambiando ES por ERA:",str.replace(resultado,"es", "era"))

# 1.2 Listas y ficheros 
# 7. Prepara un fichero que contenga varias líneas de texto. 
# Abre el fichero sobre una variable f, mediante f=open("nombre-del-fichero.txt")
f=open('FicheroTest.txt')
# 8. Ejecuta datos=f.readlines() y observa la variable datos. 
datos=f.readlines()
f.close()
print("datos:",datos)
# Es una lista en la que cada  elemento es un string que contiene una línea del fichero (no olvides f.close() después).  
# 9. Usa len(datos). 
print(f"numero de lineas del fichero = {len(datos)}")
# El resultado es el número de líneas del fichero. ¿Qué resultado te da  len(datos[0]) y qué significa? 
print("Longitud de elemento 0 de la lista len(datos[0])=",len(datos[0]))
# 10. Observa datos[0] y verás que tiene un \n al final. 
print("datos[0]=",datos[0])
# Este carácter representa el “retorno de  carro” que hay al final de cada línea del fichero. 
# Normalmente no lo queremos. 
# Las cadenas  tienen el método rstrip() que elimina todos los caracteres invisibles 
# (espacios, retornos de  carro, etc) que pueda haber al final de una cadena. 
# No modifican la propia cadena (no pueden), sino que retornan la versión sin esos caracteres finales. 
# Así: linea=datos[0].rstrip(). 
linea=datos[0].rstrip()
# Si  miras la variable linea, verás que ya no tiene al final el \n (aunque datos[0] sigue teniéndolo).
print("linea   =",linea)
print("datos[0]=",datos[0])


