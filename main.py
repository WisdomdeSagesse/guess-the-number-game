#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random as rd
from replit import clear
from art import logo

def compare_guess(rand_guess):
  guess_num = int(input("Make a guess: "))
  output = ""
  if guess_num < rand_guess:
    output = "too low"
  elif guess_num > rand_guess:
    output = "too high"
  else:
    output = "you have guessed correctly"
  print(output)
  return output

def play_game():
  #print(logo)
  random_guess = rd.randint(1, 101)
  print("Welcome to the Number Guessing Game.")
  print("I am thinking of a number between 1 and 100")
  difficulty_level = input("Choose a difficulty level. Enter 'e' for easy or 'h' for hard': ").lower()
  number_of_attempts = 0
  while difficulty_level != 'h' and difficulty_level != 'e':
      difficulty_level = input("You have entered an incorrect option. Enter 'e' for easy or 'h' for hard': ").lower()
  if difficulty_level == 'e':
      number_of_attempts = 10
  elif difficulty_level == 'h':
      number_of_attempts = 5
  print(f"You have {number_of_attempts} attempts")
  end_game = False
  while not end_game:
    guess_outcome = compare_guess(random_guess)
    if guess_outcome != "you have guessed correctly":
      number_of_attempts -= 1
      print(f"You have {number_of_attempts} attempts left")
      if number_of_attempts == 0:
          print("you are out of guesses")
          print(f"the correct guess was {random_guess}")
          end_game = True
    else:
      end_game = True
  play_again = input("Do you want to play again? Enter 'y' for yes and 'n' for no: ").lower()
  while play_again != 'y' and play_again != 'n':
    play_again = input("You have entered an incorrect option. Enter 'y' for yes and 'n' for no: ").lower()
  if play_again == 'y':
    clear()
    play_game()
  else:
    print("Game Over")


play_game()

