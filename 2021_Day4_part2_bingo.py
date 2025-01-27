data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day4_data.txt", "rt")]

numbers_ = [1,76,38,96,62,41,27,33,4,2,94,15,89,25,66,14,30,0,71,21,48,44,87,73,60,50,77,45,29,18,5,99,65,16,93,95,37,3,52,32,46,80,98,63,92,24,35,55,12,81,51,17,70,78,61,91,54,8,72,40,74,68,75,67,39,64,10,53,9,31,6,7,47,42,90,20,19,36,22,43,58,28,79,86,57,49,83,84,97,11,85,26,69,23,59,82,88,34,56,13]
array = []
ticket = []
tickno = []

def countunmarked(tick):
    cnt = 0
    for i in tick:
        for j in i:
            if isinstance(j,int): 
                # print("cislo ve stringu:", j)
                cnt = cnt + j
    return cnt

def control(tick):
    for row in tick: #kontrola řádky
        if all(isinstance(item, str) for item in row):
            return tick  
    for col in range(len(tick[0])): #kontrola sloupce
        if all(isinstance(row[col], str) for row in tick):
            return tick

def marked(array, no_):
    global tickno
    result = []

    for a, tick in enumerate(array):
        for lin in tick:
            for i, char in enumerate(lin):
                if char == no_:
                    lin[i] =  str(char)
                    try_ = control(tick)
                    if try_ != None and a not in tickno:
                        sumof = countunmarked(tick)
                        tickno.append(a)
                        # print(sumof, no_)
                        result.append(sumof*no_)
                        continue
    return result[-1] if result else None


for line in data: #vytvoření polí s ticketama
    if line == "":
        array.append(ticket)
        ticket = []
    else:
        temp = [int(cislo) for cislo in line.split()]
        ticket.append(temp)

isbingo = []
for no_ in numbers_: # hlavní program
    bingo = marked(array, no_)

    if isinstance(bingo, int):
        isbingo.append(bingo)

print("Answer part2: ", isbingo[-1])


