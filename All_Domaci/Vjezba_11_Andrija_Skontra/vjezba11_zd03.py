niz = []
ulaz = open("ulaz.txt", "r")
izlaz = open("izlaz.txt", "w")
for line in ulaz:
    niz.append(line)
print(niz)
niz.sort(key=lambda x: int(x[1]))
print(niz)

