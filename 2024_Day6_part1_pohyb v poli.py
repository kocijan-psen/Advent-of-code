import numpy as np

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day6_data.txt", "rt")]

array = []

def findsymb(data):
    symbol = "^"
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if value == symbol:
                return [row_index, col_index]

def inarray(array, i, j):
    if 0 <= i < len(array) and 0 <= j < len(array[0]):
        return True
    else:
        return False
    
def offsetstype(dir_):
    if dir_ == 0:
        return [-1,0]
    elif dir_ == 1:
        return [0,1]
    elif dir_ == 2:
        return [1,0]
    elif dir_ == 3:
        return [0,-1]
    
def sumX(finalarray, target):
    array = np.array(finalarray)
    return np.sum(array == target)
    
    pass

for line in data: # vložení dat do tabulky
    temp = []
    for char in line:
        temp.append(char)
    array.append(temp)

foundsymbpos = findsymb(array)
# print(foundsymbpos)

i = foundsymbpos[0]
j = foundsymbpos[1]

# print(array[i][j])
dir_ = 0
offseti = 1
offsetj = 0

array[i][j] = 'X'
while inarray(array, i, j) == True:
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
    
    # print(i,j)
    # for hovno in array:
    #     print(hovno)
    # print("\n")

Answer1 = sumX(array, 'X')
print(f"Odpověď na část je: {Answer1}")

    
    
