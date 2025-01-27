import hashlib
from datetime import datetime

start = datetime.now()
data = "bgvyzdsv"
n = 1

while True:
    cislo = data+str(n)
    encrypt = hashlib.md5(cislo.encode())
    encrypt.hexdigest()

    if encrypt.hexdigest().startswith("000000"):
            print ("vysledek", cislo)

            break
    else: n +=1

print(datetime.now()-start)