#!/usr/bin/python3


def no_c(my_string):
    my_string_cpy = ""
    for ch in my_string:
        if ch == "c" or ch == "C":
            continue
        my_string_cpy += ch
    return my_string_cpy
