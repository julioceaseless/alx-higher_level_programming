#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for r in range((len(matrix))):
        for c in range((len(matrix[0]))):
            if c != len(matrix[0]) - 1:
                print("{:d} ".format(matrix[r][c]), end="")
            else:
                print("{:d}".format(matrix[r][c]), end="")
        print()
