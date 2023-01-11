ulaz = open('./tekst3.txt', 'r')
izlaz = open('./izlaz3.txt', 'w')

linije = ulaz.readlines()
print(linije)

br = 1

for tekst in linije:
    izlaz.write(str(br)+"."+tekst)
    br += 1

print(izlaz)

ulaz.close()
izlaz.close()
