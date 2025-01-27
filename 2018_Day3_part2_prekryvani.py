data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day3_data.txt", "rt")]
array = []
matrix = {}
tmpcount = 1
a = 0

for line in data:
    a +=1 

for line in data:

    split = line.split(" ")
    start = split[2].split(",")

    
    startline = int(start[0])                   #začátek řádku
    startcolum = int(start[1].replace(":",""))  #začátek sloupce

    lenght = split[3].split("x")

    endline = startline + int(lenght[0]) -1   #délka záznamu v řádcích
    #print("konecřádku:",endline)

    endcolum = startcolum + int(lenght[1]) -1  #délka záznamu ve sloupcích
    #print("konecsloupce:",endcolum)

    tmp = line.split("@")
    key = str(tmp[0].replace("#",""))  
    matrix[key]= startline, endline, startcolum, endcolum

for key1 in matrix.keys():
    tmpcount = 1
    a_start = matrix[key1][0]
    a_end = matrix[key1][1]
    b_start = matrix[key1][2]
    b_end = matrix[key1][3]
    
    for key2 in matrix.keys():
        c_start = matrix[key2][0]
        c_end = matrix[key2][1]
        d_start = matrix[key2][2]
        d_end = matrix[key2][3]
        
        

        if key1 != key2:
            if (a_end<c_start or c_end<a_start) or (b_end<d_start or d_end<b_start):
                    tmpcount +=1

        #print("key1:",key1)
        #print("key2:",key2)
        #print("pocet:",tmpcount)
        #print("a:", a)
        
        if tmpcount == a:
            print("Answer:",key1)
            break
        


