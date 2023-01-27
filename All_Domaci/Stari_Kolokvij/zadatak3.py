ulaz = open("ulaz.txt", "r")
izlaz = open("izlaz.txt", "w")

linije = ulaz.readlines()
print(linije)

main_list = []
print(linije)
for i in linije:
    b = i.split(" ")
    print(b)
    main_list.append([int(b[1]), b[0]])

print(main_list)
main_list.sort()
print(main_list)
print(f"Najmanji grad u našem file-u je {main_list[0][1]}, sa {main_list[0][0]} stanovnika")
