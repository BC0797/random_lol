import random

def players_name(number_players):
    players = []
    counter = 0
    while counter < number_players:
        players.append(input(f'Player {counter + 1}: '))
        counter += 1
    return (players)


def team_number(players):
    team_order = []
    counter = 0
    while counter < players:
        numb = random.choice(range(0,10,1))
        if numb in team_order:
            if len(team_order) == players:
                break
            else:
                continue
        else:   
            team_order.append(numb)
    counter += 1
    return(team_order)
    
def positions(players, order):
    match = []
    counter = 0
    while counter < len(players):
        position = input('Position: ')
        player_1 = players[order[counter]]
        player_2 = players[order[counter +1]]
        match.append(f'{position}: {player_1} vs {player_2}')
        print(f'{position}: {player_1} vs {player_2}')
        counter += 2
    print("")
    for element in match:
        print(element)
    return match

def run():
    number_players = 10 #int(input('Number of players: '))
    names = players_name(number_players)
    order = team_number(number_players)
    players_position_team = team_number(number_players)
    positions(names, order)
    

if __name__ == '__main__':
    run()
