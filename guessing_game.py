"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random


def start_game():
    """Psuedo-code Hints
    
    1. Make sure no errors happen (non-number guesses)
    2. Errors for numbers out of the range 
    3. Add Restart option at end of game: would you like to play again?
    - if no: show a closing message
    - if yes: "Here we go again! Try to beat ____"
    4. Show Current Score when playing again
    ---> if high score gets beaten: congratulate
    5. random number has to get updated everytime. 

    
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
