#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_dict = a_dictionary.copy()
    for key, val in my_dict.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
