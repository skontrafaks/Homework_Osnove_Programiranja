#lista s najvise jedinica,printaj sve za najvise

import random

while True:
    n = int(input("Unesi n veci od nula: "))
    if n > 0:
        break
main_list = [0]*n
for i in range(n):

    main_list[i] =[random.randint(0, 1) for x in range(5)]

lista_sa_najvise_1 = []
max = 0
for i in main_list:
    if i.count(1) > max:
        max = i.count(1)

for i in main_list:
    if i.count(1) == max:
        lista_sa_najvise_1.append(i)


print(main_list)
print(max)
for i in lista_sa_najvise_1:
    print(f"Lista sa najvise jedinca: {i}")
