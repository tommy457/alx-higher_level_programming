#!/usr/bin/python3
"""Module for printing name"""


def say_my_name(first_name, last_name=""):
    """print first and last name
    Args:
        first_name (str): first name
        last_name (str): last name, default=""
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
