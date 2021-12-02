"""
Project 1 - Number Guessing Game
--------------------------------
"""

import random, statistics


def start_game():
  print("Hi there. You're about to play an epic Word Guessing Game.")
  answer = random.randint(1,10)
  attempts = 0
  attempts_list = []
  
  while True:
    guess = input("Please pick a number between 1 and 10: ")
    guess = int(guess)
    attempts += 1
    if answer == guess: 
      print("You've got it! Your guess was right on target.It took you ", attempts, " attempts.")
      attempts_list.append(attempts)
      play_again = input("Would you like to play again? (yes/no) ")
      if play_again == "yes":
        answer = random.randint(1,10)
        attempts = 0
        continue
      elif play_again == "no":
        break
    elif answer < guess :
      print("It's lower")
    elif answer > guess : 
      print("It's higher")
  mean = statistics.mean(attempts_list)
  mode = statistics.mode(attempts_list)
  median = statistics.median(attempts_list)
  print("The number of attempts was ", attempts, "\nThe mean was ", round(mean),"\nThe median was ", round(median),"\nThe mode was ", round(mode))

# Kick off the program by calling the start_game function.
start_game()