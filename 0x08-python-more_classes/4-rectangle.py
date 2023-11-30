#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """ initialize class Rectangle with dimensions """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ return the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ print the rectangle with character # """
        if self.__height == 0 or self.__width == 0:
            return ("")
        return("\n".join(("#" * self.__width for i in range(self.__height))))
    def __repr__(self):
        """
        return a representation of the object to make it possible
        to use eval
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
