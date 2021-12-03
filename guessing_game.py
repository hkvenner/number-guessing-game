"""
Project 1 - Number Guessing Game
--------------------------------
"""

import random, statistics


def start_game():
  print("Hi there. You're about to play an epic Word Guessing Game.")
  answer = random.randint(1,100)
  attempts = 0
  attempts_list = []
  
  while True:
    try:      
      guess = int(input("Please pick a number between 1 and 100: "))
      if (guess < 1) or (guess > 100):
        print("Your number was out of the desired range")
        continue
    except ValueError:
      print("You didn't enter a valid number")
      continue
    attempts += 1
    
    if answer == guess: 
        print("You've got it! Your guess was right on target.It took you {} attempts.".format(attempts))
        attempts_list.append(attempts)
        play_again = input("Would you like to play again? (yes/no) ")
        if play_again.lower() == "yes":
          print("The number of least guesses (i.e the goal you are trying to beat) is {}".format(min(attempts_list)))
          answer = random.randint(1,100)
          attempts = 0
          continue
        elif play_again.lower() == "no":
          print("No worries. Thanks for playing!")
          break
    elif answer < guess :
        print("It's lower")
        continue
    elif answer > guess : 
        print("It's higher")
        continue
        
  mean = statistics.mean(attempts_list)
  mode = statistics.mode(attempts_list)
  median = statistics.median(attempts_list)
  print(attempts_list)
  print("The number of attempts you made was {} attempts.".format(attempts))
  print("The mean was {}.".format(round(mean)))
  print("The median was {}.".format(round(median)))
  print("The mode was {}.".format(round(mode)))

start_game()