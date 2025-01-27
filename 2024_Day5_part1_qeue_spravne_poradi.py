import math

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day5_data.txt", "rt")]

rules_={}
lines_=[]
Answer = 0

def sortdata(data):
    x = True
    for line in data:
        if line == "":
            x = False
        elif x == True:
            temp = line.split("|")
            if  temp[0] not in rules_:
                rules_ [temp[0]]=[]
            
            rules_[temp[0]].append(temp[1])
        
        elif x == False:
            temp = line.split(",")
            if len(temp)>=1:
                lines_.append(temp)
    return lines_

edited = sortdata(data) #Rozdělení dat na podmínky a řady

for line_ in edited: # hlavní program, logika.... konrolované čílo nesmí být v žádné podmínce z předchozího
    cnttemp = 0
    for i in range(len(line_)):
        controlled = line_[i]
        # print("line", line_)
        while i >= 1:
            # print(f"'line': {line_[i]}, 'i': {i}, line_[i-1]: {line_[i-1]}")
            if i - 1 >= 0 and controlled in rules_:
                if line_[i-1] in rules_[controlled]:
                    # print("pravidla", rules_[line_[i - 1]])
                    break
            i -= 1 
            if i == 0:
                cnttemp +=1
    
    if cnttemp == len(line_)-1:

        numb_ = math.floor((len(line_))/2)
        # print(f"line1: {line_}")
        Answer +=int(line_[numb_])
        
print("Answer:", Answer)


