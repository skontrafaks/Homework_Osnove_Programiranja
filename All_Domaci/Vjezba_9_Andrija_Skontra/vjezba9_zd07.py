import re
ulaz = open("./tekst7.txt", "r")
izlaz = open('./izlaz7.txt', 'w')
x = ulaz.read()
x = [int(s) for s in re.findall(r'\b\d+\b', x)]
x.sort()
for i in range(len(x)):
    izlaz.write(str(x[i]) + ' ')

