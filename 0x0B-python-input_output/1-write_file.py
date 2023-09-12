#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """Method that writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as MyFile:
        return MyFile.write(text)
