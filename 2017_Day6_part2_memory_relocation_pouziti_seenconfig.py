data=[line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2017/2017_Day6_data.txt", "rt")]

memory = []
seen_configs = {}  # Slovník pro uložení konfigurací a jejich cyklů
counter = 0  # Počet cyklů

temp1 = data[0].split()
for i in range(len(temp1)):  # Převedení na int
    memory.append(int(temp1[i]))

while True:
    # Najdi index banky s nejvyšší hodnotou
    index, highest_value = max(enumerate(memory), key=lambda x: x[1])
    memory[index] = 0  # Vyprázdni tuto banku

    # Přerozdělení bloků
    for _ in range(highest_value):
        index += 1
        if index == len(memory):
            index = 0
        memory[index] += 1

    counter += 1

    # Detekce smyčky
    config_tuple = tuple(memory)  # Převod na n-tici, aby byla hashovatelná
    if config_tuple in seen_configs:
        first_occurrence = seen_configs[config_tuple]  # Získání prvního cyklu
        loop_size = counter - first_occurrence  # Velikost smyčky
        break

    # Ulož aktuální stav a jeho cyklus
    seen_configs[config_tuple] = counter

# Výstup
print("Velikost smyčky:", loop_size)