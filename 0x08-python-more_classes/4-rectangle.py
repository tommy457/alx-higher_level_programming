#!/usr/bin/python3

"""Class Rectangle"""


class Rectangle:
    """Define rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of the rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width
        Args:
            value (int): value if width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height
        Args:
            value (int): value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that return the area of the current rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that retuens the perimeter of the current rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """'Create a new string object from the given object"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = []
        for i in range(self.__height):
            rec.append("#" * self.__width)
            if i != self.__height - 1:
                rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        """Return the canonical string representation of the object"""
        return f"Rectangle({self.__width}, {self.__height})"
