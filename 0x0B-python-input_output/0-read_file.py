#!/usr/bin/python3
"""
Read a text file (UTF8)
"""


def read_file(filename=""):
    """
    reads a text file and prints it to stdout
    Uses with to close the file automatically
    """
    with open(filename, encoding="utf-8") as myFile:
        content = myFile.read()
        print(content, end="")
