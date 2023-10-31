#!/usr/bin/python3


def remove_char_at(str, n):
    count = -1
    for letter in str:
        count = count + 1
        if count == n:
            continue
        print("{}".format(letter), end='')
