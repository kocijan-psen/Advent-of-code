data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day6_data.txt", "rt")]

obrbit_list = []
counter = 0

def counterorbits(dep_, orbits, tempcounter, on_orbit): #když není v kontrolním setu je to koncovka (breakpoint pro rekurzi)
    to_find = dep_
    turn_ = tempcounter
    if to_find not in on_orbit:
        return turn_
    
    for j in range(len(orbits)):            #najdu hlednou planetu na orbitu a prohodím ji s tou na jejímž orbitu je, pak rekurze
        if to_find == orbits[j][1]:
            to_find = orbits[j][0]
            turn_ +=1
            if to_find not in on_orbit:
                return turn_
            return counterorbits(to_find, orbits, turn_, on_orbit)

for line in data:           #rozdělení dat
    temp = line.split(")")
    obrbit_list.append(temp)

on_orbit = set()            #kontrolní set - logika, když není vpravo je to koncová planeta
for i in range(len(obrbit_list)):
    on_orbit.add(obrbit_list[i][1])

Answer1=0
for depended_ in on_orbit:
    tempcounter = 0
    res_ = counterorbits(depended_, obrbit_list, tempcounter,on_orbit)
    # print(f"hledal jsem {depended_} a výsledek je: {res_}")
    Answer1 +=res_
    tempcounter = 0
    
print(f"Odpověď část 1 je {Answer1}")
            




