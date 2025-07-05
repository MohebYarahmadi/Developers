#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: main.py
import random


def main():
    MIN = 1
    MAX = 10
    MAGIC_NUMBER = random.randint(MIN, MAX)
    LIVES = 4
    win = False
    for i in range(0, LIVES):
        lives = LIVES - i
        print(f"You have {lives} lives.")
        user_input = ask_number(MIN, MAX)
        if user_input > MAGIC_NUMBER:
            print("The magic number is less than your guess.")
        elif user_input < MAGIC_NUMBER:
            print("The magic number is greater than you quess.")
        elif user_input == MAGIC_NUMBER:
            print("Greate job, you won!")
            win = True
            break
    if not win:
        print(f"You lost! The magic number was: {MAGIC_NUMBER}")


def ask_number(min, max):
    number = 0
    while number == 0:
        user_input = input(
            f"What is the magic number (between {min} and {max}): ")
        try:
            number = int(user_input)
        except ValueError:
            print("Please enter integer.")
        else:
            if number < min or number > max:
                print(f"Error: enter number between {min} - {max} please.")
                number = 0
    return number


if __name__ == "__main__":
    # If this script is run directly, call the main function
    main()
