#!/usr/bin/python3
"""
Function creates an Object from JSON file
"""


import json


def load_from_json_file(filename):
    """
    function
    """
    with open(filename) as myFile:
        return json.load(myFile)
