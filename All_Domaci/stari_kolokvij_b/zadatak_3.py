ulaz = open("ulaz.txt", "r")

linije = ulaz.readlines()
print(linije)

main_list = []
print(linije)
for i in linije:
    b = i.split(" ")
    print(b)
    main_list.append([int(b[1]), b[0]]) #radi liste unutar liste, bitno da je broj prvi element

print(main_list)
main_list.sort(reverse = True) #sorta naopako,te sorta po prvom elementu manje liste
print(main_list)
print(f"Najveca datoteka je {main_list[0][1]}, sa {main_list[0][0]} kB")