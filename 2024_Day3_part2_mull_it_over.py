import re

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day3_data.txt", "rt")]

answer2 = 0
flag = True

def control(res_): #kontrola jestli náhdou není ve stringu vložený výsledek
    tmp = res_[4:]
    test = re.findall(r'mul\([^\)]*\)',tmp)
    if len(test) == 1:
        return test[0]
    else:
        return "ok"

def controldigit(mod2):
    temp = mod2.split(",")
    if len(temp) == 2 and temp[0].isdigit() and temp[1].isdigit(): 
        x = int(temp[0])
        y = int(temp[1])
        return [x,y]
    else:
        return None

for line in data:
    #result = re.findall(r'mul\([^\)]*\)|do\(\)|don\'t\(\)',line) #vyhledám všechno začínající "mul(" a končící ")" uloží se do pole
    result = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)',line) #vyhledám všechno začínající "mul(" a končící ")" uloží se do pole
    for res_ in result:
        if res_ == "do()":
            flag = True
        elif res_ == "don\'t()":
            flag = False
        elif res_.startswith("mul") and flag == True:
            # print(res_)
            controlled = control(res_) #kontrola jestli náhdou není ve stringu vložený výsledek
            # print(controlled)
            if controlled != "ok": # pokud je ve stringu vložený výsledek nahradím ho
                res_=controlled
            # print(res_)
            # print(type(res_))
            mod1=res_[4:]           #vymažu "mul("
            mod2=mod1[:-1]          #vymažu ")"
            mod3 = controldigit(mod2)   #kontrola jestli string jsou opravudu čísla
            if mod3 != None:
                i = mod3[0]*mod3[1]
                answer2+=i


print("Answer2: ",answer2)



