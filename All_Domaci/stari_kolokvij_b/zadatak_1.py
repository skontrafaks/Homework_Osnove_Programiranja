import random

while True:
    n = int(input("Unesi n veci od nula(broj listi): "))
    if n > 0:
        break

main_list = []

for i in range(5):
    main_list.append([random.randint(0, 10) for x in range(n)])

print(main_list)
max = 0
najveca_lista = []

for i in main_list:
    if sum(i) > max:
        najveca_lista = i
        max = sum(i)
print(f"Nasa najveca lista je {najveca_lista}")
