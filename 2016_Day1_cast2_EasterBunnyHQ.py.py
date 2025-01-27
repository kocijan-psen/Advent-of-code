from ast import Break


data = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"

i = 0
j = 0
Sever = 0
Zapad = 0
Jih = 0
Vychod = 1 #První směr je doprava
x = 0
y = 0
PoziceDatabase = []
pozice = (0,0)

def Pozicevdatabazi():
    global x, y, pozice, PoziceDatabase
    if x <= 0:
        x = x*(-1)   
    if y <= 0:
        y = y*(-1)
    Blocknew = x + y
    print("Ten kraličí zmrd je:", Blocknew )
    return
def Kontrolapozice():
    global x, y, pozice, PoziceDatabase
    if pozice in PoziceDatabase:
                    Pozicevdatabazi()
    else:
        PoziceDatabase.append(pozice)

Smer = data.split(", ")

while i <= len(Smer)-1:

    x,y = pozice
 
    if Zapad == 1:
        if 'L' in Smer[i]:
            f=int(Smer[i].replace("L",""))
            for j in range(f):
                y =y - 1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Jih = 1
            Zapad = 0
            i+=1
            j=0
        else:
            f=int(Smer[i].replace("R",""))
            for j in range(f):
                y +=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Sever = 1
            Zapad = 0
            i+=1
            j=0

    elif Vychod == 1:
        if 'L' in Smer[i]:
            f=int(Smer[i].replace("L",""))
            for j in range(f):
                y +=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Sever = 1
            Vychod = 0
            i+=1
            j=0
        else:
            f=int(Smer[i].replace("R",""))
            for j in range(f):
                y -=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Jih = 1
            Vychod = 0
            i+=1
            j=0

    elif Sever == 1:
        if 'L' in Smer[i]:
            f=int(Smer[i].replace("L",""))
            for j in range(f):
                x -=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Zapad = 1
            Sever = 0
            i+=1
            j=0
        else:
            f=int(Smer[i].replace("R",""))
            for j in range(f):
                x +=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Vychod = 1
            Sever = 0
            i+=1
            j=0

    elif Jih == 1:
        if 'L' in Smer[i]:
            f=int(Smer[i].replace("L",""))
            for j in range(f):
                x +=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Vychod = 1
            Jih = 0
            i+=1
            j=0
        else:
            f=int(Smer[i].replace("R",""))
            for j in range(f):
                x -=1
                pozice = (x,y)
                Kontrolapozice()
                j+=1
            Zapad = 1
            Jih = 0
            i+=1
            j=0

if x <= 0:
    x = x*(-1)   
if y <= 0:
    y = y*(-1)

Block = x + y
print("Bloky: ", Block)
