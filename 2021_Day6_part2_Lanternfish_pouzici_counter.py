from collections import Counter

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2021/2021_Day6_data.txt", "rt")]

lanternfish = []

for line in data:
    for x in line:
        if x.isdigit():
            lanternfish.append(int(x))

fish_counter = Counter(lanternfish) # Počítadlo frekvencí, které zaznamená počet ryb v každém stádiu

days = 256  # počet kroků simulace

# Simulace
for _ in range(days):
    new_fish_counter = Counter()
    for state in range(9):
        if state == 0:
            # Rybám na konci cyklu vytvoříme nové ryby (status 8) a obnovíme je (status 6)
            new_fish_counter[6] += fish_counter[state]
            new_fish_counter[8] += fish_counter[state]
        else:
            # Ostatní ryby snížíme o jeden cyklus
            new_fish_counter[state - 1] += fish_counter[state]
    fish_counter = new_fish_counter

# Výpočet celkového počtu ryb
total_fish = sum(fish_counter.values())
print(f"Část 2: Celkový počet ryb je {total_fish}")