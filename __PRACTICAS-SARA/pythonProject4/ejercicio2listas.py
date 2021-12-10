def rota_izq1(l):
    prim=l[0]
    for pos in range (0,len(l)-1):
        l[pos]=l[pos+1]
    l[len(l)-1]=prim
    return l

def rota_izqr2(l):
    l.append(l[0])
    l.pop(0)
    return l
x=[5,11,9,6]
print(rota_izq1(x))
print(rota_izq2(x))
