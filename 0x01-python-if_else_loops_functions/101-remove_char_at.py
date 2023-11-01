#!/usr/bin/python3


def remove_char_at(str, n):
    result = ""
    count = 0
    for letter in str:
        if count == n:
            count += 1
            continue
        result += letter
        count += 1
    return result
