# Ejercicios Adicionales: 
# 1. Conversor de Unidades de Peso: 
# Escribe las expresiones que permiten hacer las  conversiones entre kilogramos y libras 
# sabiendo que cada libra equivale a  0.45359237 kilogramos. 
# Crea una variable para cada unidad y comprueba que  las conversiones se realizan correctamente en ambos sentidos.  
def KgToLb(kg): return kg * 0.45359237


def LbToKg(lb): return lb / 0.45359237


kg = 10;
lb = KgToLb(kg)

print(f"10 kg son {lb} libras")

lb = 10;
kg = LbToKg(lb)

print(f"10 lb son {kg} kg")

# Ahora componemos las funciones, deben dar el resultado 
print(f"10 kg => {KgToLb(LbToKg(10))}")
print(f"100 lb => {LbToKg(KgToLb(100))}")
# 2. Movimiento Uniformemente Acelerado 2: Haz las mismas tareas que en el  Ejercicio 3, pero con la expresión: 
# D = V_i * t + 1/2 * a * t2 
# donde D es la distancia recorrida. Escribe las otras tres expresiones que permiten  calcular V_i, a y t en función del resto de variables. Para comprobar que son  correctas puedes usar el siguiente ejemplo: 
# • V_i = 20 m/s 
# • a = 9.8 m/s 
# • t = 30 seg. 
# • D = 5010 m 
# Nota: para el cálculo del tiempo debes tener en cuenta que la expresión  resultante es una ecuación de segundo grado. Toma la raíz positiva.

# d= V_i * t + 1/2 * a * t*t 
def calcula_D(v_i,a,t): return v_i*t+1/2*a*pow(t,2) 


# V_i = (d-1/2*a*t*t)/t
def calcula_V_I(d,a,t): 
    return (d-1/2*a*pow(t,2))/t  


# a= (d-v_i*t)/(1/2*t*t)
def calcula_A(d,v_i,t): 
    return (d-v_i*t)/(1/2*pow(t,2))


# 1/2*a*t^2+v_i*t-d=0 
# OJO con los signos
def calcula_T(d,v_i,a): return (-v_i+pow(pow(v_i,2)+2*a*d,0.5))/(a)


V_i = 20
a = 9.8
t = 30
D = 5010

print(f"D  ={calcula_D(V_i,a,t)} metros debe ser {D}")
print(f"V_i={calcula_V_I(D,a,t)} m/s debe ser {V_i}")
print(f"a  ={calcula_A(D,V_i,t)} m/s2 debe ser {a}")
print(f"t  ={calcula_T(D,V_i,a)} segundos debe ser {t} (aproximadamente)")