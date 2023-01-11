f = open('./tekst1.txt', 'r')
x = f.read()
y = []
for i in range(len(x)):
    if x[i].isalpha():
        y.append(x[i])
print(''.join(y))
f.close()