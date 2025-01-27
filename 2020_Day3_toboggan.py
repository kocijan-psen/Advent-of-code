data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day3_data.txt", "rt")]
array = []
helping = []
i = 0
j = 0
k = 0
right = 0 
down = 0
count = 0

def slopes():
    global k, right, down
    
    if k == 0:
        right = 1
        down = 1
    elif k == 1:
        right = 3
        down = 1
    elif k == 2:
        right = 5
        down = 1
    elif k == 3:
        right = 7
        down = 1        
    elif k == 4:
        right = 1
        down = 2    

for line in data:
    for char in line:
        helping.append(char)
    array.append(helping)
    helping = []

for k in range(5):
    slopes()
    #print (right, down)
    while i != (len(array)-1):
        j +=right
        if j >= len(array[i]):
            j = j - int(len(array[i]))
        i +=down
        #print(i,j)

        if array[i][j] == "#":
            count +=1   
    
    helping.append(count)
    count = 0
    i = 0
    j = 0

#print(helping)
    
Answer = helping[0]*helping[1]*helping[2]*helping[3]*helping[4]

print("part1:",helping[1])
print("part2:", Answer)
        

