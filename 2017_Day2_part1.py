
data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day2_data.txt", "rt")]
#print(data)
Sum = 0

for line in data:
    list = line.split("\t")
    #print("pred:",list)
    list = sorted(list, key=int)
    #print("po:",list)
    Diff = int(list[-1])-int(list[0])
    Sum+=Diff

print("Výsledek:", Sum)

