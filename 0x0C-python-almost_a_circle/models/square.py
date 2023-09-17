#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Subclass representing a square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constractor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for the size of the current instance of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the curretnt inctance of Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that that assigns attributes."""
        if args:
            self.update_helper(*args)
        elif kwargs:
            self.update_helper(**kwargs)

    def update_helper(self, id=None, size=None, x=None, y=None):
        """Helper method to work with *args and **kwargs"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    
    def to_dictionary(self):
        """Method that returns the dictionary representation of a Square"""
        return {"id":self.id, "x":self.x, "size":self.size, "y":self.y}

    def __str__(self):
        """Returns the user readable string form of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
