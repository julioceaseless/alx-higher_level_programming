#!/usr/bin/python3
"""
The function appends text
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myFile:
        chars_appended = myFile.write(text)
    return chars_appended
