#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        sys.stderr.write("Exception: " + str(ve) + '\n')
        return False
    return True
