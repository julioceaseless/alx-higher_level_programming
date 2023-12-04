#!/usr/bin/python3
"""
Checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    return true if an object is exactly an instance
    of the specified class
    """
    return type(obj) is a_class
