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
        if type(attrs) is list and all([type(attr) is str for attr in attrs]):
            attrsList = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    attrsList[key] = value
            return attrsList

        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
