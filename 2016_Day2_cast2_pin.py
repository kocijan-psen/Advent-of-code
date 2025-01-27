dataPin = open("2016/2016_Day2_data.txt","rt")

x=2
y=0
Pin = []
Display = [ ['0','0','1','0','0'],
            ['0','2','3','4','0'],
            ['5','6','7','8','9'],
            ['0','A','B','C','0'],
            ['0','0','D','0','0']]

for radek in dataPin:
    for char in radek:
        cislo = Display [x][y]
        if char == 'U': 
            x -= 1
            if x<=-1:
                x += 1
            cislo = Display [x][y]
            if cislo == '0':
                x += 1
        elif char == 'D': 
            x += 1
            if x>=5:
                x -= 1
            cislo = Display [x][y]
            if cislo == '0':
                x -= 1
        elif char == 'L': 
            y -= 1
            if y<=-1:
                y += 1
            cislo = Display [x][y]
            if cislo == '0':
                y += 1
        elif char == 'R': 
            y += 1
            if y>=5:
                y -= 1
            cislo = Display [x][y]
            if cislo == '0':
                y -= 1
        cislo = Display [x][y]

    Pin.append(cislo)

print ("pin je: ", Pin)