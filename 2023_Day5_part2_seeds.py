data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day5_data.txt", "rt")]

seed = []
i = 0
garten = {"soil": [], "fertilizer":[],"water":[], "light" : [], "temperature" :[], "humidity" :[], "location" :[]}
type_ = ["soil", "fertilizer","water", "light", "temperature", "humidity", "location"]
seeds_part2 = []

#funguje ale extremně pomalé.... analyzovat zrychlení.... !!!

for line in data:
    if line == "":
        i +=1

    if i == 0:                  #prvni radek jsou semena
        temp = line.replace("seeds: ","")
        temp2 = temp.split()
        for x in range(0,len(temp2), 2):
                starting_ = int(temp2[x])
                count_= int(temp2[x+1])
                result = list(range(starting_, starting_ + count_))
                print("xxxx")
                for y in result:
                        # if y not in seeds_part2:
                        seeds_part2.append(y)
        print("seed")
                
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


print("garten")

final_seed = []
for s in seeds_part2:
    for level in type_:
        for item in garten[level]:
            if s in range(item[0], item[1]):
                s = s+item[2]
                break
        # print("kontrola: ", level, s)
    i +=1
    
    final_seed.append(s)
    # print("finalseed: ")

print ("asdfasdf")
# print("final: ", final_seed)
final_ = sorted(final_seed)

print("Answer part2: ", final_[0])



