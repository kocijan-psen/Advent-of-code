def getResult(key):
    result = 0
    global cnt, wires, control
    cnt += 1
    if not key in wires:
        for line in lines:
            tmp = line.split(' ')
            if tmp[len(tmp)-1] == key:
                if len(tmp) == 3:
                    if not tmp[0] in control: # 222 -> x
                        result = int(tmp[0])
                    else: #  x -> y
                        result = getResult(tmp[0])
                elif tmp[0] == "NOT": # not x -> y
                    result = 65535-int(getResult(tmp[1]))
                else:
                    if (tmp[1] == "AND"): # x and y -> z
                        if not tmp[0] in control: # 1 and x -> y
                            result = 1 & getResult(tmp[2])
                        else:
                            result = getResult(tmp[0]) & getResult(tmp[2])
                    elif (tmp[1] == "OR"): # x or y -> z
                        result = getResult(tmp[0]) | getResult(tmp[2])
                    elif (tmp[1] == "LSHIFT"): # x lshift y -> z
                        result = getResult(tmp[0]) << int(tmp[2])
                    elif (tmp[1] == "RSHIFT"): # x rshift y -> z
                        result = getResult(tmp[0]) >> int(tmp[2])
                    else:
                        print ("neznamy command:", line)
                        break 
                wires.update({key:result})
    return wires[key]

inputData = open("2015/input_day_7.txt","rt")
#inputData = open("2015/pokus.txt","rt")

lines = []

for line in inputData: 
    lines.append(line.replace("\n",""))

cnt = 0

control = {}
wires = {}
for line in lines:
    tmp = line.split(' ')
    control[tmp[len(tmp)-1]] = 0

a = getResult("a")
#print(wires)
#print(control)
print ("task 1 = ", a, cnt)

cnt = 0
wires = {}
wires["b"] = a
a = getResult("a")
print ("task 2 =", a, cnt)