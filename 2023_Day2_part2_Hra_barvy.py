data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day2_part1_data.txt", "rt")]
Sred= 12
Sgreen= 13
Sblue= 14
sum = 0

for radek in data:

    Game = {'red':[], 'green':[], 'blue':[]}
    array = []

    array=radek.split(':')

    Sets = array[1].split(';')
    #print(Sets)
    
    for i in range(len(Sets)):
        #print(Sets)
        move = Sets[i].split(',')
        #print (move)
        for j in range(len(move)):
            detail = move[j].split(' ')
            if detail[2] == 'red':
                Game['red'].extend([detail[1]])
            elif detail[2] == 'green':
                Game['green'].extend([detail[1]])
            elif detail[2] == 'blue':
                Game['blue'].extend([detail[1]])
    
    for key in Game:
        Game[key] = sorted(Game[key], key=int, reverse=True)
    for key in Game:
        first_value = Game[key][0] if Game[key] else None


    red_first = int(Game['red'][0] if Game['red'] else None)
    green_first = int(Game['green'][0] if Game['green'] else None)  
    blue_first = int(Game['blue'][0] if Game['blue'] else None)

    sum = sum + (red_first*green_first*blue_first)

print("výsledek:",sum)


            


   


     
           
            
