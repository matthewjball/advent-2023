import math
file = open('input.txt', 'r')    
times, distances = [i.strip('\n') for i in file.readlines()]

times = times.split(':')[1].lstrip().split(' ')
distances = distances.split(':')[1].lstrip().split(' ')
while '' in times: times.remove('')
while '' in distances: distances.remove('')
times = [int(i) for i in times]
distances = [int(i) for i in distances]

no_record_beating_permutations = []

def record_beating_permutations(time, distance) -> int:
    count = 0
    for i in range(0, time +1):
        if i * (time - i) > distance:
            count += 1
    return count

for i in range(0, len(times)):
    no_record_beating_permutations.append(record_beating_permutations(times[i], distances[i]))

print(f"Product of record beating permutations: {math.prod(no_record_beating_permutations)}")
