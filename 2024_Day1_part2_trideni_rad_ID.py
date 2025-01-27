data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day1_data.txt", "rt")]

left_ = []
right_ = []
similarity = 0


for line in data:
    temp = line.split()
    left_.append(int(temp[0]))
    right_.append(int(temp[1]))

left_.sort()
right_.sort()

for i in left_:         #hledám všechny výskyty v celé druhé řádě.... 
    cnt = 0
    for j in right_:
        if i == j:
            cnt +=1
    score = i*cnt       #vynásobím výskyt číslem
    similarity += score #přičtu
        

print("Answer part2: ", similarity)


