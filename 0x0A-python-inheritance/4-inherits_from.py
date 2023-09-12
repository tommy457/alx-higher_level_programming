#!/usr/bin/python3

def inherits_from(obj, a_class):
    """"function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise Fals.
    Args:
        obj (object): object to check
        a_class (class): class to check against
    """
    return isinstance(obj, a_class) and type(obj) != a_class
