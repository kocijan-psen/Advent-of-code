startrange = 278384
endrange = 824795
cnt = 0 
cnt2 = 0

def samenumber(string_):
    for i in range(len(string_)-1):
        if string_[i] == string_[i+1]:
            return True
        
def neverdecreasenumber(string_):
    never_ = 0
    for i in range(len(string_)-1):
        if string_[i] <= string_[i+1]:
            never_+=1
    if never_ == 5:
        return True
    
def notapartofagroup(string_):
    for i in range(len(string_) - 1):
        if string_[i] == string_[i + 1]: #jsou 2 stejná?
            # Kontroluje, zda nejsou součástí větší skupiny, zkontroluuji co je před dvojcí a po dvojci
            if (i == 0 or string_[i - 1] != string_[i]) and (i + 2 >= len(string_) or string_[i + 2] != string_[i]):
                return True

        
for number in range(startrange, endrange+1):
    string_ = str(number)
    condition1 = samenumber(string_)
    if condition1 == True:
        condition2 = neverdecreasenumber(string_)
        if condition2 == True:
            cnt +=1
            condition3 = notapartofagroup(string_)
            if condition3 == True:
                cnt2 +=1
                # print(string_)
print("Answer part 1 = ", cnt)
print("Answer part 2 = ", cnt2)