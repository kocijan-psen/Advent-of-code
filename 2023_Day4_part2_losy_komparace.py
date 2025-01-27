data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day4_data.txt", "rt")]

match = 0
answer2 = 0
card = 1
qty = 1
ticket_mod = []

for line in data:
    temp = line.split("|")                  #zpracování dat
    temp1 = temp[0].split(":")
    win_numb = temp1[1].split()
    ticket = temp[1].split()

    for number in win_numb:                 #spočítám shody
        if number in ticket:
            match +=1
    ticket_mod.append([card, match, qty])   #uložím číslo karty, počet shod a množství karet (to je v tuto chvíli default = 1)
    match = 0


for i in range(len(ticket_mod)):#logika (když jsou shody, ke každé další přičti požadované množství a nezapomenout množství z navýšených předchozích tiketů)
    if ticket_mod[i][1] >= 0:                                                                                 
        for j in range(1,ticket_mod[i][1]+1):
            ticket_mod[i+j][2]+=ticket_mod[i][2]

for list_ in ticket_mod:
    answer2 = answer2 + list_[2]

print("Answer part2: ", answer2)

            


    



