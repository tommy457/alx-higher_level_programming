#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    argc = len(my_list)

    if idx < 0 or argc < idx:
        return None
    for i in range(argc):
        if i == idx:
            my_list[i] = element
            break
