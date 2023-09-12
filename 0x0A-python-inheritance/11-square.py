#!/usr/bin/python3
"""Module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass representing a square inherits from Rectangle"""
    def __init__(self, size):
        """initialization of the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string representation of this square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
