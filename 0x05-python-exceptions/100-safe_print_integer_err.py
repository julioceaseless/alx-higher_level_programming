#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as vt:
        sys.stderr.write("Exception: " + str(vt) + '\n')
        return False
    return True
