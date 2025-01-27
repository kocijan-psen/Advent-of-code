data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day6_data.txt", "rt")]

memory = []
origmemory = []
counter = 1

temp1=data[0].split()
temp2 = []

for i in range(len(temp1)):         #jen kvůli převedení na int
    memory.append(int(temp1[i]))
    temp2.append(int(temp1[i]))
origmemory.append(temp2)

counter2 = 0
while True:

    index, highest_value = max(enumerate(memory), key=lambda x: x[1])
    memory[index] = 0

    for _ in range(highest_value):
        index +=1
        if index == len(memory):
            index = 0
        memory[index]+=1


    if memory in origmemory:
        print("tadá")
        break
    else:
        origmemory.append(memory.copy())
        counter+=1


print("part1", counter)
