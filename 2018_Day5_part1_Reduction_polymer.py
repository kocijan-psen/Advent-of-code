with open("C:/Users/kocij/Documents/Python/2018/2018_Day5_data.txt", "r") as file:
    data = file.read()

flag = True

def lower_upper(item1, item2):                 #kontrola jestli tam je jedna z kombinací a zároveě obě písmena jsou stejná
    if (item1.isupper() and item2.islower() or item1.islower() and item2.isupper()) and item1.lower() == item2.lower():
        return True
    
string_=data
while flag == True:                             #hlavní cyklus (flag jako kontrola jestli tam ještě nějaký prvek je)
    flag = False
    for i in range(len(string_)-1): 
        item1 = string_[i]
        item2 = string_[i+1]
        # if item1.isalpha() and item2.isalpha():
        control = lower_upper(item1,item2)
        if control == True:
            string_ = string_[:(i)]+string_[(i+2):]
            flag = True
            break

# print("newstring: ", string_)

Answer_part1 = len(string_)
print("answer part1: ", Answer_part1)