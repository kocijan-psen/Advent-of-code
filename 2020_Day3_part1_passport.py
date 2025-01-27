data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2020/2020_Day3_data.txt", "rt")]
passport = {"must":["byr","iyr","eyr","hgt","hcl","ecl","pid"]}
parametres = {"byr":range(1920,2003),"iyr":range(2010,2021),"eyr":range(2020,2031),"hgtin":range(59,77),"hgtcm":range(150,194),"hcl":6,"ecl":["amb","blu", "brn", "gry", "grn", "hzl", "oth"],"pid":9}
array = []
helping = []
count1 = 0
count2 = 0
x = ""
control = ""

#do data na konci přidat prázdný řádek


for line in data:
    if line == "":
        # print("x:",x)
        array.append(x)
        x = ""
    else:
        x = x+" "+line 

# print(array)
for i in array:
        # print(i)
        if passport["must"][0] in i:
            if passport["must"][1] in i:
                if passport["must"][2] in i:
                        if passport["must"][3] in i:
                            if passport["must"][4] in i:
                                if passport["must"][5] in i:
                                    if passport["must"][6] in i:
                                            count1 +=1
                                            helping.append(i)
for i in helping:
    j =  i.split(" ")
    for par in j:
        #   print("par:",par)
        if passport["must"][0] in par:
            tmp = par.replace(passport["must"][0]+":","")
            if int(tmp) in parametres["byr"]:
                control = control + "a"
        elif passport["must"][1] in par:
            tmp = par.replace(passport["must"][1]+":","")
            if int(tmp) in parametres["iyr"]:
                control = control + "b"
        elif passport["must"][2] in par:
            tmp = par.replace(passport["must"][2]+":","")
            if int(tmp) in parametres["eyr"]:
                control = control + "c"
        elif passport["must"][3] in par:
            tmp = par.replace(passport["must"][3]+":","")
            if "cm" in tmp:
                tmp = tmp.replace("cm","")
                if int(tmp) in parametres["hgtcm"]:
                    control = control + "d"
            if "in" in tmp:
                tmp = tmp.replace("in","")
                if int(tmp) in parametres["hgtin"]:
                    control = control + "d"
        elif passport["must"][4] in par:
            tmp = par.replace(passport["must"][4]+":","")
            if "#" in tmp:
                tmp =  len(tmp)-1
                if int(tmp) == parametres["hcl"]:
                    control = control + "e"
        elif passport["must"][5] in par:
            tmp = par.replace(passport["must"][5]+":","")
            if tmp in parametres["ecl"]:
                control = control + "f"
        elif passport["must"][6] in par:
            tmp = par.replace(passport["must"][6]+":","")
            tmp = len(tmp)
            if tmp == parametres["pid"]:
                control = control + "g"

    print("control:",control)
    sorted_control= ''.join(sorted(control))
    if sorted_control == "abcdefg":
        count2 +=1
    control = ""                                          

print("vysledek_cast1:",count1)
print("vysledek_cast2:",count2)
