#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, div, mul, sub
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        result = a + b
        print("{} + {} = {}".format(a, b, result))
    elif argv[2] == "-":
        result = a - b
        print("{} - {} = {}".format(a, b, result))
    elif argv[2] == "*":
        result = a * b
        print("{} * {} = {}".format(a, b, result))
    elif argv[2] == "/":
        result = a / b
        print("{} / {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
