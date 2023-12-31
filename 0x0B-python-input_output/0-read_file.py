#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=""):
    """Method that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode="r", encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
