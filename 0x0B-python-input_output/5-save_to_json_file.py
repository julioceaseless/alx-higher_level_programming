#!/usr/bin/python3
"""
Function wites an object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    use JSON to write an Object to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_obj))
