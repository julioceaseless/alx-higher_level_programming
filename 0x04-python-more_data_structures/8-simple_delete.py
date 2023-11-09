#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    target_key = str(key)
    if target_key in a_dictionary:
        a_dictionary.pop(target_key)
    return a_dictionary
