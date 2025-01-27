data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day2_data.txt", "rt")]
Answerpart1 = 0



for line in data:
    tmp = 0
    array = line.split(" ")
    limit = array[0].split("-")
    controled = array[1].replace(":","")

    for i in array[2]:
        if i == controled:
            tmp +=1
    #print(line, int(limit[0]),tmp,int(limit[1]))
    if int(limit[0]) <= tmp <= int(limit[1]):
        #print(line, int(limit[0]),tmp,int(limit[1]))
        Answerpart1 +=1

print("Výsledek část 1:", Answerpart1)

 