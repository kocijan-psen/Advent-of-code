data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/Day2_part1_data.txt", "rt")]
Sred= 12
Sgreen= 13
Sblue= 14
sum = 0
Game = {'GameNumber':0, "red":0, "green":0, "blue":0, "repeat":0}


for radek in data:
    
    array = []
    Game['red'] = 0
    Game['green'] = 0
    Game['blue'] = 0
    Game['repeat'] = 0
    Game['GameNumber'] = 0   

    array=radek.split(':')
    GameNo = array[0].split(' ')
    Game ['GameNumber']+= int(GameNo[1])


    Sets = array[1].split(';')
    #print(Sets)
    
    for i in range(len(Sets)):
        move = Sets[i].split(',')
        #print (move)
        for j in range(len(move)):
            detail = move[j].split(' ')
            #print(detail)
            if detail[2] == "red":
                Game ['red']+= int(detail[1])
            elif detail[2] == "green":
                Game ['green']+= int(detail[1])
            elif detail[2] == "blue":
                Game ['blue']+= int(detail[1])

        if Game ['red'] <= Sred and Game ['green'] <= Sgreen and Game ['blue'] <= Sblue:
            Game['repeat'] +=1 
            Game['red'] = 0
            Game['green'] = 0
            Game['blue'] =0
            if Game['repeat'] == len(Sets):
                sum+=Game['GameNumber']
                Game['GameNumber']=0
                Game['repeat'] = 0
          
        

print(sum)
            


   


     
           
            
