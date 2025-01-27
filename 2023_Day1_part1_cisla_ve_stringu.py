data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day1_part1_data.txt", "rt")]
Numbers = "0123456789"
Answer = 0
i = 0


for string in data:

    for char in string:
        if char in Numbers:
            i = char
            break

    string = string [::-1]

    for char in string:

        if char in Numbers:
            i = i+char
            break
    i = int(i)
    Answer = Answer + i


print ("Odpověď je:", Answer)





