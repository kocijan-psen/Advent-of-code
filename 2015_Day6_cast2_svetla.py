datasvetla = open("Den6_cast1_data.txt","rt")
rows = 1000
cols = 1000
n = 0
f = 0

def printPole(array, r, c):
    for i in range(r):
        for j in range(c):
            print(array[i][j], end=" ")
        print()

def cntPole(array, r, c):
    cnt = 0
    for i in range(r):
        for j in range(c):
            cnt += array[i][j]
    return cnt


pole = [[0 for x in range(rows)] for y in range(cols)]

for radek in datasvetla:
    
    pomocnepole = radek.split(' ')
    if pomocnepole [0] == "turn":
        Stav = pomocnepole[1]
        souradnicestart = pomocnepole[2].split(',')
        Xstart = int(souradnicestart[0])
        Ystart = int(souradnicestart[1])
        souradniceend = pomocnepole[4].split(',')
        Xend = int(souradniceend[0])
        Yend = int(souradniceend[1])
    else:
        Stav = pomocnepole[0]
        souradnicestart = pomocnepole[1].split(',')
        Xstart = int(souradnicestart[0])
        Ystart = int(souradnicestart[1])
        souradniceend = pomocnepole[3].split(',')
        Xend = int(souradniceend[0])
        Yend = int(souradniceend[1])
    
    for i in range(Xstart, Xend+1):
        for j in range(Ystart, Yend+1):
            if Stav == "on":
                pole[i][j] += 1
            elif Stav == "off":
                if pole[i][j] > 0:
                    pole[i][j] -= 1
            elif Stav == "toggle":
                pole[i][j] += 2
               
    
print(cntPole(pole,rows,cols))



