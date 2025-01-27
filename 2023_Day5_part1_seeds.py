data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day5_data.txt", "rt")]

seed = []
i = 0
garten = {"soil": [], "fertilizer":[],"water":[], "light" : [], "temperature" :[], "humidity" :[], "location" :[]}
type_ = ["soil", "fertilizer","water", "light", "temperature", "humidity", "location"]


for line in data:
    if line == "":
        i +=1
    if i == 0:                  #prvni radek jsou semena
        temp = line.split()
        for j in range(1,len(temp)):
            seed.append(int(temp[j]))
        # print(seed)
    elif i >= 1:                #nahází všechna čísla do knihovny
        temp = line.split()
        if len(temp) == 3:
            temp =line.split()
            # print("zkouska: ", temp)
            # print(type_[i-1])
            start_ = int(temp[1])               
            end_ = int(temp[1])+int(temp[2])
            diff_ = int(temp[0])-int(temp[1])
            garten[type_[i-1]].append([start_, end_, diff_])

# print(garten)
i=0                     #resetování, ať nemusím dávat další proměnnou
final_seed = []
for s in seed:
    for level in type_:
        for item in garten[level]:
            if s in range(item[0], item[1]):
                s = s+item[2]
                break
        # print("kontrola: ", level, s)
    i +=1
    final_seed.append(s)


print("final: ", final_seed)
final_seed.sort()

print("Answer part1: ", final_seed[0])



