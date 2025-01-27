data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day1_data.txt", "rt")]

array = []
count = 0
j = 0

for line in data:
    array.append(int(line))

for i in range(len(array)-1):

    if array[j+1] > array[j]:
        #print(array[i+1],array[i])
        count +=1
    j+=1

print(count)