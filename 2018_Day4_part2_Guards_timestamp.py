from datetime import datetime
from datetime import datetime, timedelta
from collections import Counter

data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2018/2018_Day4_data.txt", "rt")]
Guard = {}
Guard_time = {}

def frequency(times):
    all_minutes = []
    time_format = "%Y-%m-%d %H:%M"  # Formát časových značek

    for start_str, end_str in times:  # Pro každý interval generujeme jednotlivé minuty
        start_time = datetime.strptime(start_str, time_format)
        end_time = datetime.strptime(end_str, time_format)

        # Ošetření: ujistíme se, že začátek je dříve než konec (swap pokud je opačně)
        if start_time > end_time:
            start_time, end_time = end_time, start_time

        # Generování jednotlivých minut v daném intervalu (bez zahrnutí end_time)
        current_time = start_time
        while current_time < end_time:
            all_minutes.append(current_time.strftime("%H:%M"))
            current_time += timedelta(minutes=1)

    # Použití Counter k nalezení nejčastější minuty
    minute_counts = Counter(all_minutes)
    
    # Kontrola, zda existují nějaké minuty
    if minute_counts:
        most_common_minute, count = minute_counts.most_common(1)[0]
    else:
        most_common_minute, count = None, 0  # Vrací None, pokud nejsou žádné minuty

    return [most_common_minute, count]

def extract_timestamp(entry):                                   #vytvoření časové známky
    timestamp_str = entry.split("]")[0].strip("[]")
    return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")

sorted_data = sorted(data, key=extract_timestamp)               #setřízení podle časové známky

for a in range(len(sorted_data)):
    if "Guard" in sorted_data[a]:
        temp = sorted_data[a].split(" ")
        guard_id = temp[3].replace("#","")
        if guard_id not in Guard:
            Guard[guard_id]=0
        if guard_id not in  Guard_time: #pokus - příprava na hledání nejčastější minuty
            Guard_time[guard_id] = []
        actual = guard_id

    if "wakes" in sorted_data[a]:
        tmp1 = sorted_data[a].split("]")[0].strip("[]")  #vyfiltruju string s časovou známkou
        tmp2 = sorted_data[a-1].split("]")[0].strip("[]") 
        Guard_time[actual].append((tmp2, tmp1))#pokus - příprava na hledání nejčastější minuty
        # print("tmp",Guard_time[actual])
        format = "%Y-%m-%d %H:%M"
        dt1 = datetime.strptime(tmp1, format) # převedu string na časovou známku
        dt2 = datetime.strptime(tmp2, format)
        diff_= dt1 - dt2
        diff_minutes =  diff_.seconds//60 # rozdíl v minutách
        # print("diff_minuty: ", diff_minutes)
        Guard[actual]+=int(diff_minutes)
        # print("Guard: ", Guard)

sorted_Guard = dict(sorted(Guard.items(), key=lambda item: item[1]))
topsleep = list(sorted_Guard.items())[-1]
# print("top. ", topsleep)

# print("pokus: ", topsleep[0])

# print("Guard_time", Guard_time)
temp = {}
for guard_id, times in Guard_time.items():
    mostfrequent = frequency(times)
    if mostfrequent[0] is not None:  # Přidáme jen, pokud existuje platná minuta
        temp[guard_id] = mostfrequent

# Setřídíme podle frekvence výskytu
sorted_temp = dict(sorted(temp.items(), key=lambda item: item[1][1], reverse=True))
topfreq = list(sorted_temp.items())[0]
# Získání dat z topfreq
top_freq_id_guard = int(topfreq[0])
top_freq_minute_before = topfreq[1][0].split(":")
top_freq_minut_clean = int(top_freq_minute_before[1])

Answer_part2 = top_freq_id_guard * top_freq_minut_clean
print(f"Nejčastější minuta strážného {top_freq_id_guard}: {top_freq_minut_clean} a ten výsledek je: {Answer_part2}")

    

