#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        average = 0
        diff = 0
        for tup in my_list:
            average += tup[0] * tup[1]
            diff += tup[1]
        return float(average / diff)
    return 0
