#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: main.py

def main():
    MAGIC_NUMBER = 5
    MIN = 0
    MAX = 10
    LIVES = 4
    for i in range(0, LIVES):
        user_input = ask_number(MIN, MAX)
        if user_input > MAGIC_NUMBER:
            print("The magic number is less than your guess.")
            LIVES -= 1
            print(f"{LIVES} lives left.")
        elif user_input < MAGIC_NUMBER:
            print("The magic number is greater than you quess.")
            LIVES -= 1
            print(f"{LIVES} lives left")
        elif user_input == MAGIC_NUMBER:
            print("Greate job, you won!")
            break

def ask_number(min, max):
    user_input = input(f"What is the magic number (between {min} and {max}): ")
    number = int(user_input)
    return number


if __name__ == "__main__":
    # If this script is run directly, call the main function
    main()
