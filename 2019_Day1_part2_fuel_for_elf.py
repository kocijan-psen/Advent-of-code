import math

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day1_data.txt", "rt")]
Answer = 0
tmp = 0
number = 0

for line in data:
    number = int(line)

    while number >0 :
        number = (math.floor((int(number))/3))-2
        #print(number)
        if number < 0:
            break
        tmp +=number

print(tmp)
        
            
       
        

        


        

    