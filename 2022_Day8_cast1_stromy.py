data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day8_cast1_data.txt", "rt")]

array = []
a = -1
Seznam = []
Pocet = 0



for i in range(len(data)):
    array.append([])
    for j in data[i]:
        array[i].append(int(j)) 

for i in range(len(array)):
    for j in range(len(array[i])):
        x = array[i][j]
        if a < x:
            a = array[i][j]
            if not (i,j) in Seznam:
                Seznam.append((i,j))
        else:
            continue
    a=-1

for i in range(len(array)):
    for j in reversed(range(len(array[i]))):
        x = array[i][j]
        if a < x:
            a = array[i][j]
            if not (i,j) in Seznam:
                Seznam.append((i,j))
        else:
            continue
    a=-1

for i in range(len(array)):
    for j in range(len(array[i])):
        x = array[j][i]
        if a<x:
            a = array[j][i]
            if not (j,i) in Seznam:
                Seznam.append((j,i))
        else:
            continue    
    a=-1

for i in range(len(array)):
    for j in reversed(range(len(array[i]))):
        x = array[j][i]
        if a<x:
            a = array[j][i]
            if not (j,i) in Seznam:
                Seznam.append((j,i))
                
        else:
            continue
        
    a=-1

print(len(Seznam))

