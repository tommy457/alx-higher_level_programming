#!/usr/bin/python3

"""Class square"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """initialization of a new square
        Args:
            size (int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting value of size
        Args:
            value (int): value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
