file = open('input.txt', 'r')    
cards = [i.split(': ')[1].strip('\n').replace('  ', ' ').split(' | ') for i in file.readlines()]

points_sum = 0
count = 0

for card in cards:
    winning_numbers = card[0].split(' ')
    card_numbers = card[1].split(' ')
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            print(f"found {winning_number} in {card_numbers}")
            count += 1

    if count > 0:
        points_sum += pow(2, count-1)
    count = 0

print(f"Sum of points: {points_sum}")
    