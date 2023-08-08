#!/usr/bin/python3

def remove_char_at(str, n):

    if n >= 0:
        char = ""
        for i in range(0, len(str)):
            if n != i:
                char += str[i]
        return char
    return str
