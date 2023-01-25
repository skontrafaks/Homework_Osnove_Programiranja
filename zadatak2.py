def upper_lower(znakovi):
    malo = 0
    veliko = 0
    ostalo = 0
    for znak in znakovi:
        if znak.isupper():
            veliko += 1
        elif znak.islower():
            malo += 1
        else:
            ostalo += 1

    return print(f"Malih slova je {malo}, velikih sloga je {veliko}, te ostalih znakova je {ostalo}")

unos = input("Unesi neki niz znakova: ")
upper_lower(unos)

