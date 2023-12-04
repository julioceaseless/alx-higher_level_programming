#!/usr/bin/python3
"""
Class inherits from list
"""


class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        """
        Print sorted list
        """
        sorted_list = self[:]
        sorted_list.sort()

        print(sorted_list)
