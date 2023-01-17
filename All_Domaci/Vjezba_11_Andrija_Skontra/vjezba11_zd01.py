from random import randrange
n = 0
while n <= 0:
    n = int(input("Unesi neki broj veci od nule:"))

l = [randrange(1, 100) for i in range(n)]
parni = 0
neparni = 0
for i in range(len(l)):
    if l[i] % 2 == 0:
        parni += 1
    if l[i] % 2 == 1:
        neparni += 1

print(l, parni, neparni)