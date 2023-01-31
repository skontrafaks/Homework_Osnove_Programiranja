n = int(input("Unesi"))

a = [0] * n
for i in range(n):
    a[i] = int(input(f"Unesi {i} element"))
for i in range(n-1, -1, -2):
    print(a[i])