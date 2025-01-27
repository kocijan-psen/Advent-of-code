data = [line.replace("\n","") for line in open("C:/Users/kocij/Documents/Python/2023/2023_Day3_data.txt", "rt")]
number = ["0","1","2","3","4","5","6","7","8","9"]
array =[]
# flag = False
gearratio = {}
a = 0
temp =[]
tmp = ""

def findnumber(array, i, j): #tu sem ti dal do riti to K, L, který tu bylo zbytečně
    # to tmp v zadání funkce sem ti dal taky pryč, když ho tady pak nastavuješ na prýzdnej string.. takže je to uplně jedno :D 
    tmp=""
    # tady může bejt ještě kontrola že nemáš I/J == 0 bo tu pak moc nezajedeš "doleva" 
    while array[i][j].isdigit(): # tleskám (neironicky).. krásně použitej cyklus!, to samý pak o 3 řádky níž
        print("array[i-k][j-l]",array[i][j] )
        j-=1

    # tady ti nenápadně doplnim j+1 protože poslední index kterej ti ten vrchní cyklus přečte tak je "." :)
    j += 1
    #tenhle cyklus může bejt napsanej i jako "for nevimco in range(j,veliksotpole)".. protože čteme pouze doprava.. I složka nás nezajímá, ta je konstantní :D 
    while array[i][j].isdigit():
        print("array[i-k][j-l]",array[i][j] )
        #tady sem ti prohodil pořadí čtení.. prvně přiřadí NAČTENOU CIFRU a pak teprve inkrementuje
        tmp = tmp+array[i][j]
        j+=1
    return tmp
    
#nezapisuje číslo..... zjistit proč :)

def arenumbersthere(array, i, j):
    """
    zkontroluje okolí hvezdy a zjistí kolik je tam čísel
    """
    ilimit, jlimit = len(array), len(array[0]) # vytvořim si proměnný pro zjištění velikosti pole.. kdyby náhodou nebylo čtvercový
    temp = []
    cnt = 0
    for k in [-1,0,1]: #kontrola všech prvků kolem
        for l in [-1,0,1]:
            if k == 0 and l == 0: #když se rovnají nule, je to konrtolované číslo
                 continue
            if 0 <= i + k < ilimit and 0 <= j + l < jlimit: # tady pak používám proměnný který mam v rámci kontextu funkce #kontrola jestli jsem v poli
                if array[i-k][j-l].isdigit():
                    cnt +=1 # a tohle je co? V .. proč předáváš I, J, J, K ??? proč to není I, J, K, L ?
                    #findnumber(array, i, j, j, k, tmp) .. tohle je blbost.. proč volám naprázdno funkci která vrací nějakou hodnotu.. :D 
                    temp.append(findnumber(array, i-k, j-l)) # .. takhle už to může vypadat.. že třeba tu návratovou hodnotu funkce nacpu do pole.. nebo si jí uložim do proměnný
                    print("temp",temp)

    # tady prostě vracim co ta funkce najde a neřešim nějaký počítadlo 
    return temp

    # tohle je to počítadlo co "neřešim"
    """
    if cnt == 2:
        return temp
    """

for line in data:
    sub = []
    for item in line:
        sub.append(item)
    array.append(sub)

# print(array)
rows = len(array)
cols = len(array[0])
# print(rows)
# print(cols)
pepkovoPole = list()

for i in range(rows):
    for j in range(cols):
        # kontrola = array[i][j]
        if array[i][j] == "*":
            # volání funkce sem upravil podle změn v deklaraci funkce
            pepkovoPole = arenumbersthere(array, i, j) #nevim proč si nevracíš rovnou coučet těch čísel ale vracíš si celý pole..
            if len(pepkovoPole) == 2: # tohle je taky podmínka jak fík.. ty ve funkci zjistíš počet prvků .. tj if cnt == 2: .. a pak tady ZNOVA kontroluješ počet prvků.. ale ok to není žádnej průšvih, je to jenom redundantní kontrola.. a dává to i trošku smysl neboť ve funkci si děláš nějaký počítadlo a pak kontroluješ to počítadlo a vedle toho si tvoříš nějaký pole a na základě počítadla vracíš pole, takže kontrola zda to pole odpovídá požadavkům může být na místě, kdyby ta funkce nefungovala korektně
                print("MAIN: CHYCENY SPRAVNY POLE", pepkovoPole)
            else:
                print("hovno") # ... nice
