data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day3_data.txt", "rt")]
Answer = 0
array = []
gamma = ""
epsilon = ""

for line in data:
 array.append(line)

sorting = [[char for char in group] for group in zip(*array) ] #metoda comprehension list

#print(sorting)

for list in sorting:
    if list.count('0') > list.count('1'): #logika: pokud je víc "0" přidám "0" do gamma. Zbytek je epsilon
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

#print("gamma:", gamma)
#print("epsilon:", epsilon))

decimal_gamma = int(gamma,2)
decimal_epsilon = int(epsilon,2)
#print("dec_gamma:", decimal_gamma)
#print("dec_epsilon:", decimal_epsilon)#

Answer = decimal_gamma*decimal_epsilon
print("answer:",Answer)