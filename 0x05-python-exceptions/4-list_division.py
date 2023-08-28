#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    num = 0
    try:
        for i in range(list_length):
            try:
                c = my_list_1[i] / my_list_2[i]
                new_list.append(c)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
    except IndexError:
        print("out of range")
        new_list.append(0)
    finally:
        for j in range(list_length - len(new_list)):
            new_list.append(0)
        return new_list
