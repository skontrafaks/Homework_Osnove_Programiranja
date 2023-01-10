def palindrom(s):
    if s == s[::-1]:
        return "je palindrom"
    else:
        return "nije palindrom"

s = str(input("Unesi neke znakove:\n"))

print(f'Ovo {palindrom(s)}')