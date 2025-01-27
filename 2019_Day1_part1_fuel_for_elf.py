import math

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day1_data.txt", "rt")]
Answer = 0

for line in data:
    
    number = (math.floor((int(line))/3))-2

    Answer = Answer + number
print ("Answer:", Answer)

