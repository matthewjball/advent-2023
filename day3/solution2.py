from dataclasses import dataclass
from functools import reduce
import operator

@dataclass
class Gear:
    y: int
    x: int

@dataclass
class Digit:
    y: int
    x: int
    val: str

@dataclass
class Number:
    digits = []

    def value(self) -> int:
        value = ""
        for digit in self.digits:
            value += digit.val
        return int(value)
    
    def at_coordinate(self, y, x) -> bool:
        for digit in self.digits:
            if y == digit.y and x == digit.x:
                return True
        return False
        



file = open('input.txt', 'r')    
schematic = [i.strip('\n') for i in file.readlines()]
ratio_sum = 0
digits = []
numbers = []
gears = []

for y in range(0, len(schematic)): 
    for x in range(0,len(schematic[y])):
        if schematic[y][x] == '*':
            gears.append(Gear(y,x))
        if schematic[y][x].isdigit():
            digits.append(Digit(y,x, schematic[y][x]))
            continue
        if not schematic[y][x].isdigit() and digits:
            num = Number()
            num.digits = digits
            numbers.append(num)
            digits = []


for gear in gears:
    adj_numbers = []
    for y in range(gear.y-1, (gear.y+1)+1):
        for x in range(gear.x-1, (gear.x+1)+1):
            if y < len(schematic):
                if x < len(schematic[y]):
                    for number in numbers:
                        if number.at_coordinate(y, x):
                            adj_numbers.append(number.value())
    if len(set(adj_numbers)) == 2:
       print(f"Found {gear} with exactly 2 {set(adj_numbers)}")
       ratio_sum += reduce(operator.mul, list(set(adj_numbers)), 1)
    






print(f"Total sum of gear ratios: {ratio_sum}")