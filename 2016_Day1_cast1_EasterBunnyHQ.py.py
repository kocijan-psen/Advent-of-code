data = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"


i = 0
Sever = 0
Zapad = 0
Jih = 0
Vychod = 0
x = 0
y = 0


Smer = data.split(", ")
while i <= len(Smer)-1:
    
    if x == 0 and y == 0:
        if 'L' in Smer[i]:
            Zapad = 1
            f=Smer[i].replace("L","")
            x -= int(f)
            i+=1
        else:
            Vychod = 1
            f=Smer[i].replace("R","")
            x += int(f)
            i+=1
    elif Zapad == 1:
        if 'L' in Smer[i]:
            f=Smer[i].replace("L","")
            y -= int(f)
            Jih = 1
            Zapad = 0
            i+=1
        else:
            f=Smer[i].replace("R","")
            y += int(f)
            Sever = 1
            Zapad = 0
            i+=1
    elif Vychod == 1:
        if 'L' in Smer[i]:
            f=Smer[i].replace("L","")
            y += int(f)
            Sever = 1
            Vychod = 0
            i+=1
        else:
            f=Smer[i].replace("R","")
            y -= int(f)
            Jih = 1
            Vychod = 0
            i+=1
    elif Sever == 1:
        if 'L' in Smer[i]:
            f=Smer[i].replace("L","")
            x -= int(f)
            Zapad = 1
            Sever = 0
            i+=1
        else:
            f=Smer[i].replace("R","")
            x += int(f)
            Vychod = 1
            Sever = 0
            i+=1
    elif Jih == 1:
        if 'L' in Smer[i]:
            f=Smer[i].replace("L","")
            x += int(f)
            Vychod = 1
            Jih = 0
            i+=1
        else:
            f=Smer[i].replace("R","")
            x -= int(f)
            Zapad = 1
            Jih = 0
            i+=1


if x <= 0:
    x = x*(-1)   
if y <= 0:
    y = y*(-1)

Block = x + y
print("Bloky: ", Block)
