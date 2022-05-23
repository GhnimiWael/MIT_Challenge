#!/usr/bin/env python3

"""
Hangman Game
Computer picks a word from a list
Player makes a guess one letter at a time
"""

import random

# Constants

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Words from the given list of strings
WORDS = open("words.txt", 'r')

# Max length of the Hangman
MAX_WRONG = len(HANGMAN) - 1

# Turn a list of words into a data structure
data = []
for line in WORDS:
    data = line.split()

# Initialize variables

# Pick a word
word = random.choice(data)

# Dashes for each letter in word
current_guess = "-" * len(word)
print (current_guess)

# Wrong guess counter
wrong_guess = 0

# Used Letters Tracker
used_letters = []

# Main Loop
print("Welcome to the Hangman")
print("Try to guess the word")

while wrong_guess < MAX_WRONG and current_guess != word:
    print(HANGMAN[wrong_guess])
    print("You have used to the following letters:", used_letters)
    print("So far, the word is: ", current_guess)

    guess = input("Enter your letter guess: ")
    guess = guess.lower() # Example: TowEr --> tower

    # Check if letter was already used
    while guess in used_letters:
        print("You have already guessed that letter", guess)
        guess = input("Enter you letter guess: ")
        guess = guess.lower()

    # Add new guess to the list of guessed letters
    used_letters.append(guess)

    # Check guess
    if guess in word:
        print("You have guessed correctly!")

        # Give a new version of the word with mixed letters and dashes
        new_current_guess = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]
        
        current_guess = new_current_guess
    else:
        print("Soory that was incorrect")
        # Increase the numbero f incorrect by 1
        wrong_guess += 1

# End of the Game
if wrong_guess == MAX_WRONG:
    print(HANGMAN[wrong_guess])
    print("You have been hanged!")
    print("The correct word is", word)

else:
    print("You have won!")


