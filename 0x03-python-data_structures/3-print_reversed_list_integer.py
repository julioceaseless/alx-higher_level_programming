#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    items = len(my_list)
    for n in range(1, items + 1):
        print("{:d}".format(my_list[-n]))
