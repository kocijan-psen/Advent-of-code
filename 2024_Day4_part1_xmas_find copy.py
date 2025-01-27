data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day4_data.txt", "rt")]

array = []

def findxmas(array,i, j):
    dir_ = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    rows = len(array)
    cols = len(array[0])
    numb = 0
    for dr, dc in dir_:
        new_row = i + dr
        new_col = j + dc
        # hledám "M"
        if 0 <= new_row < rows and 0 <= new_col < cols and array[new_row][new_col] == "M":
            # print(array[new_row][new_col])
            new_row += dr
            new_col += dc
            # seru na točení, pokud je tam M jedu směrem jestli tam je "A"
            if 0 <= new_row < rows and 0 <= new_col < cols and array[new_row][new_col] == "A":
                # print(array[new_row][new_col])
                new_row += dr
                new_col += dc
                # # pokud je tam "A" jedu směrem jestli tam je "S"
                if 0 <= new_row < rows and 0 <= new_col < cols and array[new_row][new_col] == "S":
                    # print(array[new_row][new_col])
                    numb+=1
                    
    return numb 

for line in data: #naplnění pole
        temp = list(line)
        array.append(temp)


rows = len(array)
cols = len(array[0])

cnt = 0
for i in range(rows):
    for j in range(cols):
        if array[i][j] == "X":
            tmp=findxmas(array,i,j)
            cnt+=tmp
print("Answer part 1: ", cnt)


            