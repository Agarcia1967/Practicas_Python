# Ejercicio 5. 
# Escribe un programa que reciba un número n. 
# Si el número no es mayor que 1 y menor que 100, 
# el programa debe continuar pidiendo un número al usuario hasta que lo sea. 
# Después, calcula y muestra su factorización en primos. 
# Puedes utilizar la función del ejercicio anterior. 
# Por ejemplo, para n = 90 la salida debe ser: La factorización de 90 es 2*3^2*5.
#
#  Hay tres versiones del algoritmo
#       Una con bucle while
#       Otra con bucle for
#       Otra recursiva

# Esta es un funcion "sencilla" que nos dice si dos enteros son divisibles (resto cero)
def esDivisible(n:int,divisor:int)->bool: return ( n % divisor == 0 )

# Esta funcion nos dice si un numero es o no primo
# Devuelve un valor boolean (True/False)
def esPrimo(n:int)->bool:
    # return True
    # Si el numero es menor que dos NO es primo
    if (n<2): return False
    # Empezamos considerando que si es primo, y esto es asi porque dentro del bucle for
    # vamos a usar la funcion "and". 
    # Para cada iteracion del bucle, sera primo si lo es hasta ahora (no encontro divisores) 
    # y ademas en el caso que estoy considerando (divisor) TAMPOCO lo es. Por eso usa and.
    # Recordar que (A and B) es cierto SI Y SOLO SI A y B son ciertos  
    primo=True
    # Los divisores estan ente 2 y n-1
    for divisor in range(2,n):
        primo = primo and not esDivisible(n,divisor)
        # Aqui se podria poner una condicion, para que en cuanto encuentre un divisor 
        # no siga mirando ya que no será primo, es una forma de "mejorar" el calculo, 
        # ya que en cuanto tenga un divisor NO tiene sentido seguir mirando, ya NO ES PRIMO
        if not(primo): return False
    # devolvemos el valor de primo
    return primo

# Esta funcion pide un numero entre 1 y 100
# Devuelve el numero cuando cumple el criterio
def pidenumero()->int:
    # Empezamos con un valor que nos haga "entrar" en el bucle
    # Con n=0 nos aseguramos de leer por teclado el valor, al menos una vez
    n=0
    while (n<1 or n>100):
        n=int(input("Dame un numero entre 1 y 100:"))
    return n

# Esta es una version del programa con while -luego hay otra con for-
def factorizaV1(numero:int)->list:
    # Vamos a almacenar en una lista todos los factores que encontremos.
    # Esto es asi dado que una funcion solo puede devolver un valor (o un objeto)
    # y nosotros necesitamos devolver todos los factores, que son UNA LISTA
    # El caso especial es el 1. Lo tratamos aparte
    if (numero==1):
        return [1]
    # Empezamos con la lista vacia
    factores=[]
    # Vamos a utilizar esta varible idx para que tome los valores 1,2,3,..... en cada iteración
    # De esta manera miraremos en cada paso del bucle si ese valor idx es o no Primo
    idx=1
    # Para factorizar, mientras que el valor sea mayor que 1, tengo que buscar los factores
    while (numero>1):
        # Si el valor idx (1,2,3.... en cada ciclo del bucle toma un valor) es primo
        # Estrictamente para el calculo de la factorizacion no hace falta comprobar que sea primo
        # Lo hacemos asi porque es lo que pide el enunciado
        if esPrimo(idx):
            # Cuando llega aqui, sabemos que idx es Primo
            # Ahora vamos a ver si es un divisor del numero
            if esDivisible(numero,idx):
                # Si llega aqui, es primo y ademas es divisor del numero que estamos tratando
                # Lo vamos a "almacenar" en la lista de resultados que se llama factores
                # Usamos la funcion append de list para añadirlo
                factores.append(idx)
                # Usamos la division entera para recalcular el nuevo valor de "numero"
                # El proceso es como hacerlo a mano, 
                # cuando encontramos un divisor recalculamos el "nuevo" numero
                numero=numero // idx
                # Ahora ademas empezamos otra vez a buscarle divisores al "nuevo" numero
                # Empezamos de nuevo a buscar que es lo mismo que poner idx a 1
                # Recordemos que idx ira de 1,2,3,....
                idx=1
        # Si llegamos aqui, no es primo ni divisible, luego pasamos al siguiente valor de idx para probarlo
        idx=idx+1
    # Hemos ACABADO, luego devolvemos la "lista"
    return factores

