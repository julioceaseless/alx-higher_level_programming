#!/usr/bin/python3
"""
The function appends text
"""


def append_write(filename="", text=""):
    """
    Function appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        chars_appended = myFile.write(text)
    return chars_appended
