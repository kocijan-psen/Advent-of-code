data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day3_data.txt", "rt")]
array =[]
gearratio = 0
# flag = False
""""
Výsledek: 82301120
"""

def findnumber(array, x, y): # čte řádek zprava do leva, aby se dostal na začátek, pak přečte číslo zleva do prava a celé uloží. 
    tmp=""                   
    cols = len(array[0])
    while y >= 0 and array[x][y].isdigit() :
        y-=1
    y+=1
    while y < cols and array[x][y].isdigit():
        tmp = tmp+array[x][y]
        array[x][y] = "."   #číslo je nahrazeno tečkami aby se nedublovalo
        y+=1
    return tmp
 

def arenumbersthere(array, i, j):           #zkontroluje okolí a když nalezne znak  uloží pomocí fce číslo, pokud na konci jsou 2 čísla pošle jejich násobek
    """
    zkontroluje okolí hvezdy a zjistí kolik je tam čísel
    """
    temp = []
    rows = len(array)
    cols = len(array[0])
    directions =[(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        x, y = i + direction[0], j+direction[1] #projíždím okolí
        if 0 <= x < rows and 0 <= y < cols: #kontrola, že jsem indexy stále v poli
            control_ = array[x][y]
            if  control_.isdigit():
                number_=findnumber(array, x, y)
                temp.append(number_)

    print("nalezena cisla: ", temp)
    if len(temp) == 2:
        print("poslana cisla: ", temp)
        return int(temp[0])*int(temp[1])
    else:
        return "Nothing"
    


for line in data: #transfer string -> pole
    sub = []
    for item in line:
        sub.append(item)
    array.append(sub)

rows = len(array)
cols = len(array[0])

for i in range(rows):                   # hlavní cyklus
    for j in range(cols):
        # kontrola = array[i][j]
        if array[i][j] == "*":
            # print("position", i,j)
            gear = arenumbersthere(array, i, j)
            if gear == "Nothing":
                continue
            gearratio=gearratio+int(gear)

print("Answer: ", gearratio)


