#!/usr/bin/python3
"""
Class square that defines a square
by:
size(private instance attribute)
"""


class Square:
    """Initialize the class"""
    def __init__(self, size=0, position=(0, 0)):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >=0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) is not int or type(position[1]) is not int or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Define the square"""
    def area(self):
        return self.__size * self.__size

    """print in stdout the suare with character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if i == 1:
                    print("\n" * self.__position[i], end="")
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
