data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day3_data.txt", "rt")]
array = []
matrix = {}
tmpcount = 0



array = [[0 for x in range(10)] for y in range(10)]

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

    array = [[0 for x in range(10)] for y in range(10)]

    for i in range(startcolum, endcolum):
        for j in range (startline, endline):
            array[i][j] +=1


    tmp = line.split("@")
    key = str(tmp[0].replace("#",""))
    matrix[key]= array
    #print(matrix)
    array = []

    for name1 in matrix.keys():
        for name2 in matrix.keys():
            mat1 = matrix[name1]
            mat2 = matrix[name2]

            tmpcount = 0

            if mat1 != mat2:
                for i in range(len(mat1)):
                    for j in range(len(mat1[0])):
                        if mat1[i][j] + mat2[i][j] <=1:
                            tmpcount +=1
        
                    if tmpcount == 0:
                        print(name2)
                     
        