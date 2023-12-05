#!/usr/bin/python3
"""
Call class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle inherits from Geometry"
    """

    def __init__(self, width, height):
        """
        Initialize the dimensions of rectangle and validate value
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
