
from random import randrange

#Helper Functions

def number_guess_game() -> int:
    '''A function that asks the user to provide a number between 0 and 10 to initiate a game.'''
    user_guess = int(input('Can you guess my number between 1 and 10?\n'))
    return user_guess


def random_number_generator() -> int:
    '''function to generate and return a number'''
    return randrange(10)


def number_comparison(random_number, user_guess):
    '''function to compare number to guess and provide feedback'''
    if random_number > user_guess:
        print('My number was ' + str(random_number) + '. ' + str(user_guess) + ' was too low!\n')
    elif random_number < user_guess:
        print('My number was ' + str(random_number) + '. ' + str(user_guess) + ' was too high!\n')
    elif random_number == user_guess:
        print('My number was ' + str(random_number) + '. ' + str(user_guess) + ' was correct!\n')


def main():
    '''Main function calls the helpers in order'''
    random_number = random_number_generator()
    user_guess = number_guess_game()
    number_comparison(random_number, user_guess)

main()

