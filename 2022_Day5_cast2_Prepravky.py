data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day5_cast2_data.txt", "rt")]

pole =["SLW","JTNQ","SCHFJ","TRMWNGB","TRLSDHQB","MJBVFHRL","DWRNJM","BZTFHNDJ","HLQNBFT"]
#pole =["ZN","MCD","P"]

for radek in data:
    pomocnepole=radek.split(' ')
    rozsah = (int(pomocnepole[1]))
    odkud = (int(pomocnepole[3])-1)
    kam = (int(pomocnepole[5])-1)

    
    poslednichar = pole[odkud][-rozsah:]
    pole[kam] = pole[kam]+poslednichar
    pole[odkud] = pole[odkud][:-rozsah]

print("Poslední přepravky jsou",pole[0][-1], pole[1][-1],pole[2][-1],pole[3][-1],pole[4][-1],pole[5][-1],pole[6][-1],pole[7][-1],pole[8][-1])
#print("Poslední přepravky jsou",pole[0][-1], pole[1][-1],pole[2][-1])
print(pole)
