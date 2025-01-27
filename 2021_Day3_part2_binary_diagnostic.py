data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day3_data.txt", "rt")]
array = []

for line in data:
    array.append(line)

oxygen = array
i = 0
while len(oxygen)>1:
    #print ("lenght:", len(oxygen))
    #print("oxy1:", oxygen)
    zero = 0
    one = 0    
    for string in oxygen:
        if string[i][0] == '0':
            zero +=1 
        else:
            one +=1
    #print(f"zero:{zero}, one: {one}")
    #print("oxy2:", oxygen)
    if one >= zero:
        oxygen = [string for string in oxygen if string[i] == '1']
    else:
        oxygen = [string for string in oxygen if string[i] == '0']
    i +=1
#print("oxygen:", oxygen)

co2rate = array
i = 0
while len(co2rate)>1:
    zero = 0
    one = 0    
    for string in co2rate:
        if string[i][0] == '0':
            zero +=1 
        else:
            one +=1
    #print(f"zero:{zero}, one: {one}")
    #print("co22:", co2rate)
    if zero <= one:
        co2rate = [string for string in co2rate if string[i] == '0'] #list comprehension
    else:
        co2rate = [string for string in co2rate if string[i] == '1'] #list comprehension
    i +=1
#print("co2rate:", co2rate)

decimal_oxygen = int(oxygen[0],2)
decimal_co2rate = int(co2rate[0],2)
#print(f"oxy:{decimal_oxygen}, co2: {decimal_co2rate}")
Answer=decimal_co2rate*decimal_oxygen
print("answer:",Answer)
