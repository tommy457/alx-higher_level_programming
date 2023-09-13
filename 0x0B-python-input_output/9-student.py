#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Define student"""
    def __init__(self, first_name, last_name, age):
        """Constrator"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a Student instance
        """
        return self.__dict__.copy()
