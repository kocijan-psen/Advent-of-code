#datapassphrases = open("C:\Users\kocij\Documents\Python\2017\Den4_cast1_data.txt","rt")
datapassphrases=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day4_cast1_data.txt", "rt")]
JeTam = 0
OkPassphrase = 0
KontrolniPole = []
j = 0


for radek in datapassphrases:
    pomocnepole=radek.split(' ')

    for i in pomocnepole:
        
        if not i in KontrolniPole:
            KontrolniPole.append(i)
        else:
            break
    if KontrolniPole == pomocnepole:
        OkPassphrase+=1

    KontrolniPole = []
  
           
        
print("Počet Ok: ",OkPassphrase)