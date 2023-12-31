#!/usr/bin/python3
"""
class Rectangle defines a rectangle
"""


class Rectangle:
    """ Initialize Rectangle with width and height"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter for  height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return area (L * W)"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ draw the rectangle using # """
        if self.__height == 0 or self.__width == 0:
            return ("")
        return ("\n".join((str(self.print_symbol) *
                           self.__width for i in range(self.__height))))

    def __repr__(self):
        """
        Return string representation of the rectangle
        to make it easy to use eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ print message when instance of Rectange is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
