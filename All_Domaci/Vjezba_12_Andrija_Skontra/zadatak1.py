import random

while True:
    n = int(input("Unesi broj listi: "))
    if n > 0:
        break


main_list = [0]*n

for i in range(len(main_list)):
    main_list[i] = [random.randint(0,10) for i in range(5)]

print(main_list)
suma_lista = []
for i in range(len(main_list)):
    suma_lista.append(sum(main_list[i]))

print(suma_lista)
third = []

for i in range(len(main_list)):
    third.append([suma_lista[i], main_list[i]])

third.sort()
print(third)
print(f"Lista sa najvecom sumom je = {third[len(third) - 1][1]}")