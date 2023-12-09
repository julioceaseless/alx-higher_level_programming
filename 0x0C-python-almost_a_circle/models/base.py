#!/usr/bin/python3
"""
Create a clas Base
"""


class Base:
    """
    Base class for creating objects with unique identifiers

    Attributes:
    __nb_objects(int): a class attribute to keep track of the nunber of
    created objects

    Methods:
    __init__(self, id=None): initializes a Base object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
