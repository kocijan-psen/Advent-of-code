data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day8_cast1_data.txt", "rt")]

array = []
cnt = []

def alldirections (array, i, j):
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    rows = len(array)
    cols = len(array[0])
    for k in range(1, i + 1): # kontrola dolu, limit v range aby i-k bylo max 0
        score1 += 1 
        if array[i - k][j] >= array[i][j]:
            break

    for k in range(1, rows - i): #kontrola nahoru, limit nepotřebuju celé řádky stačí od kontrolovaného prvku
        score2 +=1
        if array[i + k][j] >= array[i][j]:
            break

    for k in range(1, j + 1):  #kontrola doleva, limit v range aby j-k bylo max 0
        score3 +=1
        if array[i][j - k] >= array[i][j]:
            break


    for k in range(1, cols - j):  # kontrola doprava, limit nepotřebuju celé řádky stačí od kontrolovaného prvku
        score4 +=1
        if array[i][j + k] >= array[i][j]:
            break
    
    # print(score1, score2, score3, score4)
    return score1*score2*score3*score4

for i in range(len(data)): #naházení do pole
    array.append([])
    for j in data[i]:
        array[i].append(int(j)) 

for i in range(1,len(array)-1): #hlavní program, nekontroluju okraje, zbytečný byla by to nula a i to tam psali
    for j in range(1,len(array[i])-1):
        controlled = array[i][j]
        # print("number: ", controlled)
        scenic_score = alldirections(array, i, j)
        cnt.append(scenic_score)



cnt.sort()
cnt.reverse()
print("answer part 2 is: ", cnt[0])