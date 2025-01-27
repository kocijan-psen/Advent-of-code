data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day2_data.txt", "rt")]

cnt = 0
cnt2 = 0

def direction():                            #kontrola zda je celá řada buď klesající nebo stoupající
    global temp, i
    point1 = int(temp[0])-int(temp[1])
    flag1 = None                            #výchozí hodnota
    if point1<0:
        flag1 = "up"
    elif point1>0:
        flag1 = "down"
    point2 = int(temp[i])-int(temp[i+1])
    flag2 = None                            #výchozí hodnota
    if point2<0:
        flag2 = "up"
    elif point2>0:
        flag2 = "down"
    
    if flag1 == flag2:
        return True
    else:
        return False

for line in data:                           #hlavní kód, jedu po řádcích - podmínky: nesmí se rovnat, rozdíl nesmí být víc než 3
    temp = line.split()                     #musí jen klesat nebo jen stoupat
    control =0
    for i in range(len(temp)-1):
        if temp[i] != temp[i+1]:
            if abs(int(temp[i])-int(temp[i+1])) <=3:
                flag = direction()
                if flag == True:
                    control +=1
    if control == len(temp)-1:
        cnt +=1
        # print(line)

print("Answer part1: ", cnt)

                





