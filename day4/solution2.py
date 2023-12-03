file = open('input.txt', 'r')    
cards = [i.split(': ')[1].strip('\n').replace('  ', ' ').split(' | ') for i in file.readlines()]

copies_dict = {}
#populate dictionary
for i in range(0, len(cards)):
    copies_dict["Card" +str(i+1)] = 1

count = 0

for i in range(0, len(cards)):
    winning_numbers = cards[i][0].split(' ')
    card_numbers = cards[i][1].split(' ')
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            count += 1

    if count > 0:
        for j in range(1, count+1):
            #Increment next n copies for each winning number
            copies_dict["Card" + str(i+j+1)] += copies_dict["Card" +str(i+1)]
    count = 0

print(f"Total cards: {sum(copies_dict.values())}")
    