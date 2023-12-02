#!/usr/bin/python3
"""
Module 0-add_integer.py
"""


def add_integer(a, b=98):
    """ Function adds two integers """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)
