data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day1_data.txt", "rt")]
array = []
count = 0
twice = 0
flag = True

while flag:

    for line in data:

        twice += int(line)


        if twice in array:
            flag = False
            break

        else:
            array.append(twice)
        
print("first frequency:",twice)