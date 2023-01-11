f = open('./tekst2.txt', 'r')

lista = []
dupli = []

for linija in f:
    for i in linija:
        if i not in lista:
            lista.append(i)
        elif i not in dupli:
            dupli.append(i)
print(dupli)
f.close()
