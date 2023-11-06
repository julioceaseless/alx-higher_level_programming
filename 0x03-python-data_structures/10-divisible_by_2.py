#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    status=[]

    for num in my_list:
        if num % 2 == 0:
            status.append(True)
        else:
            status.append(False)
    return status
