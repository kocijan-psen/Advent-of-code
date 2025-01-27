data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2016/2016_day6_data.txt", "rt")]

answer1 = ""

result = [''.join(chars) for chars in zip(*data)] #setřízení podle sloupců

for li in result:
    most_frequesnt = 0
    letter = ""
    for char in li:
        if li.count(char) > most_frequesnt: # když je počet ve stringu větší než ten nejčastěji se vyskytující se - vymění se
            # print("kontrola", line.count(char))
            most_frequesnt= li.count(char)
            # print(char)
            letter = char
    answer1 +=letter
print("Answer1: ", answer1)

answer2 = ""

for li in result:
    fewest_frequesnt = 100000
    letter2 = ""
    for char in li:
        if li.count(char) < fewest_frequesnt: # když je počet ve stringu větší než ten nejčastěji se vyskytující se - vymění se
            # print("kontrola", line.count(char))
            fewest_frequesnt= li.count(char)
            # print(char)
            letter2 = char
    answer2 +=letter2
print("Answer2: ", answer2)


