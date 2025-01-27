data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day6_data.txt", "rt")]

memory = []
origmemory = []
counter = 0
flag = False


temp1=data[0].split()

for i in range(len(temp1)):         #jen kvůli převedení na int
    memory.append(int(temp1[i]))


while True:

    index, highest_value = max(enumerate(memory), key=lambda x: x[1])
    memory[index] = 0

    for _ in range(highest_value):
        index +=1
        if index == len(memory):
            index = 0
        memory[index]+=1
    
    counter +=1

    if memory in origmemory:
        # Zde detekujeme opakování a zahájíme výpočet velikosti smyčky
        first_occurrence = origmemory.index(memory)  # Najdi první výskyt
        loop_size = counter - first_occurrence       # Velikost smyčky
        break

    # Ulož aktuální stav
    origmemory.append(memory.copy())

# Výstup
print("Velikost smyčky:", loop_size)