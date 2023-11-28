#!/usr/bin/python3
"""Class LockedClass with no class or object attribute"""


class LockedClass:
    """ Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""
    __new_instance__ = ["first_name"]
