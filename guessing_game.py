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
    try:
      guess = int(input("Please pick a number between 1 and 10: "))      
    except ValueError:
      print("You didn't enter a valid number")
      continue
    attempts += 1
    attempts_list.append(guess)
    if answer == guess: 
        print("You've got it! Your guess was right on target.It took you ", attempts, " attempts.")
        #attempts_list.append(attempts)
        play_again = input("Would you like to play again? (yes/no) ")
        if play_again == "yes":
          answer = random.randint(1,10)
          attempts = 0
          continue
        elif play_again == "no":
          print("No worries. Thanks for playing!")
          break
    elif answer < guess :
        print("It's lower")
        continue
    elif answer > guess : 
        print("It's higher")
        continue
    #guess = input("Your answer wasn't quite right  :( Please pick another number between 1 and 10: ")
  mean = statistics.mean(attempts_list)
  mode = statistics.mode(attempts_list)
  median = statistics.median(attempts_list)
  print(attempts_list)
  print("The number of attempts you made was ", attempts, "\nThe mean was ", round(mean),"\nThe median was ", round(median),"\nThe mode was ", round(mode))

  #print(answer)
  
    # write your code inside this function.
"""Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player. (DONE)
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    ( You can add more features/enhancements if you'd like to. )
    """


# Kick off the program by calling the start_game function.
start_game()