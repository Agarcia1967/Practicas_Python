n=1 #Introduzco un valor que inicialice a el bucle
pos=0 #Contador para conocer la posicion del dígito
max=0 #Representa el número más grande que he recibido hasta ahora
posMax=0 #Representa la posición del máximo
while n!=0: #Mientras que n sea distinto a cero comienza un bucle
    n=int(input("Dame un número positivo: ")) #Pido por pantalla un numero que sea positivo
    pos=pos+1
    if n>max: #Si n es mayor que el máximo
       max=n #Ahora ese numero será el máximo
       posMax=pos #Ahora guardo la posición de ese máximo
print("El mayor número es %d y se proporcionó en la posición %d" %(max, posMax))
