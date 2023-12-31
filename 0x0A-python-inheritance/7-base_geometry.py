#!/usr/bin/python3
"""
Creates an empty class
"""


class BaseGeometry:
    """
    this is an empty class
    """

    def area(self):
        """
        area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the values
        """

        if type(value) is not int:
            raise TypeError ("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
