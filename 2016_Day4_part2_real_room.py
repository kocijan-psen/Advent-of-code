data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2016/2016_day4_data.txt", "rt")]
Answer = 0
finding_ = "northpole object storage"  #v AOC bylo napsáno "North Pole objects"

def decoding(text, moves_):
    decoded_ = ""
    for char in text:
        if char == "-":                 #když je v textu pomlčka, má tam být mezera
            decoded_= decoded_+ " "
        else:   
            pos_= ord(char)+moves_      #převede na ascii 
            if pos_ > ord('z'):         #podmínka aby se nepřesáhla malá písmena
                pos_ -=26
            decoded_ = decoded_ + chr(pos_)
    
    return decoded_



for line in data: #hlavni program
    number_=""
    for char in line:               #zjištění ID
        if char.isdigit():
            number_ = number_+char 
    moves_ = int(number_) % 26      # úprava přes modulo (zbytek po dělení čísla)
    
    temp = line.split("[")                      #smažu to v závorkách :)
    text =  temp[0].replace("-"+number_, "")

    decoded_text = decoding(text, moves_)
    # print(decoded_text, number_)
    if decoded_text == finding_:
        
        print("Answer part 2 is: ", number_)
        break
    


    