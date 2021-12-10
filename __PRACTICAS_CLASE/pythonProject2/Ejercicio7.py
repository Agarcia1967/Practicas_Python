from math import sqrt
def distancia(x,y):
    dist=sqrt(x**2+y**2)
    return dist

x=float(input("Coordenada x: "))
y=float(input("Coordenada y: "))
sol=distancia(x,y)

print(sol)
