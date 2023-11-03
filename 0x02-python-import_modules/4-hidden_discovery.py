#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    count = 1
    size = len(dir(hidden_4))
    for name in dir(hidden_4):
        if count > (size - 3) and count <= size:
            print(name)
        count += 1
