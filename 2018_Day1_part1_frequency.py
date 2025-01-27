data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day1_data.txt", "rt")]

freq = 0

for line in data:
    freq +=int(line)

print("Result:", freq)
        