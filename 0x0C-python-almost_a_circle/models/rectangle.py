#!/usr/bin/python3
"""
Create a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
    __width (int): Width of the rectangle.
    __height (int): Height of the rectangle.
    __x (int): X-coordinate of the top-left corner.
    __y (int): Y-coordinate of the top-left corner.
    id (int): Unique identifier for the rectangle.

    Methods:
    __init__(self, width, height, x=0, y=0, id=None): Initialize
    a Rectangle object.
    width (int): Getter and setter for the width attribute.
    height (int): Getter and setter for the height attribute.
    x (int): Getter and setter for the x attribute.
    y (int): Getter and setter for the y attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.
        Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): X-coordinate (default is 0)
        y (int, optional): Y-coordinate(default is 0).
        id (int, optional): Unique identifier (default is None).
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for the x coordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y coordinate"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area"""
        return (self.width * self.height)

    def display(self):
        """draw the rectangle using #"""
        for units in range(self.y):
            print("")
        for h in range(self.height):
            for w in range((self.width + self.x)):
                if w < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        """magic str method to print text represenation of rect"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        assigns argument to each attribute using *args
        Args:
        *args: variables are in the order (width, height, x, y)

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle.

        Returns:
        dict: A dictionary containing the attributes of the Rectangle.
        """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
