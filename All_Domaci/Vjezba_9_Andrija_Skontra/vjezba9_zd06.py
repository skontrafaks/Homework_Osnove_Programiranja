ulaz = open("./tekst6.txt", "r")
izlaz = open('./izlaz6.txt', 'w')
x = ulaz.readlines()

for i in range(len(x)):
    x[i] = x[i].split(' ')

print(x)

d = {}

for i in range(len(x)):
    d[x[i][0]] = round(float(x[i][1]) / (float(x[i][2])**2), 2)

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}  # sortiraj po value

for key, value in d.items():
    izlaz.write(f"{key}\t {value}")
    izlaz.write("\n")
