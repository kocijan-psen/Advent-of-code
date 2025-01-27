data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day4_data.txt", "rt")]

multiple = 0
answer = 0

for line in data:
    temp = line.split("|")
    temp1 = temp[0].split(":")
    win_numb = temp1[1].split()
    # print(win_numb)
    ticket = temp[1].split()
    # print(ticket)
    for number in win_numb:
        if number in ticket:
            if multiple == 0:
                multiple = 1
            else:
                multiple = multiple + multiple
    if multiple != 0:
        answer  = answer + multiple
    multiple = 0


print("answer: ", answer)
            


    



