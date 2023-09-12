#!/usr/bin/python3
"""Module for Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass representing a rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialization of the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that return the area of the current rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print a string represantation od the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
