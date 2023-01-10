import sys
path = sys.path.append('Vjezba_8_Andrija_Skontra')


def unos_broja_u_listu(l):
    n = input("Unesi realan broj: ")
    if n:
        try:
            n = float(n)
            l.append(n)
        except ValueError:
            return l
    else:
        return l


def max_element(l):
    if len(l) > 0:
        return max(l)

def unos_int():
    n = input("Unesi neki cijeli broj: \n")
    return int(n)

def prost(n):
    brj = 0
    for i in range(1,n+1):
        if n % i == 0:
            brj += 1
    if brj <= 2:
        return True
    else:
        return False

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

def palindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False