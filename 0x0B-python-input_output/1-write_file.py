#!/usr/bin/python3
"""
Writes text to a file
"""


import os


def write_file(filename="", text=""):
    """
    this function writes text to a file and returns
    the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        chars_written = myFile.write(text)
    return chars_written
