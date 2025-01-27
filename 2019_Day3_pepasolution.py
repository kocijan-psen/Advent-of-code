data=[line.replace("\n","") for line in open("AOC/2019/input_day3.txt", "rt")]

x, y = 0, 0
arr = list()

def move(wire, x, y):
    d = wire[0]
    l = int(wire[1:])
    nx, ny = 0, 0

    if d == "U":
        nx = x + l
        return (nx, y)
    elif d == "R":
        ny = y - l
        return (x, ny)
    elif d == "D":
        nx = x - l
        return (nx, y)
    elif d == "L":
        ny = y + l
        return (x, ny)


def getIntersection(data1, data2):
    x, y = 0, 0

    #print(f"data1: {data1} ; data2: {data2}")

    sx1, sy1 = data1[0]
    ex1, ey1 = data1[1]

    if sx1 > ex1:
        tmp = sx1
        sx1 = ex1
        ex1 = tmp

    if sy1 > ey1:
        tmp = sy1
        sy1 = ey1
        ey1 = tmp        

    sx2, sy2 = data2[0]
    ex2, ey2 = data2[1]

    if sx2 > ex2:
        tmp = sx2
        sx2 = ex2
        ex2 = tmp

    if sy2 > ey2:
        tmp = sy2
        sy2 = ey2
        ey2 = tmp
    
    #print(f"start: {sx1, sy1} ,end: {ex1, ey1} ; start: {sx2, sy2} ,end: {ex2, ey2}")

    if sy1 in [n for n in range(sy2,ey2+1)] and sx2 in [n for n in range(sx1,ex1+1)]:
        #print(f"cross: {(True, sx2, sy1)}")
        return (True, sx2, sy1)
        
    if sx1 in [n for n in range(sx2,ex2+1)] and sy2 in [n for n in range(sy1,ey1+1)]:
        #print(f"cross: {(True, sx1, sy2)}")
        return (True, sx1, sy2)

    return (False, 0, 0)

def getSteps(line):
    sx, sy = line[0]
    ex, ey = line[1]

    #print(line)
    #print(abs(sx-ex) + abs(sy-ey))
    return (abs(sx-ex) + abs(sy-ey))

for i in range(len(data)):
    wires = data[i].split(",")
    arr.append(list())
    x, y= 0 , 0
    for wire in wires:
        tmp = (x, y)
        (x, y) = move(wire, x, y)
        arr[i].append([tmp,(x,y),int(wire[1:])])

task1 = []
task2 = []
w1steps, w2steps = 0, 0

for i in range(len(arr[0])):
    w2steps = 0
    for j in range(len(arr[1])):
        cross = getIntersection(arr[0][i], arr[1][j])
        if not cross[0]:
            w2steps += arr[1][j][2]
        else:
            #print(cross)
            task1.append(abs(cross[1])+abs(cross[2]))
            task2.append(w1steps+getSteps([arr[1][j][0],(cross[1],cross[2])]) + w2steps+getSteps([arr[0][i][0],(cross[1],cross[2])]))
            w2steps += arr[1][j][2]

    w1steps += arr[0][i][2]

task1.sort()
task2.sort()

# 15002 je hodne
print("task1: ", task1[1] if task1[0] == 0 else task1[0])

# 12438 je málo 
print("task2: ", task2[1] if task2[0] == 0 else task2[0])
