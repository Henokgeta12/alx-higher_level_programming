#!/usr/bin/python3
def delete_at(my_list=None, idx=0):
    if idx >= len(my_list):
        return my_list
    else:
        my_list.remove(idx)

    return my_list
