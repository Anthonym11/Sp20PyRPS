import random

symbols = ['rock', 'paper', 'scissors']

player_wins = 0
computer_wins = 0

while max([player_wins, computer_wins]) < 3:
    player_symbol = None
    while player_symbol is None:
        input_symbol = input("What symbol do you want?")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print('Haha, thats funny. Just pick rock, paper, or scissors to play the game.')

    computer_symbol = random.choice(symbols)

    print('player: ', player_symbol)
    print('computer:', computer_symbol)
    
    if player_symbol == computer_symbol:
        print('TIE!')
    elif player_symbol == 'rock':
        if computer_symbol == 'paper':
            print('COMPUTER WINS!')
            computer_wins += 1
        else:
            print('PLAYER WINS!')
            player_wins += 1
    elif player_symbol == 'scissors':
        if computer_symbol == 'rock':
            print('COMPUTER WINS')
            computer_wins += 1
        else:
            print('PLAYER WINS')
            player_wins += 1
    elif player_symbol == 'paper':
        if computer_symbol == 'scissors':
            print('COMPUTER WINS')
            computer_wins += 1
        else:
            print('PLAYER WINS')
            computer_wins += 1

    print('Player wins: ')
    print(player_wins)
    print('Computer wins: ')
    print(computer_wins)
