#!/usr/bin/python3
"""
create a pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal's triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1]]  # initialize first row with 1

    # iterate for remaining rows
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]  # initialize new row with 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # add 1 to the end
        triangle.append(new_row)
    return triangle
