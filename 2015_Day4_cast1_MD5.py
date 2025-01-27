import hashlib


data = "iwrupvqb"
Pepa = "bgvyzdsv"

sample = "pqrstuv"
n = 1

while True:
    cislo = Pepa+str(n)
    encrypt = hashlib.md5(cislo.encode())
    encrypt.hexdigest()

    if encrypt.hexdigest().startswith("00000"):
            print ("vysledek", cislo)
            break
    else: n +=1

