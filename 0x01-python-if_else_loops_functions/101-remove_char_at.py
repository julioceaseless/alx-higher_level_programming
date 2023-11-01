#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    count = -1
    for letter in str:
        count = count + 1
        if count == n:
            count += 1
            continue
        result += letter
    return result
