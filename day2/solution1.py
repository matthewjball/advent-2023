RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def valid_game(game) -> bool:
    rounds = game.split(': ')[1].split('; ')
    for round in rounds:
        pulls = round.split(', ')
        for pull in pulls:
            num = int(pull.split(' ')[0])
            colour = pull.split(' ')[1]
            match(colour):
                case 'red':
                    if num > RED_MAX:
                        return False
                case 'green':
                    if num > GREEN_MAX:
                        return False
                case 'blue':
                    if num > BLUE_MAX:
                        return False
    return True



file = open('input.txt', 'r')

id_sum = 0
games = [i for i in file.readlines()]

for game in games:
    if valid_game(game.strip('\n')):
        id_sum += int(game.split(': ')[0].split(' ')[1])
    

print(f"Total sum of valid games: {id_sum}")
