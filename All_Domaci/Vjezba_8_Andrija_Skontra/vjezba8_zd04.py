l = [1,2,3,4,5,6,7,8,9]

print("Naša lista:", l)

s = int(input("Unesi broj koji zelis provjeriti nalazi li se u listi:\n"))

def binarnoPretrazivanje (l,s):
    srednji = int((len(l) - 1)/2)
    if len(l) == 2:
        srednji = 1
    if len(l) == 1:
        return False
    elif l[srednji] < s:
        l = l[srednji:]
        return binarnoPretrazivanje(l, s)
    elif l[srednji] > s:
        l = l[:srednji]
        return binarnoPretrazivanje(l, s)
    else:
        return True


print(binarnoPretrazivanje(l,s))