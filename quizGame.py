import random

count = [0, 0]


def run_game():
    numbers = random.randint(1, 12), random.randint(1, 12)
    correct_answer = numbers[0] * numbers[1]
    math_check = bool(check_math(correct_answer, numbers))
    tally_score(math_check, count)
    play_again()


def check_math(correct_answer, numbers):
    user_guess = int(input('What is {} x {}? '.format(numbers[0], numbers[1])))
    if user_guess == correct_answer:
        print('That is correct!')
        return True
    else:
        print('That is incorrect...')
        return False


def tally_score(math_check, tally):
    if math_check:
        tally[0] += 1
        tally[1] += 1
    else:
        tally[1] += 1
    print('You have gotten {} questions right out of {} questions. '.format(tally[0], tally[1]))


def play_again():
    player_response = ''

    while player_response == '':
        player_response = input('Would you like to do more math? (Y/N) ').upper()
        if player_response == 'Y':
            run_game()
        elif player_response != 'N':
            player_response = ''
        else:
            print('Have a nice day!')


run_game()
