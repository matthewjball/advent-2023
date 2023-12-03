from dataclasses import dataclass

@dataclass
class Digit:
    y: int
    x: int
    val: str


def valid_part_no(digits, schematic) -> bool:
    for digit in digits:
        print(f"Looking at the digit{digit}")
        for y in range(digit.y-1, (digit.y+1)+1):
            for x in range(digit.x-1, (digit.x+1)+1):
                if y < len(schematic):
                    if x < len(schematic[y]):
                        if schematic[y][x] != '.' and not schematic[y][x].isdigit():
                            print(f"Valid part at {y,x} found: {schematic[y][x]}")
                            return True
    return False

file = open('input.txt', 'r')    
schematic = [i.strip('\n') for i in file.readlines()]
part_sum = 0
digits = []

for y in range(0, len(schematic)): 
    for x in range(0,len(schematic[y])):
        if schematic[y][x].isdigit():
            digits.append(Digit(y,x, schematic[y][x]))
            continue
        if not schematic[y][x].isdigit() and digits:
            print(f"evaluating {digits}")
            if valid_part_no(digits, schematic):
                value = ""
                for digit in digits:
                    value += digit.val
                part_sum += (int(value))
            digits = []
            print("\n\n")

print(f"Total sum of part values: {part_sum}")