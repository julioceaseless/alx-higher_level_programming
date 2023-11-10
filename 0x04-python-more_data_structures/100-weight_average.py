#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        dividend = sum(s * w for s, w in my_list)
        divisor = sum(w for s, w in my_list)
        return (dividend/divisor)
    return (0)
