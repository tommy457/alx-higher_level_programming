#!/usr/bin/python3
"""Module for the Base class"""

import json


class Base:
    """Define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation
        of list_objs to a file"""
        if list_objs:
            list_objs = [instance.to_dictionary() for instance in list_objs]
        with open(str(cls.__name__) + ".json", "w") as f:
            return f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method tha returns an instance with all attributes already set"""
        if dictionary:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        try:
            with open(str(cls.__name__) + ".json", "r") as jfile:
                list_dicts = Base.from_json_string(jfile.read())
                return [cls.create(**_dict) for _dict in list_dicts]
        except IOError:
            return []
