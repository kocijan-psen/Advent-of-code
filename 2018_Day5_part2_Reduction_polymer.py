with open("C:/Users/kocij/Documents/Python/2018/2018_Day5_data.txt", "r") as file:
    data = file.read()
flag = True
j = 97
lenpolymers = []

def lower_upper(item1, item2):              #kontrola zda je tam požadovaný prvkek
    if (item1.isupper() and item2.islower() or item1.islower() and item2.isupper()) and item1.lower() == item2.lower():
        return True
    
def part1(dataorig,flag):                   #řešení z části 1, vymaže požadované prvky např. "aA" a "Aa"

    string_=dataorig
    while flag == True:
        flag = False
        for i in range(len(string_)-1): 
            item1 = string_[i]
            item2 = string_[i+1]
            control = lower_upper(item1,item2)
            if control == True:
                string_ = string_[:(i)]+string_[(i+2):]
                flag = True
                break
    return len(string_)


for i in range(65,91):                          #hlavní cyklus
    dataorig = data                             #výmaz malých i velkých písmen
    tmp1 = chr(i)
    if tmp1 in dataorig:
        dataorig = dataorig.replace(tmp1,"")
    tmp2 = chr(j)
    if tmp2 in dataorig:
        dataorig = dataorig.replace(tmp2,"")
    j+=1

    lenpoly = part1(dataorig, flag)
    lenpolymers.append(lenpoly)

lenpolymers = sorted(lenpolymers)               #setřízení (hledám nejmenší)
print("Answer part2: ", lenpolymers[0])
