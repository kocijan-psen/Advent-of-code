data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day2_data.txt", "rt")]
Answer = 0
i = 0
j = 0

for line in data:
    tmp = 0
    array = line.split(" ")
    if array[0] == "forward":
        i += int(array[1])
    elif array[0] == "up":
        j += int(array[1])
    elif array[0] == "down":
        j -= int(array[1])
    else:
        print("Něco je špatně v:", line)

if i < 0:
    i = i * (-1)
if j < 0:
    j = j * (-1)

Answer = i*j
print("výsledek je:", Answer)

 