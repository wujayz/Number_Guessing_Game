"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random


def start_game():
    """Psuedo-code Hints
    
       
    """
    # write your code inside this function.
    player_name = input("Welcome to the number guessing game! \nWhat's your name?  ")

    upper_range = 100
    lower_range = 1
    number = random.randrange(lower_range, upper_range, 1)
    guess = input("Guess a number between the range {} and {}  ".format(lower_range, upper_range))
    tries = 1
    while number != guess:
      tries += 1
      try: 
        guess = int(guess)
        if guess > 100 or guess < 1:
          raise ValueError("You can only choose a number between {} and {}.".format(lower_range, upper_range))
          guess = input("Try again: ")
      except ValueError as err:
        print("That is not a valid value. {}".format(err))
        guess = input("Try again: ")
      else:
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
    print("Got it! It took you {} tries! ".format(tries))

       

    restart = input("The game has finished. Would you like to start again? (yes/no) ")
    if restart.lower() == "yes":
      print("Here we go again {}. See if you can break your high score of {} tries!".format(player_name, tries))
      start_game()
    else:
      print("Thank you for playing. Come again. ")
          

# Kick off the program by calling the start_game function.
start_game()
