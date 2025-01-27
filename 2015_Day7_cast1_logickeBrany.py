from ast import If
from dataclasses import replace
from lib2to3.pgen2.token import STRING

data = open("2015_Day7_cast1_logickeBrany.txt","rt")
databrany = []
knihovnadraty = []

for radek in data:
    databrany.append(radek)
    draty = radek.split(" -> ")
    #vstupkabel = draty[0]
    vystupkabel =draty[1].replace("\n","")
    knihovnadraty.append(vystupkabel)

#print('co je v knihovne', knihovnadraty)

def funkce (dratD):
    vysledek = 0
    global knihovnadraty, databrany

    for radek in databrany:
        data = radek.split(" -> ")
        vstupkabel = data[0]
        vystupkabel =data[1].replace("\n","")

        if vystupkabel == dratD:
            pole = vstupkabel.split(' ')
            if len(pole) == 1: #číslo nebo kabel
                if pole[0] in knihovnadraty:
                    vysledek = int(funkce(pole[0])) #musím udělat to vložení
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
                        vysledek = int(funkce(pole[0])) & int(funkce(pole[2]))
                    else:
                        vysledek = int(pole[0]) & int(funkce(pole[2])) #pole[0] číselná hodnota
                elif pole[1] == "OR":
                    vysledek =int(funkce(pole[0])) | int(funkce(pole[2]))
                elif pole[1] == "RSHIFT":
                    vysledek = int(funkce(pole[0])) >> int(pole[2])
                elif pole[1] == "LSHIFT":
                    vysledek = int(funkce(pole[0])) << int(pole[2])
    return vysledek
print('Výsledek:', funkce("a"))