# Esta es una verion usando un bucle FOR que igual se entiende mejor que la del while 
# Hacer aqui el break dentro del for es equivalente a hacer la inicializacion de idx dentro del while
def factorizaV2(numero:int)->list:
    # Vamos a almacenar en una lista todos los factores que encontremos.
    # Esto es asi dado que una funcion solo puede devolver un valor (o un objeto)
    # y nosotros necesitamos devolver todos los factores, que son UNA LISTA
    # El caso especial es el 1. Lo tratamos aparte
    if (numero==1):
        # devolvemos una lista con el numero 1 y acabamos
        return [1]
    # Empezamos con la lista vacia
    factores=[]
    # Vamos a utilizar esta varible idx para que tome los valores 1,2,3,..... en cada iteración
    # De esta manera miraremos en cada paso del bucle si ese valor idx es o no Primo
    # Para factorizar, mientras que el valor sea mayor que 1, tengo que buscar los factores
    while (numero>1):
        # Si el valor idx (1,2,3.... en cada ciclo del bucle toma un valor) es primo
        # Estrictamente para el calculo de la factorizacion no hace falta comprobar que sea primo
        # Lo hacemos asi porque es lo que pide el enunciado
        for idx in range(2,numero+1):
            if esPrimo(idx):
                # Cuando llega aqui, sabemos que idx es Primo
                # Ahora vamos a ver si es un divisor del numero
                if esDivisible(numero,idx):
                    # Si llega aqui, es primo y ademas es divisor del numero que estamos tratando
                    # Lo vamos a "almacenar" en la lista de resultados que se llama factores
                    # Usamos la funcion append de list para añadirlo
                    factores.append(idx)
                    # Usamos la division entera para recalcular el nuevo valor de "numero"
                    # El proceso es como hacerlo a mano, 
                    # cuando encontramos un divisor recalculamos el "nuevo" numero
                    numero=numero // idx
                    # Ahora ademas empezamos otra vez a buscarle divisores al "nuevo" numero
                    # "Salimos" del bucle pues hay un "nuevo" numero y debemos empezar
                    # de nuevo desde el 2 hasta n para buscar nuevos divisores a este 
                    break
       
    # Hemos ACABADO, luego devolvemos la "lista"
    return factores

# Esta es una verion recusiva para acabar con el tema
def factorizaV3(numero:int, factores: list)->list:
    # Vamos a almacenar en una lista todos los factores que encontremos.
    # Esto es asi dado que una funcion solo puede devolver un valor (o un objeto)
    # y nosotros necesitamos devolver todos los factores, que son UNA LISTA
    # El caso basico, de parada, es que el numero sea 1, entonces no hay nada que hacer
    # mas que devolver la lista que nos hayan pasado
    if (numero == 1 and len(factores)==0): 
        factores.append(1)
        return factores

    # Para factorizar, mientras que el valor sea mayor que 1, tengo que buscar los factores
    # En cada iteracion del for
        # Si el valor idx (1,2,3.... en cada ciclo del bucle toma un valor) es primo
        # Estrictamente para el calculo de la factorizacion no hace falta comprobar que sea primo
        # Lo hacemos asi porque es lo que pide el enunciado
    for idx in range(2,numero+1):
        if esPrimo(idx):
            # Cuando llega aqui, sabemos que idx es Primo
            # Ahora vamos a ver si es un divisor del numero
            if esDivisible(numero,idx):
                # Si llega aqui, es primo y ademas es divisor del numero que estamos tratando
                # Lo vamos a "almacenar" en la lista de resultados que se llama factores
                # Usamos la funcion append de list para añadirlo
                factores.append(idx)
                # Usamos la division entera para recalcular el nuevo valor de "numero"
                # El proceso es como hacerlo a mano, 
                # cuando encontramos un divisor recalculamos el "nuevo" numero
                numero=numero // idx
                # Ahora ademas empezamos otra vez a buscarle divisores al "nuevo" numero
                # Ahora lo que toca es "calcular" la factorizacion del "nuevo" numero
                # Para ello pasamos el nuevo numero y la "lista" que calculada hasta ahora 
                # Recordemos que la funcion devuelve la lista de factores del nuevo numero
                return factorizaV3(numero, factores)
                # "Salimos" del bucle pues hay un "nuevo" numero y debemos empezar
                # de nuevo desde el 2 hasta n para buscar nuevos divisores a este 
                # el break esta implicito en el return 
       
    # Hemos ACABADO, luego devolvemos la "lista".
    return factores


