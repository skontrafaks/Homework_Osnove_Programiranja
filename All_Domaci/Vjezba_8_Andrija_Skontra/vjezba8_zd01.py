from math import sqrt

def zbroj(a,b):
    x = a + b
    return x

print(zbroj(3,4))

def zbroj_znamenaka(a):
    a = [int(y) for y in str(a)]
    a = sum(a)
    return a

print(zbroj_znamenaka(232))

def udaljenost_od_0(x,y):
    d = sqrt(x**2 + y **2)
    return d

print(udaljenost_od_0(3,0))

def udaljenost_tocaka(x1,y1,x2,y2):
    d = sqrt((x1 - x2) ** 2 + (y1 -y2) ** 2)
    return d

print(udaljenost_tocaka(2,0,-2,0))




