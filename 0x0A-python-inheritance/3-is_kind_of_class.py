#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    Args:
        obj (object): object to ckeck
        a_class (class): class to check against
    """
    return isinstance(obj, a_class)
