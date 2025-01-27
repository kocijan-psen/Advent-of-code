data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day4_data.txt", "rt")]

numbers_ = [1,76,38,96,62,41,27,33,4,2,94,15,89,25,66,14,30,0,71,21,48,44,87,73,60,50,77,45,29,18,5,99,65,16,93,95,37,3,52,32,46,80,98,63,92,24,35,55,12,81,51,17,70,78,61,91,54,8,72,40,74,68,75,67,39,64,10,53,9,31,6,7,47,42,90,20,19,36,22,43,58,28,79,86,57,49,83,84,97,11,85,26,69,23,59,82,88,34,56,13]

array = []
ticket = []

def countunmarked(tick):
    cnt = 0
    for i in tick:
        for j in i:
            if isinstance(j,int): 
                # print("cislo ve stringu:", j)
                cnt = cnt + j
    return cnt

def control(tick):
    i = 0
    j = 0
    
    for j in range(len(tick)):
        if all(isinstance(item, str) for item in tick[i]):
            return tick
        if all(isinstance(row[j], str) for row in tick):
            return tick

def marked(array, no_):
    for tick in array:
        for lin in tick:
            for i, char in enumerate(lin):
                if char == no_:
                    lin[i] =  str(char)
                    pokus = control(tick)
                    if pokus != None:
                        sumof = countunmarked(tick)
                        print(sumof, no_)
                        return sumof*no_


for line in data: #vytvoření polí s ticketama
    if line == "":
        array.append(ticket)
        ticket = []
    else:
        temp = [int(cislo) for cislo in line.split()]
        ticket.append(temp)


for no_ in numbers_: # hlavní program
    bingo = marked(array, no_)
    if isinstance(bingo, int):
        print("bingo:", bingo)
        break
    else:
        continue

