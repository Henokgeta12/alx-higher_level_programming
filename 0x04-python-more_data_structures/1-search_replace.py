#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lop = my_list[:]
    lop[search - 1] = replace
    return lop
