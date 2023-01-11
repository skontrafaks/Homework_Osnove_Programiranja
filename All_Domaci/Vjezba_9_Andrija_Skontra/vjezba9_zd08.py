# program za kompresiju teksta koji radi na principu da rijeći koje se ponavljaju dobivaju
# jednostavnije vrijednosti u brojevima, te na taj nacin smanjujemo broj bajtova u slucajevima kad nam se rijeci cesto ponavljaju
# moze napraviti dekompresiju samo file-ova koje je vec kompresirao

answer = input("Do you want to compress or decompress:\n")

if answer.lower() == "compress":

    text_file = input("Input the TEXT FILE NAME of the text you want to compress(without the extension .txt):\n")
    ulaz = open(f"./{text_file}.txt", "r")
    text_list = ulaz.read()
    text_list = text_list.split(" ")
    my_dict = {val: i for i, val in enumerate(text_list, start=1)}

    with open(f'compressed_{text_file}.txt', 'w') as izlaz:
        for key, value in my_dict.items():
            izlaz.write(f"{key} : {value} ")
        for i in text_list:
            for key, value in my_dict.items():
                if i == key:
                    izlaz.write(f"{value} ")

elif answer.lower() == "decompress":

    text_file = input("Input the TEXT FILE NAME of the text you want to decompress(without the extension .txt):\n")
    ulaz = open(f"./{text_file}.txt", "r")
    text_list = ulaz.read()
    text_list = text_list.split(" ")
    decomp_dict = {}
    for i in range(1, len(text_list)):
        if text_list[i] == ":":
            decomp_dict[text_list[i + 1]] = text_list[i - 1]
    with open(f'decompressed_{text_file}.txt', 'w') as izlaz:
        for i in range(1, len(text_list)):
            if text_list[i - 1] != ":":
                try:
                    number = int(text_list[i])
                    key = decomp_dict.get(text_list[i])
                    izlaz.write(f"{key} ")
                except ValueError:
                    pass


