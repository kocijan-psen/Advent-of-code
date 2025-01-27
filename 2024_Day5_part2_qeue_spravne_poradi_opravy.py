import math

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day5_data.txt", "rt")]

rules_={}
lines_=[]
Answer2 = 0
wrong = []

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

def findwrong(line_,rules_):
    for i in range(len(line_)):
        controlled = line_[i]
        while i >= 1:
            if i - 1 >= 0 and controlled in rules_:
                if line_[i-1] in rules_[controlled]:
                    return False
            i-=1
    return True

def modify(line_):                  #logika, pokud je kontrolovaný prvek v pravidlech, prohodí se čísla mezi sebou
    for i in range(len(line_)):
        controlled = line_[i]
        j = i
        while j >= 1:
            if j - 1 >= 0 and controlled in rules_:
                if line_[j-1] in rules_[controlled]:
                    tmp = line_[j-1]                    #dočasné úložiště
                    line_[j-1] = controlled             #přepíšu pozici "j-1"
                    line_[i] = tmp                      #přepíšu pozici "i", musí tam být i, jelikož se odkazuji na původní pozici... "j" je pomocná
                    # print(line_)
                    return line_
            j-=1

edited = sortdata(data) #Rozdělení dat na podmínky a řady

for line_ in edited: # vyhledání špatných řádků
    found_ = True
    found_ = findwrong(line_,rules_)
    if found_ == False:
        wrong.append(line_)

x = False
for line_ in wrong: 
    while x == False:
        mod_= modify(line_)
        x = findwrong(mod_,rules_)
        if x == True:
            numb_ = math.floor((len(line_))/2)
            # print(f"line1: {line_}")
            Answer2 +=int(line_[numb_])
            x = False
            break

print(f"Odpověď část 2 je: {Answer2}")



