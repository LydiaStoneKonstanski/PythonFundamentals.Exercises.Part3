#Helper Functions

#Function prompts for language
def request_language_input():
    user_choice = int(input('For English press 1.\n' + 'Para español, marca 2. \n' + 'Pour le française, appuyez 3.'))
    return user_choice

#function prompts for name in chosen language
def name_prompt(user_choice):
    if user_choice == 1:
        name = input('What is your name?')
        return name
    elif user_choice == 2:
        name = input('Como se llama?')
        return name
    elif user_choice == 3:
        name = input('Comment vous appelez-vous?')
        return name
    else:
        print('I am sorry, I do not understand your choice.')

#greet recieves the name from name_input and prints it with a greeting
def multilingual_greet(name, user_choice):
    if user_choice == 1:
        print('Hi ' + name + '!')
    elif user_choice == 2:
        print('Hola ' + name + '!')
    elif user_choice == 3:
        print('Bonjour ' + name + '!')
    return

#Main function calls the helpers in order
def main():
    user_choice = request_language_input()
    name = name_prompt(user_choice)
    multilingual_greet(name, user_choice)

#calls main to run the program
main()


