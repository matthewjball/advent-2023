file = open('input.txt', 'r')    
times, distances = [i.strip('\n') for i in file.readlines()]

time = int(times.split(':')[1].lstrip().replace(" ", ""))
distance = int(distances.split(':')[1].lstrip().replace(" ", ""))

def record_beating_permutations(time, distance) -> int:
    count = 0
    for i in range(0, time +1):
        if i * (time - i) > distance:
            count += 1
    return count


print(f"Number of record beating permutations: {record_beating_permutations(time, distance)}")
