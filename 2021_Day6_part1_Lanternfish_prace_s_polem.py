data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day6_data.txt", "rt")]

lanternfish = []

for line in data:
    for x in line:
        if x.isdigit():
            lanternfish.append(int(x))

# print(f"pred zacaktem {lanternfish}")
for i in range(80):
    for j in range(len(lanternfish)):
        lanternfish[j] -=1
        if lanternfish[j] == -1:
            lanternfish[j] = 6
            lanternfish.append(8)


    # print(f"cyklus {lanternfish}")

print(f"Odpověď část 1 je: {len(lanternfish)}")