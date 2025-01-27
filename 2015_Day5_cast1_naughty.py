
datanaughty = open("2015_Day5_cast1_podklady.txt","rt")

samohlaska = 0
Podminka1 = False
Podminka2 = False
Podminka3 = False
Naughty = 0
Splnuje = 0

for radek in datanaughty:
    for char in radek:
        if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
            samohlaska +=1

            if samohlaska >=3:
                Podminka1 = True
                break

    for char in radek:
        doublechar=char+char
        if doublechar in radek:
            Podminka2 = True
            break

    #for a in range(len(radek)-1):
    #    if radek[a+1] == radek[a]:
    #        Podminka2 = True
    #        break
                
    if (not 'ab' in radek) and (not 'cd' in radek) and (not 'pq' in radek) and (not 'xy' in radek):
        Podminka3 = True

    if (Podminka1 == True) and (Podminka2 == True) and (Podminka3 == True):
        Naughty +=1

    Podminka1 = False
    Podminka2 = False
    Podminka3 = False
    samohlaska = 0
    


print("Naughty cunt:)", Naughty)
