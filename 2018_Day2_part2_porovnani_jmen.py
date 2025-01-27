data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day2_data.txt", "rt")]
checked = []
Winner = {'difference':100,'first':"text",'second':"text"}
index = 0
diff = 0
Answer = ""


for i in data:
    for j in data:
        diff = 0
        if i != j:
            presence = any(i in pair and j in pair for pair in checked)
            if not presence:
                checked.append([])
                checked[index].append(i)
                checked[index].append(j)
                index +=1
                for char1, char2 in zip(i, j):
                    if char1 != char2:
                        diff +=1
                if Winner["difference"] > diff:
                    Winner["difference"] = diff
                    Winner["first"]=i
                    Winner["second"] = j
#print(checked)

print(Winner)
for symb1, symb2 in zip(Winner["first"],Winner["second"]):
    if symb1 == symb2:
        Answer = Answer + symb1

print("Výsledek:",Answer)

                

        


