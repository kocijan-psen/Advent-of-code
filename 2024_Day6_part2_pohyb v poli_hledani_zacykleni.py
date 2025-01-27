import numpy as np
import copy

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day6_data.txt", "rt")]

array = []

def findsymb(data):                                     #vyhledání začátku
    symbol = "^"
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if value == symbol:
                return [row_index, col_index]

def inarray(array, i, j):                               #kontrola, jestli je pozice v poli
    if 0 <= i < len(array) and 0 <= j < len(array[0]):
        return True
    else:
        return False
    
def offsetstype(dir_):                                  #směr pohybu
    offsets = [[-1,0],[0,1],[1,0],[0,-1]]
    return offsets[dir_]
    
def sumX(finalarray, target):                          #součet "X" z části 1
    array = np.array(finalarray)
    return np.sum(array == target)
    
def poscontrol(array, i, j, dir_, xnumb):              #kontrola jestli se proces zacyklil (originál z části 1)
    roundcontrol = 0
    while inarray(array, i, j) == True:
        offsets_ = offsetstype(dir_)
        offseti = offsets_[0]
        offsetj = offsets_[1]
        i +=offseti
        j +=offsetj

        if inarray(array,i,j) == False:
            return False
        if array[i][j] == '#':
            if dir_ == 0:
                i +=1
            elif dir_ == 1:
                j -=1
            elif dir_ == 2:
                i -= 1
            elif dir_ == 3:
                j +=1

            dir_ +=1
            if dir_ == 4:
                dir_ = 0
        elif array[i][j] == 'X':
            continue
        else:
            array[i][j] = 'X'
        roundcontrol +=1
        if roundcontrol == 3*xnumb:                     #kontrola (jestli projede vícekrát, je zacyklený)
            return True

for line in data: # vložení dat do tabulky
    temp = []
    for char in line:
        temp.append(char)
    array.append(temp)

arraybckup = copy.deepcopy(array) # záloha pro další použití

foundsymbpos = findsymb(array) #vyhledám začátek
i = foundsymbpos[0]
j = foundsymbpos[1]

dir_ = 0
offseti = 1
offsetj = 0

while inarray(array, i, j) == True: # první cyklus (projedu jako v části 1, abych definoval cestu)
    offsets_ = offsetstype(dir_)
    offseti = offsets_[0]
    offsetj = offsets_[1]
    i +=offseti
    j +=offsetj

    if inarray(array,i,j) == False:
        break
    if array[i][j] == '#':
        if dir_ == 0:
            i +=1
        elif dir_ == 1:
            j -=1
        elif dir_ == 2:
            i -= 1
        elif dir_ == 3:
            j +=1

        dir_ +=1
        if dir_ == 4:
            dir_ = 0
    else:
        array[i][j] = 'X'

coords_ = []                        #zjistím souřadnice "X"
for a in range(len(array)):
    for b in range(len(array[0])):
        if array[a][b] == "X":
            coords_.append([a,b])

xnumb = len(coords_)                   #pro kontrolu zacyklení.... 
answer2 = 0
for coord in coords_:
    array2 = copy.deepcopy(arraybckup)
    dir_ = 0
    offseti = 1
    offsetj = 0
    x = coord[0]
    y = coord[1]
    array2[x][y]= "#"

    if poscontrol(array2, foundsymbpos[0], foundsymbpos[1], dir_,xnumb) == True:
        answer2 += 1

print(f"Odpověď na část 2 je: {answer2}")
