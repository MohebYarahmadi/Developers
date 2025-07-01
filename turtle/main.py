#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: main.py
import turtle


def main():
    t = turtle.Turtle()

    # draw_junks(t)

    # stairs(t, 30, 5)
    # rectangle(t, 100, 50)
    squares(turtle=t, starting_size=10, number=50, offset=4)

    turtle.done()


def draw_junks(turtle):
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(45)


def stairs(turtle, length, steps):
    for i in range(0, steps):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        # length -= 2
    turtle.forward(length)


def rectangle(turtle, width, height):
    for i in range(0, 2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


def square(turtle, size):
    for i in range(0, 4):
        turtle.forward(size)
        turtle.left(90)


def squares(turtle, starting_size, number, offset=0):
    for i in range(0, number):
        size = (i + 1) * starting_size
        # turtle.forward(size)
        # turtle.left(90)
        square(turtle, size)
        turtle.left(offset)


if __name__ == "__main__":
    main()
