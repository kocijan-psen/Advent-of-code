Pepa = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/output_pepa.txt", "rt")]
Honza = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/output_ja.txt", "rt")]
data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/Day1_part2_data.txt", "rt")]
file = open("C:/Users/kocij/Documents/Python/2023/Day1_testdata.txt", "a")
pole = []


for i in range(1000):
    if Pepa[i] != Honza[i]:
        pole.append(i)
for i in pole:
    file.write (data[i]+"\n")
file.close()