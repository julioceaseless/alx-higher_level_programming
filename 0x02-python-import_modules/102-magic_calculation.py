import magic_calculation_102 as magic


def magic_calculation(a, b):
    if a < b:
        add = magic.add(a, b)
        for i in range(4, 6):
            add = magic.add(add, i)
        return add
    return magic.sub(a, b)
