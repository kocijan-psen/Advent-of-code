data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day1_data.txt", "rt")]

left_ = []
right_ = []
diff_ =0

for line in data:       #roztřízení řádků do polí
    temp = line.split()
    left_.append(int(temp[0]))
    right_.append(int(temp[1]))

left_.sort()            #seřazení od nejmenšího
right_.sort()

# print("left:",left_)
# print("right:",right_)

for i in range(len(left_)):             #odečítám po jednom od sebe a sčítám rozdíly v absolutní hodnnotě
    tmp = abs(left_[i]-right_[i])
    diff_ += tmp
    # print(left_[i], right_[i],diff_)

print("Answer part1: ", diff_)


