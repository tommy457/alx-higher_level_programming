#!/usr/bin/python3
"""Module for class_to_json method."""


def class_to_json(obj):
    """Method that returns dictionary description of json object."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
