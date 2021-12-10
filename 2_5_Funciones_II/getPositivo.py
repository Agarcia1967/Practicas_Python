# Esta funcion lee un valor int positivo de teclado

# Esta funcion OBLIGA a que el valor sea positivo, sino sigue preguntando
def getIntPositivo(texto:str):
    entrada:int=-1
    while (entrada<0):
        entrada=int(input(texto))
    return entrada
