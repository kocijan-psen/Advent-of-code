def funkce (dratD):
    vysledek = 0
    global knihovnadraty, nalezeneDraty
    databrany = open("2015_Day7_cast1_logickeBrany.txt","rt")
    if not dratD in nalezeneDraty:
        for radek in databrany:
            data = radek.split(" -> ")
            vstupkabel = data[0]
            vystupkabel =data[1].replace("\n","")

            if vystupkabel == dratD:
                pole = vstupkabel.split(' ')
                if len(pole) == 1: #číslo nebo kabel
                    if pole[0] in knihovnadraty:
                        vysledek = funkce(pole[0]) #musím udělat to vložení
                    else: 
                        vysledek = int(pole[0])
                
                elif len(pole) == 2: #první pole vždy "NOT"
                    if pole[1] in knihovnadraty:
                        vysledek = 65535-int(funkce(pole[1]))  #musím udělat to vložení
                    else:
                        vysledek = 65535-int(pole[1])
                
                elif len(pole) == 3:
                    if pole[1] == "AND":
                        if pole[0] in knihovnadraty:
                            vysledek = funkce(pole[0]) & funkce(pole[2])
                        else:
                            vysledek = int(pole[0]) & funkce(pole[2]) #pole[0] číselná hodnota
                    elif pole[1] == "OR":
                        vysledek =funkce(pole[0]) | funkce(pole[2])
                    elif pole[1] == "RSHIFT":
                        vysledek = funkce(pole[0]) >> int(pole[2])
                    elif pole[1] == "LSHIFT":
                        vysledek = funkce(pole[0]) << int(pole[2])

                nalezeneDraty.update({dratD:int(vysledek)})
    return nalezeneDraty[dratD]


databrany = open("2015_Day7_cast1_logickeBrany.txt","rt")

knihovnadraty = []
nalezeneDraty = {}

for radek in databrany:
    draty = radek.split(" -> ")
    vystupkabel =draty[1].replace("\n","")
    knihovnadraty.append(vystupkabel)

print('co je v knihovne', knihovnadraty)

a = funkce("a")
print('Výsledek:',a)

nalezeneDraty = {}
nalezeneDraty["b"] = a
print(funkce("a"))