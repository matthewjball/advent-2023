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
        if in_val in range(mapping_range.dest, mapping_range.dest + mapping_range.step):
            return mapping_range.source + (in_val - mapping_range.dest)
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

seed_pairs = []
for i in range(0, len(seeds), 2):
    seed_pairs.append([seeds[i], seeds[i+1]])

def valid_initial_seed(seed_val) -> bool:
    for seed_pair in seed_pairs:
        if (int(seed_pair[0])) <= seed_val <= int(seed_pair[0])+ int(seed_pair[1]):
            return True
    return False


#For every number, starting from 0        
for i in range(0, sys.maxsize):
    print(f"Checking location value {i}...")
    curr_val = i
    for mapping in reversed(mappings):
        curr_val = mapped_value(curr_val, mapping)
    if valid_initial_seed(curr_val):
        print(f"Lowest location value from initial seeds: {i}")
        sys.exit()


    
