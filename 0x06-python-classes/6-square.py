#!/usr/bin/python3

"""Class square"""


class Square:
    """Define square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of a new square
        Args:
            size (int): size of new square
            position (int, int): position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrive size of the current square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("ze must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the current square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the position of the aquare"""
        if not all([
                isinstance(value, tuple),
                len(value) == 2,
                all([isinstance(val, int) for val in value]),
                all([val >= 0 for val in value])]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the current square"""
        return self.__size ** 2

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size, end='')
                print()
