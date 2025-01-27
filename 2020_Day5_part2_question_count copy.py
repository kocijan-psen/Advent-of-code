data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day5_data.txt", "rt")]

groups = []
temp = []
temp2 = []

def calculator(group,control_):
    answers = {}
    count = 0
    for undergroup in group:
        for char in undergroup:
            if char not in answers:
                answers[char]=1
            else:
                answers[char]+=1
    for i,j in answers.items():
        if j == control_:
            count +=1
    return count    

for line in data:       # hlavni kod
    if line == "":      # roztridim data
        groups.append(temp2)
        temp2 = []
    else:
        for char in line:
            temp.append(char)
        temp2.append(temp)
        temp = []
        
# print(groups)

answer2 = 0
for group in groups:            # kontroluju skupiny. Logika jestli je počet pismen rovný počtu polí, je to shodná odpověď
    control_ = len(group)
    # print("control: ",control_)
    count = calculator(group, control_)
    answer2 = answer2 + count

print("answer part2: ",answer2)


