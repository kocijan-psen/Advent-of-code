data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day2_data.txt", "rt")]
letters = {}
i = 0
j = 0
twice = 0
triple = 0

for line in data:

    for char in line:
        if char in letters:
            letters[char]+=1
        else:
            letters[char] = 1
    #print(letters)

    for char in letters:
        value = letters[char]
        if value == 2 and i == 0:
            twice +=1
            i +=1
        if value == 3 and j == 0:
            triple +=1
            j +=1
        if i == 1 and j == 1:
            i = 0
            j = 0
            break
    #print(twice, triple)
    letters = {}
    i = 0
    j = 0


Sum = twice * triple

print("Výsledek:", Sum)



