#!/usr/bin/python3
"""Module for append_write method"""


def append_write(filename="", text=""):
    """Method that appends to a text file (UTF8)
    returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as MyFile:
        return MyFile.write(text)
