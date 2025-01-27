dataTrojuhelniky = open("2016/2016_Day3_data.txt","rt")
SeznamRozmeru = []
Pocet = 0
a = 0
x = 0

for radek in dataTrojuhelniky:
    OpravenyRadek=radek.replace('\n','')

    PoleRozmeru = OpravenyRadek.split(' ')
    PocetVPoli = len(PoleRozmeru)

    for a in range((PocetVPoli)):
        if not PoleRozmeru[a] == '':
            Delka = PoleRozmeru[a]
            SeznamRozmeru.append(Delka)
        a += 1

    Rozmer1 = int(SeznamRozmeru[0])
    Rozmer2 = int(SeznamRozmeru[1])
    Rozmer3 = int(SeznamRozmeru[2])

    NejvetsiRozmer = [Rozmer1, Rozmer2, Rozmer3]
    NejvetsiRozmer.sort()

    #JeToTrojuhelnik = int(NejvetsiRozmer[2]) - int(NejvetsiRozmer[0]) - int(NejvetsiRozmer[1])

    #if not JeToTrojuhelnik >= 0:
    #    Pocet +=1

    if NejvetsiRozmer[2] < (NejvetsiRozmer[0] + NejvetsiRozmer[1]):
        Pocet +=1

    SeznamRozmeru = []
    NejvetsiRozmer = []

print("Počet trojůhelníků je:",Pocet)

