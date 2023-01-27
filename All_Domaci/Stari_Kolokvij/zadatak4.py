from math import sqrt

def udaljenost_tocaka(T_1, T_2):
    d = sqrt((T_1[0] - T_2[0])**2 + (T_1[1] - T_2[0])**2)
    return d

x1 = int(input("Unesi tocku x1: "))
y1 = int(input("Unesi tocku y1: "))
x2 = int(input("Unesi tocku x2: "))
y2 = int(input("Unesi tocku y2: "))

T_1 = (x1, y1)
T_2 = (x2, y2)

print(round(udaljenost_tocaka(T_1, T_2), 2))