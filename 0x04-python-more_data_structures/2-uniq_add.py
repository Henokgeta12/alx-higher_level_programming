#!/usr/bin/python3
def uniq_add(my_list=None):
    if my_list is None:
        my_list = []

    x = 0
    for b in set(my_list):
        x += b
    return x
