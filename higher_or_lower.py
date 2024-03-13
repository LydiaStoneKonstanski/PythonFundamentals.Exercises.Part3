#A function that asks the user to provide a number between 0 and 10.
from random import randrange

#Helper Functions
#function to intitiate game
def number_guess_game():
    user_guess = int(input('Can you guess my number between 1 and 10?\n'))
    return user_guess

#function to generate and return a number
def random_number_generator():
    return randrange(10)

#function to compare number to guess and provide feedback
def number_comparison(random_number, user_guess):
    if random_number > user_guess:
        print('My number was ' + str(random_number) + '. ' + str(user_guess) + ' was too low!\n')
    elif random_number < user_guess:
        print('My number was ' + str(random_number) + '. ' + str(user_guess) + ' was too high!\n')
    elif random_number == user_guess:
        print('My number was ' + str(random_number) + '. ' + str(user_guess) + ' was correct!\n')

#Main function calls the helpers in order
def main():
    random_number = random_number_generator()
    user_guess = number_guess_game()
    number_comparison(random_number, user_guess)

#calls main to run the program
main()

