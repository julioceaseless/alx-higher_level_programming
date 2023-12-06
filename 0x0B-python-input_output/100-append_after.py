#!/usr/bin/python3
"""
insert a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename) as my_file:
        file_lines = []
        for line in my_file:
            file_lines.append(line)
            if search_string in line:
                file_lines.append(new_string)

    with open(filename, mode="w") as my_file:
        my_file.writelines(file_lines)
