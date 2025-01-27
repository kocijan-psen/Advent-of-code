data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day3_data.txt", "rt")]
array = []
countpart1 = 0
countpart2 = 0


array = [[0 for x in range(1000)] for y in range(1000)]

for line in data:
    #print(line)
    split = line.split(" ")
    start = split[2].split(",")

    
    startline = int(start[0])                   #začátek řádku
    startcolum = int(start[1].replace(":",""))  #začátek sloupce
    #print("startradek:",startline)
    #print("startsloupec:",startcolum)


    lenght = split[3].split("x")
    #print(lenght)

    endline = startline + int(lenght[0])    #délka záznamu v řádcích
    #print("konecřádku:",endline)

    endcolum = startcolum + int(lenght[1])  #délka záznamu ve sloupcích
    #print("konecsloupce:",endcolum)

    for i in range(startcolum, endcolum):
        for j in range (startline, endline):
            array[i][j] +=1

    #for row in array:
    #    print(row)

for i in range(len(array)):
    for j in range(len(array)):
        if array[i][j] >=2:
            countpart1 +=1

print("Vysledek část 1:",countpart1)