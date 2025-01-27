dataPin = open("2016/2016_Day2_data.txt","rt")

x=1
y=1
Pin = []

Display = [ [1,2,3],
            [4,5,6],
            [7,8,9]]

for radek in dataPin:
    for char in radek:
        if char == 'U': x -=1
        elif char == 'D': x +=1
        elif char == 'L': y -=1
        elif char == 'R': y +=1
        
        if x<=-1: 
            x+=1
        elif x>=5:
            x-=1
        elif y<=-1:
            y+=1
        elif y>=3:
            y-=1
        cislo = Display [x][y]
    Pin.append(cislo)

print ("pin je: ", Pin)