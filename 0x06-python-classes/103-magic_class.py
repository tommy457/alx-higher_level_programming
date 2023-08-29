#!/usr/bin/python3

"""Class of MagicClass"""

import math


class MagicClass:
    """Define a circle."""

    def __init__(self, radius=0):
        """Initialization of MagicClass.
        Arg:
            radius (float or int): radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the current MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return The circumference of the current MagicClass."""
        return 2 * math.pi * self.__radius
