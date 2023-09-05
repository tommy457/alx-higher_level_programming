#!/usr/bin/python3
"""Module for text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args:
        text (str): text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ".:?"
    for char in chars:
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
    print(text, end="")
