# EJERCICIO 3.
# IMPORTAR Y PROCESAR DATOS DE EXCEL 
# Descarga el fichero llamado datos-paises.xls. 
# Ábrelo en Excel y verás que contiene 
#    una lista de nombres  de país, 
#    de número de habitantes de cada uno de ellos, 
#    y de número de teléfonos móviles. 
# Desde Excel  guárdalo con la opción “Guardar como…” y elige “CSV separado por comas”. 
# Eso te creará el fichero  datos-paises.csv 
# Si abres dicho fichero datos-paises.csv con cualquier editor de texto (por ejemplo con notepad++)  
# podrás ver que simplemente consta de una línea por cada fila de la hoja Excel, 
# y en cada línea se han  volcado los contenidos de las celdas, separados por punto y coma. 
# Desde el editor, borra la primera línea del fichero que has generado, 
# pues no contiene datos de ningún  país, sino la cabecera de la tabla. 
# A la vista del formato csv, escribe programas en python que te permitan: 
# 1. Calcular el número total de habitantes (suma de todos los países) 
f=open('paises.csv')
datos=f.readlines()
paises=[]
lineas=[]
habitantes=[]
for idx in range(len(datos)):
    # Los datos estan en cada linea separados por punto y coma
    tmp=datos[idx].split(";")
    paises.append(tmp[0]);
    lineas.append(float(tmp[1]))
    habitantes.append(float(tmp[2]))
f.close()
totHab = 0
for idx in range(len(habitantes)):
    totHab= totHab +  habitantes[idx]
print("Numero total de habitantes:", totHab)
# 2. Calcular el número promedio de habitantes por país (suma de habitantes entre número de países) 
promedio=totHab/len(habitantes)
print ('Promedio habitantes por pais:', promedio)
# 3. Generar otro archivo csv que contenga 
#        la lista de países 
#        y el número promedio de teléfonos móviles por habitante de cada uno. 
f = open("salida.csv", "w")
f.write("pais;mediaTlfnos"+ '\n')
for idx in range(len(paises)):
    f.write(paises[idx]+";"+str(lineas[idx]/habitantes[idx])+ '\n')
f.close()
# 4. Encontrar los países cuyo número de habitantes sea cercano al número promedio calculado en el  paso 2 
#    (entenderemos que es cercano si la diferencia es menor de un millón). 
print("Paises con habitantes cercano al promedio:")
for idx in range(len(habitantes)):
     if abs(habitantes[idx]-promedio)<10000000:
        print(paises[idx]," ", habitantes[idx], " ", abs(promedio-habitantes[idx]))
# 5. ¡Otras cosas que se te ocurran! (por ejemplo ¿cuál es el país que tiene más teléfonos móviles por  habitante?) 