# 90 factorizado en: [2, 3, 3, 5]
# 91 factorizado en: [7, 13]
# 1024 factorizado en: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# 1967 factorizado en: [7, 281]

def escribe(factores:list)->str:
    # En factores nos llega una lista del estilo
    # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # Lo que vamos a hacer es ir consumiendola desde el final 
    # Para ello usamos la funcion POP de list
    
    cadena=''
    while (len(factores)>0):
        # Empezamos "extrayendo" con pop el ultimo elemento.
        # Esto tiene dos efectos, por un lado sacamos el ultimo valor
        # ademas se elimina de la lista
        item=factores.pop()
        # En la variable nele vamos a "contar" cuantos elementos hay "iguales" en la lista
        # esto nos dara el valor del exponente para escribir la cadena por ejemplo de 3^2
        # si la lista fuese [....,3,3]
        nele=1
        # Ahora mientras la lista tenga mas numeros (len(factores)>0) 
        # y ADEMAS el ultimo de la lista sea igual al que hemos extraido (item)
        while (len(factores)>0 and factores[-1]==item):
            # Como es igual lo sacamos de la lista
            factores.pop()
            # Anotamos que tenemos uno mas
            nele+=1
        # Ahora vamos a darle formato a la cadena
        # Tenemos dos casos diferentes:
        #      Por un lado los que el exponente es 1
        #      Por otro los que el exponente es > 1
        # usamos la concatenacion de cadenas y
        # la funcion format para generar una cadena con formato
        if (nele==1 or item==1 ):
            cadena = cadena + "*{}".format(item)
            # print("%d" %(item),end="*")
        else:
            cadena = cadena + "*{}^{}".format(item,nele)
            # print("%d^%d" %(item,nele),end="*")
    # print("1")
    # La cadena en este punto empieza por un * que no tiene sentido devolver
    # Lo que hacemos es devolver desde el segundo caracter hasta el final
    # Eje:  *2*3^2*5 y queremos devolver 2*3^2*5
    return cadena[1:]

# Esta es una funcion auxiliar para no tener que escribir cada vez toda la cadena
# Recibe el numero a calcular y llama al resto imprimiendo el resultado por pantalla
def testFactoriza(n):
    # Probamos las versiones
    print ('V1:La factorizacion de %5d es %s' %(n, escribe(factorizaV1(n))))
    print ('V2:La factorizacion de %5d es %s' %(n, escribe(factorizaV2(n))))
    # En el caso de la recursiva tenemos que "inicializar" la lista a vacio
    print ('V3:La factorizacion de %5d es %s' %(n, escribe(factorizaV3(n,[]))))
    

# testFactoriza(1)
# testFactoriza(10)
# testFactoriza(90)
# testFactoriza(121)
# testFactoriza(333)

# Llamamos a la funcion para que el usuario introduzca un valor
testFactoriza(pidenumero())
