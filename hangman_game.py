# -*- coding: utf-8 -*-
"""hangman game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Cwzi0U74TbDd3kw8NPZM98DMMPZwnh8
"""

#Hangman in python

import random
def choose_word():

       words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

       return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play():
    word = choose_word()
    guessed = []
    tries = 6
    print("Let's play Hangman!")

    while tries > 0:
        print(display_hangman(tries))
        print(f'Word: {" ".join([letter if letter in guessed else "_" for letter in word])}')
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess not in word:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
        else:
            print("Hoorey! Good guess!")

        if all(letter in guessed for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(display_hangman(tries))
        print(f"Sorry, you ran out of tries. The word was: {word}")

if __name__ == "__main__":
    play()