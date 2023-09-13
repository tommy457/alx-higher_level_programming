#!/usr/bin/python3
"""Module for append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """Method that inserts a line of text to a file,
    after each line containing a specific string"""
    text = ""
    with open(filename) as MyFileRead:
        for line in MyFileRead:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as MyFileWrite:
        MyFileWrite.write(text)
