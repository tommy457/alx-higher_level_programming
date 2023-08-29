#!/usr/bin/python3

"""Class square"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """initialization of new square
        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return square area"""
        return self.__size ** 2
