from dataclasses import dataclass
import sys

@dataclass
class Range:
    dest: int
    source: int
    step: int

@dataclass
class Mapping:
    name: str
    ranges: []

file = open('input.txt', 'r')    
lines = [i.strip('\n') for i in file.readlines()]

seeds = lines[:1][0].split(': ')[1].split(' ')
lines = lines[2:]
mappings = []


def mapped_value(in_val, mapping) -> int:
    for mapping_range in mapping.ranges:
        if in_val in range(mapping_range.source, mapping_range.source + mapping_range.step):
            return mapping_range.dest + (in_val - mapping_range.source)
    return in_val
        

mapping = Mapping('', [])
    
for line in lines:
    if line == "":
        mappings.append(mapping)
        mapping = Mapping('', [])
    elif 'map' in line:
        mapping.name = line
    else:
        dest, source, step = line.split(' ')
        mapping.ranges.append(Range(int(dest), int(source), int(step)))

lowest_val = sys.maxsize


for seed in seeds:
    curr_val = int(seed)
    for mapping in mappings:
        curr_val = mapped_value(curr_val, mapping)
    if curr_val < lowest_val:
        lowest_val = curr_val
        print(f"new lowest value: {lowest_val}")

print(f"lowest location value {lowest_val}")


    
