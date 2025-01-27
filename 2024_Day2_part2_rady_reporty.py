data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2024/2024_Day2_data.txt", "rt")]

cnt = 0

def create_variants(temp):
    return [temp[:j] + temp[j+1:] for j in range(len(temp))]

def direction():                            #kontrola zda je celá řada buď klesající nebo stoupající
    global temp
    is_up = all(int(temp[j]) < int(temp[j+1]) for j in range(len(temp)-1))
    is_down = all(int(temp[j]) > int(temp[j+1]) for j in range(len(temp)-1))
    # print(is_up, is_down)
    return is_up or is_down
    
def conditions():
    global temp
    for k in range(len(temp) - 1):
        if temp[k] == temp[k+1]:  # Čísla se nesmí rovnat
            return False
        if abs(int(temp[k]) - int(temp[k+1])) >= 4:  # Rozdíl nesmí být >= 4
            return False
    return direction()  # Zkontroluje, zda je monotónní (stoupající nebo klesající)

for line in data:                           #hlavní kód, jedu po řádcích - podmínky: nesmí se rovnat, rozdíl nesmí být víc než 3
    temp = line.split()                     #musí jen klesat nebo jen stoupat
    control =0
    result_ = conditions()
    if result_ == True:
        cnt+=1
    else:
        variants = create_variants(temp)
        for variant_index, variant in enumerate(variants):
            temp = variant
            result_ = conditions()
            # print(result_)
            if result_ == True:
                cnt+=1
                break

print("Answer part2: ", cnt)

            