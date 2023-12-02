def game_power(game) -> int:
    rounds = game.split(': ')[1].split('; ')

    max_red = 0
    max_green = 0
    max_blue = 0

    for round in rounds:
        pulls = round.split(', ')
        for pull in pulls:
            num = int(pull.split(' ')[0])
            colour = pull.split(' ')[1]
            match(colour):
                case 'red':
                    if num > max_red:
                        max_red = num
                case 'green':
                    if num > max_green:
                        max_green = num
                case 'blue':
                    if num > max_blue:
                        max_blue = num

    return max_red * max_green * max_blue



file = open('input.txt', 'r')

power_sum = 0
games = [i for i in file.readlines()]

for game in games:
    power_sum += game_power(game.strip('\n'))
    

print(f"Total sum of valid games: {power_sum}")



