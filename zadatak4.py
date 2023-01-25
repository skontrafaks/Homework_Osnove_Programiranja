def projekcija_na_os_x(T):
    T[1] = 0
    return print(f"Projekcija vase tocke na os x je tocka T({T[0]}, {T[1]})")

x = int(input("Unesi x koordinatu: "))
y = int(input("Unesi y koordinatu: "))

T = [x, y]
projekcija_na_os_x(T)
