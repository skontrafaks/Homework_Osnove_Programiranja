from moj_modul import palindrom
s = str(input("Unesi neki niz znakova: \n"))
def najduzi_polindrom(s):
    najduzi = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            rijec = s[i:j]
            if palindrom(rijec) == True:
                if len(rijec) > len(najduzi):
                    najduzi = rijec
    return najduzi

print(najduzi_polindrom(s))