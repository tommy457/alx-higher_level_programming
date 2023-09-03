#!/usr/bin/python3
"""Module for print_square"""


def print_square(size):
    """function that prints square with the character #
    Args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

