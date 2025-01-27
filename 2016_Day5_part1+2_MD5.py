import hashlib


data = "ffykfhsq"
n = 0
answer = ""


while len(answer)<8:
    number = (data+str(n)).encode()   # number = f"{data}{n}".encode()
    encrypt = hashlib.md5(number).hexdigest()

    if encrypt.startswith("00000"):
        #     print(encrypt)
            answer += encrypt[5]
            
    n +=1

print("Answer part 1: ", answer)

#část 2

password = ["_"] * 8  # Inicializace prázdného hesla s osmi místy
filled_positions = set()
n = 0  # počáteční hodnota pro n

while "_" in password:
    number = (data + str(n)).encode()  # přidání hodnoty n ke stringu data a kódování
    encrypt = hashlib.md5(number).hexdigest()

    if encrypt.startswith("00000"):
        position = encrypt[5]
        value = encrypt[6]

        if position.isdigit():
            position = int(position)
            if 0 <= position < 8 and position not in filled_positions:
                password[position] = value
                filled_positions.add(position)  # Označení pozice jako obsazené

    n += 1  # zvýšení n mimo podmínku

final_password = ''.join(password)  # sloučení hesla do řetězce
print("Answer part 2:", final_password)