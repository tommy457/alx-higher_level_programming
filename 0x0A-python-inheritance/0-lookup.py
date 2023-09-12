#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """function that returns the list of
    available attributes and methods of an object
    Args:
        obj (object):
    """
    return dir(obj)
