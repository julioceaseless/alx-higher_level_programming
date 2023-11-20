#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    items = 0
    try:
        while (items < x):
            print("{}".format(my_list[items]), end="")
            items = items + 1
        print()
    except Exception:
        print()
    return (items)
