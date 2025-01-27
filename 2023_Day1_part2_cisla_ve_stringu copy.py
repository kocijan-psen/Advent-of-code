data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day1_part2_data.txt", "rt")]
find1 = "0123456789"
find2 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
Answer = 0
i = ""
helping = ""
flag = False

def whatwrite ():
    global i
    if number == "zero":
        i = "0"
    elif number == "one":
        i = "1"
    elif number == "two":
        i = "2"
    elif number == "three":
        i = "3"
    elif number == "four":
        i = "4"
    elif number == "five":
        i = "5"
    elif number == "six":
        i = "6"
    elif number == "seven":
        i = "7"
    elif number == "eight":
        i = "8"
    elif number == "nine":
        i = "9"
    return i

for string in data:
    helping = ""
    i = ""
    j = ""

    for char in string:
        if flag == True:
            break

        if char in find1:
            i = char
            flag = True
            break
        else:
            helping = helping + char
            for number in find2:
                if number in helping:
                    whatwrite()
                    flag = True
                    break
    j = i
    flag = False
    
    
    revstring = ''.join(reversed(string))
    helping = ""

    for char in revstring:
        if flag == True:
            break
    
        if char in find1:
            i = char
            break
        else:
            helping = helping + char
            helping2 = helping[::-1]
            for number in find2:
                if number in helping2:
                    whatwrite()
                    flag = True
                    break
    
    j = j + i
    print(j)

    flag = False
    k = int(j)
    Answer = Answer + k
print ("odpoved", Answer)




   

    
