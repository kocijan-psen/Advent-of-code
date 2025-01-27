databID=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Den4_cast1_data.txt", "rt")]

Fullycontained =0
Overlap = 0

for radek in databID:
    pomocnepole = radek.split(',')
    elf1 =pomocnepole[0].split('-')
    elf2 =pomocnepole[1].split('-')

    if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])) or (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
        Fullycontained +=1
    
print('Počet párů je:', Fullycontained)
