import random  # this is the random module


# x = random.randint(1,6) this will give a random int between 1 and 6
# y = random.random() this will give a random float between 0 and 1

# myList = ['rock','paper','scissors'] you can use a list too!
# z = random.choice(myList) use the random.choice function to pull at random from a list

# cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
# random.shuffle(cards) you can shuffle items in a list as well.

# print(x)
# print(y)
# print(z)
# print(cards)

# Lets try a Rock / Paper / Scissors game!


def RPC():
    choices = ['ROCK', 'PAPER', 'SCISSORS']  # establish list of choices
    opponent_choice = random.choice(choices)  # generate opponents option
    player_choice = ''

    while player_choice not in choices:
        player_choice = input('Choose Rock, Paper, or Scissors: ').upper()
        if player_choice == opponent_choice:
            print('You chose {} and your opponent chose {}'.format(player_choice, opponent_choice))
            print('Its a DRAW!')
        elif player_choice == 'ROCK' and opponent_choice == 'SCISSORS':
            print('You chose {} and your opponent chose {}'.format(player_choice, opponent_choice))
            print('You WIN!')
        elif player_choice == 'SCISSORS' and opponent_choice == 'PAPER':
            print('You chose {} and your opponent chose {}'.format(player_choice, opponent_choice))
            print('You WIN!')
        elif player_choice == 'PAPER' and opponent_choice == 'ROCK':
            print('You chose {} and your opponent chose {}'.format(player_choice, opponent_choice))
            print('You WIN!')
        elif player_choice == 'PAPER' or player_choice == 'ROCK' or player_choice == 'SCISSORS':
            print('You chose {} and your opponent chose {}'.format(player_choice, opponent_choice))
            print('You LOSE')


def Rpc_Auto():
    i = 20
    choices = ['ROCK', 'PAPER', 'SCISSORS']  # establish list of choices
    opponent_choice = random.choice(choices)  # generate opponents option
    my_choice = ''
    win_count = 0
    loss_count = 0
    draw_count = 0
    while my_choice not in choices:
        while i > 0:
            print('You have {} wins, {} losses, and {} draws!'
                  .format(win_count, loss_count, draw_count))
            my_choice = random.choice(choices)
            if my_choice == opponent_choice:
                print('You chose {} and your opponent chose {}. ITS A DRAW!'
                      .format(my_choice, opponent_choice))
                draw_count += 1
            elif my_choice == 'ROCK' and opponent_choice == 'SCISSORS':
                print('You chose {} and your opponent chose {}. YOU WIN!'
                      .format(my_choice, opponent_choice))
                win_count += 1
            elif my_choice == 'SCISSORS' and opponent_choice == 'PAPER':
                print('You chose {} and your opponent chose {}. YOU WIN!'
                      .format(my_choice, opponent_choice))
                win_count += 1
            elif my_choice == 'PAPER' and opponent_choice == 'ROCK':
                print('You chose {} and your opponent chose {}. YOU WIN!'
                      .format(my_choice, opponent_choice))
                win_count += 1
            elif my_choice=='PAPER' or my_choice=='ROCK' or my_choice=='SCISSORS':
                print('You chose {} and your opponent chose {}. YOU LOSE!'
                      .format(my_choice, opponent_choice))
                loss_count += 1
            i -=1

def Rpc2_Auto():
    i = 20
    choices = ['ROCK', 'PAPER', 'SCISSORS']  # establish list of choices
    opponent_choice = random.choice(choices)  # generate opponents option
    my_choice = ''
    tally = {'win_count': 0, 'loss_count': 0, 'draw_count': 0}
    while my_choice not in choices:
        while i > 0:
            print(f"You have {tally['win_count']} wins, {tally['loss_count']} losses, and {tally['draw_count']} draws.")
            my_choice = random.choice(choices)
            if my_choice == opponent_choice:
                print('You chose {} and your opponent chose {}. ITS A DRAW!'.format(my_choice, opponent_choice))
                tally['draw_count'] += 1
            elif my_choice == 'ROCK' and opponent_choice == 'SCISSORS':
                print('You chose {} and your opponent chose {}. YOU WIN!'.format(my_choice, opponent_choice))
                tally['win_count'] += 1
            elif my_choice == 'SCISSORS' and opponent_choice == 'PAPER':
                print('You chose {} and your opponent chose {}. YOU WIN!'.format(my_choice, opponent_choice))
                tally['win_count'] += 1
            elif my_choice == 'PAPER' and opponent_choice == 'ROCK':
                print('You chose {} and your opponent chose {}. YOU WIN!'.format(my_choice, opponent_choice))
                tally['win_count'] += 1
            elif my_choice == 'PAPER' or my_choice == 'ROCK' or my_choice == 'SCISSORS':
                print('You chose {} and your opponent chose {}. YOU LOSE!'.format(my_choice, opponent_choice))
                tally['loss_count'] +=1
            i -=1



Rpc2_Auto()