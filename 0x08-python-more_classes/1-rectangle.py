#!/usr/bin/python3

"""Class Rectangle"""


class Rectangle:
    """Define rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of the rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width
        Args:
            value (int): value if width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height
        Args:
            value (int): value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
