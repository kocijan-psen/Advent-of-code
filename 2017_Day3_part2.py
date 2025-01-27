i = 500
j = 500
Puzzle_input = 277678
array = [[]]
turn = 0
k = 1
index = 0
steps = 1
a = 1
tmp = 0

def aroundcontrol (array, i, j):
    cnt = 0
    directions =[(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        x, y = i + direction[0], j+direction[1] #projíždím okolí
        cnt = cnt + array[x][y]
    return cnt


array = [[0 for x in range(1000)] for y in range(1000)]

while a <= Puzzle_input:

    if a == 1 and tmp ==0 : #jen pro začátek
        array[i][j]=a
        tmp+=1
    else:
        for step in range(steps):

            if turn == 0:
                j +=1
            elif turn == 1:
                i -=1
            elif turn == 2:
                j-=1
            else:
                i+=1
            
            a = aroundcontrol(array, i, j)
            array[i][j]=a


            if a > Puzzle_input:
                print("Answer: ",a)
                break
        turn +=1
        if turn ==4:
            turn = 0
        index +=1
        if index >= 2:
            steps +=1
            index = 0
   


