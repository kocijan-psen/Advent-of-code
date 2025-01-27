data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day5_data.txt", "rt")]

rows=1000
cols=1000

array = [[0 for x in range(rows)] for y in range(cols)] #přípravné pole

for line in data:
    
    temp = line.split(" -> ")
    temp1 = temp[0].split(",")
    x1 = int(temp1[0])
    y1 = int(temp1[1])
    temp2 = temp[1].split(",")
    x2 = int(temp2[0])
    y2 = int(temp2[1])
    # print(x1,y1,x2,y2)
    if y1 == y2:
        lowerx, upperx = sorted([x1,x2])
        for i in range(lowerx,upperx+1):
            array[y1][i] +=1
    elif x1 == x2:
        lowery, uppery = sorted([y1,y2])
        for j in range(lowery,uppery+1):
            array[j][x1] +=1
    elif abs(x2 - x1) == abs(y2 - y1):  # Diagonální čára
        for k in range(0, abs(x2 - x1) + 1):
            if x1 < x2 and y1 < y2:
                array[y1 + k][x1 + k] += 1
            elif x1 < x2 and y1 > y2:
                array[y1 - k][x1 + k] += 1
            elif x1 > x2 and y1 < y2:
                array[y1 + k][x1 - k] += 1
            elif x1 > x2 and y1 > y2:
                array[y1 - k][x1 - k] += 1

# for ble in array:
#     print(ble)

answerpart2 = 0
for a in array:
    for b in a:
        if b >=2:
            answerpart2 +=1

print("answer part2: ", answerpart2)

    



