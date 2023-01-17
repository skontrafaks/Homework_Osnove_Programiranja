niz = []
ulaz = open("ulaz.txt", "r")
izlaz = open("izlaz.txt", "w")
for line in ulaz:
    niz.append(line)
print(niz)
niz.sort(key=lambda x: x.split()[-1])
print(niz)
brj = 1
for i in niz:
    izlaz.writelines(f"{brj}. {i}")
    brj += 1

