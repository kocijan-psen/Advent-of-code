
data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day2_data.txt", "rt")]
#print(data)
Sum = 0

for line in data:
    list = line.split("\t")
    #print("pred:",list)
    list = sorted(list, key=int)
    #print("po:",list)

    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                if int(list[i]) % int(list[j]) == 0:
                    result = int(list[i])/int(list[j])
                    Sum += result

print("Výsledek:", Sum)

