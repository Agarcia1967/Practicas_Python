# Ejercicio 11 
# Dado un número entero n (n≥0), 
# escribir un programa para obtener la cadena de caracteres de unos y ceros 
# correspondiente a su representación en binario 
# sin utilizar la función predefinida bin.


n=int(input("Introduzca un N (mayor o igual a 0):"))
if (n<0):
    print("El numero debe ser positivo")
    quit()
# El cero es un caso especial, para no complicat el while lo podemos poner aqui
if (n==0):
    binario='0'
else:
    binario=''
numero=n
while (numero>0):
    digito = numero % 2
    if ( digito == 0 ):
        binario = '0' + binario
    else:
        binario = '1' + binario
    numero = int(numero/2)

print (binario) 