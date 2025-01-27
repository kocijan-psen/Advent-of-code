databatohy=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day3_cast2_data.txt", "rt")]

PrvekVBatohu1 = []
PrvekVBatohu2 = []
SpolecnyPrvek = []
Priorita = 0
Prvek = 0

for radek in databatohy:
    Prvek +=1
    if Prvek == 1:
        for i in radek:
            PrvekVBatohu1.append(i)   

    if Prvek == 2:
        for j in radek:
            PrvekVBatohu2.append(j)
   
    if Prvek == 3:
        for k in radek:
            if k in PrvekVBatohu1 and k in PrvekVBatohu2:
                SpolecnyPrvek.append(k)
                PrvekVBatohu1 = []
                PrvekVBatohu2 = []
                Prvek = 0
                break
    

for char in SpolecnyPrvek:
    if ord(char) >= 91:
        Priorita += (int(ord(char))-96)
    else:
        Priorita += (int(ord(char))-38)

print ("Součet priorit je:", Priorita)
        

