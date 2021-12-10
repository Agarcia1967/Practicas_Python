def resuelveec1gr(a,b):
    #Resuelve la ecuación ax+b=0
    """"Resuelve la ecuación ax+b=0,
        Parámetros:
        -a: Primer coeficiente
        -b: Segundo coeficiente
        Salida: solución ax+b=0"""
    x=-b/a
    return x

from math import sqrt
def resuelveec2gr(a,b,c):
    #Resuelve ax^2+bx+c=+
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    return x1, x2
