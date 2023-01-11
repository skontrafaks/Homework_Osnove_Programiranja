otvori = open("./tekst4.txt", "r")
izlaz = open('./izlaz4.txt', 'w')
x = otvori.readlines()


for i in range(len(x)):
    x[i] = x[i].split(' ')

for i in range(len(x)):
    if x[i][1] == '+':
        izlaz.write(str(float(x[i][0]) + float(x[i][2]))+"\n")
    if x[i][1] == '-':
        izlaz.write(str(float(x[i][0]) - float(x[i][2]))+"\n")
    if x[i][1] == '*':
        izlaz.write(str(float(x[i][0]) * float(x[i][2]))+"\n")
    if x[i][1] == '/':
        izlaz.write(str(float(x[i][0]) / float(x[i][2]))+"\n")
otvori.close()
izlaz.close()
