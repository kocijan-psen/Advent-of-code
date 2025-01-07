data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2019/2019_Day6_data.txt", "rt")]

obrbit_list = []
counter = 0

def counterorbits(to_find, orbits,path,x):
    # print(path)
    if to_find == x:
        # print("jsem tu")
        return path
    else:
        for j in range(len(orbits)):
            if to_find == orbits[j][1]:
                # print(f"to find před změnou: {to_find}")
                to_find = orbits[j][0]
                path.append(orbits[j][0])
                # if to_find not in on_orbit:
                #     # print("jsem tu")
                #     return path
                # print(f"to find po změně: {to_find}")
                return counterorbits(to_find, orbits,you,x)

for line in data:
    temp = line.split(")")
    obrbit_list.append(temp)

on_orbit = set()
before_orbits = set()                    #kontrolní set - logika, když není vpravo je to koncová planeta
for i in range(len(obrbit_list)):
    on_orbit.add(obrbit_list[i][1])
    before_orbits.add(obrbit_list[i][0])

yx = before_orbits - on_orbit
x = yx.pop()  # Extrahuje jediný prvek ze setu



both_paths = []
for depended_ in on_orbit:                          #vytvořím si celou cestu orbitů pro YOU a SAN
    if depended_ == "YOU" or depended_ == "SAN":
        you = []
        res_= counterorbits(depended_, obrbit_list, you,x)
        res_.reverse()                                      #otočím, aby cesta byla od začátku
        both_paths.append(res_)


while both_paths[0][0] == both_paths[1][0]:             #vyčistím si pole o ty prvky, kde je cesta stejná
    both_paths[0].remove(both_paths[0][0])
    both_paths[1].remove(both_paths[1][0])
    # print(both_paths)

Answer2 = len(both_paths[0]+both_paths[1])
print(f"Odpověď na část 2 je: {Answer2}")           




