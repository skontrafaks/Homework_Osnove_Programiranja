x1 = int(input("Unesi tocku: "))
x2 = int(input("Unesi tocku: "))
x3 = int(input("Unesi tocku: "))
y1 = int(input("Unesi tocku: "))
y2 = int(input("Unesi tocku: "))
y3 = int(input("Unesi tocku: "))
T1 = (x1, y1)
T2 = (x2, y2)
T3 = (x3, y3)

def povrsina():
    P = 0.5 * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))
    if P <= 0:
        print("Nesto nije dobro uneseno")
    else:
        print(f"Povrsina trokuta je {P}")

povrsina()