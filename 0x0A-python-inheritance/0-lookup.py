#!/usr/bin/python3
"""
Function returns a list
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    available_members = [member for member in dir(obj)]
    return available_members
