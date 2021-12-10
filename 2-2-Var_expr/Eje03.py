"""
 Ejercicio 3.- Movimiento Uniformemente Acelerado 
 La ecuación básica que rige un movimiento uniformemente acelerado viene dada por  la expresión: 
 V_f = V_i + a t
 donde V_f es la velocidad final, 
       V_i es la velocidad inicial, 
       a es la aceleración y 
       t  indica el tiempo. 
 Escribe las otras tres expresiones que permiten calcular V_i, a y t en función del resto de variables. 
 Para comprobar que son correctas puedes usar el  siguiente ejemplo: 
  • V_i = 20 m/s 
  • a = 9.8 m/s 
  • t = 30 seg. 
  • V_f = 314 m/s 
 La idea es que asignes el valor de las otras tres variables 
 y calcules el valor de la  cuarta variable mediante la expresión correspondiente. 
"""
V_i = 20
a = 9.8
t = 30
V_f = 314

# Lo vamos a hacer usando funciones. Una para cada caso.

def calcula_vf(vi,a,t): return vi+a*t


def calcula_vi(vf,a,t): return (vf-a*t)


def calcula_a(vf,vi,t): return (vf-vi)/t


def calcula_t(vf,vi,a): return (vf-vi)/a

print(f"Calcula vf({V_i},{a},{t})={calcula_vf(V_i,a,t)} debe ser {V_f}")
print(f"Calcula vi({V_f},{a},{t})={calcula_vi(V_f,a,t)} debe ser {V_i}")
print(f"Calcula a({V_f},{V_i},{t})={calcula_a(V_f,V_i,t)} debe ser {a}")
print(f"Calcula t({V_f},{V_i},{a})={calcula_a(V_f,V_i,a)} debe ser {t}")