#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0
    if len(argv) == 1:
        print("{:d}".format(result))
    elif len(argv) == 2:
        result = int(argv[1])
        print("{:d}".format(result))
    else:
        i = 1
        while i < len(argv):
            result += int(argv[i])
            i = i + 1
            print("{:d}".format(result))
