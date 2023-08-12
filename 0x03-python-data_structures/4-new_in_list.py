#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    argc = len(my_list) - 1

    if idx >= 0 and idx <= argc:
        copy_list[idx] = element
    return copy_list
