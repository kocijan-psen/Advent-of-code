data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day1_part2_data.txt", "rt")]
find1 = "0123456789"
find2 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
#findnumber = ["zero",'0', "one",'1', "two",'2', "three",'3', "four",'4', "five",'5', "six",'6', "seven",'7', "eight", '8',"nine",'9']
Answer = 0
i = ""
helping = ""
flag = False
file = open("C:/Users/kocij/Documents/Python/2023/Day1_part2_dkdkdk.txt", "a")

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
                    print(helping)
                    if number == "zero":
                        i = "0"
                        helping = ""
                        flag = True
                        break
                    elif number == "one":
                        i = "1"
                        helping = ""
                        flag = True
                        break
                    elif number == "two":
                        i = "2"
                        helping = ""
                        flag = True
                        break
                    elif number == "three":
                        i = "3"
                        helping = ""
                        flag = True
                        break
                    elif number == "four":
                        i = "4"
                        helping = ""
                        flag = True
                        break
                    elif number == "five":
                        i = "5"
                        helping = ""
                        flag = True
                        break
                    elif number == "six":
                        i = "6"
                        helping = ""
                        flag = True
                        break
                    elif number == "seven":
                        i = "7"
                        helping = ""
                        flag = True
                        break
                    elif number == "eight":
                        i = "8"
                        helping = ""
                        flag = True
                        break
                    elif number == "nine":
                        i = "9"
                        helping = ""
                        flag = True
                        break
    flag = False
    
    
    revstring = ''.join(reversed(string))
    helping = ""

    for char in revstring:
        if flag == True:
            break
    
        if char in find1:
            j = char
            break
        else:
            helping = helping + char
            helping2 = helping[::-1]
            for number in find2:
                if number in helping2:
                    
                    if number == "zero":
                        j = "0"
                        helping = ""
                        flag = True
                        break
                    elif number == "one":
                        j = "1"
                        helping = ""
                        flag = True
                        break
                    elif number == "two":
                        j = "2"
                        helping = ""
                        flag = True
                        break
                    elif number == "three":
                        j = "3"
                        helping = ""
                        flag = True
                        break
                    elif number == "four":
                        j = "4"
                        helping = ""
                        flag = True
                        break
                    elif number == "five":
                        j = "5"
                        helping = ""
                        flag = True
                        break
                    elif number == "six":
                        j = "6"
                        helping = ""
                        flag = True
                        break
                    elif number == "seven":
                        i = "7"
                        helping = ""
                        flag = True
                        break
                    elif number == "eight":
                        j = "8"
                        helping = ""
                        flag = True
                        break
                    elif number == "nine":
                        j = "9"
                        helping = ""
                        flag = True
                        break
    
    k = i + j
    file.write(k+"\n")

    flag = False
    l = int(k)
    Answer = Answer + l
print ("odpoved", Answer)
file.close()



   

    
