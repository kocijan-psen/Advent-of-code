data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_day6_data.txt", "rt")]

answer1 = 0
temp2 = []
sorted = []

for line in data:
    temp = line.split()
    temp2.append(temp)

# print(temp2)
# print(len(temp2))

for i in range(1,len(temp2[0])):                #sortace do polí aby byla rychlost a distance u sebe
    sorted.append([temp2[0][i],temp2[1][i]])

# print(sorted)

for race in sorted:
    record_ = 0
    for holding in range(0,int(race[0])+1):     #doba držení snižuje čas proto jen mezi sebou po jednom odečítám
        speed =  int(race[0])-holding
        dist_ = speed*holding
        if dist_ > int(race[1]):
            record_+=1
    if answer1 == 0:
        answer1 +=record_
    else:
        answer1 = answer1*record_

print(f"Výsledek části 1 je: {answer1}")

part2 = []
for line in data:                               #zpracování dat pro část 2, jen vytvořím z řádku jedno číslo
    result = line.replace(" ","")
    if "Time:" in result:
        result=result.replace("Time:","")
    if "Distance:" in result:
        result=result.replace("Distance:","")
    part2.append(int(result))

print("part2", part2)



part2record = 0
for holding in range(0,part2[0]+1):     #v části 2 definované limity
        speed =  part2[0]-holding
        dist_ = speed*holding
        if dist_ > int(part2[1]):
            part2record+=1

print(f"Výsledek část 2 je: {part2record}")