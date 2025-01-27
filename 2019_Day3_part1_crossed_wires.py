data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day3_data.txt", "rt")]
array = []
Wire1 = []
Wire2 = []
temp = []
Final = []


def separatewire(direction,i): #roztřízení dat a vložení do knihovny. Logika krokování po jednom ať nevynechám žádnou pozici, kde se dráty můžou protnout.
    global Wire1,Wire2, a, b, temp

    if "D" in direction:
        j = int(direction.replace("D",""))
        for _ in range(j):
            a-=1
            if i == 0:
                Wire1.append([a,b])
            if i == 1:
                Wire2.append([a,b])
                if [a,b] in Wire1:
                    temp.append([a,b])
          
    elif "U" in direction:
        j = int(direction.replace("U",""))
        for _ in range(j):
            a+=1
            if i == 0:
                Wire1.append([a,b])
            if i == 1:
                Wire2.append([a,b])
                if [a,b] in Wire1:
                    temp.append([a,b])

    elif "L" in direction:
        j = int(direction.replace("L",""))
        for _ in range(j):
            b-=1              
            if i == 0:
                Wire1.append([a,b])
            if i == 1:
                Wire2.append([a,b])
                if [a,b] in Wire1:
                    temp.append([a,b])

    elif "R" in direction:
        j = int(direction.replace("R",""))
        for _ in range(j):
            b+=1
            if i == 0:
                Wire1.append([a,b])
            if i == 1:
                Wire2.append([a,b])
                if [a,b] in Wire1:
                    temp.append([a,b])



#hlavni program
for line in data: #rozdeleni dat
    array.append(line.split(",")) 


a = 0
b = 0
i = 0
for numbers in array: # roztrizeni
    for number in numbers:
        separatewire(number.strip(),i)
    i +=1
    a = 0
    b = 0


for k in temp:
    if k[0] < 0:
        k[0] = k[0]*(-1)
    if k[1] < 0:
        k[1] = k[1]*(-1)
    cnt = k[0]+k[1]
    k.append(cnt)

print(temp)

minimum = 1000000
for k in temp:
    if int(k[2]) < minimum:
        minimum = k[2]
        n = [k[0],k[1]]
print("souradnice minima",n)
print("minimum",minimum)

print("výsledek", minimum)





    

    

