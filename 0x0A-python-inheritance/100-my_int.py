#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """Custam MyInt class"""
    def __eq__(self, other):
        """Equals == inverted"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Not-equals != inverted"""
        return int(self) == int(other)
