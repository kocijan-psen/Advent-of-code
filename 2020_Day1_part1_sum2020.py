import math

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day1_data.txt", "rt")]

array = []
flag = False


for line in data:
    array.append(int(line))
    

for i in range(len(array)):
    if flag == True:
        break
    for j in range(len(array)-1):
        #print("i:",array[i])
        #print("j:",array[j])
        if i != j:
            if array[i] + array[j] == 2020:
                Answer = array[i]*array[j]
                Flag = True
                break

print("Výsledek:", Answer)
