#!/usr/bin/python3
"""
Creates a class MyInt that inherits from int:

    *MyInt is a rebel. MyInt has == and != operators inverted
    *You are not allowed to import any module
"""


class MyInt(int):
    """
    This class has inverted operators
    """
    def __eq__(self, other):
        """
        Inverts == to !=
        """
        return False

    def __ne__(self, other):
        """
        inverts != to ==
        """
        return True
