import random

print("Hi welcome to the Guessing Game!, This is a number guessing game.\nYou got 8 chances to guess the number. Let's start the game")

number_to_guess = random.randrange(100)

chances = 8

guess = 0

while guess < chances:

    guess += 1
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
        break

    elif guess >= chances and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    elif my_guess > number_to_guess:
        print('Too high! Try again. ')

    elif my_guess < number_to_guess:
        print('Too Low! Try again ')
