def sum_pot1(l, n):
    s=0
    for item in l:
        s=s+item**n
    return s

def sum_pot2(l,n):
    x=[]
    for item in l:
        x.append(item**n)
    return sum (x)

print(sum_pot1([5,11,9],2))
print(sum_pot2([5,11,9],2))
