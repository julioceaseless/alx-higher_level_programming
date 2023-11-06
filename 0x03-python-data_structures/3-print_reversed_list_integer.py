#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    items = len(my_list)
    while items > 0:
        print("{:d}".format(my_list[items - 1]))
        items -= 1
