# hangman-game

This Python script, hangman_game.py, is a console-based implementation of the classic word-guessing game, Hangman. The player attempts to guess a hidden word by suggesting letters within a limited number of tries.

# Features
Word Selection: The game selects a random word from a predefined list of words.
Player Guessing: The player guesses letters, and the script checks if the guessed letter is in the word.
Game State Tracking: Tracks and displays the current progress (letters guessed correctly, letters still hidden) and the number of attempts remaining.
Win/Loss Condition: The game ends when the player either guesses the word or runs out of attempts.

# Prerequisites
This script requires Python 3. There are no external dependencies, so you can run it directly.

# Usage
Run the Script:

python hangman_game.py

Gameplay:
The script will display the hidden word as a series of underscores _ representing each letter.
The player enters one letter per turn to guess a letter in the word.
If the letter is correct, it replaces the corresponding underscores.
If incorrect, the number of attempts remaining decreases.

Game End:
The game will announce if the player has guessed the word correctly or if they have run out of attempts, displaying the full word at the end.

# Customization
Word List: To modify the list of words, locate the predefined list in the script and add or remove words as desired.

# Game Rules
The player wins by guessing all letters in the word within the allowed attempts.
The player loses if they run out of attempts without guessing the entire word.
