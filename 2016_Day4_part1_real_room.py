data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2016/2016_day4_data.txt", "rt")]
Answer = 0

def define_(roomno):
    temp = {}

    for letter in roomno:
        if letter.isdigit():
            continue
        elif letter not in temp:
            temp[letter] = 1
        elif letter in temp:
            temp[letter] +=1
    # print(temp)
    return temp


def control(checksum, roomno):
    summaryrooms = define_(roomno)
    id_ = ""
    notinchecksum = {}
    cnt = 0

    for letter in roomno:
        if letter.isdigit():
            id_ = id_ + letter
        
    for key, value in summaryrooms.items():
        if key not in checksum:
            notinchecksum[key] = value
    # print("not in:", notinchecksum)
    if len(notinchecksum) == 0:
        max_other = 0
    else:
        max_other = max(notinchecksum.values())
    # print("max: ", max_other)

    for key, value in summaryrooms.items():
        if key in checksum and value >= max_other:
            cnt +=1
    
    if cnt == 5:
        return int(id_)
      
    # sorted_by_value = dict(sorted(summaryrooms.items(), key= lambda item: item[1], reverse=True)) #setřídím knihovnu od největší k nejmenší
    # print(sorted_by_value)

    # keys = list(summaryrooms.keys()) #vyhledám 5 nejčastějších
    # cnt = 0
    # for key in range(0,5):
    #     if keys[key] in checksum:
    #        cnt +=1


for line in data:                       #hlavní kod
    checksum = []
    temp = line.split("[")
    roomno = temp[0].replace("-","")
    # print (roomno)
    checkers = temp[1].replace("]","")
    for char in checkers:               #vytvoření kontrolních prvků v knihovně
        checksum.append(char)
    
    roomid = control(checksum, roomno)
    # print(roomid)
    if roomid != None:
        Answer = Answer + roomid

print("Answer part1 = ", Answer)
 