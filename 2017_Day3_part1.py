i = 0
j = 0
Puzzle_input = 277678
array = []
turn = 0
k = 1
index = 0
steps = 1
a = 1



while a <=Puzzle_input:

    if a == 1:
        i = 0
        j = 0
        #print(a,i,j)
        a+=1
        
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
            #print(a,i,j)
            a+=1
            if a == Puzzle_input+1:
                break
            
    
        turn +=1

        if turn ==4:
            turn = 0

        index +=1
        if index >= 2:
            steps +=1
            index = 0
   
    
Sum = abs(i)+abs(j)

print(Sum)

