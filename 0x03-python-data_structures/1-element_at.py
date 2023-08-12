#!/usr/bin/python3

def element_at(my_list, idx):

    argc = len(my_list)

    if idx < 0 or argc < idx:
        return None

    for i in range(argc):
        if i == idx:
            return my_list[i]
