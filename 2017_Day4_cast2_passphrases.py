datapassphrases=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day4_cast2_data.txt", "rt")]
JeTam = 0
OkPassphrase = 0
KontrolniPole = []
UpravenePole = []


for radek in datapassphrases:
    pomocnepole=radek.split(' ')

    for i in pomocnepole:
        i = ''.join(sorted(i))
        UpravenePole.append(i)
        
    for j in UpravenePole:
        
        if not j in KontrolniPole:
            KontrolniPole.append(j)
        else:
            break
    if KontrolniPole == UpravenePole:
        OkPassphrase+=1

    KontrolniPole = []
    UpravenePole = []
           
        
print("Počet Ok: ",OkPassphrase)