znakovi = str(input("Unesi neki niz znakova:"))
def samoglasnik(niz_znakova):
    broj_samoglasnika = 0
    for i in niz_znakova:
        if i == "a" or i == "e" or i == "o" or i == "i" or i == "u":
            broj_samoglasnika += 1
    return broj_samoglasnika

print(f"Broj samoglasnika u nasem strigu je {samoglasnik(znakovi)}")
print(f"A postotak svih samoglasnika je {((samoglasnik(znakovi))/len(znakovi))*100} %")