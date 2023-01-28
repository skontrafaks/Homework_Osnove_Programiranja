import random

def igra_pogadanja(trazeni_broj, brojac):
    unos = int(input("Unesi broj izmedu 1-10 (0 ako zelite prekiniti program): "))
    if unos == 0:
        return None
    if unos == trazeni_broj:
        return brojac + 1
    brojac += 1
    if unos < 0 or unos > 10:
        print("Pogresan unos")
        return igra_pogadanja(trazeni_broj, brojac)
    else:
        if not unos == trazeni_broj:
            return igra_pogadanja(trazeni_broj, brojac)

brojac = 0
trazeni_broj = random.randint(1,10)
broj_pokusaja = igra_pogadanja(trazeni_broj,brojac)
if broj_pokusaja != None:
    print(f"Broj pogoden iz {broj_pokusaja}. pokusaja.")


