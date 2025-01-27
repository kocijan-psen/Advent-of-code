data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day3_data.txt", "rt")]
number = ["0","1","2","3","4","5","6","7","8","9"]
array =[]
tmp = ""
temp = []
flag = False
gearratio = []

for line in data:
    sub = []
    for item in line:
        sub.append(item)
    array.append(sub)

print(array)
rows = len(array)
cols = len(array[0])
# print(rows)
# print(cols)

for i in range(rows):
    for j in range(cols):
        # kontrola = array[i][j]
        if array[i][j] in number:
            tmp = tmp + array[i][j]
            # print(array[i][j])
            for k in [-1,0,1]: #kontrola všech prvků kolem
                for l in [-1,0,1]:
                    if k == 0 and l == 0: #když se rovnají nule, je to konrtolované číslo
                        continue
                    if 0 <= i + k < rows and 0 <= j + l < cols: #kontrola jestli jsem v poli
                        pokus = array[i+k][j+l]
                        if pokus not in number and pokus !=".": #když to není číslo nebo tečka je to special znak.
                            flag = True
                            
        if flag == False and (j+1 >= cols or array[i][j+1] not in number):
             tmp = "" 


        if flag == True and (j+1 >= cols or array[i][j+1] not in number):
                    temp.append(tmp) 
                    tmp = "" 
                    flag = False 
# print(temp)
sum = 0    
for no in temp:
     sum = sum + int(no)

print("vysledek:", sum)





