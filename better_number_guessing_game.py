#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program creates a better number guessing game

import random


def main():
    # this function creates the game

    # input
    number_guessed = int(input("Enter the number between 0 - 9: "))

    # process
    random_number = random.randint(0, 9)  # a number between 0 and 9
    if number_guessed == random_number:
        print("You guessed correct!")
    else:
        print("Incorrect, the number was {0}".format(random_number))

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
