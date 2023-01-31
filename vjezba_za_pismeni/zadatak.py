ulaz = open("imena.txt", "r")
f = ulaz.read()
linije = f.split("\n")

a = sorted(linije, key=lambda x: len(x))
print(a)