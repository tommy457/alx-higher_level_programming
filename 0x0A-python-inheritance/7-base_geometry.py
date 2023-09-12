#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """Define BaseGeometry"""
    def area(self):
        """Method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value
        Args:
            name: (str): name
            value (int): value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("name> must be greater than 0")
