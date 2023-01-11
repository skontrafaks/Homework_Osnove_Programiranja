otvori = open("./tekst5.txt", "r")
izlaz = open('./izlaz5.txt', 'w')
x = otvori.read()
brojac = 0
for i in x:
    if i in '0123456789':
        brojac += 1


def broji_znamenke(z, string):
    brj = 0
    for i in string:
        if i == str(z):
            brj += 1
    return brj


for i in range(10):
    frekvencija = round((broji_znamenke(i, x) / brojac), 2)
    postotak = round((frekvencija * 100), 2)
    izlaz.write(f'{i} -> {frekvencija} -> {postotak}%\n')
