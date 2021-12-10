# Ejercicio 6. 
# Escribe un programa que lea letras sueltas del usuario hasta que reciba un “.” 
# e informe de cuántas vocales y consonantes ha recibido devolviendo el mensaje 
# “Ha introducido … letras: … vocales y … consonantes”.


def contieneCaracter(str, set):
    # Recorremos el conjunto de caracteres a comprobar
    for c in set:
        # Si alguno de esos caracteres esta presente en la cadena devolvemos 1
        if c in str: return 1
    # Si llego hasta aqui es que esta el caracter en el conjunto
    # str puede ser un string no solo un caracter
    return 0

consonantes:int = 0
vocales:int = 0
caracter = ''
while (caracter!='.'):
    caracter=input('Caracter siguiente (. para acabar)')
    if (caracter!='.'):
        vocales += contieneCaracter(caracter,('aeiou'))
        consonantes += contieneCaracter(caracter,('bcdfghjklmnpqrstvwxyz'))

print("Has introducido %d vocales y %d consonantes" %(vocales,consonantes))
