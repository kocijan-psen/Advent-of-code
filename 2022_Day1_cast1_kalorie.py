datakalorie=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2022/2022_Day1_cast1_data.txt", "rt")]

elfpole = []
KalorieElfu = []
n = 0

for radek in datakalorie:
    if radek =='':
        kalorie = sum(elfpole)
        n +=1
        KalorieElfu.append(kalorie)
        elfpole = []
    if radek !='':
        elfpole.append(int(radek))
print("Kalorie neseřazené:", KalorieElfu)

KalorieElfu.sort()
Nejvetsihodnota = KalorieElfu[n-1]
Trinej = KalorieElfu[n-1] + KalorieElfu[n-2] + KalorieElfu[n-3] 

print("Kalorie seřazené:", KalorieElfu)

print("Největší kalorie jsou:", Nejvetsihodnota)
print("Součet 3 je:", Trinej)   