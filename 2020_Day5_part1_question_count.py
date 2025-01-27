data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day5_data.txt", "rt")]

groups = []
temp = []

for line in data:
    if line == "":
        groups.append(temp)
        temp = []
    else:
        for char in line:
            temp.append(char)
# print(groups)

count = 0
for group in groups:
    unique = set()
    for i in group:
        unique.add(i)
    # print(unique)
    count = count + len(unique)

print("answer part1: ",count)

#part2
