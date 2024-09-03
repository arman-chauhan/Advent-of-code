#
# Day 2: Cube Conundrum
#


max_values = {'red': 12, 'green': 13, 'blue': 14}
valid_games = []
id_sum = 0
power_sum = 0

with open('input.txt', 'r') as file:
    games = file.read().strip().split('\n')

    for id, game in enumerate(games):
        x = game.find(' ')
        y = game.find(':')
        gameIndex = game[x:y]
        rounds = game[y + 1:].split(';')

        valid = True
        min_values = {'red': 0, 'green': 0, 'blue': 0}
        for r in rounds:
            for i in r.split(','):
                cube = i.strip().split(' ')
                if int(cube[0]) > min_values[cube[1]]:
                    min_values[cube[1]] = int(cube[0])

                if int(cube[0]) > max_values[cube[1]]:
                    valid = False
        if valid:
            id_sum += int(gameIndex)
            valid_games.append(game)

        p = 1
        for v in min_values.values():
            p *= v

        power_sum += p

list(map(print, valid_games))
print('-' * 50)
print(id_sum)
print(power_sum)
