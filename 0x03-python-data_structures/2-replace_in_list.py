#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    argc = len(my_list)

    for i in range(argc):
        if i == idx:
           my_list[i] = element
           break
    return my_list
