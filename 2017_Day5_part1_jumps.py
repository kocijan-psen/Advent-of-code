data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day5_data.txt", "rt")]
 
filt_data = []
i = 0
cnt =1

for char in data:
    filt_data.append(int(char))


while i in range(len(filt_data)):
    filt_data[i] = filt_data[i]+1
    offset_ = filt_data[i]
    i = i + offset_-1
    if i not in range(len(filt_data)):
        break
    else:
        cnt +=1
        # print(filt_data)

print("Answer part1: ", cnt)

# part 2 
i = 0
cnt2 =1
orig_filt_data = []

for char in data:
    orig_filt_data.append(int(char))

while i in range(len(orig_filt_data)):
    offset_2 = orig_filt_data[i] #posunuto kvůli té podmínce
    if offset_2 >=3:
        orig_filt_data[i] = orig_filt_data[i]-1
    else: 
        orig_filt_data[i] = orig_filt_data[i]+1
    i = i + offset_2                #odebráno oproti part1 "-1" kvůli změně pořadí
    if i not in range(len(orig_filt_data)):
        break
    else:
        cnt2 +=1
        # print(orig_filt_data)

print("Answer part2: ", cnt2)
