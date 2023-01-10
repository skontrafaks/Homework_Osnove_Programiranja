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

def main():
    if prost(unos_int()) == True:
        print("Broj je prost")
    else:
        print("Broj nije prost")

main()