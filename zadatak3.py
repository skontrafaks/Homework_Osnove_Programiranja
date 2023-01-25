ulaz = open("kalorije.txt", "r")
izlaz = open("izlaz.txt", "w")

lista_redaka = ulaz.readlines()
combined = []
for x in lista_redaka:
    y = x.split(" ")
    combined.append([int(y[1]), y[0]]) #int() briše \n !

combined.sort(reverse=True)

for i in combined:
    izlaz.write(f"{i[1]} {i[0]}\n")

ulaz.close()
izlaz.close()