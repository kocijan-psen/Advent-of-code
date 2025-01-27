data = 3,225,1,225,6,6,1100,1,238,225,104,0,1102,35,92,225,1101,25,55,225,1102,47,36,225,1102,17,35,225,1,165,18,224,1001,224,-106,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,68,23,224,101,-91,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,217,13,224,1001,224,-1890,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,69,77,224,1001,224,-5313,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,102,50,22,224,101,-1800,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,89,32,225,1001,26,60,224,1001,224,-95,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,51,79,225,1102,65,30,225,1002,170,86,224,101,-2580,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,39,139,224,1001,224,-128,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,54,93,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226

input_value = 5  # Vstupní hodnota pro ID tepelného radiátoru

# Převod na seznam (pokud je třeba)
array = list(data)

pointer = 0  # Ukazatel na aktuální instrukci

def get_value(mode, param):
    """Vrací hodnotu podle režimu parametru."""
    return array[param] if mode == 0 else param

while pointer < len(array):
    # Dekódování instrukce a režimů parametrů
    instruction = array[pointer]
    opcode = instruction % 100
    mode1 = (instruction // 100) % 10
    mode2 = (instruction // 1000) % 10
    mode3 = (instruction // 10000) % 10  # Nebude použito pro zápis

    if opcode == 1:  # Sčítání
        param1 = get_value(mode1, array[pointer + 1])
        param2 = get_value(mode2, array[pointer + 2])
        dest = array[pointer + 3]
        array[dest] = param1 + param2
        pointer += 4
    elif opcode == 2:  # Násobení
        param1 = get_value(mode1, array[pointer + 1])
        param2 = get_value(mode2, array[pointer + 2])
        dest = array[pointer + 3]
        array[dest] = param1 * param2
        pointer += 4
    elif opcode == 3:  # Uložení vstupu
        dest = array[pointer + 1]
        array[dest] = input_value
        pointer += 2
    elif opcode == 4:  # Výstup hodnoty
        param1 = get_value(mode1, array[pointer + 1])
        print("Output:", param1)  # Vypíše diagnostický kód
        pointer += 2
    elif opcode == 5:  # Skok, pokud true
        param1 = get_value(mode1, array[pointer + 1])
        param2 = get_value(mode2, array[pointer + 2])
        if param1 != 0:
            pointer = param2
        else:
            pointer += 3
    elif opcode == 6:  # Skok, pokud false
        param1 = get_value(mode1, array[pointer + 1])
        param2 = get_value(mode2, array[pointer + 2])
        if param1 == 0:
            pointer = param2
        else:
            pointer += 3
    elif opcode == 7:  # Menší než
        param1 = get_value(mode1, array[pointer + 1])
        param2 = get_value(mode2, array[pointer + 2])
        dest = array[pointer + 3]
        array[dest] = 1 if param1 < param2 else 0
        pointer += 4
    elif opcode == 8:  # Rovnost
        param1 = get_value(mode1, array[pointer + 1])
        param2 = get_value(mode2, array[pointer + 2])
        dest = array[pointer + 3]
        array[dest] = 1 if param1 == param2 else 0
        pointer += 4
    elif opcode == 99:  # Konec programu
        print("Program finished.")
        break
    else:
        print(f"Unknown opcode {opcode} at position {pointer}")
        break