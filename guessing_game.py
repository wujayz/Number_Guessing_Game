import random


def start_game():
  upper_range = 100
  lower_range = 1
  number = random.randrange(lower_range, upper_range, 1)
  guess = input("Guess a number between the range {} and {}. ".format(
      lower_range, upper_range))
  tries = 0

  while number != guess:
    tries += 1
    error = guess.isdigit()
    if error != True:
      guess = input("You have entered a word. Enter a number ")
    elif int(guess) > upper_range or int(guess) < lower_range:
      guess = input("You can only choose a number between {} and {}. \nTry again. ".format(
          lower_range, upper_range))
    elif number < int(guess):
      print("It's lower")
      guess = input("Try again: ")
    elif number > int(guess):
      print("It's higher")
      guess = input("Try again: ")
    else:
        break
  print("Got it! It took you {} tries! ".format(tries))

  restart = input(
      "The game has finished. Would you like to start again? (yes/no) ")
  if restart.lower() == "yes":
    print("Here we go again {}. See if you can break your high score of {} tries.".format(
        player_name, tries))
    start_game()
  else:
    print("Thank you for playing. Come again. ")


player_name = input("Welcome to the number guessing game. What's your name?  ")
start_game()
