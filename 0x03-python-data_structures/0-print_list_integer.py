#!/usr/bin/python3
def print_list_integer(my_list=[]):
    argc = len(my_list)
    for i in range(argc):
        print("{:d}".format(my_list[i]))
