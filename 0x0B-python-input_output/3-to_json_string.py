#!/usr/bin/python3
"""
Write json.
Uses json's dump string fuction to translate a python
value into a string of json formated data
"""


import json

def to_json_string(my_obj):
    """
    Function that returns the JSON representation
    of an object (string)
    """

    return json.dumps(my_obj)
