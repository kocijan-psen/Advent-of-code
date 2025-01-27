data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day3_data.txt", "rt")]
array = []
a = 0
b = 0
i = 0
Wire1 = []
Wire2 = []
temp = []
cross1 = []
cross2 = []


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
for line in data:
    array.append(line.split(",")) #rozdeleni dat

for numbers in array: # roztrizeni
    for number in numbers:
        separatewire(number.strip(),i)
    i +=1
    a = 0
    b = 0

print(temp)

step = 0
for tmp1 in Wire1:
    step +=1
    if tmp1 in temp:
        cross1.append(step)
        
step = 0
for tmp2 in Wire2:
    step +=1
    if tmp2 in temp:
        cross2.append(step)
final = []
for x in range(len(cross1)):
    final.append(cross1[x]+cross2[x])

final.sort()

Answer = final[0]

print("Answer:", Answer)
    








    

    

