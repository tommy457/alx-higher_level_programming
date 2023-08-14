#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    argc = len(my_list) - 1
    if argc >= 0:
        for i in range(argc, -1, -1):
            print("{:d}".format(my_list[i]))
