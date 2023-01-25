import random

def izvuci_broj():
    broj = random.randint(1,10)
    return broj

brojac = 0
while True:
    unos = int(input("Unesi broj izmedu 1-10 (0 ako zelite prekiniti program): "))
    if unos < 0 or unos > 10:
        print("Pogresan unos")
    else:
        brojac += 1
    if unos == 0:
        break
    if unos == izvuci_broj():
        print(f"Broj je pogoden iz {brojac}. pokušaja")
        break
