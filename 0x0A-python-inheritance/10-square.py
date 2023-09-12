#!/usr/bin/python3
"""Module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass representing a square that inherits from rectangle"""
    def __init__(self, size):
        """initialization of the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
