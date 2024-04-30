# Guess-the-number

This Python script implements a simple number guessing game where the player has to guess a randomly generated 4-digit number within a limited number of attempts.

## Getting Started
To start the game, simply run the script in a Python environment. Follow the on-screen instructions to play the game.

## Instructions
1. The player has 10 chances to guess a randomly generated 4-digit number.
2. After each guess, the game provides feedback on how many digits are in the correct position.
3. The game ends when the player correctly guesses the number or runs out of chances.
4. At the end of the game, the correct number is revealed, and the player can choose to play again.

## Usage
```
run the executable file
```

## Implementation Details
The script uses the random module to generate a random 4-digit number for the player to guess.
Regular expressions (re module) are used to validate user input to ensure it consists of exactly 4 digits.
The generate_random_number function generates a random 4-digit number as a string.
The get_user_input function prompts the user for input and validates it using a regular expression pattern.
The check_guess function compares the user's guess with the randomly generated number and provides feedback on the correctness of the guess.
The play_game function controls the main game loop, allowing the player to make multiple guesses until they either guess the correct number or run out of chances.
The main function serves as the entry point of the script, allowing the player to play the game multiple times if desired.
