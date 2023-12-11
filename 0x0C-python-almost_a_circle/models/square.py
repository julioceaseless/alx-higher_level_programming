#!/usr/bin/python3
"""
Square class, inherits from Rectangle.

Attributes:
width (int): Width of the square.
height (int): Height of the square.
x (int): X-coordinate of the top-left corner.
y (int): Y-coordinate of the top-left corner.
id (int): Unique identifier for the square.

Methods:
__init__(self, size, x=0, y=0, id=None): Initialize a Square object.
size (int): Getter and setter for the size attribute.
update(self, *args, **kwargs): Update attributes using a variable
number of arguments and key-value pairs.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.
        Args:
        size (int): Size of the square.
        x (int, optional): X-coordinate of the top-left corner
        y (int, optional): Y-coordinate of the top-left corner
        id (int, optional): Unique identifier (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.height

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes using a variable number of arguments
        and key-value pairs.
        Args:
        *args: Variable number of arguments in the order (size, x, y).
        **kwargs: Variable number of key-value pairs representing attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        return the text representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """
        return a dictionary representation of a square
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
