#!/usr/bin/env python3
def no_c(my_string):
    modified_string = ""
    if 'c' not in my_string and 'C' not in my_string:
        return my_string
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            modified_string += char
    return modified_string
