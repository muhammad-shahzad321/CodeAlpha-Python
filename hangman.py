"""
CodeAlpha Internship - Task 1: Hangman Game
A simple text-based Hangman game.
"""

import random

# Small list of 5 predefined words
WORDS = ["python", "internship", "program", "keyboard", "developer"]

MAX_WRONG = 6  # maximum incorrect guesses allowed


def show_status(word, guessed_letters, wrong_count):
    """Print the current word progress, guessed letters and lives left."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "none")
    print(f"Wrong guesses: {wrong_count}/{MAX_WRONG}")


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_count = 0

    print("=" * 35)
    print("       WELCOME TO HANGMAN")
    print("=" * 35)
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.")

    while wrong_count < MAX_WRONG:
        show_status(word, guessed_letters, wrong_count)

        # Win check: all letters of the word are guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            return

        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_count += 1
            print(f"Wrong! '{guess}' is not in the word.")

    # Loop ended because wrong guesses reached the limit
    print(f"\nGame over! You lost. The word was: {word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()