datakkamennuzkypapir=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day2_cast1_data.txt", "rt")]

Body = 0


for radek in datakkamennuzkypapir:
    pomocnepole=radek.split(' ')

    if pomocnepole[0] == 'A' and pomocnepole[1] == 'Z':
        Body +=3
    elif pomocnepole[0] == 'A' and pomocnepole[1] == 'Y':
        Body +=8
    elif pomocnepole[0] == 'C' and pomocnepole[1] == 'Y':
        Body +=2
    elif pomocnepole[0] == 'C' and pomocnepole[1] == 'X':
        Body +=7
    elif pomocnepole[0] == 'B' and pomocnepole[1] == 'Z':
        Body +=9
    elif pomocnepole[0] == 'B' and pomocnepole[1] == 'X':
        Body +=1
    elif pomocnepole[0] == 'A' and pomocnepole[1] == 'X':
        Body +=4
    elif pomocnepole[0] == 'B' and pomocnepole[1] == 'Y':
        Body +=5
    elif pomocnepole[0] == 'C' and pomocnepole[1] == 'Z':
        Body +=6
    
    pomocnepole=[]

print("Počet bodů:", Body)