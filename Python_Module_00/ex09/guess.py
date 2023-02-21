#!/usr/bin/env python3

import sys
from random import randint

if __name__ != "__main__":
    sys.exit()

print("This is an interactive guessing game!")
print(
    "You have to enter a number between",
    "1 and 99 to find out the secret number."
)
print("Type 'exit' to end the game.")
print("Good luck!\n")

secret = randint(1, 99)
guess = 0
count = 0


def _hint(guess: int, secret: int):
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")


while guess != secret:
    print("What's your guess between 1 and 99?")
    guess = input(">> ")

    if guess == "exit":
        print("Goodbye!")
        sys.exit()

    # count must be incremented
    # even if the guess is not a number or out of range
    count += 1

    try:
        guess = int(guess)
    except ValueError:
        print("That's not a number.")
        continue

    if guess < 1 or guess > 99:
        print("Out of range.")
        continue

    _hint(guess, secret)

if guess == 42:
    print(
        "The answer to the ultimate question of life,",
        "the universe and everything is 42."
    )
if count == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!")
    print(f"You won in {count} attempts!")
