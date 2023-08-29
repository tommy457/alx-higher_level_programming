#!/usr/bin/python3

"""Class square"""


class Square:
    """Define square"""

    def __init__(self, size=0):
        """initialization of new square
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
        """Return square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Return == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return >= compmarison to a Square."""
        return self.area() >= other.area()
