"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    player_name = input("Welcome to the number guessing game! \nWhat's your name?  ")

    upper_range = 100
    lower_range = 1
    number = random.randrange(lower_range, upper_range, 1)
    guess = input("Guess a number between the range {} and {}  ".format(lower_range, upper_range))
    trys = 1
    guess = int(guess)
    while number != guess:
      trys += 1
      if number < guess:
        print("It's lower")
        guess = input("Try again: ")
        guess = int(guess)
      elif number > guess:
        print("It's higher")
        guess = input("Try again: ")
        guess = int(guess)
      elif number == guess:
        break
    
    print("Got it! It took you {} tries! ".format(trys))
    


# Kick off the program by calling the start_game function.
start_game()
