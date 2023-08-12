#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxx = my_list[0]
    for num in my_list[1:]:
        if num > maxx:
           maxx = num
    return maxx
