data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day2_data.txt", "rt")]

Answerpart2 = 0


for line in data:

    array = line.split(" ")
    limit = array[0].split("-")
    controled = array[1].replace(":","")
    
    j = array[2] #den 2 část 2
    #print (line, j[int(limit[0])-1], j[int(limit[1])-1])


    if (j[int(limit[0])-1] == controled or j[int(limit[1])-1] == controled) and not (j[int(limit[0])-1] == controled and j[int(limit[1])-1] == controled):
        #logika podmínky musí se rovnat jen jedna z pozic, ne obě zároveň
        #print (line, j[int(limit[0])-1], j[int(limit[1])-1])
        Answerpart2 +=1
        
        


print("Výsledek část 2:", Answerpart2)
 