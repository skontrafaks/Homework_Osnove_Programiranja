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


def main():
    l = []
    br = -1
    while len(l) > br:
        unos_broja_u_listu(l)
        br += 1
    else:
        print(max_element(l))
        print(l)


main()