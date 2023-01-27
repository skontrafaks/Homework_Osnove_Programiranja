def Alfanumericki(znakovi):
    Broj = 0
    Slovo = 0
    for znak in znakovi:
        if znak.isupper():
            Slovo += 1
        if znak.islower():
            Slovo += 1
        if znak.isdigit():
            Broj += 1
    return Broj, Slovo

Unos = input("Unesi neke znakove: ")
broj, slovo = Alfanumericki(Unos)
print(f"Ovi znakovi sadrze ovoliko brojeva: {broj}\nTe sadrze ovoliko slova: {slovo} ")
