databatohy=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day3_cast1_data.txt", "rt")]

pomocnepole = []
SpolecnyPrvek = []
Priorita = 0

for radek in databatohy:
    prvniartikl,druhyartikl = radek[:len(radek)//2], radek[len(radek)//2:]
    for i in prvniartikl:
        pomocnepole.append(i)
    for j in druhyartikl:
        if j in pomocnepole:
            SpolecnyPrvek.append(j)
            break
    pomocnepole =[]

for char in SpolecnyPrvek:
    if ord(char) >= 91:
        Priorita += (int(ord(char))-96)
    else:
        Priorita += (int(ord(char))-38)

print ("Součet priorit je:", Priorita)
        

