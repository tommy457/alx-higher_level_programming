#!/usr/bin/python3

def is_same_class(obj, a_class):
    """function that returns True if the object is 
    exactly an instance of the specified class ; otherwise False
    Args:
        obj (object): object to be cheked
        a_class (class): class to check against
    """
    return type(obj) ==  a_class
