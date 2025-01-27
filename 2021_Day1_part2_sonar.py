data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/Day1_data.txt", "rt")]

array = []
arraymod = []
count = 0
j = 0
k=0

for line in data:
    array.append(int(line))

for i in range(0,len(array)-2):
    
    j = array[k]+array[k+1]+array[k+2]
    #arraymod.append(j)
    k+=1


print(arraymod)
j = 0
for i in range(len(arraymod)-1):

    if arraymod[j+1] > arraymod[j]:
        count +=1
    #print(arraymod[j],arraymod[j+1])
    j+=1
    


print(count)