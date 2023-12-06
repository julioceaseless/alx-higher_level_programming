#!/usr/bin/python3
"""
Adds attributes if possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds attribute to object if it is possible
    """

    if hasattr(obj, '__dict__') and not callable(obj):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
