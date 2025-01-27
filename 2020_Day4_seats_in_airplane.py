import math

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day4_data.txt", "rt")]
row = []
col = []
seatid = []


for i in range(1,7):
    a = round((127)*0.5**i)
    row.append(a)

for j in range(1,3):
    b = round((8)*0.5**j)
    col.append(b)

# print(len(row))

# print(len(col))
for line in data:
    rowstart = 0
    rowend = 127
    colstart = 0
    colend = 7
    for k in range(0,7):
        # print(k)
        if line[k] == "F":
            if k == 6:
                x = rowstart
            else:
                rowend = rowend - row[k]
        if line[k] == "B":
            if k == 6:
                x = rowend
            else:
                rowstart = rowstart + row[k]
        # print(f"rowstart: {rowstart}, rowend: {rowend}")
    for l in range(3):
        if line[l+7] == "L":
            if l == 2:
                y = colstart
            else:
                colend = colend - col[l]
        if line[l+7] == "R":            
            if l == 2:
                y = colend
            else:
                colstart= colstart + col[l]
        # print(f"colstart: {colstart}, colend: {colend}")
# print(f"x: {x}, y: {y}")

    seat = x*8+y
    seatid.append(seat)
    # print("seatID: ", seat)

print("Answer: ",seatid[-1])


seatid.sort()
for a in range(len(seatid)):
    if seatid[a]-seatid[a+1] == -2:
        myseat=seatid[a]+1
        print("Answer part2: ",myseat)
        break
               




    


    