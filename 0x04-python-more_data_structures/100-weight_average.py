#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    divisor = 0
    dividend = 0
    quotient = 0

    list_len = len(my_list)
    for i in range(list_len):
        dividend += my_list[i][0] * my_list[i][1]
        divisor += my_list[i][1]
    quotient = dividend / divisor
    return quotient
