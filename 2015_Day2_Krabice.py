
dataKrabice = open("2015/2015_Day2_Krabice_podklady.txt","rt")
Plocha = 0
PlochaCelkem = 0
Ribbon = 0
RibbonCelkem = 0
Ribbonbow = 0

for radek in dataKrabice:
    
    poleCisel = radek.split('x')
    length = int(poleCisel[0])
    width = int(poleCisel[1])
    height = int(poleCisel[2])


    Plocha1 = length*width
    Plocha2 = length*height
    Plocha3 = width*height

    NajdiNejmensi = [ Plocha1, Plocha2, Plocha3]
    NajdiNejmensi.sort()
    NejmensiRibbon = [ length, width, height]
    NejmensiRibbon.sort()

    Plocha = 2*Plocha1+2*Plocha2+2*Plocha3+NajdiNejmensi[0]
    Ribbonbow = length*width*height
    Ribbon = NejmensiRibbon[0]+NejmensiRibbon[0]+NejmensiRibbon[1]+NejmensiRibbon[1]+Ribbonbow
    RibbonCelkem += Ribbon

    PlochaCelkem += Plocha
    NajdiNejmensi=[]

print("Papír je:",PlochaCelkem)
print("Masle je:",RibbonCelkem)
exit()