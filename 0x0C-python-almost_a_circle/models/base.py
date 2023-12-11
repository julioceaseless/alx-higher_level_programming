#!/usr/bin/python3
"""
Create a clas Base
"""
import json


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
        """Initialize the Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of an object (string)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json string representation of object to a file
        """
        list_dicts = []
        filename = f"{cls.__name__}.json"
        if list_objs is not None:
            for each_class in list_objs:
                if isinstance(each_class, cls):
                    list_dicts.append(each_class.to_dictionary())
        with open(filename, mode='w') as filename:
            filename.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This class method returns an instance with all
        attributes already set
        """
        cls_list = ['Square', 'Rectangle']
        if cls.__name__ == cls_list[0]:
            dummy = cls(2)
        if cls.__name__ == cls_list[1]:
            dummy = cls(1, 2)
        if cls.__name__ in cls_list:
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances
        """
        try:
            filename = f"{cls.__name__}.json"
            with open(filename, mode="r") as filename:
                data = filename.read()
                list_dicts = cls.from_json_string(data)
                new_list = []
                for dicts in list_dicts:
                    new_list.append(cls.create(**dicts))
                return new_list
        except FileNotFoundError:
            return []
