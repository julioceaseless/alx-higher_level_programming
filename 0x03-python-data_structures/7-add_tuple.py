#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    num1 = 0
    num2 = 0
    for i in tuple_a:
        if i == tuple_a[0]:
            num1 = num1 + i
        elif i == tuple_a[1]:
            num2 = num2 + i
    for j in tuple_b:
        if j == tuple_b[0]:
            num1 = num1 + j
        elif j == tuple_b[1]:
            num2 = num2 + j
    return (num1, num2)
