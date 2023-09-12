#!usr/bin/python3
"""Module for add_attribute method"""


def add_attribute(obj, name, value):
    """Method adds a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
