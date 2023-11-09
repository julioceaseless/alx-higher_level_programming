#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    current_num = 0
    next_num = 0
    next_char = ""
    count = 0
    for i in roman_string:
        if i in roman_dict:
            current_num += roman_dict[i]
            if next_num < roman_dict[i]:
                current_num -= next_num * 2
            next_num = roman_dict[i]
            if i == next_char:
                count += 1
                if count == 3:
                    return 0
            else:
                count = 0
            next_char = i[:]
    return current_num
