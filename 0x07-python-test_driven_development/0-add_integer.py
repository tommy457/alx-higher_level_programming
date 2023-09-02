#!/usr/bin/python3
"""module for add_integer"""


def add_integer(a, b=98):
    """function that adds 2 integers.
    Args:
        a (int): first integer
        b (int): second integer, default 98.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
