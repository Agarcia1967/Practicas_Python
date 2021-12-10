def nutricion (p,h):
    IMC=p/h**2
    if IMC<18.5:
        return "Bajo peso"
    elif 18.5<IMC and IMC<25:
        return "Normal"
    elif 25<IMC and IMC<30:
        return "Sobrepeso"
    elif IMC>=30:
        return "Obesidad"

p=float(input("Introduce un peso en kilogramos: "))
h=float(input("Introduce una altura en metros: "))
sol=nutricion(p,h)
print(sol)
