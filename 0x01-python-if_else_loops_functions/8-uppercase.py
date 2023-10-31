#!/usr/bin/python3


def uppercase(str):
    for ch in str:
        ch = ord(ch)
        if (ch > 96 and ch < 123):
            ch = ch - 32
        ch = chr(ch)
        print("{}".format(ch), end='')
    print("")
