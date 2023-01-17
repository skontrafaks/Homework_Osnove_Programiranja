from random import randrange
player_lista = []
broj = 1
for i in range(7):
    if broj == 0:
        break
    broj = int(input("Unesi broj izmedu 1 i 39: "))
    if broj == 0:
        break
    while (broj < 1 or broj > 39) or (broj in player_lista):
        print("pogresan unos probajte ponovno.")
        broj = int(input("Unesi broj izmedu 1 i 39: "))
        if broj == 0:
            break
    player_lista.append(broj)

def izvlacenje_brojeva():
    izvucena_lista = []
    for i in range(7):
        izvucena_lista.append(randrange(1,40))
    return izvucena_lista

def usporedi(lista1, lista2):
    brj = 0
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            brj += 1
    return brj

if usporedi(player_lista, izvlacenje_brojeva()) == 7:
    print("JACKPOT")
else:
    print(f"{usporedi(player_lista, izvlacenje_brojeva())} je broj pogodenih brojeva")
