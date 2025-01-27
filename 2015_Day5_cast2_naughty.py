
datanaughty = open("2015_Day5_cast1_podklady.txt","rt")


Podminka1 = False
Podminka2 = False
Naughty = 0
Splnuje = 0

for radek in datanaughty:

    for a in range(len(radek)-1):
        doublechar = radek[a]+radek[a+1]
        if radek.count(doublechar) >=2:
                Podminka1 = True
                break

    for a in range(len(radek)-2):
        if radek[a+2] == radek[a]:
            Podminka2 = True
            break

    if (Podminka1 == True) and (Podminka2 == True):
        Naughty +=1

    Podminka1 = False
    Podminka2 = False
    a = 0
    


print("Naughty cunt:)", Naughty)
