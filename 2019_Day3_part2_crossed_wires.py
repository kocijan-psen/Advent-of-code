data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day3_data.txt", "rt")]
array = []
a = 0
b = 0
i = 0
j = 0
Wire1 = [[0,0,0,0,0]] #pos[0] = začátek X, pos[1] = začátek y, pos[2] = konec X, pos[3] = konec y, pos[4] delka dratu
Wire2 = [[0,0,0,0,0]] #pos[0] = začátek X, pos[1] = začátek y, pos[2] = konec X, pos[3] = konec y, pos[4] delka dratu
temp = []
minlenght = []
dir = True


def separatewire(direction,i): #logika, vytvořím úsečky
    global Wire1,Wire2,j

    if "D" in direction:
        if i == 0:
            sub = Wire1[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[2]-=int(direction.replace("D",""))
            sub[4]+=int(direction.replace("D",""))

            Wire1.append(sub)
        if i == 1:
            sub = Wire2[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[2]-=int(direction.replace("D",""))
            sub[4]+=int(direction.replace("D",""))

            Wire2.append(sub)
  
    elif "U" in direction:
        if i == 0:
            sub = Wire1[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[2]+=int(direction.replace("U",""))
            sub[4]+=int(direction.replace("U",""))
            Wire1.append(sub)
        if i == 1:
            sub = Wire2[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[2]+=int(direction.replace("U",""))
            sub[4]+=int(direction.replace("U",""))

            Wire2.append(sub)

    elif "L" in direction:
        if i == 0:
            sub = Wire1[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[3]-=int(direction.replace("L",""))
            sub[4]+=int(direction.replace("L",""))

            Wire1.append(sub)
        if i == 1:
            sub = Wire2[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[3]-=int(direction.replace("L",""))
            sub[4]+=int(direction.replace("L",""))
            Wire2.append(sub)

    elif "R" in direction:
        if i == 0:
            sub = Wire1[j][:]            
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[3]+=int(direction.replace("R",""))
            sub[4]+=int(direction.replace("R",""))

            Wire1.append(sub)
        if i == 1:
            sub = Wire2[j][:]
            sub[0] = sub[2]
            sub[1] = sub[3]
            sub[3]+=int(direction.replace("R",""))
            sub[4]+=int(direction.replace("R",""))

            Wire2.append(sub)
    j+=1

#hlavni program
for line in data:
    array.append(line.split(",")) #rozdeleni dat

for numbers in array: # roztrizeni
    for number in numbers:
        separatewire(number.strip(),i)
    i +=1
    j = 0

del Wire1[0]
del Wire2[0]
for k in Wire1:
    for l in Wire2:
        #print(k, l)
        if k[0] == k[2]: # pokud souhlasí, jedu po x
            if k[0] in range(min(l[0],l[2]), max(l[0],l[2]+1)) and l[1] in range(min(k[1],k[3]), max(k[1],k[3]+1)):
                lenWire1 = k[4]-abs(k[3]-l[3]) #logika - už v průběhu přičítám délky a ve chvíli průsečíku, odečtu jen rozdíl délky
                lenWire2 = l[4]-abs(k[2]-l[2])
                totallenght = lenWire1 + lenWire2
                temp.append([k[0],l[1],totallenght])
                minlenght.append(totallenght)
                #print("1st",k, l,k[0],l[1])
        else:                             #když nejedu po x, jedu po y
            if k[1] in range(min(l[1],l[3]), max(l[1],l[3]+1)) and l[0] in range(min(k[0],k[2]), max(k[0],k[2]+1)):
                lenWire1 = k[4]-abs(k[2]-l[2])
                lenWire2 = l[4]-abs(k[3]-l[3])
                totallenght = lenWire1 + lenWire2
                temp.append([k[1],l[0],totallenght])
                minlenght.append(totallenght)
                #print("2nd",k, l,k[1],l[0])



minlenght.sort()
print("Nejmenši delka dratů je:",minlenght[1])
print(temp)










    

    

