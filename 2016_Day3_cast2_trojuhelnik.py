dataTrojuhelniky = open("2016/2016_Day3_data.txt","rt")
RozmeryTrojuhelniku = []
Seznam = []

Pocet = 0
i = 0
a = 0
x = 0
y = 0


for radek in dataTrojuhelniky:

    OpravenyRadek=radek.replace('\n','')

    PoleRozmeru = OpravenyRadek.split(' ')
    PocetVPoli = len(PoleRozmeru)

    for a in range((PocetVPoli)):
        if not PoleRozmeru[a] == '':
            Delka = PoleRozmeru[a]
            RozmeryTrojuhelniku.append(int(Delka))
        a += 1
    
    Seznam.append(RozmeryTrojuhelniku)
    RozmeryTrojuhelniku = []


for y in range(3):
    x = 0
    while x < len(Seznam):

        hodnota1 = int(Seznam[x][y])
        hodnota2 = int(Seznam[x+1][y])
        hodnota3 = int(Seznam[x+2][y])

        NejvetsiRozmer = [hodnota1, hodnota2,hodnota3]
        NejvetsiRozmer.sort()

        #if NejvetsiRozmer[2] < (NejvetsiRozmer[0] + NejvetsiRozmer[1]):
        #    Pocet +=1
        Kontrola = NejvetsiRozmer[2] - (NejvetsiRozmer[0] + NejvetsiRozmer[1])
        if Kontrola < 0:
           Pocet +=1
        x += 3
        
    NejvetsiRozmer = []

print("Trojúhelníků je:", Pocet)