#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    argc = len(my_list) - 1

    if idx <= argc and idx >= 0 and argc >= 0:
        my_list.remove(my_list[idx])
    return my_list
