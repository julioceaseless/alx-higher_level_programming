#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        A list of strings representing the available attributes and methods.
    """
    available_members = [member for member in dir(obj)]
    return available_members
