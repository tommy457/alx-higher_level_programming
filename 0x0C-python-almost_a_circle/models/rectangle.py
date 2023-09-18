#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Subclass representing a rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width att"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width att"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height att"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height att"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x att"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x att"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y att"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y att"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method that returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Method that prints in stdout the
        Rectangle instance with the character #
        """
        for col in range(self.y):
            print("")
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Method that gns an argument to each attribute"""
        if args:
            self.update_helper(*args)
        elif kwargs:
            self.update_helper(**kwargs)

    def update_helper(self, id=None, width=None, height=None, x=None, y=None):
        """Helper method to work with *args and **kwargs"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }

    def __str__(self):
        """Returns the user readable string form of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
