#!/usr/bin/python3
"""
Create class Square based off of rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class Square inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
